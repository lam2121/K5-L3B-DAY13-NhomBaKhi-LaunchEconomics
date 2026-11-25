# Báo cáo nhóm

## 1. Thông tin nhóm

- **Tên nhóm:** NhomBaKhi
- **Lớp:** L3B
- **Repo nhóm:** `K5-L3B-DAY13-NhomBaKhi-LaunchEconomics`
- **Thành viên:** xem [TEAM.md](../../TEAM.md) (`Nguyễn Văn Lâm` – `2A202604115`, `Nguyễn Duy Hưng` – `2A202604110`, `Nguyễn Trọng Khiêm` – `2A202604109`, `Phạm Văn Chiêu` – `2A202604033`).

## 2. Mục tiêu và cách tiếp cận

Nhóm xây dựng bộ **hồ sơ launch v0** cho trợ lý hoàn phí của công ty giả định LogiX-VN từ mẫu dữ liệu giả lập `1.200` yêu cầu (`1.624` lần chạy) nhằm trả lời bốn câu hỏi trình hội đồng **Gate 2a**: có đáng chạy không (chi phí thật và độ nhạy), nhân viên có dùng không (chỉ số và event), khi hỏng xử lý thế nào (phân loại PAIR và khắc phục), và thiết kế pilot có đối chứng, đủ cỡ mẫu, có luật dừng. Bốn thành viên phân vai rõ ràng theo từng checkpoint: viết code mô hình hoá, kiểm số độc lập, gắn nhãn lỗi, và giữ hồ sơ xuyên suốt.

## 3. Giải pháp

- **Nhiệm vụ A & B (CP1–CP2 — Mô hình chi phí và độ nhạy):** Cài đặt ba hàm A1 đạt 3/3 phép thử biết trước (`1,20 · 1,25 · 1,25`), viết `mo_hinh(...)` cộng mọi lần chạy kể cả lỗi (đọc CSV với `keep_default_na=False`), phân rã theo 4 `loai`, cộng chi phí cố định `40 triệu đ/tháng`, phân tích 9 kịch bản độ nhạy + 1 cặp, so sánh chi phí cả hệ thống theo giới hạn chạy lại và mô phỏng xem lại 100% trong [src/lab13.py](../../src/lab13.py) và [bang_chi_phi.md](bang_chi_phi.md).
- **Nhiệm vụ C (CP3 — Phân loại lỗi và khắc phục):** Hai thành viên gắn nhãn đối chiếu 20 ca theo 5 loại Google PAIR (nguyên nhân gốc), thống nhất các ca lệch kèm định nghĩa viết lại và lập bảng khắc phục 5 ca có event/đối soát đo được và một vai trò phụ trách trong [bang_loi.md](bang_loi.md).
- **Nhiệm vụ D (CP4 — Thiết kế pilot):** Tính 5 bài toán cỡ mẫu (`D1`), kiểm tra 5 câu tách tác động (`D2`), tính tỉ lệ `mo_lai_trong_7_ngay` hiện tại và hoàn thiện kế hoạch triển khai cùng 3 luật dừng 4 vế `NẾU – TRONG – THÌ – KHÔNG THÌ` trong [pilot_plan.yaml](pilot_plan.yaml).
- **Nhiệm vụ E (CP5 — Chỉ số, rủi ro và hồ sơ Gate 2a):** Đặc tả 5 chỉ số (3 chính thức tính thử trên `1.200` yêu cầu + 2 tự đề xuất), liệt kê `10` event gắn `trace_id` và `3` rủi ro kinh tế trong [chi_so.md](chi_so.md); tổng hợp thành hồ sơ một trang trong [ho_so_launch_v0.md](ho_so_launch_v0.md) và chuẩn bị [phieu_cham.md](phieu_cham.md) cho phiên duyệt chéo.

## 4. Kết quả

