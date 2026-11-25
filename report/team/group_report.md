# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: 3npc
- Lớp: L3B
- Thành viên: xem [TEAM.md](../../TEAM.md) (Ngô Minh Cương, Đoàn Trí Hùng, Trần Quang Hà)

## 2. Mục tiêu và cách tiếp cận

Nhóm xây dựng bộ **hồ sơ launch v0** cho trợ lý hoàn phí của LogiX-VN từ dữ liệu giả lập (`1.200` yêu cầu, `1.624` lần chạy) nhằm trả lời 4 câu hỏi cốt lõi trước hội đồng **Gate 2a**: chi phí thật mỗi việc thành công, mức độ sử dụng và bộ event theo dõi, phân loại lỗi kèm phương án khắc phục, và thiết kế pilot có đối chứng đủ cỡ mẫu kèm luật dừng viết trước.

Nhóm 3 thành viên chia việc song song theo từng checkpoint (CP1–CP5) để tránh xung đột file: đổi người viết code sau giờ giải lao (Ngô Minh Cương viết A1–B4, Đoàn Trí Hùng viết D1–E1 và chạy kiểm chứng trên máy thứ 2), hai người gắn nhãn độc lập 20 ca lỗi ở CP3, và Trần Quang Hà giữ hồ sơ `ho_so_launch_v0.md` xuyên suốt từ đầu buổi.

## 3. Giải pháp

- **Nhiệm vụ A & B (Mô hình chi phí và độ nhạy):** viết `src/lab13.py` qua 3 phép thử A1 (`1,20 · 1,25 · 1,25`), tính chi phí theo trace (tử số tính mọi lần chạy kể cả lỗi, mẫu số chỉ đếm việc thành công), tách theo 4 loại yêu cầu, cộng chi phí cố định 40 triệu đ/tháng và chạy 9 kịch bản độ nhạy + kịch bản cặp + giới hạn chạy lại + xem lại 100%. Chi tiết: [bang_chi_phi.md](bang_chi_phi.md).
- **Nhiệm vụ C (Phân loại lỗi & khắc phục):** hai thành viên gắn nhãn độc lập 20 ca lỗi theo 5 loại Google PAIR trong 8 phút, đạt đồng thuận `20/20 (100%)`, lập bảng khắc phục 5 ca (đủ 5 loại) có cách phát hiện đo được và 1 vai trò phụ trách. Chi tiết: [bang_loi.md](bang_loi.md).
- **Nhiệm vụ D (Kế hoạch pilot):** tính cỡ mẫu theo 3 đơn vị chia (yêu cầu, nhân viên, depot), chọn chia theo `staff` (`20+20` cụm, phân tầng theo depot), chấp nhận đánh đổi MDE 6 điểm (`m >= 299` yc/NV, `DE = 6,96`), thiết kế 3 luật dừng đủ 4 vế `NẾU – TRONG – THÌ – KHÔNG THÌ` và cơ chế rollback 30 phút. Chi tiết: [pilot_plan.yaml](pilot_plan.yaml).
- **Nhiệm vụ E (Chỉ số, event, rủi ro & hồ sơ launch v0):** tính thử 3 chỉ số trên 1.200 yêu cầu, đề xuất thêm 2 chỉ số (dùng và an toàn), thiết kế 11 event có `trace_id` khớp chéo với chỉ số và bảng lỗi, lập 3 dòng rủi ro kinh tế và tổng hợp 1 trang hồ sơ Gate 2a. Chi tiết: [chi_so.md](chi_so.md), [ho_so_launch_v0.md](ho_so_launch_v0.md).

## 4. Kết quả

