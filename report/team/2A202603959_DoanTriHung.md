# Báo cáo cá nhân — DoanTriHung-2A202603959

## 1. Thông tin thành viên

- Họ tên: Đoàn Trí Hùng
- MSSV: 2A202603959
- Email: 26ai.hungdt2@vinuni.edu.vn
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): Người kiểm số (CP1–CP2) + Người gắn nhãn 1 (CP3) + Người viết code (CP4–CP5, duyệt chéo C7)

## 2. Phần việc phụ trách

- **CP1 & CP2 (Người kiểm số):** Tính tay đối chiếu kết quả mô hình chi phí từ `src/lab13.py`, kiểm tra tính đối xứng độ nhạy và hoàn thiện toàn bộ bảng A1–A4, B1–B4 trong `report/team/bang_chi_phi.md`.
- **CP3 (Người gắn nhãn 1):** Độc lập gắn nhãn 20 ca lỗi theo 5 loại của Google PAIR, đối chiếu đồng thuận với Người gắn nhãn 2 và lập bảng khắc phục 5 ca trong `report/team/bang_loi.md`.
- **CP4 (Đổi vai sang Người viết code):** Viết phần tính cỡ mẫu D1, power thực tế ở mức 5 điểm và tỉ lệ mở lại 7 ngày hiện tại trong `src/lab13.py`, chạy kiểm tra toàn bộ trên máy thứ hai.
- **CP5 & Duyệt chéo:** Tính thử 3 chỉ số E1 trong `src/lab13.py`, hoàn thiện bảng đặc tả chỉ số E1 và bảng rủi ro kinh tế E2 trong `report/team/chi_so.md`; chấm tiêu chí C7 khi duyệt chéo Gate 2a và hỗ trợ hoàn thiện `report/team/group_report.md`.

## 3. Đóng góp cụ thể

- Đối chiếu số liệu và điền đầy đủ bảng A1 (`1,20 · 1,25 · 1,25`), A2 (`4.472 đ` [simulated], gấp `16,3×` hoá đơn/yc; chi phí cả hệ thống `5.865 đ/yc = 0,49×` [simulated]), A3 (loại `quoc_te` `1,88×` và `doi_tac` `0,85×`), A4 (cố định `40 triệu đ/tháng` cho `noi_dia + hang_nang`: `4.599 đ = 0,38×` ở `45.000` yc/tháng và `5.784 đ = 0,48×` ở nửa khối lượng [simulated]) trong `report/team/bang_chi_phi.md`.
- Hoàn thiện phân tích độ nhạy B1–B4 trong `report/team/bang_chi_phi.md`: kiểm tra đối xứng (giảm một nửa = −½ gấp đôi), xếp hạng 3 yếu tố nhạy nhất (`1. Số ca làm lại +51,8% · 2. Tỉ lệ xem lại +40,7% · 3. Lương nhân viên +23,1%`), so sánh giới hạn chạy lại (`2 lần` rẻ nhất cho cả hệ thống: `6.901.220 đ` [simulated]), và kịch bản xem lại 100% (`11.743 đ = 0,98×` với 9 phút làm lại; `12.415 đ = 1,03×` với `15,3` phút dữ liệu [simulated]).
- Gắn nhãn độc lập 20 ca lỗi (`Nhãn người 1`), đạt đồng thuận `20/20` (`100%`) với Người gắn nhãn 2, và điền bảng khắc phục 5 ca (đủ 5 loại, có cách phát hiện đo được và 1 vai trò phụ trách) trong `report/team/bang_loi.md`.
- Viết hàm `co_mau(...)` và `tinh_power_hai_ti_le(...)` tính 5 câu D1 (`1.251` theo yêu cầu; `3.103` với `m=75` → `42 NV/nhóm`, không đủ 40 người; tối đa `1.000` với `20 NV/nhóm`; tối đa `300` với `6 depot/nhóm`; `m ≥ 299` và `DE = 6,96` ở mức chênh 6 điểm `859`/nhóm), power còn `0,64` ở mức 5 điểm, và tỉ lệ `mo_lai_trong_7_ngay` hiện tại (`4,25%` toàn mẫu, `3,97%` trong phạm vi pilot) trong `src/lab13.py`.
- Tính thử 3 chỉ số E1 (`82,83%`, `27,12%`, `4,25%`) trong `src/lab13.py` và điền đầy đủ bảng E1 (5 chỉ số) + bảng rủi ro kinh tế E2 (3 dòng lấy số từ `bang_chi_phi.md`, có nhãn `simulated` và vai trò phụ trách) trong `report/team/chi_so.md`.

## 4. Bằng chứng

- Các commit cá nhân trên nhánh `main` (tác giả `hungdt31`): `62468dc` (CP1 `bang_chi_phi.md`), `eb432ba` (CP2 `bang_chi_phi.md`), `e3c048c` (CP3 `bang_loi.md`), `27068db` (CP4 `src/lab13.py`), `081cd8f` (CP5 `src/lab13.py` & `chi_so.md`).
- Các file đã đóng góp trực tiếp: `src/lab13.py`, `report/team/bang_chi_phi.md`, `report/team/bang_loi.md`, `report/team/chi_so.md`.
- Chạy kiểm tra toàn bộ `cd src && python3 lab13.py` trên máy cá nhân: đạt đủ 3 phép thử A1 (`1.20`, `1.25`, `1.25`), kiểm tra đối xứng B1 ĐẠT, và in đầy đủ bảng A2–A4, B1–B4, D1, E1.

## 5. Công cụ AI đã dùng

- **Công cụ:** Trợ lý AI (Gemini) tích hợp trong IDE.
- **Mục đích sử dụng:** Hỗ trợ tóm tắt yêu cầu từng checkpoint, kiểm tra chéo công thức Python (`co_mau`, `tinh_power_hai_ti_le`, tỉ lệ E1), rà soát nhãn `simulated` và quy chuẩn trình bày bảng biểu trong `bang_chi_phi.md`, `bang_loi.md`, `chi_so.md`.
- **Cách tự kiểm tra kết quả:**
  - Đối chiếu tay các phép thử A1 (`(1 - 0,2²)/0,8 = 1,20`) và các con số tổng hợp với tài liệu hướng dẫn `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (sai số `0%`, đạt ngưỡng `≤ 2%`).
  - Tự chạy lại toàn bộ `cd src && python3 lab13.py` trên máy cá nhân để kiểm chứng output thực tế từ hai file CSV gốc.
  - Kiểm tra tự động không còn từ cấm (chỉ dùng kế hoạch pilot, không viết như đã chạy chính thức) trong `report/team/` và mọi số từ cột `*_simulated` đều có nhãn `simulated`.

## 6. Tự đánh giá

- Hoàn thành đúng tiến độ và đầy đủ các đầu việc được phân công từ CP1 đến CP5 trong `plan.md`, phối hợp nhịp nhàng khi đổi vai từ Kiểm số/QA (CP1–CP3) sang Viết code (CP4–CP5) để đảm bảo code chạy sạch trên 2 máy khác nhau trong nhóm.
- Hiểu rõ bản chất kinh tế đằng sau mô hình chi phí (giờ công xem lại/làm lại chiếm `92,5%` tổng chi phí chứ không chỉ nhìn hoá đơn token), cách phân loại lỗi theo nguyên nhân gốc và lý do phải chấp nhận đánh đổi `MDE = 6 điểm` (`power = 0,64` ở 5 điểm) khi giới hạn chỉ có 40 nhân viên.
