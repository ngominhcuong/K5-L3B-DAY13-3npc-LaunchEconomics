# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | ... |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | ... |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | ... |
| Dùng | Nhóm tự đề xuất: ... | ... | Không cần tính |
| An toàn | Nhóm tự đề xuất: ... | ... | Không cần tính |

Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent. (Nhóm thiết kế 11 event, phủ đủ 5 chỉ số E1, đo giờ nhân viên thật để thay cột `_simulated`, và khớp toàn bộ bảng phát hiện lỗi trong `bang_loi.md`.)

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách / cổng CSKH | `request_id`, `loai`, `depot`, `arm`, `so_tien_vnd`, `created_at`, `trace_id` | Khi khách gửi yêu cầu hoàn phí |
| `input_validation_failed` | Cổng tiếp nhận / Agent | `request_id`, `loai_loi_dau_vao`, `ma_nhap`, `trace_id` | Khi đầu vào của khách sai định dạng (vd mã sàn TMĐT thay vì mã vận đơn) |
| `agent_run_completed` | Agent | `run_id`, `attempt`, `tokens_in`, `tokens_out`, `tool_calls`, `status`, `pricing_version`, `trace_id` | Sau mỗi lần chạy của agent, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | `staff_id`, `so_tien_de_xuat`, `shown_at`, `trace_id` | Khi gợi ý của trợ lý hiển thị cho nhân viên |
| `staff_review_decision` | Nhân viên CSKH | `staff_id`, `quyet_dinh` (`giu`/`sua`/`bo`), `phut_xem_lai` (đo thật), `trace_id` | Khi nhân viên bấm giữ, sửa hoặc bỏ gợi ý |
| `staff_rework_completed` | Nhân viên CSKH | `staff_id`, `phut_lam_lai` (đo thật), `ly_do`, `trace_id` | Khi nhân viên hoàn tất xử lý lại một ca trợ lý làm sai |
| `refund_ledger_write` | Dịch vụ sổ cái | `idempotency_key`, `so_tien_hoan`, `ket_qua` (`ok`/`loi`), `written_at`, `trace_id` | Khi ghi nhận giao dịch hoàn tiền vào sổ cái |
| `handoff_to_staff` | Agent | `reason` (`thieu_du_lieu`/`qua_gioi_han`/`ngoai_pham_vi`), `tom_tat`, `trace_id` | Khi agent dừng và chuyển yêu cầu sang nhân viên |
| `ticket_closed` | Hệ thống ticket | `request_id`, `closed_at`, `nguoi_dong`, `trace_id` | Khi yêu cầu hoàn phí được đóng |
| `ticket_reopened` | Khách hàng / CSKH | `request_id`, `reopened_at`, `reason`, `trace_id` | Khi yêu cầu bị mở lại sau khi đã đóng |
| `audit_sample_checked` | Bộ phận kế toán | `request_id`, `so_tien_da_hoan`, `so_tien_dung`, `pricing_version`, `checked_at`, `trace_id` | Hằng tuần khi kiểm tra mẫu 100 đơn so với bảng giá hiện hành |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- **Chính (`% yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày`):** tính từ `refund_request_created` (tổng yêu cầu & mốc `created_at`) + `ticket_closed` (`closed_at - created_at <= 24h`) + `ticket_reopened` (không phát sinh trong 7 ngày kể từ `closed_at`), nối theo `trace_id` và `request_id`.
- **Dùng (`Tỉ lệ bỏ qua gợi ý`):** tính từ `staff_review_decision` = số event có `quyet_dinh` là `sua` hoặc `bo` chia cho tổng số event `staff_review_decision`.
- **An toàn (`Tỉ lệ lỗi lọt đến khách`):** tính từ `ticket_reopened` (phát sinh trong 7 ngày từ `closed_at`) chia cho tổng `refund_request_created`.
- **Dùng (nhóm tự đề xuất — gợi ý: `% yêu cầu nhóm can thiệp được mở bằng trợ lý`):** tính từ `agent_suggestion_shown` chia cho tổng `refund_request_created` có `arm = treatment`.
- **An toàn (nhóm tự đề xuất — gợi ý: `% đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần`, bắt lỗi ngầm ca 5 & 17):** tính từ `audit_sample_checked` = số bản ghi có `so_tien_da_hoan != so_tien_dung` chia tổng số đơn được kiểm tra mẫu.
- **Bổ trợ đo chi phí thật (thay thế cột `_simulated` sau tuần 1 pilot):** tính từ `agent_run_completed` (`tokens_in`, `tokens_out`, `tool_calls`) + `staff_review_decision` (`phut_xem_lai`) + `staff_rework_completed` (`phut_lam_lai`) nối cùng `trace_id`.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... |
