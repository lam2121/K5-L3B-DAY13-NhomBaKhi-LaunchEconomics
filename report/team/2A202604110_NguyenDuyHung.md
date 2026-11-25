# Báo cáo cá nhân — NguyenDuyHung

> Lưu ý nộp bài: Đổi tên file thành `<MSSV>_NguyenDuyHung.md` (theo quy tắc `report/team/MSSV_HoTen.md` trong `SUBMISSION.md`) sau khi điền MSSV. Giữ nguyên file mẫu `MSSV_HoTen.md`.

## 1. Thông tin thành viên

- Họ tên: Nguyễn Duy Hưng
- MSSV: 2A202604110
- Email: nguyenduyhung101010@gmail.com
- GitHub: Hungnd1208
- Vai trong nhóm: **Người kiểm số (Thành viên 2)**

## 2. Phần việc phụ trách

- Kiểm số độc lập cho code tính toán trong `src/lab13.py`, đối chiếu công thức và số liệu với tài liệu `docs/du_lieu_va_cong_thuc.md`.
- Điền, kiểm chứng và hoàn thiện toàn bộ bảng số liệu và câu trả lời ở Nhiệm vụ A (A1–A4) và Nhiệm vụ B (B1–B4) trong `report/team/bang_chi_phi.md`.
- Kiểm soát tuân thủ quy tắc của lab: gắn nhãn `simulated` cho mọi số liệu tính từ các cột `_simulated`, câu trả lời $\le 3$ dòng có số liệu, không chứa từ cấm trong hồ sơ.
- (Tiếp theo ở CP3–CP5): Hỗ trợ kiểm tra đồng thuận/quy tắc bảng lỗi (`bang_loi.md`), kiểm chứng cỡ mẫu & tính hợp lệ của `pilot_plan.yaml`, đối chiếu chỉ số/rủi ro (`chi_so.md`), soát hồ sơ `ho_so_launch_v0.md` và chạy kiểm thử `src/lab13.py` trên máy thứ hai.

## 3. Đóng góp cụ thể

- **CP1 — Kiểm số Nhiệm vụ A (`bang_chi_phi.md`):**
  - Chạy kiểm thử `src/lab13.py` trên máy cá nhân (Python 3.12.10), xác nhận đạt 3/3 phép thử A1 (`1,20`, `1,25`, `1,25`).
  - Đối chiếu độc lập từng khoản chi phí A2 trên `1.200` yêu cầu (`1.624` lần chạy): token `245.585 đ`, tool `84.000 đ` (`93.804 đ` ở attempt > 1), xem lại `1.780.000 đ` (`simulated`), làm lại `2.264.000 đ` (`simulated`), tổng `4.373.585 đ`, CPS `4.472 đ` (`simulated`, gấp `16,3 lần` hoá đơn `274,7 đ/yc`), và chi phí cả hệ thống `5.865 đ/yc = 0,49×` (`simulated`).
  - Tính kiểm chứng tỉ lệ `ok` theo từng lần thử (`attempt` 1, 2, 3) cho A3 (`quoc_te` giảm từ `30,00%` $\rightarrow$ `11,43%` $\rightarrow$ `2,15%`) và xác nhận phân bổ chi phí cố định A4 cho phạm vi `noi_dia` + `hang_nang` (`4.599 đ = 0,38×` ở quy mô 45.000 yc/tháng; `5.784 đ = 0,48×` ở nửa khối lượng, `simulated`).
- **CP2 — Kiểm số Nhiệm vụ B (`bang_chi_phi.md`):**
  - Kiểm chứng 9 kịch bản B1 bằng tính đối xứng (mức giảm khi giảm một nửa bằng đúng 1/2 mức tăng khi gấp đôi) và kiểm tra tính cộng tuyến tính ở B2 (`Token x2 + Xem lại x2 = 6.543 đ`, `+46,3%`, `simulated`).
  - Đối chiếu bài toán tối ưu chi phí cả hệ thống B3: xác nhận giới hạn `2 lần` rẻ nhất cho công ty (`6.901.220 đ`, `simulated`), khác với giới hạn `1 lần` cho CPS thấp nhất (`4.111 đ`, `simulated`, đẩy thêm `85` ca sang nhân viên).
  - Kiểm chứng B4 (`noi_dia` + `hang_nang` xem lại 100%) ở cả hai mức phút làm lại (`9 phút`: `11.743 đ = 0,98×`; trung bình thực tế `15,3 phút`: `12.415 đ = 1,03×`, `simulated`) và tính mức hoà vốn thời gian xem lại (`≤ 5,1 phút` và `≤ 4,8 phút`).

## 4. Bằng chứng

- File báo cáo chi phí đã hoàn thiện A1–A4 và B1–B4: `report/team/bang_chi_phi.md`.
- Các commit đã đẩy lên nhánh `main` cho phần Nhiệm vụ A và B: `3919c20` (`bangchiphi`), `97dc3d6` (`nhiem vu b`).
- Kết quả chạy kiểm chứng `src/lab13.py` và đối chiếu độc lập bằng Python trên `src/logix_runs.csv` và `src/logix_requests.csv`.

## 5. Công cụ AI đã dùng

- **Công cụ:** Antigravity (trợ lý AI).
- **Mục đích sử dụng:** Hỗ trợ viết script Python đối chiếu độc lập số liệu từ hai file CSV, tính mức hoà vốn B4 và tỉ lệ `ok` theo `attempt` ở A3, và rà soát định dạng/nhãn `simulated` khi điền `report/team/bang_chi_phi.md`.
- **Cách tự kiểm tra:** Đối chiếu từng kết quả với đầu ra của `src/lab13.py`, kiểm tra quy tắc đối xứng của 9 kịch bản B1, kiểm tra chênh lệch làm tròn giữa tổng thành phần và CPS, và quét từ cấm trước khi cập nhật báo cáo.

## 6. Tự đánh giá

- Hoàn thành đúng tiến độ phần việc của Người kiểm số đến hết CP1 & CP2 trước khi chuyển sang CP3.
- Sẽ bổ sung MSSV, đổi tên file theo đúng định dạng `<MSSV>_NguyenDuyHung.md` và cập nhật thêm phần đóng góp CP3–CP5 trước khi nộp bài cuối buổi.
