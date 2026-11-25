# Team

## Thông tin nhóm

- Tên nhóm: 3npc
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-3npc-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: `https://github.com/ngominhcuong/K5-L3B-DAY13-3npc-LaunchEconomics`, nhánh `main` (PR đóng gói cuối sau `0e5007d`)

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Ngô Minh Cương | 2A202603954 | 26ai.cuongnm5@vinuni.edu.vn | ngominhcuong | Người viết code (CP1–CP2) + Kiểm soát kỹ thuật |
|   2 | Đoàn Trí Hùng | 2A202603959 | 26ai.hungdt2@vinuni.edu.vn | hungdt31 | Người kiểm số (CP1–CP2) + Gắn nhãn 1 (CP3) + Người viết code (CP4–CP5) |
|   3 | Trần Quang Hà | 2A202603962 | 26ai.hatq@vinuni.edu.vn | tranha1764 | Người gắn nhãn 2 kiêm giữ hồ sơ |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

## Ngô Minh Cương - 2A202603954

### Phần việc phụ trách

- Người viết code (CP1–CP2) + Kiểm soát kỹ thuật (CP3–CP5, duyệt chéo C8).

### Đóng góp cụ thể

- Viết hàm A1–A4 và kịch bản độ nhạy B1–B4 trong `src/lab13.py`.
- Bổ sung ngưỡng đo được ca 4 và thuộc tính `pricing_version` ca 17 trong `report/team/bang_loi.md`.
- Viết 3 luật dừng 4 vế, `rollback` trong `report/team/pilot_plan.yaml`; thiết kế 11 event có `trace_id` và kiểm tra chéo trong `report/team/chi_so.md`.

### Bằng chứng

- Commit `e891e89`, `7d3e428`, `08e251b`, `6daf713`, `382ae3c`.

## Đoàn Trí Hùng - 2A202603959

### Phần việc phụ trách

- Người kiểm số (CP1–CP2) + Gắn nhãn 1 (CP3) + Đổi vai viết code (CP4–CP5, duyệt chéo C7).

### Đóng góp cụ thể

- Đối chiếu số liệu và hoàn thiện toàn bộ bảng A1–A4, B1–B4 trong `report/team/bang_chi_phi.md`.
- Gắn nhãn độc lập 20 ca lỗi (`Nhãn người 1`) và lập bảng khắc phục 5 ca trong `report/team/bang_loi.md`.
- Viết phần tính cỡ mẫu/power D1 và chỉ số E1 trong `src/lab13.py`; điền E1 và E2 rủi ro kinh tế trong `report/team/chi_so.md`.

### Bằng chứng

- Commit `62468dc`, `eb432ba`, `e3c048c`, `27068db`, `081cd8f`.

## Trần Quang Hà - 2A202603962

### Phần việc phụ trách

- Người gắn nhãn 2 kiêm giữ hồ sơ (`ho_so_launch_v0.md`, lead `pilot_plan.yaml`, `TEAM.md`, duyệt chéo C6).

### Đóng góp cụ thể

- Tổng hợp thông tin nhóm/thành viên vào `TEAM.md` và cập nhật xuyên suốt 7 mục + đề xuất `Go có điều kiện` trong `report/team/ho_so_launch_v0.md`.
- Gắn nhãn độc lập 20 ca lỗi (`Nhãn người 2`), đối chiếu đồng thuận 20/20 (100%) và soát vai trò phụ trách trong `report/team/bang_loi.md`.
- Điền D1, D2, đánh đổi và các trường cấu hình pilot trong `report/team/pilot_plan.yaml`.
- Trình bày chính 1 phút bảo vệ hồ sơ trước hội đồng `K5-L3B-404` (đạt `30/30`), chấm chéo C6 & tổng hợp `report/team/phieu_cham.md`, hoàn thiện kết quả duyệt chéo trong `report/team/group_report.md` và báo cáo cá nhân `report/team/2A202603962_TranQuangHa.md`.

### Bằng chứng

- Commit `8ee8140`, `382689f`, `5001163`, `e827c23`, `e9d5cfb`, `66336ab`, `698db7e` (và PR đóng gói cuối).
