# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 82,83% (994 / 1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 27,12% (48 / 177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 4,25% (51 / 1.200) |
| Dùng | Nhóm tự đề xuất: Tỉ lệ kích hoạt trợ lý trong nhóm can thiệp | Số yêu cầu của nhóm can thiệp có gợi ý trợ lý chia tổng số yêu cầu nhóm can thiệp | Không cần tính |
| An toàn | Nhóm tự đề xuất: Tỉ lệ hoàn sai tiền qua kiểm tra mẫu | Số đơn hoàn lệch số tiền đúng (kiểm tra mẫu 100 đơn/tuần) chia 100 | Không cần tính |

Chỉ số chính trong đợt chạy thử là `82,83%` (không viết "trợ lý đã nâng chỉ số từ 0,70" vì đợt chạy thử không có nhóm đối chứng).

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | `request_id`, `loai`, `so_tien`, `arm`, `trace_id` | Khi khách gửi yêu cầu |
| `agent_run_completed` | Agent | `attempt`, `tokens_in`, `tokens_out`, `tool_calls`, `status`, `trace_id` | Sau mỗi lần chạy, kể cả lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | `staff_id`, `so_tien_de_xuat`, `arm`, `trace_id` | Khi gợi ý trợ lý hiện ra |
| `staff_review_decision` | Nhân viên CSKH | `staff_id`, `quyet_dinh` (`giu`/`sua`/`bo`), `phut_xem_lai_thuc`, `trace_id` | Khi bấm giữ, sửa hoặc bỏ |
| `staff_rework_completed` | Nhân viên CSKH | `staff_id`, `phut_lam_lai_thuc`, `ly_do`, `trace_id` | Khi nhân viên hoàn tất làm lại |
| `refund_ledger_write` | Dịch vụ sổ cái | `idempotency_key`, `so_tien`, `status`, `trace_id` | Khi ghi nhận lệnh hoàn tiền |
| `handoff_to_staff` | Agent | `reason`, `loai`, `tom_tat`, `trace_id` | Khi chuyển yêu cầu sang nhân viên |
| `ticket_closed` | Hệ thống ticket | `request_id`, `closed_at`, `closed_within_24h`, `trace_id` | Khi đóng yêu cầu |
| `ticket_reopened` | Khách hàng / CSKH | `request_id`, `reopened_at`, `reason`, `trace_id` | Khi mở lại trong 7 ngày |
| `audit_sample_checked` | Kế toán / Đối soát | `request_id`, `so_tien_da_hoan`, `so_tien_dung`, `lech_tien`, `trace_id` | Kiểm tra mẫu hằng tuần (100 đơn) |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- **Chỉ số chính (`82,83%`):** Tính bằng `refund_request_created` (mẫu số, lọc theo `arm` và `loai`), `ticket_closed` (đóng trong 24h) và `ticket_reopened` (không mở lại trong 7 ngày), nối theo `trace_id`.
- **Chỉ số dùng 1 — Tỉ lệ bỏ qua gợi ý (`27,12%`):** Tính bằng `staff_review_decision` (`sua` + `bo` chia tổng lượt xem lại) nối với `agent_suggestion_shown` qua `trace_id`.
- **Chỉ số an toàn 1 — Tỉ lệ lỗi lọt đến khách (`4,25%`):** Tính bằng `ticket_reopened` (mở lại trong 7 ngày) chia tổng `refund_request_created` theo `trace_id`.
- **Chỉ số dùng 2 (tự đề xuất) — Tỉ lệ kích hoạt trợ lý:** Tính bằng `agent_suggestion_shown` chia tổng `refund_request_created` thuộc nhóm can thiệp (`arm = treatment`).
- **Chỉ số an toàn 2 (tự đề xuất) — Tỉ lệ hoàn sai tiền qua kiểm tra mẫu:** Tính bằng `audit_sample_checked` (số bản ghi có `lech_tien != 0` chia tổng mẫu kiểm tra hằng tuần). Cả 5 chỉ số đều đo được từ danh sách event trên.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | Chi phí tăng `+51,8%`, từ `4.472 đ` lên `6.787 đ/việc` (`simulated`) | Tỉ lệ `lam_lai` theo tuần `> 7%` (đợt chạy thử là `48/982 = 4,9%` trong phạm vi) | Thu hẹp về `noi_dia` và rà soát `20` trace phát sinh làm lại | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | Chi phí lên `11.743 đ = 0,98×` (`9` phút làm lại) hoặc `12.415 đ = 1,03×` ở mức thực tế `15,3` phút/ca (`simulated`), đắt hơn nhân viên tự làm | Tỉ lệ yêu cầu được xem lại còn `> 50%` ở cuối bước `0,25` hoặc thời gian xem lại `> 4,8 phút/lần` | Áp dụng giảm tỉ lệ xem lại theo bậc khi tỉ lệ `sua + bo < 15%` và rút ngắn giao diện xem lại | Trưởng nhóm CSKH |
| Khối lượng yêu cầu thấp hơn dự kiến | Cố định `40 triệu đ/tháng` làm chi phí tăng thêm `+1.185 đ/việc` (`4.599 đ` ở `45.000` yc) và lên `+2.370 đ/việc` (`5.784 đ`) khi giảm một nửa khối lượng (`simulated`) | Số việc thành công theo tuần `< 50%` kế hoạch | Tạm dừng mở rộng bước rollout và rà soát lại chi phí cố định hàng tháng | Kế toán trưởng |