- **Chi phí thật & phạm vi pilot (`bang_chi_phi.md`):** Toàn mẫu đạt `978/1.200` việc thành công với CPS `4.472 đ` (`simulated`), gấp `16,3×` hoá đơn token+tool/yêu cầu (`274,7 đ`); giờ nhân viên chiếm `92,5%` (làm lại `51,8%`, xem lại `40,7%`). Chi phí cả hệ thống hiện là `5.865 đ/yêu cầu = 0,49×` mức nhân viên tự làm `12.000 đ` (`simulated`). Chỉ `noi_dia` (`2.696 đ = 0,22×`, `95,0%`) và `hang_nang` (`8.221 đ = 0,69×`, `74,1%`) đáng đưa vào pilot (cộng cố định còn `4.599 đ = 0,38×` ở `45.000` yc/tháng và `5.784 đ = 0,48×` ở nửa khối lượng, `simulated`); loại `quoc_te` (`22.515 đ = 1,88×`, `27,3%`) và `doi_tac` (`10.215 đ = 0,85×`, đều tính phần giờ `simulated`).
- **Độ nhạy & giới hạn chạy lại (`bang_chi_phi.md`):** Ba yếu tố nhạy nhất (`simulated`): (1) số ca làm lại (`+51,8% / −25,9%`), (2) tỉ lệ xem lại (`+40,7% / −20,3%`), (3) lương nhân viên (`+23,1%`). Giới hạn `2` lần chạy tối ưu chi phí cả hệ thống (`6.901.220 đ`, `simulated`) so với `1` lần (`7.449.781 đ`) và `3` lần (`7.037.585 đ`). Nếu phải xem lại 100% trong phạm vi pilot, CPS tăng lên `11.743 đ = 0,98×` (9 phút làm lại) hoặc `12.415 đ = 1,03×` ở mức thực tế `15,3` phút/ca (`simulated`).
- **Lỗi, chỉ số & thiết kế pilot:** Đồng thuận ban đầu 20 ca là `15/20 = 75%`, sau khi viết lại định nghĩa nguyên nhân gốc đã thống nhất `20/20`. Chỉ số trong đợt chạy thử (chưa có đối chứng): chính `82,83%` (`994/1.200`), bỏ qua gợi ý `27,12%` (`48/177`), mở lại 7 ngày `4,25%` (`51/1.200`; trong phạm vi pilot `3,97%`). Thiết kế pilot chia theo nhân viên (`20 + 20` cụm tại 12 depot), đánh đổi nới MDE lên `6` điểm (`n = 859/nhóm`, `m ≥ 299`, `DE = 6,96`, power giảm còn `0,642` nếu tác động thật là 5 điểm).
- **Đề xuất cuối (`ho_so_launch_v0.md`):** **Go có điều kiện** cho pilot phạm vi `noi_dia + hang_nang` (giới hạn `2` lần chạy) kèm 4 điều kiện bắt buộc về sửa lỗi ca `20` & ca `7`, ký chấp nhận đánh đổi thống kê, bật đủ `10` event đo thật sau tuần 1 và lộ trình giảm xem lại theo bậc (`≤ 4,8` phút/lần).
- **Kết quả duyệt chéo Gate 2a:** *(Cập nhật sau phiên chấm chéo lúc 17:00 cùng [phieu_cham.md](phieu_cham.md)).*

## 5. Khó khăn và cách xử lý

- **Xử lý dữ liệu rỗng trong CSV:** Nếu không truyền `keep_default_na=False` khi đọc `logix_requests.csv`, ô trống ở `quyet_dinh_xem_lai` thành `NaN` gây sai tỉ lệ dùng -> đã cố định tham số này trong `src/lab13.py` và đối chiếu tay.
- **Đồng thuận gắn nhãn CP3 dưới 80%:** Đối chiếu ban đầu đạt `15/20 = 75%` (lệch ở ca `3, 6, 8, 9, 13` do lẫn giữa biểu hiện phản hồi và nguyên nhân gốc) -> hai người gắn nhãn đã viết lại định nghĩa phân biệt cho từng loại lỗi và thống nhất `20/20` ca trước khi lập bảng khắc phục.
- **Giới hạn cỡ mẫu với 40 nhân viên:** Trần cỡ mẫu hiệu dụng `20 / 0,02 = 1.000 < 1.251` không đủ cho mức chênh 5 điểm -> nhóm chọn đánh đổi minh bạch lên MDE `6` điểm (`m ≥ 299`), nêu rõ rủi ro power `0,642` trong hồ sơ.
- **Đồng bộ nhiều file qua Git:** Xuất hiện một số điểm lệch nhỏ giữa các lần gộp nhánh (email thành viên, ký hiệu LaTeX trong bảng Markdown, diễn đạt ở `bang_loi.md`, và cấu hình giới hạn `2` lần chạy giữa `pilot_plan.yaml` với `ho_so_launch_v0.md`) -> nhóm đã rà soát chéo và đồng bộ dứt điểm trước Gate 2a.

