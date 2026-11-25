"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
from statistics import NormalDist
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p: float, k: int | None = None) -> float:
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    return 1.0 / p if k is None else (1.0 - (1.0 - p) ** k) / p


def ti_le_thanh_cong(p: float, k: int | None = None) -> float:
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    return 1.0 if k is None else 1.0 - (1.0 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p: float, k: int | None = None) -> float:
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs: pd.DataFrame, reqs: pd.DataFrame,
            gia_vao: float = 26, gia_ra: float = 130, gia_tool: float = 15,
            luong_phut: float = 2000, he_so_xem_lai: float = 1.0,
            he_so_lam_lai: float = 1.0, max_lan_chay: int | None = None) -> dict:
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])].copy()

    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = runs['tokens_in'] / 1000.0 * gia_vao + runs['tokens_out'] / 1000.0 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = (reqs['ket_qua'] == 'thanh_cong').sum()

    return {
        'token': tien_token.sum(),
        'tool': tien_tool.sum(),
        'chay_lai': (tien_token + tien_tool)[runs['attempt'] > 1].sum(),
        'xem_lai': xem_lai,
        'lam_lai': lam_lai,
        'tong': tong,
        'thanh_cong': int(thanh_cong),
        'cps': tong / thanh_cong if thanh_cong > 0 else 0.0,
        'hoa_don_moi_yc': (tien_token.sum() + tien_tool.sum()) / len(reqs) if len(reqs) > 0 else 0.0,
    }


