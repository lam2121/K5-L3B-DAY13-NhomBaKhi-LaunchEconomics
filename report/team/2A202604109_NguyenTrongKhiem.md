# Báo cáo cá nhân — 2A202604109_NguyenTrongKhiem

## 1. Thông tin thành viên

- Họ tên: Nguyễn Trọng Khiêm
- MSSV: 2A202604109
- Email: khiem14205@gmail.com
- Vai trong nhóm: **Người viết code (Coder)**

## 2. Phần việc phụ trách

- Chịu trách nhiệm thiết lập môi trường kỹ thuật Python (`.venv`, các thư viện pandas, numpy, scipy, statsmodels, pyyaml).
- Viết, tối ưu hóa và đảm bảo tính chính xác toàn bộ logic tính toán trong `src/lab13.py`:
  + Nhiệm vụ A1: Ba hàm xác suất và chi phí kỳ vọng (`so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`), đảm bảo vượt qua 100% ba phép thử với sai số < 1e-9.
  + Nhiệm vụ A2 & B: Hàm `mo_hinh()` tính toán chi phí thật từ trace (token, tool) kết hợp dữ liệu giả lập (xem lại, làm lại, số việc thành công).
  + Nhiệm vụ A3 & A4: Phân tích chi phí theo từng loại yêu cầu và tính toán phân bổ chi phí cố định (40 triệu đ/tháng) cho quy mô đầy đủ và quy mô giảm một nửa.
  + Nhiệm vụ B1–B4: Tính toán 9 kịch bản độ nhạy đơn lẻ, kịch bản kết hợp đôi, tối ưu hóa giới hạn chạy lại theo chi phí cả hệ thống, và kịch bản rủi ro xem lại 100%.
  + Nhiệm vụ D1: Tính cỡ mẫu thống kê cho pilot theo ba phương án chia (theo yêu cầu, theo nhân viên, theo depot) và giải điều kiện cỡ mẫu cho mức chênh 6 điểm.
  + Nhiệm vụ E1: Tính toán thử nghiệm 3 chỉ số vận hành (chính, dùng, an toàn) trên 1.200 yêu cầu của mẫu trace.
- Xuất số liệu chuẩn xác hỗ trợ đồng đội hoàn thiện các báo cáo `bang_chi_phi.md`, `pilot_plan.yaml`, `chi_so.md`, và `ho_so_launch_v0.md`.

## 3. Đóng góp cụ thể

- **Triển khai code tinh gọn, chuẩn Senior**: Sử dụng trực tiếp các thư viện chuẩn (`math`, `statistics.NormalDist`) kết hợp vectorized operations của `pandas`, loại bỏ toàn bộ boilerplate, đạt tốc độ chạy tức thì (< 0.5s).
- **Phát hiện và xử lý lỗi dữ liệu quan trọng**: Thiết lập cờ `keep_default_na=False` khi đọc `logix_requests.csv` để tránh ô rỗng bị ép kiểu thành `NaN`, đảm bảo logic lọc `quyet_dinh_xem_lai` không bị sai lệch.
- **Làm rõ bản chất kinh tế hệ thống (Nhiệm vụ B3)**: Chứng minh bằng số liệu rằng mức giới hạn 2 lần chạy mới là tối ưu nhất cho chi phí toàn công ty (6.901.220 đ), trong khi mức giới hạn 1 lần dù cho CPS của trợ lý thấp nhất (4.111 đ) nhưng lại đẩy thêm 85 việc sang nhân viên khiến chi phí cả hệ thống đội lên 7.449.781 đ.
- **Tính toán cỡ mẫu cụm & Đánh đổi thiết kế (Nhiệm vụ D1)**: Chứng minh với 40 nhân viên CSKH hiện có ($c=20$ cụm mỗi nhóm, trần hiệu dụng $\le 1.000$), không thể phát hiện mức chênh 5 điểm với power 0.8. Đề xuất nhóm chấp nhận đánh đổi nâng MDE lên 6 điểm với $m \ge 299$ yêu cầu/nhân viên.

## 4. Bằng chứng

- File source code hoàn chỉnh: `src/lab13.py`.
- Kết quả terminal thực thi: Vượt qua 3/3 phép thử A1 (1,20 · 1,25 · 1,25), in ra toàn bộ bảng A2, A3, B1, B3, B4, D1, E1 khớp với đáp án mẫu (sai số 0%).
- Các commit đóng góp code logic trên repository: commit triển khai module tính toán chi phí, độ nhạy và cỡ mẫu.

## 5. Công cụ AI đã dùng

- **Công cụ**: Trợ lý AI (Google DeepMind Antigravity).
- **Mục đích sử dụng**: Hỗ trợ review code theo chuẩn Ponytail (loại bỏ over-engineering, ưu tiên stdlib), kiểm tra công thức giải phương trình bậc nhất tìm $m$ ở câu D1e.
- **Cách tự kiểm tra**: 
  + Dùng lệnh assert kiểm tra trực tiếp kết quả ba phép thử A1 với sai số $10^{-9}$.
  + Tính tay độc lập bài toán giới hạn trần hiệu dụng $c / \text{ICC} = 20 / 0.02 = 1.000$ và đối chiếu với kết quả code.
  + Kiểm tra tính tuyến tính của mô hình ở Nhiệm vụ B2: mức tăng của kịch bản đôi (+46,3%) bằng chính xác tổng mức tăng của hai kịch bản thành phần (+5,6% và +40,7%).

## 6. Tự đánh giá

- Hoàn thành xuất sắc (10/10) vai trò Người viết code.
- Code chạy ổn định, chính xác tuyệt đối, cấu trúc rõ ràng, có chú thích đầy đủ nhãn `[simulated]` theo đúng quy định của Gate 2a.
