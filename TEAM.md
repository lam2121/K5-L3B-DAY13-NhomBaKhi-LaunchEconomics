# Team

## Thông tin nhóm

- Tên nhóm: NhomBaKhi
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-NhomBaKhi-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: https://github.com/lam2121/K5-L3B-DAY13-NhomBaKhi-LaunchEconomics, nhánh `main`, commit mới nhất trên `main` trước 23h59 GMT+7 (mốc Gate 2a đã xác nhận: `40f5298`)

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Nguyễn Văn Lâm | 2A202604115 | 26ai.lamnv@vinuni.edu.vn | lam2121 | Người gắn nhãn 2, kiêm giữ hồ sơ (Trưởng nhóm) |
|   2 | Nguyễn Duy Hưng | 2A202604110 | nguyenduyhung101010@gmail.com | Hungnd1208 | Người kiểm số |
|   3 | Nguyễn Trọng Khiêm | 2A202604109 | khiem14205@gmail.com | KhiemNTK | Người viết code |
|   4 | Phạm Văn Chiêu | 2A202604033 | chieupham1011@gmail.com | pvchiu | Người gắn nhãn 1 |

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

Sao chép mục dưới đây cho từng thành viên.

## NguyenVanLam-2A202604115

### Phần việc phụ trách

- Trưởng nhóm; Người gắn nhãn 2, kiêm giữ hồ sơ (`report/team/ho_so_launch_v0.md`, gắn nhãn 20 ca độc lập ở CP3 và tham gia hoàn thiện `report/team/bang_loi.md`).

### Đóng góp cụ thể

- Khởi tạo/cập nhật thông tin nhóm và phân vai trong `TEAM.md`; tự gắn nhãn độc lập 20 ca lỗi (cột `Nhãn người 2`, đồng thuận ban đầu `15/20 = 75%`, thống nhất `20/20` cùng định nghĩa viết lại và bảng 5 ca khắc phục); tổng hợp CP1–CP3 vào `report/team/ho_so_launch_v0.md`; rà soát xung đột, kiểm tra chạy `src/lab13.py`, YAML và quy tắc nộp bài; tổng hợp `report/team/group_report.md`, dựng slide `report/bao_cao_gate2a_NhomBaKhi.html` và hoàn thiện phiếu chấm chéo Gate 2a (`report/team/phieu_cham.md`).

### Bằng chứng

- Các commit `1434e29`, `ca84383`, `326a9f1`, `b97eef9`, `d9d1961`, `40f5298`; [Bảng lỗi CP3](report/team/bang_loi.md), [Hồ sơ launch v0](report/team/ho_so_launch_v0.md), [Báo cáo nhóm](report/team/group_report.md), [Phiếu chấm hội đồng](report/team/phieu_cham.md) và [báo cáo cá nhân](report/team/2A202604115_NguyenVanLam.md).

## NguyenDuyHung-2A202604110

### Phần việc phụ trách

- Người kiểm số (kiểm chứng độc lập số liệu từ `src/lab13.py` và hai file CSV, điền `report/team/bang_chi_phi.md`, rà soát CP3 và hoàn thiện CP4–CP5).

### Đóng góp cụ thể

- Kiểm chứng độc lập và điền toàn bộ Nhiệm vụ A–B (`bang_chi_phi.md`), tính tỉ lệ `ok` theo `attempt` ở A3 và mức hoà vốn B4; bổ sung định nghĩa viết lại và chuẩn hoá độ đo ở `bang_loi.md`; hoàn thiện và kiểm chứng `pilot_plan.yaml` (đồng bộ giới hạn `2` lần chạy vào `scope`, kiểm tra `yaml.safe_load` và `statsmodels` ra power `0,642`), hoàn thiện `chi_so.md` và Mục 4–7 cùng đề xuất `Go có điều kiện` trong `ho_so_launch_v0.md`.

### Bằng chứng

- Các commit `3919c20`, `97dc3d6`, `c1b8c8b`, `12feb89`, `d36bf78`, `1acd7d2`, `e8b7a5f`, `46cb7da`; [Bảng chi phí](report/team/bang_chi_phi.md), [Kế hoạch pilot](report/team/pilot_plan.yaml), [Chỉ số và rủi ro](report/team/chi_so.md), [Hồ sơ launch v0](report/team/ho_so_launch_v0.md) và [báo cáo cá nhân](report/team/2A202604110_NguyenDuyHung.md).

## NguyenTrongKhiem-2A202604109

### Phần việc phụ trách

- Người viết code (viết và chạy `src/lab13.py` cho nhiệm vụ A, B, D1, E1).

### Đóng góp cụ thể

- Thiết lập và triển khai toàn bộ tính toán trong `src/lab13.py` (A1 đạt 3/3 phép thử, `mo_hinh` xử lý `keep_default_na=False`, A2–A4, B1–B4, D1 tính cỡ mẫu cụm/đánh đổi MDE 6 điểm, và tính thử chỉ số E1) xuất số liệu chuẩn xác cho các báo cáo nhóm.

### Bằng chứng

- Commit `ce36374`; [src/lab13.py](src/lab13.py) và [báo cáo cá nhân](report/team/2A202604109_NguyenTrongKhiem.md).

## PhamVanChieu-2A202604033

### Phần việc phụ trách

- Người gắn nhãn 1 (đọc đề, theo dõi điều kiện "Xong khi", gắn nhãn 20 ca độc lập ở CP3 và tham gia hoàn thiện `report/team/bang_loi.md`).

### Đóng góp cụ thể

- Đọc kỹ đề bài, rà soát điều kiện "Xong khi" của các checkpoint.
- Gắn nhãn độc lập 20 ca lỗi ở CP3, đối chiếu với Người gắn nhãn 2 (đạt 15/20 ca trùng = 75%).
- Soạn thảo và thống nhất quy tắc phân biệt cho 5 ca lệch (ca 3, 6, 8, 9, 13) và cùng chốt bảng khắc phục cho 5 loại lỗi của Google PAIR.
- Hoàn thành báo cáo cá nhân và rà soát các tiêu chí nghiệm thu của nhóm.

### Bằng chứng

- Commit `0d77751`: Document CP3 label comparison and individual report.
- Commit `c621ea6`: Finalize agreed CP3 labels and mitigations.
- Commit `5a39fac`: Update individual report (`2A202604033_PhamVanChieu.md`), member contact info and CP3 wording.
- [Bảng lỗi CP3](report/team/bang_loi.md) và [Báo cáo cá nhân](report/team/2A202604033_PhamVanChieu.md).