# ---------- Nhiệm vụ D1 · Cỡ mẫu ----------
def co_mau(p1: float, p2: float, alpha: float = 0.05, power: float = 0.8) -> int:
    """Cỡ mẫu mỗi nhóm khi so sánh 2 tỉ lệ độc lập (z-test 2 phía)."""
    za = NormalDist().inv_cdf(1.0 - alpha / 2.0)
    zb = NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2.0
    return math.ceil(
        (za * math.sqrt(2 * pb * (1 - pb)) + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2
        / ((p2 - p1) ** 2)
    )


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)

    print('=' * 65)
    print('A1 · KIỂM TRA PHÉP THỬ ĐÁP ÁN BIẾT TRƯỚC')
    print('=' * 65)
    kiem_tra_dap_an_biet_truoc()

    print('\n' + '=' * 65)
    print('A2 · MÔ HÌNH CHI PHÍ TOÀN BỘ 1.200 YÊU CẦU')
    print('=' * 65)
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:16s} {gia_tri:>14,.0f}')
    print(f"-> Gấp: {ket_qua['cps'] / ket_qua['hoa_don_moi_yc']:.1f} lần hóa đơn")
    print(f"-> Chi phí cả hệ thống: {(ket_qua['tong'] + 222 * BASELINE) / len(reqs):,.0f} đ/yc = {((ket_qua['tong'] + 222 * BASELINE) / len(reqs)) / BASELINE:.2f}x baseline")

    # TODO CP1 · Nhiệm vụ A3: tính lại theo từng giá trị của cột loai.
    print('\n' + '=' * 65)
    print('A3 · PHÂN RÃ THEO LOẠI YÊU CẦU')
    print('=' * 65)
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        sub_reqs = reqs[reqs['loai'] == loai]
        kq_l = mo_hinh(runs, sub_reqs)
        so_yc = len(sub_reqs)
        tc_pct = kq_l['thanh_cong'] / so_yc * 100
        lan_chay_tb = runs[runs['request_id'].isin(sub_reqs['request_id'])].shape[0] / so_yc
        print(f"{loai:10s} | YC: {so_yc:3d} | Thành công: {tc_pct:5.1f}% | Lần/YC: {lan_chay_tb:.2f} | CPS: {kq_l['cps']:8,.0f} đ [sim] | So 12k: {kq_l['cps'] / BASELINE:4.2f}x")

    # Nhiệm vụ A4: Chi phí cố định
    print('\n' + '=' * 65)
    print('A4 · CHI PHÍ CỐ ĐỊNH (PHẠM VI noi_dia + hang_nang: 900 TC / 1.200 YC)')
    print('=' * 65)
    scope_reqs = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    kq_scope = mo_hinh(runs, scope_reqs)
    tc_thang_full = 45000 * kq_scope['thanh_cong'] / len(reqs)  # 33.750
    co_dinh_full = 40000000 / tc_thang_full                     # 1.185
    cps_full = kq_scope['cps'] + co_dinh_full                   # 4.599
    co_dinh_half = 40000000 / (tc_thang_full / 2)              # 2.370
    cps_half = kq_scope['cps'] + co_dinh_half                   # 5.784
    print(f"Full quy mô (45k YC/tháng) : Cố định {co_dinh_full:,.0f} đ/việc -> CPS có cố định: {cps_full:,.0f} đ = {cps_full / BASELINE:.2f}x [sim]")
    print(f"Một nửa quy mô             : Cố định {co_dinh_half:,.0f} đ/việc -> CPS có cố định: {cps_half:,.0f} đ = {cps_half / BASELINE:.2f}x [sim]")

    # TODO CP2 · Nhiệm vụ B: đổi từng yếu tố, ghi vào bảng độ nhạy.
    print('\n' + '=' * 65)
    print('B1 & B2 · BẢNG ĐỘ NHẠY (9 KỊCH BẢN + 1 CẶP)')
    print('=' * 65)
    kich_ban = {
        'Giá token gấp đôi':        dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa':   dict(gia_vao=13, gia_ra=65),
        'Xem lại gấp đôi':          dict(he_so_xem_lai=2),
        'Xem lại giảm một nửa':     dict(he_so_xem_lai=0.5),
        'Làm lại gấp đôi':          dict(he_so_lam_lai=2),
        'Làm lại giảm một nửa':     dict(he_so_lam_lai=0.5),
        'Lương tăng 25%':           dict(luong_phut=2500),
        'Tối đa 2 lần chạy':        dict(max_lan_chay=2),
        'Chỉ 1 lần chạy':           dict(max_lan_chay=1),
    }
    goc = ket_qua['cps']
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        print(f'{ten:26s} : {cps:8,.0f} đ [sim] | Thay đổi: {(cps / goc - 1) * 100:+6.1f}%')
    cps_cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    print(f"{'Token x2 + Xem lại x2':26s} : {cps_cap:8,.0f} đ [sim] | Thay đổi: {(cps_cap / goc - 1) * 100:+6.1f}%")

    # Nhiệm vụ B3: Giới hạn số lần chạy và chi phí cả hệ thống
    print('\n' + '=' * 65)
    print('B3 · GIỚI HẠN SỐ LẦN CHẠY VÀ CHI PHÍ CẢ HỆ THỐNG')
    print('=' * 65)
    for limit in [1, 2, 3]:
        kw = dict(max_lan_chay=limit) if limit < 3 else {}
        kq_lim = mo_hinh(runs, reqs, **kw)
        that_bai = len(reqs) - kq_lim['thanh_cong']
        ca_he_thong = kq_lim['tong'] + that_bai * BASELINE
        print(f"Giới hạn {limit} lần | Trợ lý: {kq_lim['tong']:10,.0f} đ | Hỏng: {that_bai:3d} | Cả HT: {ca_he_thong:10,.0f} đ | CPS: {kq_lim['cps']:6,.0f} đ [sim]")

    # Nhiệm vụ B4: Xem lại 100%
    print('\n' + '=' * 65)
    print('B4 · XEM LẠI 100% (noi_dia + hang_nang)')
    print('=' * 65)
    scope_runs = runs[runs['request_id'].isin(scope_reqs['request_id'])]
    tien_token_tool_scope = (scope_runs['tokens_in'] / 1000 * 26 + scope_runs['tokens_out'] / 1000 * 130 + scope_runs['tool_calls'] * 15).sum()
    runs_ok_req_ids = set(scope_runs[scope_runs['status'] == 'ok']['request_id'])
    so_yc_ok = len(scope_reqs[scope_reqs['request_id'].isin(runs_ok_req_ids)])  # 948
    tien_xem_lai_100 = so_yc_ok * 5 * LUONG_PHUT                                # 9.480.000
    so_lam_lai_scope = (scope_reqs['ket_qua'] == 'lam_lai').sum()               # 48
    tien_lam_lai_9m = so_lam_lai_scope * 9 * LUONG_PHUT                         # 864.000
    tong_b4_9m = tien_token_tool_scope + tien_xem_lai_100 + tien_lam_lai_9m
    cps_b4_9m = tong_b4_9m / kq_scope['thanh_cong']                             # 11.743
    phut_lam_lai_thuc_te = reqs[reqs['ket_qua'] == 'lam_lai']['phut_lam_lai_simulated'].mean() # 15.3
    tien_lam_lai_15m = so_lam_lai_scope * phut_lam_lai_thuc_te * LUONG_PHUT
    tong_b4_15m = tien_token_tool_scope + tien_xem_lai_100 + tien_lam_lai_15m
    cps_b4_15m = tong_b4_15m / kq_scope['thanh_cong']                           # 12.414
    print(f"Xem lại 100% (9 phút làm lại)  : {cps_b4_9m:8,.0f} đ = {cps_b4_9m / BASELINE:.2f}x [sim]")
    print(f"Xem lại 100% (15,3 phút làm lại): {cps_b4_15m:8,.0f} đ = {cps_b4_15m / BASELINE:.2f}x [sim]")

    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    print('\n' + '=' * 65)
    print('D1 · CỠ MẪU CHO PILOT (baseline 0,70 -> 0,75, power 0,8, alpha 0,05, ICC 0,02)')
    print('=' * 65)
    n_yc = co_mau(0.70, 0.75)
    print(f"a · Chia theo yêu cầu : {n_yc} yêu cầu mỗi nhóm")
    de_m75 = 1 + (75 - 1) * 0.02
    n_m75 = math.ceil(n_yc * de_m75)
    print(f"b · Theo nhân viên (m=75): {n_m75} yc/nhóm -> {math.ceil(n_m75 / 75)} người/nhóm (tổng {math.ceil(n_m75 / 75) * 2} > 40: KHÔNG ĐỦ)")
    print(f"c · 20 nhân viên/nhóm : Trần c/ICC = 20 / 0,02 = 1.000 (< {n_yc}: KHÔNG ĐẠT)")
    print(f"d · 6 depot mỗi nhóm  : Trần 6 / 0,02 = 300 (< {n_yc}: KHÔNG ĐẠT)")
    n_6pt = co_mau(0.70, 0.76)
    m_min = math.ceil((n_6pt * 0.98) / (20 - n_6pt * 0.02))
    de_299 = 1 + (m_min - 1) * 0.02
    print(f"e · Mức chênh 6 điểm  : {n_6pt} yc/nhóm -> Cần m >= {m_min} yc/người (DE = {de_299:.2f})")

    # Nhiệm vụ E1: Thử nghiệm chỉ số
    print('\n' + '=' * 65)
    print('E1 · TÍNH THỬ CHỈ SỐ TRÊN 1.200 YÊU CẦU')
    print('=' * 65)
    chinh_cnt = ((reqs['dong_trong_24h'] == 1) & (reqs['mo_lai_trong_7_ngay'] == 0)).sum()
    chinh_pct = chinh_cnt / len(reqs) * 100
    xem_df = reqs[reqs['duoc_xem_lai'] == 1]
    bo_qua_cnt = xem_df['quyet_dinh_xem_lai'].isin(['sua', 'bo']).sum()
    bo_qua_pct = bo_qua_cnt / len(xem_df) * 100
    an_toan_cnt = (reqs['mo_lai_trong_7_ngay'] == 1).sum()
    an_toan_pct = an_toan_cnt / len(reqs) * 100
    print(f"Chỉ số chính (% đóng 24h & ko mở lại 7d): {chinh_pct:.2f}% ({chinh_cnt}/{len(reqs)})")
    print(f"Chỉ số dùng (% bỏ qua/sửa gợi ý)        : {bo_qua_pct:.2f}% ({bo_qua_cnt}/{len(xem_df)})")
    print(f"Chỉ số an toàn (% mở lại 7 ngày)        : {an_toan_pct:.2f}% ({an_toan_cnt}/{len(reqs)})")
