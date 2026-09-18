# =========================
# HOAT DONG 4
# CHUYEN DOI KIEU DU LIEU
# =========================

print("=== BAI 4.1: EP KIEU TUONG MINH ===")

chuoi_so = "25"
so = int(chuoi_so)

print(so, type(so))


so_thuc = float("3.14")

print(so_thuc, type(so_thuc))


danh_sach = list((1, 2, 3))

bo_ba = tuple([4, 5, 6])

tap_hop = set([1, 2, 2, 3, 3, 3])

tu_dien = dict([
    ("a", 1),
    ("b", 2)
])

print("List:", danh_sach)
print("Tuple:", bo_ba)
print("Set:", tap_hop)
print("Dictionary:", tu_dien)


print("\n=== BAI 4.2: EP KIEU SO THUC ===")

so_hop_le = int(float("3.14"))

print(so_hop_le)


print("\n=== BAI 4.3: CHUYEN DOI NGAM DINH ===")

ket_qua = 5 + 2.5

print(ket_qua, type(ket_qua))


ket_qua_2 = "Diem: " + str(8.5)

print(ket_qua_2)