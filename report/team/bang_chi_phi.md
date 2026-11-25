# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 | `logix_runs.csv` | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated` | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated` | simulated |
| Tổng chi phí | 4.373.585 | tổng bốn khoản trên | có phần simulated |
| Số việc thành công | 978 | `ket_qua == 'thanh_cong'` | đo từ trace |
| Chi phí mỗi việc thành công | 4.472 | tổng chi phí ÷ 978 | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | (245.585 + 84.000) ÷ 1.200 | đo từ trace |

- Chi phí mỗi việc thành công gấp bao nhiêu lần "hoá đơn chia số yêu cầu"? Gấp **16,3 lần** (`4.472 đ` [simulated] so với `274,7 đ`). Nếu so với nhân viên tự làm (`12.000 đ`), tính cả 222 ca `chuyen_nhan_vien` thì chi phí cả hệ thống là **5.865 đ/yêu cầu = 0,49×** [simulated].
- Khoản nào chiếm tỉ trọng lớn nhất trong tổng chi phí, bao nhiêu phần trăm? **Làm lại** chiếm lớn nhất: **51,8%** (`2.264.000 đ`, simulated), tiếp theo là xem lại **40,7%** (`1.780.000 đ`, simulated); tổng giờ nhân viên chiếm **92,5%** [simulated].

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ (simulated) | 0,22× (simulated) |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ (simulated) | 0,69× (simulated) |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ (simulated) | 1,88× (simulated) |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ (simulated) | 0,85× (simulated) |

- Loại nào không đáng để trợ lý xử lý? Với loại đó, cho chạy lại tới 3 lần có giúp không? **`quoc_te`** không đáng xử lý (`22.515 đ = 1,88×` [simulated], thành công `27,3%`); `doi_tac` sát ngưỡng (`0,85×` [simulated]) nên cũng loại khỏi pilot. Chạy lại tới 3 lần không giúp vì tỉ lệ `ok` của `quoc_te` giảm mạnh (`30,0%` → `11,4%` → `2,2%`), lỗi lặp lại chỉ tốn thêm tiền.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ (simulated) | 0,38× (simulated) |
| Một nửa khối lượng | 16.875 | 2.370 đ | 5.784 đ (simulated) | 0,48× (simulated) |

- Chi phí cố định có đổi kết luận không? Ở khối lượng nào? Không đổi kết luận ở cả `45.000` yc/tháng (`4.599 đ = 0,38×` [simulated]) lẫn nửa khối lượng `22.500` yc/tháng (`5.784 đ = 0,48×` [simulated]), vẫn rẻ hơn `12.000 đ`. Tuy nhiên chi phí cố định/việc tăng gấp đôi (`1.185 đ` → `2.370 đ`) khi khối lượng giảm một nửa.

## B1 · Đổi từng yếu tố

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | ... | ... |
| Giá token giảm một nửa | 13 đ và 65 đ | ... | ... |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | ... | ... |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | ... | ... |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | ... | ... |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | ... | ... |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | ... | ... |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | ... | ... |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | ... | ... |

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: ...
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: 1. ... · 2. ... · 3. ...

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | ... | ... | ... | ... |
| 2 lần | ... | ... | ... | ... |
| 3 lần | ... | ... | ... | ... |

- Giới hạn nào rẻ nhất cho công ty? Có trùng với giới hạn cho chi phí mỗi việc thành công thấp nhất không? ...

## B4 · Nếu phải xem lại tất cả

- Chi phí mỗi việc thành công khi xem lại 100% (`noi_dia` + `hang_nang`), so với 12.000 đ: ...
- Kết quả này nói gì về thứ pilot cần học được? ...
