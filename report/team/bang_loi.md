# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Đối chiếu nhãn

Người gắn nhãn 1: Phạm Văn Chiêu (đã duyệt bộ nhãn có hỗ trợ AI) · Người gắn nhãn 2: Nguyễn Văn Lâm (bộ nhãn đã ghi trong repo).

Bảng dưới dùng để thảo luận các ca lệch. Tỷ lệ đồng thuận chính thức cần hai bộ nhãn gốc được làm độc lập trong 8 phút.

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | ... |
| 2 | Hệ thống | Hệ thống | Có | ... |
| 3 | Ngữ cảnh | Hệ thống | Không | ... |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | ... |
| 5 | Ngầm | Ngầm | Có | ... |
| 6 | Do người dùng | Ngữ cảnh | Không | ... |
| 7 | Hệ thống | Hệ thống | Có | ... |
| 8 | Hệ thống | Ngầm | Không | ... |
| 9 | Do người dùng | Giới hạn hệ thống | Không | ... |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | ... |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | ... |
| 12 | Ngầm | Ngầm | Có | ... |
| 13 | Giới hạn hệ thống | Hệ thống | Không | ... |
| 14 | Do người dùng | Do người dùng | Có | ... |
| 15 | Hệ thống | Hệ thống | Có | ... |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | ... |
| 17 | Ngầm | Ngầm | Có | ... |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | ... |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | ... |
| 20 | Hệ thống | Hệ thống | Có | ... |

**Tỉ lệ trùng khi đối chiếu tham khảo:** 15 / 20 = 75% (lệch ở ca 3, 6, 8, 9 và 13).

**Tỉ lệ đồng thuận từ hai bộ nhãn độc lập:** Chờ xác nhận.

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- Ca 3 — Đề xuất phân biệt Ngữ cảnh với Hệ thống bằng cách kiểm tra trợ lý có hoàn đúng kênh quy định hay đã chọn sai kênh.
- Ca 6 — Đề xuất xem khách chọn nhầm luồng hay luồng được chọn đúng nhưng giả định của hệ thống chưa khớp tình huống.
- Ca 8 — Đề xuất tách việc dẫn sai điều khoản khỏi câu hỏi lỗi lộ ngay hay chỉ được phát hiện khi kiểm tra sau.
- Ca 9 — Đề xuất xem khách có thể sửa mã nhập sang loại hợp lệ hay yêu cầu vẫn vượt khả năng tra cứu khi mã đã đúng.
- Ca 13 — Đề xuất phân biệt yêu cầu ngoài phạm vi bảo hiểm với cách trợ lý phản hồi sai khi gặp yêu cầu ngoài phạm vi.

Hai người gắn nhãn sẽ xác nhận quy tắc và điền nhãn thống nhất sau khi trao đổi.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

Bản nháp dùng năm ca có cùng nhãn trong lần đối chiếu. Nhóm sẽ rà lại cách đo và người phụ trách khi chốt.

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Trước mỗi lệnh hoàn, ghi sự kiện `refund_account_validation_failed` kèm `trace_id` nếu số tài khoản không hợp lệ theo quy tắc của ngân hàng nhận. | Yêu cầu khách kiểm tra lại số tài khoản và chỉ gửi lệnh sau khi dữ liệu hợp lệ. | Kỹ sư tích hợp thanh toán |
| 7 | Hệ thống | Với mỗi thông báo hoàn thành công, kiểm có xác nhận ghi sổ cái theo `trace_id`. Cảnh báo khi có ít nhất một thông báo thiếu xác nhận. | Giữ trạng thái chờ xác minh và chuyển cho nhân viên đối soát nếu hết lượt thử lại. | Kỹ sư phụ trách sổ cái |
| 16 | Ngữ cảnh | Kiểm giờ địa phương của mỗi thông báo Zalo. Ghi sự kiện kèm `trace_id` nếu gửi trong khung giờ yên lặng đề xuất từ 22:00 đến trước 07:00. | Đưa thông báo vào hàng đợi và gửi sau khi hết khung giờ yên lặng. | Phụ trách sản phẩm thông báo |
| 11 | Giới hạn hệ thống | Ghi sự kiện `unsupported_input` kèm `trace_id` cho mỗi đầu vào âm thanh khi kênh chưa hỗ trợ. | Yêu cầu nhập bằng chữ và cung cấp lựa chọn chuyển sang nhân viên nếu khách cần hỗ trợ. | Phụ trách kênh CSKH |
| 5 | Ngầm | Mỗi tuần đối soát các lệnh hoàn của đơn có mã giảm giá với số tiền thực trả. Mở ca kiểm tra khi phát hiện ít nhất một lệnh hoàn vượt số tiền thực trả. | Sửa nguồn tiền dùng để tính hoàn và chuyển các lệnh lệch cho nhân viên đối soát. | Phụ trách đối soát hoàn phí |
