# Báo cáo cá nhân — Ngô Minh Cương - 2A202603954

## 1. Thông tin thành viên

- Họ tên: Ngô Minh Cương
- MSSV: 2A202603954
- Email: 26ai.cuongnm5@vinuni.edu.vn
- Vai trong nhóm: Người viết code (CP1–CP2) + Kiểm soát kỹ thuật (CP3–CP5, duyệt chéo C8)

## 2. Phần việc phụ trách

- **Bước 0:** Thiết lập môi trường Python (`src/.venv`), cài đặt thư viện trong `src/requirements.txt` và xác minh chạy thử.
- **CP1 (Nhiệm vụ A):** Viết code phần A1–A4 trong `src/lab13.py` (3 phép thử đáp án biết trước, mô hình chi phí `mo_hinh(...)`, tách theo loại yêu cầu, chi phí cố định).
- **CP2 (Nhiệm vụ B):** Viết code phân tích độ nhạy B1–B4 trong `src/lab13.py` (9 kịch bản đơn, kịch bản cặp, chi phí cả hệ thống theo giới hạn chạy lại, kịch bản xem lại 100% ở cả 2 mức phút làm lại).
- **CP3 (Nhiệm vụ C):** Rà soát kỹ thuật `report/team/bang_loi.md`, bổ sung ngưỡng đo được và thuộc tính trace.
- **CP4 (Nhiệm vụ D):** Thiết kế 3 luật dừng đủ 4 vế (`NẾU – TRONG – THÌ – KHÔNG THÌ`), quy trình `rollback` trong `report/team/pilot_plan.yaml` và chạy kiểm tra `yaml.safe_load` + soát dấu `?`.
- **CP5 (Nhiệm vụ E) & Đóng gói:** Thiết kế 11 event có `trace_id` và mục kiểm tra chéo trong `report/team/chi_so.md`; chạy kiểm tra tổng thể cuối buổi (code, YAML, quy tắc nhãn `simulated`, không chứa từ cấm).

## 3. Đóng góp cụ thể

- Hoàn thiện A1–A4 trong `src/lab13.py`: 3 phép thử A1 đạt (`1,20 · 1,25 · 1,25`), tính CPS toàn mẫu `4.472 đ` (`simulated`, gấp `16,3×` hoá đơn `274,7 đ`), chi phí cả hệ thống `5.865 đ/yc` (`0,49×`), tách 4 loại yêu cầu và tỉ lệ `ok` theo `attempt`, cộng cố định 40 triệu đ/tháng (`4.599 đ` ở 45.000 yc/tháng, `5.784 đ` ở 22.500 yc/tháng).
- Hoàn thiện B1–B4 trong `src/lab13.py` kèm `assert` tự kiểm tra tính đối xứng B1 và tính tuyến tính B2; chỉ ra giới hạn `2` lần rẻ nhất cho cả hệ thống (`6.901.220 đ`) khác với CPS thấp nhất ở `1` lần (`4.111 đ`), và xem lại 100% đẩy CPS lên `11.743 đ` (`0,98×`) đến `12.415 đ` (`1,03×`, `simulated`).
- Bổ sung ngưỡng cảnh báo `> 5%` cho ca 4 và làm rõ thuộc tính `pricing_version` gắn cùng `trace_id` cho ca 17 trong `report/team/bang_loi.md`.
- Viết 3 `stop_rules` (an toàn, chi phí, sử dụng) và `rollback` 30 phút trong `report/team/pilot_plan.yaml`; thiết kế 11 event có `trace_id` và bảng kiểm tra chéo phủ đủ 5 chỉ số E1 trong `report/team/chi_so.md`.
- Rà soát nhất quán toàn repo (`bang_chi_phi.md`, `bang_loi.md`, `chi_so.md`, `pilot_plan.yaml`, `ho_so_launch_v0.md`) và hoàn thiện khung `report/team/group_report.md`.

## 4. Bằng chứng

- File đóng góp trực tiếp: `src/lab13.py`, `report/team/bang_loi.md`, `report/team/pilot_plan.yaml`, `report/team/chi_so.md`, `report/team/group_report.md`.
- Các commit trên nhánh `main`:
  - `e891e89` — CP1: A1–A4 trong `src/lab13.py`.
  - `7d3e428` — CP2: độ nhạy B1–B4 trong `src/lab13.py`.
  - `08e251b` — CP3: ngưỡng ca 4 và thuộc tính `pricing_version` ca 17 trong `report/team/bang_loi.md`.
  - `6daf713` — CP4: 3 `stop_rules` 4 vế và `rollback` trong `report/team/pilot_plan.yaml`.
  - `382ae3c` — CP5: 11 event `trace_id` và kiểm tra chéo trong `report/team/chi_so.md`.

## 5. Công cụ AI đã dùng

- **Công cụ:** Antigravity (trợ lý AI trong IDE).
- **Mục đích sử dụng:** Tóm tắt yêu cầu đề bài và phân chia kế hoạch làm việc theo checkpoint cho nhóm 3 người; gợi ý triển khai hàm A1–A4, B1–B4 trong `src/lab13.py`; rà soát kỹ thuật bảng lỗi, luật dừng 4 vế, danh sách event `trace_id` và checklist nộp bài.
- **Cách tự kiểm tra kết quả:**
  - Chạy trực tiếp `python lab13.py` trong `src/.venv`, kiểm tra 3 phép thử A1 in `ĐẠT`, các `assert` đối xứng B1 và tuyến tính B2 đều `ĐẠT`, đối chiếu từng con số với hướng dẫn và slide chữa (lệch 0%).
  - Chạy `yaml.safe_load` và kiểm tra không còn dấu `?` ngoài comment trên `report/team/pilot_plan.yaml`.
  - Chạy lệnh tìm kiếm đảm bảo `0` từ cấm trong toàn bộ `report/team/` và xác nhận đầy đủ nhãn `simulated`.

## 6. Tự đánh giá

- Hoàn thành đúng tiến độ các mốc CP1–CP5, bàn giao code sạch để thành viên 2 đổi vai viết tiếp D1–E1 và chạy thông suốt trên cả hai máy.
- Nắm rõ bản chất mô hình chi phí (tử số tính mọi lần chạy, mẫu số chỉ đếm việc thành công), sự khác biệt giữa tối ưu CPS riêng lẻ và chi phí cả hệ thống (B3), và cơ chế thiết kế luật dừng + event `trace_id` cho pilot Gate 2a.
- Điểm cần rút kinh nghiệm: cần cập nhật `TEAM.md` và thống nhất tên hiển thị trong các file báo cáo ngay từ đầu buổi để không phải rà soát lại ở cuối buổi.