- **Chi phí thật & so sánh baseline:** CPS toàn mẫu là **4.472 đ** (`simulated`), gấp **16,3×** hoá đơn token+tool (`274,7 đ/yc`); giờ nhân viên chiếm **92,5%** (làm lại `51,8%`, xem lại `40,7%`). Tính cả `222` ca không thành công (`× 12.000 đ`), chi phí cả hệ thống là **5.865 đ/yc = 0,49×** (`simulated`).
- **Phạm vi pilot & cố định:** chỉ chọn `noi_dia` (`2.696 đ = 0,22×`) và `hang_nang` (`8.221 đ = 0,69×`), loại `quoc_te` (`22.515 đ = 1,88×`, tỉ lệ `ok` tụt `30,0% → 11,4% → 2,2%`) và `doi_tac` (`10.215 đ = 0,85×`). Cộng cố định 40 triệu đ/tháng trong phạm vi: **4.599 đ (`0,38×`)** ở 45.000 yc/tháng và **5.784 đ (`0,48×`)** ở 22.500 yc/tháng (`simulated`).
- **Độ nhạy & điểm gãy:** Top 3 yếu tố nhạy nhất là **1. Làm lại (`+51,8%`) · 2. Xem lại (`+40,7%`) · 3. Lương nhân viên (`+23,1%`)** (`simulated`). Giới hạn **2 lần chạy** rẻ nhất cho cả hệ thống (`6.901.220 đ`), khác với CPS thấp nhất ở 1 lần (`4.111 đ`). Xem lại 100% đẩy CPS lên **11.743 đ (`0,98×`)** (9 phút làm lại) đến **12.415 đ (`1,03×`)** (15,3 phút thực tế, `simulated`).
- **Chỉ số đợt chạy thử (chưa có đối chứng):** chính **82,83%** (`994/1.200`), bỏ qua gợi ý **27,12%** (`48/177`), mở lại 7 ngày **4,25%** (`51/1.200`).
- **Đề xuất cuối ([ho_so_launch_v0.md](ho_so_launch_v0.md)):** **Go có điều kiện** cho pilot `noi_dia + hang_nang` với 4 điều kiện có người phụ trách và ngày kiểm tra (sửa ca 7 & 20; ký chấp nhận MDE 6 điểm / power `0,64` ở mức 5 điểm; bật đủ 11 event `trace_id` thay số `simulated` sau tuần 1; có lộ trình giảm xem lại theo bậc).
- **Kết quả duyệt chéo Gate 2a:** Hội đồng nhóm **K5-L3B-404** chấm **30/30 điểm** (C6: `10/10`, C7: `10/10`, C8: `10/10`) với quyết định **`Go có điều kiện`** (ghi nhận trình bày nhất quán với bằng chứng, nêu rõ con số bất lợi và nhãn `simulated`; câu hỏi phản biện tập trung vào lý do chọn MDE `6` điểm thay cho `5` điểm và đánh đổi power `~0,64`). Phiếu nhóm mình chấm nhóm 404 (`20/30`, `Go có điều kiện`) nằm tại [phieu_cham.md](phieu_cham.md).

## 5. Khó khăn và cách xử lý

- **Nhóm 3 người so với khung 4 vai của đề:** khắc phục bằng cách gộp vai kiểm soát kỹ thuật cho thành viên 1, chuyển vai viết code cho thành viên 2 sau giờ giải lao (CP4–CP5), và tách file theo từng checkpoint để làm song song không xung đột Git.
- **Giới hạn 40 nhân viên không đủ mẫu cho mức chênh 5 điểm theo cụm:** nhóm tính rõ trần cỡ mẫu hiệu dụng (`1.000 < 1.251`), chọn chia theo `staff` (`20+20` cụm) để bảo đảm tách tác động và công khai đánh đổi MDE 6 điểm (power `0,64` nếu hiệu ứng thật 5 điểm) ngay trong `pilot_plan.yaml` và `ho_so_launch_v0.md`.

## 6. Tổng hợp đóng góp

Chi tiết phân vai, đóng góp cụ thể và danh sách commit của từng thành viên được khai báo đầy đủ trong [TEAM.md](../../TEAM.md) và các báo cáo cá nhân trong `report/team/`.

## 7. Hạn chế và hướng cải thiện

- Thời gian xem lại và làm lại hiện là số `simulated`; cần thu thập dữ liệu đo thật từ 2 event `staff_review_decision` và `staff_rework_completed` ngay trong tuần 1 pilot để hiệu chỉnh lại mô hình chi phí.
- Độ nhạy B4 cho thấy xem lại 100% không mang lại lợi ích kinh tế; cần thử nghiệm lộ trình hạ tỉ lệ xem lại theo ngưỡng tin cậy và rút thời gian xem lại xuống dưới `5` phút/ca.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, [arxiv.org/abs/2504.13359](https://arxiv.org/abs/2504.13359)
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure", [pair.withgoogle.com](https://pair.withgoogle.com)
- Tài liệu `statsmodels`, lớp `NormalIndPower` (`stats.power`)
