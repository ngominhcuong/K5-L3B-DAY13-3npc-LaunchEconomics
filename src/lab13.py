"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    return 1 / p if k is None else (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    return 1.0 if k is None else 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, chay_lai, xem_lai, lam_lai, tong, thanh_cong, cps, hoa_don_moi_yc.
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    chay_lai = (tien_token + tien_tool)[runs['attempt'] > 1].sum()
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    return dict(
        token=tien_token.sum(),
        tool=tien_tool.sum(),
        chay_lai=chay_lai,
        xem_lai=xem_lai,
        lam_lai=lam_lai,
        tong=tong,
        thanh_cong=thanh_cong,
        cps=tong / thanh_cong,
        hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs),
    )


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)

    # ---------- CP1 · A1 ----------
    kiem_tra_dap_an_biet_truoc()
    print(f'  A1.1 (k=2):  {so_lan_chay_ky_vong(0.8, 2):.2f}')
    print(f'  A1.2 (k=∞):  {so_lan_chay_ky_vong(0.8):.2f}')
    print(f'  A1.3 (k=3):  {he_so_chi_phi_moi_viec_thanh_cong(0.8, 3):.2f}')

    # ---------- CP1 · A2 ----------
    print('\n=== A2 · Mô hình chi phí từ trace ===')
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        fmt = f'{gia_tri:>14,.1f}' if ten == 'hoa_don_moi_yc' else f'{gia_tri:>14,.0f}'
        print(f'{ten:16s} {fmt}')
    ti_le_gap = ket_qua['cps'] / ket_qua['hoa_don_moi_yc']
    khong_tc = len(reqs) - ket_qua['thanh_cong']
    chi_phi_he_thong_moi_yc = (ket_qua['tong'] + khong_tc * BASELINE) / len(reqs)
    print(f"Gấp hoá đơn/yc:   {ti_le_gap:.1f}x")
    print(f"Tỉ trọng làm lại: {ket_qua['lam_lai'] / ket_qua['tong'] * 100:.1f}% [simulated]")
    print(f"Tỉ trọng xem lại: {ket_qua['xem_lai'] / ket_qua['tong'] * 100:.1f}% [simulated]")
    print(f"Chi phí cả hệ thống/yc (cộng {khong_tc} ca không thành công × 12.000 đ): "
          f"{chi_phi_he_thong_moi_yc:,.0f} đ ({chi_phi_he_thong_moi_yc / BASELINE:.2f}x) [simulated]")

    # ---------- CP1 · A3 ----------
    print('\n=== A3 · Tách theo loại yêu cầu ===')
    print(f"{'Loại':12s} {'Số YC':>6s} {'Tỉ lệ TC':>9s} {'Lần/YC':>8s} {'CPS [sim]':>12s} {'So 12k':>8s}")
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        sub = reqs[reqs['loai'] == loai]
        kq = mo_hinh(runs, sub)
        tc_rate = kq['thanh_cong'] / len(sub) * 100
        lan_tb = sub['so_lan_chay'].mean()
        print(f"{loai:12s} {len(sub):>6d} {tc_rate:>8.1f}% {lan_tb:>8.2f} {kq['cps']:>12,.0f} {kq['cps'] / BASELINE:>7.2f}x")

    print('\nTỉ lệ lần chạy status == ok theo loại và attempt (%):')
    runs_loai = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    runs_loai['is_ok'] = (runs_loai['status'] == 'ok').astype(float) * 100
    bang_ok = runs_loai.pivot_table(index='loai', columns='attempt', values='is_ok', aggfunc='mean')
    print(bang_ok.reindex(['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']).round(1))

    # ---------- CP1 · A4 ----------
    print('\n=== A4 · Chi phí cố định (phạm vi noi_dia + hang_nang) ===')
    CHI_PHI_CO_DINH = 40_000_000
    sub_pilot = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    kq_pilot = mo_hinh(runs, sub_pilot)
    ti_le_tc_mau = kq_pilot['thanh_cong'] / len(reqs)
    print(f"CPS trong phạm vi (chưa cố định): {kq_pilot['cps']:,.0f} đ "
          f"(tong={kq_pilot['tong']:,.0f} đ, thanh_cong={kq_pilot['thanh_cong']}/{len(reqs)}) [simulated]")
    for nhan, kl_thang in [('45.000 yc/tháng', 45_000), ('Một nửa (22.500 yc/tháng)', 22_500)]:
        viec_tc_thang = kl_thang * ti_le_tc_mau
        co_dinh_moi_viec = CHI_PHI_CO_DINH / viec_tc_thang
        cps_cong_cd = kq_pilot['cps'] + co_dinh_moi_viec
        print(f"  {nhan:26s} | TC/tháng: {viec_tc_thang:>8,.0f} | Cố định/việc: {co_dinh_moi_viec:>6,.0f} đ | "
              f"CPS+CĐ: {cps_cong_cd:>6,.0f} đ ({cps_cong_cd / BASELINE:.2f}x) [simulated]")

    # ---------- CP2 · B1: Đổi từng yếu tố ----------
    print('\n=== B1 · Bảng độ nhạy (đổi từng yếu tố) ===')
    kich_ban = {
        'Giá token gấp đôi':      dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa': dict(gia_vao=13, gia_ra=65),
        'Xem lại gấp đôi':        dict(he_so_xem_lai=2.0),
        'Xem lại giảm một nửa':   dict(he_so_xem_lai=0.5),
        'Làm lại gấp đôi':        dict(he_so_lam_lai=2.0),
        'Làm lại giảm một nửa':   dict(he_so_lam_lai=0.5),
        'Lương tăng 25%':         dict(luong_phut=2500),
        'Tối đa 2 lần chạy':      dict(max_lan_chay=2),
        'Chỉ 1 lần chạy':         dict(max_lan_chay=1),
    }
    goc = ket_qua['cps']
    b1_pct = {}
    print(f"{'Kịch bản':26s} {'CPS [sim]':>10s} {'Thay đổi':>10s}")
    for ten, kw in kich_ban.items():
        cps_kb = mo_hinh(runs, reqs, **kw)['cps']
        pct = (cps_kb / goc - 1) * 100
        b1_pct[ten] = pct
        print(f'{ten:26s} {cps_kb:>10,.0f} {pct:>+9.1f}%')

    # Tự kiểm tra tính đối xứng B1: giảm một nửa == -1/2 mức tăng của gấp đôi
    for goc_ten in ['Giá token', 'Xem lại', 'Làm lại']:
        tang = b1_pct[f'{goc_ten} gấp đôi']
        giam = b1_pct[f'{goc_ten} giảm một nửa']
        assert abs(giam + tang / 2) < 1e-9, f'Lệch đối xứng ở {goc_ten}'
    print('Kiểm tra đối xứng B1 (giảm nửa = -1/2 gấp đôi): ĐẠT')

    # ---------- CP2 · B2: Đổi một cặp và xếp hạng ----------
    print('\n=== B2 · Đổi một cặp và xếp hạng ===')
    cps_cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2.0)['cps']
    pct_cap = (cps_cap / goc - 1) * 100
    assert abs(pct_cap - (b1_pct['Giá token gấp đôi'] + b1_pct['Xem lại gấp đôi'])) < 1e-9
    print(f"Token ×2 + Xem lại ×2: {cps_cap:,.0f} đ ({pct_cap:+.1f}%) [simulated] — khớp tổng 2 tác động riêng: ĐẠT")
    print("Xếp hạng 3 yếu tố nhạy nhất: 1. Số ca làm lại · 2. Tỉ lệ xem lại · 3. Lương nhân viên")

    # ---------- CP2 · B3: Giới hạn chạy lại ----------
    print('\n=== B3 · Giới hạn chạy lại (chi phí cả hệ thống) ===')
    print(f"{'Giới hạn':10s} {'Tổng trợ lý':>14s} {'Không TC':>10s} {'Cả hệ thống':>14s} {'CPS [sim]':>10s}")
    for gioi_han in [1, 2, 3]:
        kq_gh = mo_hinh(runs, reqs, max_lan_chay=gioi_han)
        khong_tc_gh = len(reqs) - kq_gh['thanh_cong']
        ca_he_thong = kq_gh['tong'] + khong_tc_gh * BASELINE
        print(f"{gioi_han} lần      {kq_gh['tong']:>14,.0f} {khong_tc_gh:>10d} {ca_he_thong:>14,.0f} {kq_gh['cps']:>10,.0f}")

    # ---------- CP2 · B4: Xem lại 100% (noi_dia + hang_nang) ----------
    print('\n=== B4 · Xem lại 100% (phạm vi noi_dia + hang_nang) ===')
    runs_pilot = runs[runs['request_id'].isin(sub_pilot['request_id'])]
    so_yc_co_ok = int(runs_pilot.loc[runs_pilot['status'] == 'ok', 'request_id'].nunique())
    so_ca_lam_lai = int((sub_pilot['ket_qua'] == 'lam_lai').sum())
    token_tool_pilot = kq_pilot['token'] + kq_pilot['tool']
    tc_pilot = kq_pilot['thanh_cong']

    # Theo đề: 5 phút xem lại/ca có ok, 9 phút làm lại/ca lam_lai
    tien_xem_100 = so_yc_co_ok * 5 * LUONG_PHUT
    phut_lam_lai_tb = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean()
    print(f"Phạm vi: {len(sub_pilot)} yc | Có ≥1 lần ok: {so_yc_co_ok} | Ca làm lại: {so_ca_lam_lai} | "
          f"Token+Tool: {token_tool_pilot:,.0f} đ | Thành công: {tc_pilot}")
    for nhan, phut_ll in [('Đề bài (9,0 phút/ca)', 9.0), (f'Thực tế dữ liệu ({phut_lam_lai_tb:.1f} phút/ca)', phut_lam_lai_tb)]:
        tien_ll = so_ca_lam_lai * phut_ll * LUONG_PHUT
        tong_b4 = token_tool_pilot + tien_xem_100 + tien_ll
        cps_b4 = tong_b4 / tc_pilot
        phut_xem_hoa_von = (BASELINE * tc_pilot - token_tool_pilot - tien_ll) / (so_yc_co_ok * LUONG_PHUT)
        print(f"  {nhan:32s} | Tổng: {tong_b4:>11,.0f} đ | CPS: {cps_b4:>7,.0f} đ ({cps_b4 / BASELINE:.2f}x) | "
              f"Hoà vốn xem lại ≤ {phut_xem_hoa_von:.1f} phút [simulated]")

    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower
