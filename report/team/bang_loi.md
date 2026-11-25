# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Đối chiếu nhãn

Người gắn nhãn 1: Phạm Văn Chiêu (đã duyệt bộ nhãn có hỗ trợ AI) · Người gắn nhãn 2: Nguyễn Văn Lâm (bộ nhãn đã ghi trong repo).

Cột nhãn thống nhất ghi kết quả đã chốt sau khi hai người trao đổi. Tỷ lệ đồng thuận chính thức cần hai bộ nhãn gốc được làm độc lập trong 8 phút.

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Hệ thống | Không | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Ngữ cảnh | Không | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Ngầm | Không | Hệ thống |
| 9 | Do người dùng | Giới hạn hệ thống | Không | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Hệ thống | Không | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận giữa hai bộ nhãn:** 15 / 20 = 75% (lệch ở 5 ca: 3, 6, 8, 9 và 13). Sau khi viết lại định nghĩa và thống nhất quy tắc phân biệt, bộ nhãn thống nhất khớp 20 / 20 = 100% nhãn tham khảo.

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- Ca 3 — Phân biệt Ngữ cảnh với Hệ thống bằng cách kiểm tra trợ lý có hoàn đúng kênh quy định hay đã chọn sai kênh.
- Ca 6 — Xem khách chọn nhầm luồng hay luồng được chọn đúng nhưng giả định của hệ thống chưa khớp tình huống.
- Ca 8 — Tách việc dẫn sai điều khoản khỏi câu hỏi lỗi lộ ngay hay chỉ được phát hiện khi kiểm tra sau.
- Ca 9 — Xem khách có thể sửa mã nhập sang loại hợp lệ hay yêu cầu vẫn vượt khả năng tra cứu khi mã đã đúng.
- Ca 13 — Phân biệt yêu cầu ngoài phạm vi bảo hiểm với cách trợ lý phản hồi sai khi gặp yêu cầu ngoài phạm vi.

Hai người gắn nhãn đã chốt giữ nhãn ở cột Người 1 cho năm ca lệch.

### Định nghĩa đã viết lại (do đồng thuận 75% < 80%)

Gắn nhãn theo **nguyên nhân gốc**, không theo vị trí cần sửa:

- **Do người dùng:** Khách nhập sai/thiếu thông tin, chọn nhầm luồng hoặc bấm nhầm (ca 1, 6, 9, 14); thiếu gợi ý sửa nằm ở phần khắc phục.
- **Hệ thống:** Trợ lý làm sai thiết kế/chính sách, bịa căn cứ hoặc lỗi tích hợp **và có người/log thấy ngay** (ca 2, 7, 8, 15, 20).
- **Ngữ cảnh:** Trợ lý làm **đúng thiết kế và chính sách**, nhưng giả định ngầm không khớp hoàn cảnh/kỳ vọng khách (ca 3, 10, 16, 18).
- **Giới hạn hệ thống:** Yêu cầu ngoài phạm vi, thiếu dữ liệu hoặc định dạng không hỗ trợ (ca 4, 11, 13, 19), kể cả khi cách từ chối chưa khéo.
- **Ngầm:** Có sai sót về số tiền hoặc chi phí nhưng **cả khách lẫn hệ thống không nhận ra** cho tới khi đối soát/kiểm tra mẫu (ca 5, 12, 17).

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

Hai người gắn nhãn đã duyệt bảng khắc phục cho năm ca có cùng nhãn trong lần đối chiếu.

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Event `refund_account_validation_failed` kèm `trace_id` trước mỗi lệnh hoàn; tổng hợp theo ngày, cảnh báo khi `> 2%` số yêu cầu/ngày. | Yêu cầu khách kiểm tra lại số tài khoản và chỉ gửi lệnh sau khi dữ liệu hợp lệ. | Kỹ sư tích hợp thanh toán |
| 7 | Hệ thống | Đối soát mỗi giờ giữa thông báo hoàn thành công và bản ghi sổ cái `ok` theo `trace_id`; cảnh báo khi `≥ 1` ca thiếu xác nhận. | Giữ trạng thái chờ xác minh và chuyển cho nhân viên đối soát nếu hết lượt thử lại. | Kỹ sư phụ trách sổ cái |
| 16 | Ngữ cảnh | Event `zalo_quiet_hours_sent` kèm `trace_id` khi kiểm tra giờ địa phương trong khung `22:00–07:00`; cảnh báo theo ngày khi `≥ 1` ca vi phạm. | Đưa thông báo vào hàng đợi và gửi sau khi hết khung giờ yên lặng. | Phụ trách sản phẩm thông báo |
| 11 | Giới hạn hệ thống | Event `unsupported_input` (`type=audio`) kèm `trace_id` cho mỗi đầu vào âm thanh; tổng hợp theo tuần, cảnh báo khi `> 5%` tổng yêu cầu. | Yêu cầu nhập bằng chữ và cung cấp lựa chọn chuyển sang nhân viên nếu khách cần hỗ trợ. | Phụ trách kênh CSKH |
| 5 | Ngầm | Đối soát hằng tuần các lệnh hoàn đơn có mã giảm giá (kèm `trace_id`) với số tiền thực trả; mở ca kiểm tra khi `≥ 1` lệnh vượt số tiền thực trả. | Sửa nguồn tiền dùng để tính hoàn và chuyển các lệnh lệch cho nhân viên đối soát. | Phụ trách đối soát hoàn phí |
