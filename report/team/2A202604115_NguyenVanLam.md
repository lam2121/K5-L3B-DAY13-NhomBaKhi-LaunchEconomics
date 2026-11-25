# Báo cáo cá nhân — NguyenVanLam-2A202604115

## 1. Thông tin thành viên

- Họ tên: Nguyễn Văn Lâm
- MSSV: 2A202604115
- Email: 26ai.lamnv@vinuni.edu.vn
- Vai trong nhóm: Người gắn nhãn 2, kiêm giữ hồ sơ (Trưởng nhóm)

## 2. Phần việc phụ trách

- Trưởng nhóm: quản lý repo nhóm `K5-L3B-DAY13-NhomBaKhi-LaunchEconomics`, điều phối phân công và theo dõi tiến độ các checkpoint.
- Người giữ hồ sơ: tổng hợp và cập nhật dần 7 mục vào `report/team/ho_so_launch_v0.md`, kiểm soát nhãn `simulated`, quy tắc 5 của lab (chỉ duyệt kế hoạch pilot, không duyệt chạy chính thức) và vai trò phụ trách.
- Người gắn nhãn 2 (CP3): tự đọc và gắn nhãn độc lập 20 ca lỗi theo 5 loại Google PAIR, đối chiếu đồng thuận với Người gắn nhãn 1, viết quy tắc phân biệt và hoàn thiện `report/team/bang_loi.md`.

## 3. Đóng góp cụ thể

- **Tổ chức nhóm & repo (`TEAM.md`):** Khởi tạo thông tin nhóm `NhomBaKhi`, lớp `L3B`, bảng phân công 4 thành viên, nhân bản mục cá nhân cho từng thành viên và đồng nhất email nộp bài (`26ai.lamnv@vinuni.edu.vn`).
- **Giữ hồ sơ CP1 & CP2 (`report/team/ho_so_launch_v0.md`):** Đối chiếu đầu ra từ `src/lab13.py` và `report/team/bang_chi_phi.md` để cập nhật Mục 1 (*Chi phí mỗi việc thành công*: `4.472 đ/việc`, gấp `16,3×` hoá đơn `274,7 đ`, phạm vi `noi_dia + hang_nang` có cố định `4.599 đ` ở 45k yc / `5.784 đ` ở nửa khối lượng, `simulated`), Mục 2 (*Ba yếu tố nhạy nhất*: làm lại `+51,8% / −25,9%`, xem lại `+40,7% / −20,3%`, lương NV `+23,1%`, `simulated`), và Mục 3 (*So với nhân viên tự làm*: cả hệ thống `5.865 đ = 0,49×`, phạm vi pilot `0,38× / 0,48×`, rủi ro B4 xem lại 100% lên `11.743 đ = 0,98×` hoặc `12.415 đ = 1,03×`, `simulated`).
- **Gắn nhãn lỗi CP3 (`report/team/bang_loi.md` & Mục 5 `ho_so_launch_v0.md`):** Tự gắn nhãn độc lập 20 ca lỗi trước khi trao đổi (cột `Nhãn người 2`); đối chiếu với Người gắn nhãn 1 (`Phạm Văn Chiêu`) đạt đồng thuận ban đầu `15/20 = 75%` (lệch ở các ca `3, 6, 8, 9, 13`); cùng thống nhất 5 ca lệch về đúng nguyên nhân gốc (`20/20` khớp cuối cùng), bổ sung định nghĩa viết lại và bảng khắc phục 5 ca (`1, 7, 16, 11, 5`), rồi cập nhật Mục 5 vào `report/team/ho_so_launch_v0.md`.
- **Rà soát chéo, tổng hợp báo cáo nhóm & duyệt chéo Gate 2a:** Kiểm tra xung đột Git, chạy kiểm chứng `src/lab13.py` (3 phép thử A1 đạt `1,20 · 1,25 · 1,25`), kiểm tra `pilot_plan.yaml` bằng `yaml.safe_load` (hợp lệ, không còn `?` ngoài chú thích), rà từ cấm theo quy tắc 5 của `README.md`, sửa lỗi hiển thị mũi tên `$\rightarrow$` → `→` ở Mục 7 `ho_so_launch_v0.md`, và rà lại diễn đạt dòng 7 của `bang_loi.md`; tổng hợp `report/team/group_report.md` từ báo cáo của 4 thành viên; dựng slide trình bày `report/bao_cao_gate2a_NhomBaKhi.html` và cùng nhóm chấm chéo **Nhóm Dota (Lớp L3B)** vào `report/team/phieu_cham.md` (`30/30`, `Go có điều kiện`).

