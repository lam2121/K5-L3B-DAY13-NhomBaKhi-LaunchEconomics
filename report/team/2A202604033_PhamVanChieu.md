# Báo cáo cá nhân — Phạm Văn Chiêu

## 1. Thông tin thành viên

- Họ tên: Phạm Văn Chiêu
- MSSV: 2A202604033
- Email: chieupham1011@gmail.com
- GitHub: pvchiu
- Nhóm: NhomBaKhi
- Vai trong nhóm: Người gắn nhãn 1

## 2. Phần việc phụ trách

- Đọc đề và theo dõi điều kiện “Xong khi” ở từng checkpoint.
- Gắn nhãn độc lập 20 ca lỗi trong 8 phút ở CP3. Giữ bộ nhãn riêng cho đến khi cả hai người gắn nhãn đã chốt.
- Phối hợp với Nguyễn Văn Lâm để đối chiếu hai bộ nhãn gốc, tính tỷ lệ đồng thuận, ghi quy tắc cho các ca bất đồng và hoàn thiện bảng khắc phục 5 ca.

## 3. Đóng góp cụ thể

- Duyệt bộ 20 nhãn tham khảo có hỗ trợ AI và ghi kết quả đối chiếu với bộ nhãn Nguyễn Văn Lâm đã công bố.
- Chuẩn bị quy tắc cho 5 ca lệch và cùng Nguyễn Văn Lâm chốt nhãn thống nhất, duyệt bảng khắc phục cho 5 loại lỗi.

## 4. Bằng chứng

- [Bảng lỗi CP3](bang_loi.md): kết quả đối chiếu độc lập đạt 15/20 ca trùng (75%, lệch ở ca 3, 6, 8, 9, 13). Nhóm đã viết lại định nghĩa/quy tắc phân biệt cho 5 ca lệch và thống nhất giữ nhãn theo cột Người 1, đủ điều kiện nghiệm thu CP3.
- Các commit trên repo: commit `0d77751` (ghi nhận đối chiếu nhãn CP3 và báo cáo cá nhân), commit `c621ea6` (chốt nhãn thống nhất CP3 và bảng khắc phục).

## 5. Công cụ AI đã dùng

- Codex / Gemini hỗ trợ đọc tài liệu, rà tiêu chí “Xong khi”, đề xuất 20 nhãn tham khảo, đối chiếu từng ca và soạn nháp quy tắc phân biệt cùng bảng khắc phục.
- Tôi đã tự đọc đề, rà soát và duyệt lại toàn bộ nhãn tham khảo, đối chiếu độc lập từng ca với Nguyễn Văn Lâm, cùng thống nhất quy tắc phân biệt cho các ca lệch và duyệt bảng khắc phục.

## 6. Tự đánh giá

- **Dấu hiệu phân biệt ca dễ nhầm:** Ca 6 và ca 9 rất dễ nhầm giữa lỗi "Do người dùng" và "Hệ thống" / "Giới hạn hệ thống". Dấu hiệu cốt lõi là bám sát nguyên nhân gốc: nếu khách chọn sai luồng hoặc nhập sai mã ngay từ đầu thì gốc rễ là lỗi Do người dùng; việc trợ lý thiếu tính năng gợi ý chỉ là biện pháp xử lý ở cột khắc phục chứ không thay đổi bản chất nguyên nhân lỗi ban đầu.
- **Điểm rút kinh nghiệm:** Ở lần gắn nhãn sau, cần thống nhất kỹ bảng định nghĩa 5 loại lỗi của Google PAIR với các thành viên trước khi gắn nhãn độc lập để đạt tỷ lệ đồng thuận cao hơn (> 80%) ngay từ vòng đầu tiên mà không mất nhiều thời gian thảo luận quy tắc phân biệt.
