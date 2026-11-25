# Báo cáo cá nhân — 2A202604110_NguyenDuyHung

## 1. Thông tin thành viên

- Họ tên: Nguyễn Duy Hưng
- MSSV: 2A202604110
- Email: nguyenduyhung101010@gmail.com
- GitHub: Hungnd1208
- Vai trong nhóm: **Người kiểm số (Thành viên 2)**

## 2. Phần việc phụ trách

- Kiểm số độc lập cho code tính toán trong `src/lab13.py`, đối chiếu công thức và số liệu với `docs/du_lieu_va_cong_thuc.md`.
- Điền, kiểm chứng và hoàn thiện toàn bộ bảng số liệu và câu trả lời ở Nhiệm vụ A (A1–A4) và Nhiệm vụ B (B1–B4) trong `report/team/bang_chi_phi.md`.
- Rà soát, kiểm số đồng thuận và bổ sung định nghĩa viết lại / độ đo cho bảng lỗi CP3 (`report/team/bang_loi.md`).
- Hoàn thiện và kiểm chứng kế hoạch pilot CP4 (`report/team/pilot_plan.yaml`) cùng đặc tả chỉ số, event, rủi ro và hồ sơ launch v0 CP5 (`report/team/chi_so.md`, `report/team/ho_so_launch_v0.md`).
- Kiểm soát tuân thủ quy tắc của lab: gắn nhãn `simulated` cho mọi số liệu từ các cột `_simulated`, câu trả lời $\le 3$ dòng có số liệu, không sử dụng từ cấm trong hồ sơ.

## 3. Đóng góp cụ thể

- **CP1 — Kiểm số Nhiệm vụ A (`bang_chi_phi.md`):**
  - Chạy kiểm thử `src/lab13.py` trên máy cá nhân (Python 3.12.10), xác nhận đạt 3/3 phép thử A1 (`1,20`, `1,25`, `1,25`).
  - Đối chiếu độc lập từng khoản chi phí A2 trên `1.200` yêu cầu (`1.624` lần chạy): token `245.585 đ`, tool `84.000 đ` (`93.804 đ` ở attempt > 1), xem lại `1.780.000 đ` (`simulated`), làm lại `2.264.000 đ` (`simulated`), tổng `4.373.585 đ`, CPS `4.472 đ` (`simulated`, gấp `16,3 lần` hoá đơn `274,7 đ/yc`), và chi phí cả hệ thống `5.865 đ/yc = 0,49×` (`simulated`).
  - Tính kiểm chứng tỉ lệ `ok` theo từng lần thử (`attempt` 1, 2, 3) cho A3 (`quoc_te` giảm từ `30,00%` $\rightarrow$ `11,43%` $\rightarrow$ `2,15%`) và xác nhận phân bổ chi phí cố định A4 cho phạm vi `noi_dia` + `hang_nang` (`4.599 đ = 0,38×` ở quy mô 45.000 yc/tháng; `5.784 đ = 0,48×` ở nửa khối lượng, `simulated`).
- **CP2 — Kiểm số Nhiệm vụ B (`bang_chi_phi.md`):**
  - Kiểm chứng 9 kịch bản B1 bằng tính đối xứng (mức giảm khi giảm một nửa bằng đúng 1/2 mức tăng khi gấp đôi) và kiểm tra tính cộng tuyến tính ở B2 (`Token x2 + Xem lại x2 = 6.543 đ`, `+46,3%`, `simulated`).
  - Đối chiếu bài toán tối ưu chi phí cả hệ thống B3: xác nhận giới hạn `2 lần` rẻ nhất cho công ty (`6.901.220 đ`, `simulated`), khác với giới hạn `1 lần` cho CPS thấp nhất (`4.111 đ`, `simulated`, đẩy thêm `85` ca sang nhân viên).
  - Kiểm chứng B4 (`noi_dia` + `hang_nang` xem lại 100%) ở cả hai mức phút làm lại (`9 phút`: `11.743 đ = 0,98×`; trung bình thực tế `15,3 phút`: `12.415 đ = 1,03×`, `simulated`) và tính mức hoà vốn thời gian xem lại (`≤ 5,1 phút` và `≤ 4,8 phút`).