## 4. Bằng chứng

- `1434e29`: điền `TEAM.md`, tạo `report/team/2A202604115_NguyenVanLam.md`, ghi 20 nhãn độc lập vào cột `Nhãn người 2` trong `report/team/bang_loi.md`, cập nhật tên nhóm/lớp ở `report/team/ho_so_launch_v0.md`.
- `ca84383`: điền Mục 1, 2, 3 (CP1 và CP2) trong `report/team/ho_so_launch_v0.md`.
- `326a9f1`: cập nhật Mục 5 (CP3) trong `report/team/ho_so_launch_v0.md` và cập nhật email liên hệ.
- `b97eef9`: đồng nhất email trong `TEAM.md`, chỉnh lại dòng 7 trong `report/team/bang_loi.md` và sửa ký hiệu `→` ở Mục 7 `report/team/ho_so_launch_v0.md`.
- `d9d1961`: cập nhật đầy đủ `report/team/2A202604115_NguyenVanLam.md`, tổng hợp `report/team/group_report.md` và đồng bộ `TEAM.md`.
- `40f5298`: dựng slide trình bày Gate 2a (`report/bao_cao_gate2a_NhomBaKhi.html`) và hoàn thiện `report/team/phieu_cham.md` chấm chéo Nhóm Dota.

## 5. Công cụ AI đã dùng

- **Công cụ:** Trợ lý AI trong IDE (Antigravity / Gemini).
- **Mục đích sử dụng:** Giải thích vai trò và quy trình từng checkpoint; tạo khung `TEAM.md` và báo cáo cá nhân; kiểm tra đối chiếu bộ 20 nhãn lỗi **sau khi đã tự gắn độc lập** và giải thích nguyên nhân gốc cho 5 ca lệch (`3, 6, 8, 9, 13`); tóm tắt số liệu đã có vào `ho_so_launch_v0.md` và rà soát xung đột/quy tắc trình bày giữa các file nhóm.
- **Cách tự kiểm tra:**
  - Tự đọc 20 ca trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` và gắn nhãn độc lập trước; giữ nguyên bộ nhãn ban đầu (`15/20 = 75%`) ở cột `Nhãn người 2` khi đối chiếu với Người gắn nhãn 1.
  - Tự chạy lại `python lab13.py` trong `src/` để đối chiếu từng con số với `bang_chi_phi.md`, `chi_so.md`, `ho_so_launch_v0.md` (`4.472 đ`, `16,3×`, `5.865 đ = 0,49×`, `12.415 đ = 1,03×`, `82,83%`, `27,12%`, `4,25%`).
  - Kiểm tra `yaml.safe_load` trên `pilot_plan.yaml` và quét kiểm tra quy tắc 5 của `README.md` cùng nhãn `simulated` trên toàn bộ `report/team/`.

## 6. Tự đánh giá

- **Điểm làm tốt:** Hoàn thành đúng vai trò Trưởng nhóm và Người giữ hồ sơ; cập nhật hồ sơ cuốn chiếu theo từng checkpoint, chủ động phát hiện và xử lý các lỗi xung đột định dạng/nhất quán trước phiên duyệt chéo Gate 2a.
- **Hạn chế và bài học:** Khi gắn nhãn độc lập CP3 đạt `15/20 = 75%` (lệch 5 ca `3, 6, 8, 9, 13` do nhầm giữa cách trợ lý phản hồi với nguyên nhân gốc ở đầu vào/phạm vi/lỗi đã lộ ra). Sau khi viết lại định nghĩa phân loại cùng Người gắn nhãn 1 đã hiểu rõ và thống nhất chính xác `20/20` ca.
- **Việc đã hoàn tất & đóng gói nộp bài:** Đã hoàn thành đầy đủ phần việc cá nhân, báo cáo nhóm (`group_report.md`), slide trình bày Gate 2a (`bao_cao_gate2a_NhomBaKhi.html`) và phiếu chấm chéo (`phieu_cham.md`); kiểm tra lần cuối trước deadline `23h59 GMT+7`, push nhánh `main` và nộp link repo lên LMS.
