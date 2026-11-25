# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): NhomBaKhi (Lớp L3B)
- Nhóm được chấm: Nhóm Dota (Lớp L3B)

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | Đề xuất `Go có điều kiện` khớp số liệu, nêu đủ 2 bất lợi (`xem lại 100%` lên `0,98–1,04×` `simulated`; `power = 0,64` ở mức 5 điểm) kèm `5` điều kiện có vai trò và hạn kiểm tra (`12-04`, `12-11`, `12-18`). Khi phản biện đã đồng ý bật tối đa `2` lần chạy từ đầu (`3.980.391 đ` vs `4.056.513 đ`, `simulated`) và bổ sung 3 ngưỡng hạ xem lại ngày `18/12` (`sua + bo < 15%`, `0` ca sai tiền, `≤ 5` phút). |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 10 | Mọi con số từ `_simulated` đều có nhãn `simulated`; phân biệt rõ `82,83%` đợt chạy thử chưa đối chứng; thu hẹp phạm vi `noi_dia` (`0,22×`, `95,0%`) + `hang_nang` (`0,69×`, `74,1%`) và loại `quoc_te` (`1,88×`, `27,3%`, `ok` tụt `30,0% → 2,2%`) & `doi_tac` (`0,85×`). |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 10 | Chia `20 + 20` NV phân tầng `12` depot (`n = 859/nhóm`, `m ≥ 299`, `DE = 6,96`), có biện pháp chống học chéo và `3` luật dừng 4 vế có ngưỡng, thời hạn, người tắt cờ (`30 phút`). Khi hỏi đáp đã nhận lỗi gộp cố định vào ngưỡng `8.000 đ` (sửa thành chỉ tính biến đổi `3.414 đ`), bổ sung event `so_cai_ghi_hoan` (ngưỡng `0`, tắt ngay `30 phút`) và cam kết dời lịch theo đủ `299` đơn. |
| **Tổng** | | | | **30 / 30** | |

**Quyết định của hội đồng:** Go có điều kiện

**Lý do:** Hồ sơ khớp bằng chứng, trung thực về dữ liệu `simulated` và các bất lợi (`power = 0,64`, xem lại 100%). Trong hỏi đáp, đội trình giải trình chính xác mọi con số kiểm chứng và nhận sửa 4 điểm thiếu sót (tách cố định `40 triệu` khỏi ngưỡng `8.000 đ`, bật giới hạn `2` lần chạy từ đầu, chốt ngưỡng giảm xem lại `18/12`, thêm event `so_cai_ghi_hoan` tắt ngay khi có `1` ca trùng, và dời ngày chốt nếu thiếu `299` đơn); cần cập nhật các điểm này vào bản nộp cuối.

**Một câu hỏi cho đội trình:** Luật dừng `8.000 đ` (có cố định) có tự kích hoạt ở tuần 1–2 (`4–10` người) không, và thu hẹp về `noi_dia` có giảm được tiền thuê cố định mỗi việc không? *(Ngoài ra hội đồng hỏi thêm 4 câu kiểm chứng về giới hạn `2` lần chạy & ngưỡng `18/12`, event sổ cái, chống học chéo/dời lịch, và hiệu ứng trần `82,83%`.)*

**Câu trả lời của đội trình (ghi lại tại buổi):** Nhóm nhận đây là lỗi trong file vì cộng `40 triệu` khiến bước `4` người tốn `15.266 đ` và `10` người tốn `8.155 đ` (`simulated`), đồng thời thu về `noi_dia` làm cố định `4` người tăng từ `11.852 đ` lên `13.623 đ`. Nhóm cam kết sửa bản nộp: (1) ngưỡng `8.000 đ` chỉ đo chi phí biến đổi (`3.414 đ`), theo dõi cố định riêng ở E2; (2) bật tối đa `2` lần chạy ngay từ đầu (`3.980.391 đ` vs `4.056.513 đ`, `simulated`) và hạ xem lại `100% → 50%` ngày `18/12` nếu `sua + bo < 15%` (hiện `21,09%`, `27/128`), `0` ca sai tiền và `≤ 5` phút thật; (3) thêm event `so_cai_ghi_hoan` (`idempotency_key`, ngưỡng `0`, tắt ngay `30 phút`); (4) tách chỗ/ca chống học chéo và dời `decision_date` tới khi đủ `299` đơn + `7` ngày; (5) đo đối chứng ở bước `0.10` để hiệu chỉnh cỡ mẫu nếu vượt `0,80` (do chạy thử phạm vi đạt `92,26%`).