- **CP3 — Kiểm tra & hoàn thiện Nhiệm vụ C (`bang_loi.md`):**
  - Kiểm đếm lại tỉ lệ đồng thuận giữa hai bộ nhãn (`15/20 = 75%`, giữ nguyên hai cột nhãn độc lập theo đúng quy định `RULES.md`).
  - Bổ sung mục định nghĩa đã viết lại theo nguyên nhân gốc (bắt buộc khi đồng thuận `< 80%`) và chuẩn hoá cách phát hiện có event, `trace_id`, ngưỡng và tần suất đo cụ thể cho bảng khắc phục 5 ca.
- **CP4 — Hoàn thiện & kiểm chứng `pilot_plan.yaml`:**
  - Điền đầy đủ 5 câu cỡ mẫu D1 (`1.251`, `3.103`, trần `1.000`, trần `300`, `859` ở MDE `0,06` với `m >= 299`, `DE = 6,96`), 5 câu kiểm tra tách tác động D2, đánh đổi power (`0,642` ở mức 5 điểm), ngưỡng an toàn theo nền thực tế (`4,25%` toàn mẫu; `3,97%` phạm vi `noi_dia + hang_nang`), và 3 luật dừng đủ 4 vế `NẾU – TRONG – THÌ – KHÔNG THÌ`.
  - Tự chạy kiểm tra `yaml.safe_load` (`YAML OK, rules: 3`), quét dấu `?` ngoài chú thích và từ cấm, tính kiểm chứng `mo_lai scope = 3,97 %` và `power at 5pt = 0,642` bằng `statsmodels`, đồng thời rà soát chéo toàn dự án để chỉnh lại Luật dừng 2 và `scope` cho nhất quán với giới hạn 2 lần chạy.
- **CP5 — Hoàn thiện `chi_so.md` và `ho_so_launch_v0.md`:**
  - Điền đặc tả chỉ số E1 (`82,83%`, `27,12%`, `4,25%` và 2 chỉ số tự đề xuất), 10 event có `trace_id` kèm bảng kiểm tra chéo và 3 dòng rủi ro kinh tế E2 lấy số trực tiếp từ `bang_chi_phi.md`.
  - Hoàn thiện mục 4–7 và đề xuất cuối `Go có điều kiện` (nêu thẳng các con số bất lợi kèm 4 điều kiện có người phụ trách và hạn kiểm tra) trong `report/team/ho_so_launch_v0.md`.

## 4. Bằng chứng

- Các file hồ sơ đã cập nhật/hoàn thiện: `report/team/bang_chi_phi.md`, `report/team/bang_loi.md`, `report/team/pilot_plan.yaml`, `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md`.
- Các commit đã đẩy lên nhánh `main`: `3919c20` (`bangchiphi`), `97dc3d6` (`nhiem vu b`), `c1b8c8b` (`canhan`), `12feb89` (đổi tên file cá nhân theo MSSV).
- Kết quả chạy kiểm chứng trực tiếp trên máy cá nhân: `python lab13.py` (đạt 3/3 phép thử A1), `yaml.safe_load` (`YAML OK, rules: 3`), `mo_lai scope: 3.97 %`, `power at 5pt: 0.642`.

## 5. Công cụ AI đã dùng

- **Công cụ:** Antigravity (trợ lý AI).
- **Mục đích sử dụng:** Hỗ trợ viết lệnh/script Python đối chiếu độc lập số liệu từ hai file CSV, tính mức hoà vốn B4, tỉ lệ `ok` theo `attempt` ở A3, kiểm tra nhất quán giữa `pilot_plan.yaml` và các file hồ sơ, và rà soát định dạng/nhãn `simulated`.
- **Cách tự kiểm tra:** Đối chiếu từng kết quả với đầu ra của `src/lab13.py`, kiểm tra quy tắc đối xứng của 9 kịch bản B1, tự chạy các lệnh PowerShell kiểm tra `yaml.safe_load`, `statsmodels` (`NormalIndPower`), kiểm tra không còn dấu `?` ngoài chú thích và không có từ cấm trong `report/team/`.

## 6. Tự đánh giá

- Hoàn thành đầy đủ vai trò **Người kiểm số (Thành viên 2)** từ CP1 đến CP5, đảm bảo tính khớp nối số liệu (sai số $\le 2\%$), nhãn `simulated` đầy đủ và tính nhất quán giữa code, kế hoạch pilot và hồ sơ launch v0 trước buổi duyệt chéo Gate 2a.
