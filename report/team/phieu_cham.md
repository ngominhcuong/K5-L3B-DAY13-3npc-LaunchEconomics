# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): 3npc (Lớp L3B)
- Nhóm được chấm: 404 (`KemmVSAI/K5-L3B-DAY13-404-LaunchEconomics`)

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 5 | Đề xuất `Go có điều kiện` khớp ở việc thu hẹp phạm vi (`noi_dia + hang_nang`, loại `quoc_te` `1,88×` và `doi_tac` `0,85×`), nhưng **bỏ qua các con số bất lợi**: không nêu power còn `~0,64` khi chọn MDE `6` điểm (`859`/nhóm), không nêu chi phí kịch bản xem lại 100% B4 (`11.743–12.415 đ`) và thiếu lộ trình hạ xem lại; Mục 4 chưa ghi 3 con số tính thử (`82,83%`, `27,12%`, `4,25%`); Mục 1–4 ghi `"Người kiểm số"` thay cho vai trò công ty. |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 10 | Gắn `[simulated]` và trạng thái `Giả lập` ở các mục số liệu giả lập (Mục 1, 2, 3, 6, 7), Điều kiện 3 yêu cầu chuyển sang `"chi phí đo thật"`; thu hẹp phạm vi về `noi_dia + hang_nang` có lý do bằng số (`quoc_te` `1,88×`, `doi_tac` `0,85×`). *(Góp ý thêm: nên bổ sung CPS riêng của `noi_dia` `0,22×`, `hang_nang` `0,69×` và chi phí cố định `40 triệu/tháng`.)* |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 5 | Đạt đối chứng đồng thời, chia `20/20` nhân viên đủ cụm và đủ mẫu cho MDE `6` điểm (`859`/nhóm, `~299` yc/người, hạn `2027-01-05`), có ngưỡng `6%` (3 ngày), `8.000 đ/việc` (2 tuần), `40%`; nhưng trong `ho_so_launch_v0.md` **chưa ghi rõ thời hạn cho ngưỡng `40%`**, thiếu vế hành động dừng/cơ chế rollback mất bao lâu, chưa nêu cách giảm spillover, và Điều kiện 1 giao `"Người kiểm số"` thay cho vai trò có thẩm quyền. *(Có thể cân nhắc nâng lên `10` nếu đội trình chứng minh đủ 3 luật 4 vế & rollback trong `pilot_plan.yaml` khi hỏi–đáp.)* |
| **Tổng** | | | | **20 / 30** | |

**Quyết định của hội đồng:** Go có điều kiện

**Lý do:** Hồ sơ của nhóm 404 có mô hình chi phí chặt chẽ (`4.472 đ` CPS, `5.865 đ = 0,49×` cả hệ thống `[simulated]`), thu hẹp phạm vi hợp lý khỏi `quoc_te` (`1,88×`) và `doi_tac` (`0,85×`), đồng thuận gắn nhãn `20/20 (100%)` và thiết kế được pilot chia cụm `20/20` nhân viên (`859` yc/nhóm). Tuy nhiên, để đủ điều kiện mở pilot cần bổ sung: (1) công khai và ký chấp nhận đánh đổi power `~0,64` ở mức 5 điểm; (2) bổ sung kịch bản xem lại 100% (B4) và lộ trình giảm tỉ lệ xem lại theo bậc để giữ chi phí dưới `8.000 đ/việc`; (3) làm rõ cơ chế rollback và chuẩn hóa vai trò phụ trách sang vai trò vận hành công ty thay cho `"Người kiểm số"`.

**Một câu hỏi cho đội trình:** Nếu tuần đầu pilot phải xem lại 100% câu trả lời (kịch bản B4), chi phí mỗi việc thành công là bao nhiêu so với `12.000 đ`, và nhóm có lộ trình gì để hạ về dưới ngưỡng `8.000 đ/việc` ở Điều kiện 3 (cũng như cơ chế rollback và đánh đổi power ở mức 5 điểm)?

**Câu trả lời của đội trình (ghi lại tại buổi):** Dựa trên hồ sơ đã gửi, nhóm 404 chọn giới hạn phạm vi `noi_dia + hang_nang` (loại `quoc_te` `1,88×`, tạm loại `doi_tac` `0,85×`), chia `20/20` nhân viên (`859` yc/nhóm, `~299` yc/người, chốt `2027-01-05`) và đặt 3 điều kiện theo dõi trần mở lại `6%` (3 ngày), chi phí đo thật `≤ 8.000 đ/việc` (2 tuần) và bỏ qua gợi ý `≤ 40%`; hồ sơ hiện **chưa nêu** con số xem lại 100% (B4), lộ trình hạ xem lại theo bậc, con số power `~0,64` ở mức 5 điểm hay thời gian rollback cụ thể.
