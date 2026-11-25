# Báo cáo cá nhân — TranQuangHa-2A202603962

## 1. Thông tin thành viên

- Họ tên: Trần Quang Hà
- MSSV: 2A202603962
- Email: 26ai.hatq@vinuni.edu.vn
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): Người gắn nhãn 2 kiêm giữ hồ sơ (`PM/Doc`, tổng hợp `ho_so_launch_v0.md`, lead `pilot_plan.yaml`, duyệt chéo C6)

## 2. Phần việc phụ trách

- **Mốc 0 & Quản lý nhóm:** Khởi tạo thông tin nhóm (`3npc`, `L3B`), bảng thành viên và tổng hợp đóng góp trong `TEAM.md`; giữ nhịp thời gian và rà soát 5 quy tắc bắt buộc của lab xuyên suốt các checkpoint.
- **CP1 & CP2 (`report/team/ho_so_launch_v0.md`):** Đối chiếu kết quả mô hình chi phí A1–A4 và độ nhạy B1–B4 với slide chữa; cập nhật Mục 1, Mục 2 và Mục 3 vào hồ sơ launch v0 đúng quy chuẩn nhãn `simulated`, trạng thái `Giả lập` và 1 vai trò phụ trách.
- **CP3 (`report/team/bang_loi.md` & Mục 5):** Thực hiện bộ nhãn độc lập 20 ca lỗi (`Nhãn người 2`), đối chiếu tính tỉ lệ đồng thuận với Người gắn nhãn 1, thống nhất quy tắc ranh giới, soát cột *"Ai phụ trách"* trong bảng khắc phục 5 ca và cập nhật Mục 5 vào `ho_so_launch_v0.md`.
- **CP4 (`report/team/pilot_plan.yaml` & Mục 6):** Lead điền phần chú thích D1 (5 câu a–e), D2 (5 câu tách tác động), đánh đổi đã chấp nhận, tỉ lệ mở lại hiện tại và các trường cấu hình YAML (`owner`, `scope`, `assignment`, `rollout`, `primary_metric`, `identifiability`, `interim_looks`, `decision_date`, `simulated_inputs`); cập nhật Mục 6 vào `ho_so_launch_v0.md`.
- **CP5 (`report/team/ho_so_launch_v0.md`):** Chốt Mục 4, cập nhật trạng thái Mục 6, điền Mục 7 và viết đề xuất cuối (`Go có điều kiện`) trước mốc 17:00.
- **Duyệt chéo Gate 2a & Đóng gói:** Trình bày chính 1 phút bảo vệ hồ sơ trước hội đồng, chấm tiêu chí C6 cho nhóm $n+1$ trong `report/team/phieu_cham.md`, và phối hợp hoàn thiện báo cáo nhóm cuối buổi.

## 3. Đóng góp cụ thể

- Cập nhật **Mục 1, Mục 2, Mục 3** trong `report/team/ho_so_launch_v0.md`: CPS toàn mẫu `4.472 đ` (`simulated`, gấp `16,3×` hoá đơn `274,7 đ/yc`), chi phí cả hệ thống `5.865 đ/yc = 0,49×` (`simulated`), phạm vi `noi_dia + hang_nang` cộng cố định 40 triệu đ/tháng (`4.599 đ = 0,38×` ở 45.000 yc/tháng và `5.784 đ = 0,48×` ở nửa khối lượng, `simulated`), loại `quoc_te` (`1,88×`) và `doi_tac` (`0,85×`), xếp hạng 3 yếu tố nhạy nhất (`1. Làm lại +51,8% · 2. Xem lại +40,7% · 3. Lương nhân viên +23,1%`), và xem lại 100% ở B4 (`11.743 đ = 0,98×` đến `12.415 đ = 1,03×`, `simulated`).
- Hoàn thiện bộ nhãn độc lập 20 ca lỗi (`Nhãn người 2`: `PM/Doc`), đạt đồng thuận `20/20 (100%)` với `Nhãn người 1`, ghi quy tắc ranh giới cho các ca dễ nhầm (`6, 9, 12, 13, 18`) và cập nhật **Mục 5** vào `ho_so_launch_v0.md`.
- Hoàn thiện phần phân tích cỡ mẫu D1 (`1.251`; `3.103 / 42 NV`; trần `1.000` với 20 NV/nhóm; trần `300` với 6 depot; `m ≥ 299` và `DE = 6,96` khi chấp nhận MDE 6 điểm `859`/nhóm), 5 câu kiểm tra tách tác động D2, nêu rõ đánh đổi power còn `~0,64` ở mức 5 điểm, tỉ lệ mở lại hiện tại (`4,25%` toàn mẫu, `3,97%` trong phạm vi) và các trường YAML trong `report/team/pilot_plan.yaml`.
- Chốt **Mục 4** (`82,83%`, `27,12%`, `4,25%`, đủ 11 event `trace_id`), cập nhật **Mục 6** (`Xong, có bằng chứng`), **Mục 7** (`Giả lập`), và đề xuất **`Go có điều kiện`** kèm 4 điều kiện có vai trò phụ trách và ngày kiểm tra cụ thể trong `report/team/ho_so_launch_v0.md`; điền đầy đủ thông tin nhóm và thành viên vào `TEAM.md`.

