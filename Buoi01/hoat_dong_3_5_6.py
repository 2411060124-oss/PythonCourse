# ==========================================
# HOAT DONG 3 - DINH DANH & PEP8
# ==========================================

print("===== HOAT DONG 3 =====")

# Bai 3.1 - Kiem tra dinh danh
# Hop le:
# _tam_thoi, Diem_TB, so, luong, MAX_SPEED, diemTB, sinhVien1
#
# Khong hop le:
# 1diem     -> bat dau bang so
# gia-tri   -> chua dau gach ngang
# class     -> la tu khoa Python
# 2024_data -> bat dau bang so
# tong$     -> chua ky tu $

# Bai 3.2 - Dat ten bien theo chuan PEP8

ten = "Nguyen Van A"
diem_toan = 8.5
diem_van = 7.0
so_luong_mon_hoc = 2

MUCLUONGTOITHIEU = 5000000

print("Ho ten:", ten)
print("Diem Toan:", diem_toan)
print("Diem Van:", diem_van)
print("So luong mon hoc:", so_luong_mon_hoc)
print("Muc luong toi thieu:", MUCLUONGTOITHIEU)

# ==========================================
# HOAT DONG 5 - TOAN TU
# ==========================================

print("\n===== HOAT DONG 5 =====")

# Bai 5.1 - Toan tu so hoc

a = 17
b = 5

print("\n--- Bai 5.1 ---")
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a // b =", a // b)
print("a % b =", a % b)
print("a ** b =", a ** b)


# Bai 5.2 - Toan tu so sanh va logic

diem = 6.5
tuoi = 20

print("\n--- Bai 5.2 ---")

dat_kha = diem >= 6.5 and diem < 8.0
chua_du_18_hoac_tren_60 = tuoi < 18 or tuoi > 60

print("Dat loai Kha?", dat_kha)
print("Chua du 18 hoac tren 60?", chua_du_18_hoac_tren_60)
print("Phu dinh dieu kien:", not chua_du_18_hoac_tren_60)


# Bai 5.3 - Toan tu gan

x = 10

print("\n--- Bai 5.3 ---")

x += 5
print("Sau += 5:", x)

x -= 2
print("Sau -= 2:", x)

x *= 3
print("Sau *= 3:", x)

x /= 2
print("Sau /= 2:", x)

x //= 2
print("Sau //= 2:", x)

x **= 2
print("Sau **= 2:", x)


# Toan tu in va is

danh_sach = [1, 2, 3, "python"]

print("3 co trong danh_sach?", 3 in danh_sach)

a_list = danh_sach
print("Hai bien cung tham chieu?", danh_sach is a_list)


# Bai 5.4 - Do uu tien toan tu

print("\n--- Bai 5.4 ---")

print(2 + 3 * 4 ** 2)
print((2 + 3) * 4 ** 2)
print(10 > 5 and 3 < 1 or not False)

# ==========================================
# HOAT DONG 6 - BIEN & DYNAMIC TYPING
# ==========================================

print("\n===== HOAT DONG 6 =====")

# Bai 6.1 - Dynamic typing

bien = 10
print(bien, type(bien))

bien = "Xin chao"
print(bien, type(bien))

bien = 3.14
print(bien, type(bien))

bien = True
print(bien, type(bien))


# Bai 6.2 - Mini bai toan tong hop

ho_ten = "Nguyen Van A"
diem_toan = 8.0
diem_ly = 7.5
diem_hoa = 9.0

dtb = (diem_toan + diem_ly + diem_hoa) / 3

la_gioi = dtb >= 8.0
la_kha = dtb >= 6.5 and dtb < 8.0
la_trung_binh = dtb >= 5.0 and dtb < 6.5
la_yeu = dtb < 5.0

print("\nHo ten:", ho_ten)
print("DTB:", round(dtb, 2))
print("Dat loai Gioi?", la_gioi)
print("Dat loai Kha?", la_kha)
print("Dat loai Trung binh?", la_trung_binh)
print("Dat loai Yeu?", la_yeu)
print("Kieu du lieu cua la_gioi:", type(la_gioi))