## 6. Tổng hợp đóng góp

Chi tiết phân công và bằng chứng nằm trong [TEAM.md](../../TEAM.md); tóm tắt theo báo cáo cá nhân của 4 thành viên:
- **Nguyễn Văn Lâm (`2A202604115` — Trưởng nhóm · Người gắn nhãn 2, kiêm giữ hồ sơ):** Điều phối repo nhóm, tổng hợp [ho_so_launch_v0.md](ho_so_launch_v0.md) (Mục 1–3, 5), gắn nhãn độc lập 20 ca và hoàn thiện [bang_loi.md](bang_loi.md), rà soát xung đột và quy tắc nộp bài; xem [2A202604115_NguyenVanLam.md](2A202604115_NguyenVanLam.md).
- **Nguyễn Duy Hưng (`2A202604110` — Người kiểm số):** Kiểm chứng độc lập số liệu và điền [bang_chi_phi.md](bang_chi_phi.md) (A1–A4, B1–B4, tỉ lệ `ok` theo `attempt`, hoà vốn B4); bổ sung định nghĩa viết lại và chuẩn hoá độ đo cho [bang_loi.md](bang_loi.md); hoàn thiện và kiểm chứng [pilot_plan.yaml](pilot_plan.yaml) (đồng bộ giới hạn `2` lần chạy vào `scope`, kiểm tra `yaml.safe_load` & `statsmodels` ra power `0,642`), [chi_so.md](chi_so.md) và Mục 4–7 cùng đề xuất cuối trong [ho_so_launch_v0.md](ho_so_launch_v0.md); xem [2A202604110_NguyenDuyHung.md](2A202604110_NguyenDuyHung.md).
- **Nguyễn Trọng Khiêm (`2A202604109` — Người viết code):** Cài đặt môi trường, viết và tối ưu [src/lab13.py](../../src/lab13.py) vượt qua 3/3 phép thử A1 và xuất toàn bộ kết quả A2–A4, B1–B4, D1, E1; xem [2A202604109_NguyenTrongKhiem.md](2A202604109_NguyenTrongKhiem.md).
- **Phạm Văn Chiêu (`2A202604033` — Người gắn nhãn 1):** Đọc đề và theo dõi điều kiện "Xong khi" ở từng checkpoint; gắn nhãn độc lập 20 ca lỗi CP3 đối chiếu đạt `15/20 = 75%` (lệch ca `3, 6, 8, 9, 13`), soạn thảo và thống nhất quy tắc phân biệt 5 ca lệch kèm bảng khắc phục 5 loại lỗi trong [bang_loi.md](bang_loi.md), và rà soát tiêu chí nghiệm thu nhóm; xem [2A202604033_PhamVanChieu.md](2A202604033_PhamVanChieu.md).

## 7. Hạn chế và hướng cải thiện

- Thời gian xem lại và làm lại hiện dùng cột giả lập (`_simulated`), cần thay bằng dữ liệu đo thật từ `staff_review_decision` và `staff_rework_completed` sau tuần đầu của pilot.
- Dữ liệu chạy thử trước đó không có nhóm đối chứng nên chỉ mô tả được hiện trạng (`82,83%`), chưa kết luận được hiệu quả nhân quả trước khi chạy pilot đối chứng.
- Cần hoàn tất [phieu_cham.md](phieu_cham.md) sau phiên duyệt chéo Gate 2a và điền `commit chốt` trong [TEAM.md](../../TEAM.md) ở lần push cuối cùng.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models* (`arxiv.org/abs/2504.13359`).
- Google PAIR, *People + AI Guidebook*, chương *Errors + Graceful Failure*.
- Tài liệu `statsmodels` (`NormalIndPower`, `stats.power`) và tài liệu bài lab ([du_lieu_va_cong_thuc.md](../../docs/du_lieu_va_cong_thuc.md), `src/logix_runs.csv`, `src/logix_requests.csv`).
