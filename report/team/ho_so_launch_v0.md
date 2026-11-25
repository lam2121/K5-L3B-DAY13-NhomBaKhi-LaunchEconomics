# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: NhomBaKhi · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | Toàn mẫu: `4.472 đ/việc` (`978/1.200` yc, gấp `16,3×` hoá đơn `274,7 đ`, `simulated`; giờ NV `92,5%`). Phạm vi `noi_dia` (`2.696 đ`, `95,0%`) + `hang_nang` (`8.221 đ`, `74,1%`): `3.414 đ` chưa cố định; cộng cố định 40 triệu/tháng = `4.599 đ` (45k yc) hoặc `5.784 đ` (nửa khối lượng, `simulated`). Loại `quoc_te` (`22.515 đ`, `27,3%`) và `doi_tac` (`10.215 đ`). | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | 1. Số ca làm lại (`+51,8%` lên `6.787 đ` khi ×2; `−25,9%` khi ÷2) · 2. Tỉ lệ xem lại (`+40,7%` lên `6.292 đ` khi ×2; `−20,3%` khi ÷2) · 3. Lương nhân viên (`+23,1%` lên `5.506 đ` khi +25%) (`simulated`). Giá token ít nhạy (`+5,6%`). Giới hạn 2 lần chạy rẻ nhất toàn hệ thống (`6.901.220 đ`, `simulated`). | Giả lập | Trưởng nhóm CSKH |
| 3 · So với nhân viên tự làm | Baseline NV tự làm: `12.000 đ/yc`. Cả hệ thống hiện tại (gồm `222` ca không thành công): `5.865 đ/yc = 0,49×`; phạm vi `noi_dia + hang_nang` sau cố định: `0,38×` ở 45k yc (`0,48×` ở nửa khối lượng) (`simulated`). **Rủi ro B4:** nếu xem lại 100%, CPS lên `11.743 đ = 0,98×` (9 phút làm lại) hoặc `12.415 đ = 1,03×` (mức thực tế `15,3` phút/ca, `simulated`). | Giả lập | Kế toán trưởng |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Đợt chạy thử (chưa có đối chứng): chính `82,83%` (`994/1.200`), tỉ lệ bỏ qua gợi ý `27,12%` (`48/177`), an toàn `mo_lai_trong_7_ngay` `4,25%` (`51/1.200`; trong phạm vi pilot `3,97%`). Đã đặc tả `10` event đều có `trace_id` để đo đủ `3` chỉ số chính thức và `2` chỉ số đề xuất thêm (tỉ lệ kích hoạt trợ lý, tỉ lệ hoàn sai tiền khi kiểm tra mẫu). | Xong, có bằng chứng | PM trợ lý hoàn phí |
| 5 · Bảng lỗi và cách khắc phục | Phân loại `20` ca theo 5 nhóm PAIR (`Do người dùng` 4, `Hệ thống` 5, `Ngữ cảnh` 4, `Giới hạn` 4, `Ngầm` 3); đồng thuận độc lập ban đầu `15/20 = 75%` (< `80%`, đã viết lại định nghĩa nguyên nhân gốc và thống nhất đạt `20/20`). Đủ `5` phương án khắc phục có event/`trace_id`, ngưỡng và tần suất đo cụ thể. | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot plan | Chia theo nhân viên (`20` cụm/nhóm, đối chứng song song tại `12` depot, rollout `[10%, 25%, 50%]`), phạm vi `noi_dia + hang_nang`. Với `40` NV (trần `1.000 < 1.251`), chấp nhận nới MDE lên `6` điểm (`n = 859/nhóm`, `m ≥ 299`, `DE = 6,96`); **bất lợi:** nếu hiệu ứng thật chỉ `5` điểm thì power giảm còn `0,642`. Đủ `3` luật dừng 4 vế, ngày quyết định `2027-01-05`. | Xong, có bằng chứng | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | (1) Ca làm lại ×2 $\rightarrow$ `+51,8%` lên `6.787 đ` (`simulated`, theo dõi `> 7%/tuần`); (2) Xem lại 100% kéo dài $\rightarrow$ `11.743 đ = 0,98×` (9 phút) hoặc `12.415 đ = 1,03×` ở mức thực tế `15,3` phút/ca (`simulated`, hoà vốn `≤ 4,8–5,1` phút); (3) Giảm `50%` khối lượng $\rightarrow$ cố định tăng lên `2.370 đ/việc`, tổng `5.784 đ` (`simulated`). | Giả lập | PM trợ lý hoàn phí |

**Đề xuất:** **Go có điều kiện** cho pilot phạm vi `noi_dia + hang_nang` (giới hạn `2` lần chạy để tối ưu chi phí cả hệ thống `6.901.220 đ`, `simulated`), kèm bốn điều kiện bắt buộc:

- Sửa hai lỗi nghiêm trọng trước khi mở cờ pilot: thêm khoá chống trùng lệnh hoàn (ca `20`) và đối soát xác nhận sổ cái trước khi báo khách (ca `7`) — **Kỹ sư trưởng agent**, hạn kiểm tra: `2026-12-01`.
- Ký xác nhận đánh đổi thống kê: chấp nhận MDE `6` điểm (`n = 859/nhóm`, `m ≥ 299`) và rủi ro **power giảm còn `0,642`** nếu hiệu ứng thật là `5` điểm — **Giám đốc vận hành LogiX-VN**, hạn kiểm tra: `2026-12-01`.
- Bật đủ `10` event có `trace_id` và thay toàn bộ phút `_simulated` bằng thời gian xem lại/làm lại đo thật sau tuần 1 — **PM trợ lý hoàn phí**, hạn kiểm tra: `2026-12-08`.
- Áp dụng lộ trình giảm tỉ lệ xem lại theo bậc (từ bước `0,25` khi tỉ lệ `sua + bo < 15%`) và giữ thời gian xem lại `≤ 4,8` phút/lần để tránh kịch bản xem lại 100% đội chi phí lên `12.415 đ = 1,03×` (`simulated`) — **Trưởng nhóm CSKH**, hạn kiểm tra: `2026-12-15`.
