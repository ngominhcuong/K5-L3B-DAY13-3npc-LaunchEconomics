# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: 3npc · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | **4.472 đ** (`simulated`), gấp **16,3×** hoá đơn token+tool (`274,7 đ/yc`); phạm vi `noi_dia + hang_nang` cộng cố định 40 tr/tháng: **4.599 đ** ở 45.000 yc/tháng, **5.784 đ** ở 22.500 yc/tháng (`simulated`) | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | **1. Làm lại** (+51,8% / −25,9%) · **2. Xem lại** (+40,7% / −20,3%) · **3. Lương nhân viên** (+23,1% khi +25%) (`simulated`); giá token cuối bảng (+5,6% khi ×2); xem lại 100% (`noi_dia+hang_nang`): **11.743 đ = 0,98×** (9p làm lại) hoặc **12.415 đ = 1,03×** (15,3p thực tế) (`simulated`) | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Cả hệ thống (gồm 222 ca không thành công × 12.000 đ): **5.865 đ/yc = 0,49×** (`simulated`); phạm vi pilot + cố định: **0,38×** (45.000 yc) và **0,48×** (22.500 yc) (`simulated`); loại `quoc_te` (**1,88×**) và `doi_tac` (**0,85×**) | Giả lập | Giám đốc vận hành LogiX-VN |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Đợt chạy thử: chính **82,83%** (`994/1.200`), bỏ qua gợi ý **27,12%** (`48/177`), mở lại 7 ngày **4,25%** (`51/1.200`) *(không kết luận đã nâng vì chưa có đối chứng)*; đủ **11 event** có `trace_id` & **2** chỉ số tự đề xuất | Xong, có bằng chứng | PM trợ lý hoàn phí |
| 5 · Bảng lỗi và cách khắc phục | Đồng thuận **20/20 (100%)** cho 20 ca lỗi theo 5 loại Google PAIR; bảng khắc phục đủ 5 loại (Ca 9, 7, 18, 4, 17) có phát hiện đo được & 1 vai trò phụ trách; ưu tiên sửa ca 7 & ca 20 trước pilot | Xong, có bằng chứng | PM trợ lý hoàn phí |
| 6 · Pilot plan | Chia theo `staff` (**20+20** cụm, ngẫu nhiên theo depot), phạm vi `noi_dia + hang_nang`; chấp nhận **MDE 6 điểm** (`n = 859`/nhóm, `m ≥ 299` yc/NV, `DE = 6,96`; power còn **~0,64** ở mức 5 điểm); đủ **3 luật dừng** 4 vế & rollback 30 phút (`decision_date: 2027-01-05`) | Xong, có bằng chứng | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | Làm lại ×2: **+51,8%** lên **6.787 đ/việc** (`simulated`); xem lại 100% kéo dài: **11.743 đ = 0,98×** (9p) hoặc **12.415 đ = 1,03×** (15,3p) (`simulated`); giảm 50% khối lượng: cố định **+2.370 đ/việc** (`simulated`) | Giả lập | PM trợ lý hoàn phí |

**Đề xuất:** **Go có điều kiện** cho pilot phạm vi `noi_dia + hang_nang` (loại `quoc_te` **1,88×** và `doi_tac` **0,85×**; chưa mở toàn công ty). Các điều kiện bắt buộc:
- Sửa lỗi đối soát sổ cái khi API trả 503 (ca 7) và bổ sung khoá chống trùng `idempotency_key` (ca 20) — **Kỹ sư trưởng agent**, trước ngày mở pilot (`2026-11-30`).
- Ký chấp nhận đánh đổi **MDE 6 điểm** (`n = 859`/nhóm, `m ≥ 299` yc/NV; power chỉ còn **0,64** nếu hiệu ứng thật 5 điểm) và ngưỡng an toàn `+2 điểm %` / trần `6%` — **Giám đốc vận hành LogiX-VN**, trước ngày mở pilot (`2026-11-30`).
- Bật đủ **11 event** có `trace_id` để thay thế số giờ nhân viên `simulated` bằng số đo thật sau tuần 1 — **Kỹ sư trưởng agent**, kiểm tra ngày `2026-12-07`.
- Áp dụng lộ trình giảm tỉ lệ xem lại theo bậc (từ 100% ở bước `0.10`, chỉ hạ khi `sua + bo < 15%` và thời gian xem lại `< 5` phút, vì xem lại 100% đẩy CPS lên `11.743 đ = 0,98×` đến `12.415 đ = 1,03×` `simulated`) — **Trưởng nhóm CSKH**, kiểm tra cuối bước `0.25` (`2026-12-14`).