## 4. Bằng chứng

- Các file đóng góp trực tiếp: `TEAM.md`, `report/team/ho_so_launch_v0.md`, `report/team/bang_loi.md`, `report/team/pilot_plan.yaml`, `report/team/2A202603962_TranQuangHa.md`.
- Các commit trên nhánh `main`:
  - `8ee8140` — CP1: cập nhật Mục 1 và Mục 3 trong `report/team/ho_so_launch_v0.md`.
  - `382689f` — CP2: cập nhật Mục 2 trong `report/team/ho_so_launch_v0.md`.
  - `5001163` — CP3: hoàn thiện đồng thuận 20/20 trong `report/team/bang_loi.md` và Mục 5 trong `report/team/ho_so_launch_v0.md`.
  - `e827c23` — CP4: điền D1–D2, đánh đổi và cấu hình `report/team/pilot_plan.yaml` + Mục 6 trong `report/team/ho_so_launch_v0.md`.
  - `e9d5cfb` — CP5: hoàn thiện 7 mục + đề xuất `Go có điều kiện` trong `report/team/ho_so_launch_v0.md` và điền `TEAM.md`.

## 5. Công cụ AI đã dùng

- **Công cụ:** Antigravity (trợ lý AI trong IDE).
- **Mục đích sử dụng:** Tóm tắt hướng dẫn lab, đối chiếu quy trình theo `plan.md`, hỗ trợ rà soát số liệu và định dạng các file hồ sơ (`ho_so_launch_v0.md`, `pilot_plan.yaml`, `TEAM.md`), gợi ý phân tích ranh giới 5 loại lỗi Google PAIR ở CP3 và soạn báo cáo cá nhân.
- **Cách tự kiểm tra kết quả:**
  - Tự thiết lập môi trường `src/.venv` trên Windows PowerShell và chạy trực tiếp `python lab13.py` để xác minh toàn bộ output A1–A4 (`1.20 · 1.25 · 1.25`), B1–B4, D1 và E1 khớp với số liệu nhóm đã đưa vào hồ sơ.
  - Kiểm tra `pilot_plan.yaml` bằng `yaml.safe_load` và kiểm chứng power (`0.642` ở `n = 859`) qua `statsmodels`.
  - Rà soát lại lập luận nguyên nhân gốc cho 20 ca lỗi (đặc biệt các ca ranh giới 6, 12, 13, 18) và chạy lệnh kiểm tra đảm bảo `0` từ cấm (không viết như đã chạy chính thức), đầy đủ nhãn `simulated` và mỗi mục chỉ có 1 vai trò phụ trách.

## 6. Tự đánh giá

- Hoàn thành đúng tiến độ toàn bộ các mốc từ Mốc 0 đến CP5 theo `plan.md`, giữ luồng làm việc tách nhánh/tạo Pull Request sạch sẽ không gây conflict với hai thành viên còn lại.
- Nắm vững bức tranh kinh tế của agent (giờ nhân viên chiếm `92,5%` tổng chi phí, xem lại 100% có thể làm chi phí tiệm cận hoặc vượt `12.000 đ/việc`), lý do thu hẹp phạm vi pilot về `noi_dia + hang_nang` và cách trình bày minh bạch các đánh đổi bất lợi (power `0,64`, lỗi ca 7/20, số `simulated`) khi bảo vệ trước hội đồng Gate 2a.
- Điểm cần tiếp tục hoàn thiện ở phần cuối buổi: ghi nhận đầy đủ kết quả chấm chéo vào `report/team/phieu_cham.md`, cập nhật phản hồi của hội đồng vào `report/team/group_report.md` và bổ sung `commit chốt` vào `TEAM.md` trước khi nộp link lên LMS.
