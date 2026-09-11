# =========================
# HOAT DONG 1
# DICTIONARY CO BAN
# =========================

sinh_vien = {
    "ho_ten": "Nguyen Van A",
    "nam_sinh": 2004,
    "diem_tb": 8.5
}

print("=== BAI 1.1 ===")
print(sinh_vien["ho_ten"])
print(sinh_vien.get("diem_tb"))
print(sinh_vien.get("lop", "Chua co"))


print("\n=== BAI 1.2 ===")

# Them khoa moi
sinh_vien["lop"] = "CNTT01"

# Sua gia tri
sinh_vien["diem_tb"] = 9.0

print(sinh_vien)

# Xoa diem_tb
diem_cu = sinh_vien.pop("diem_tb")

print(sinh_vien, "- diem da xoa:", diem_cu)

# Cap nhat nhieu gia tri
sinh_vien.update({
    "nam_sinh": 2003,
    "email": "a@example.com"
})

print(sinh_vien)


# =========================
# HOAT DONG 2
# DUYET DICTIONARY
# =========================

print("\n=== HOAT DONG 2 ===")

diem_mon_hoc = {
    "Toan": 8.0,
    "Ly": 7.5,
    "Hoa": 9.0,
    "Van": 6.5
}

print("Danh sach mon hoc:")
for mon in diem_mon_hoc.keys():
    print(mon)

print("\nDanh sach diem:")
for diem in diem_mon_hoc.values():
    print(diem)

print("\nMon hoc va diem:")
for mon, diem in diem_mon_hoc.items():
    print(f"{mon}: {diem}")

tong_diem = 0

for diem in diem_mon_hoc.values():
    tong_diem = tong_diem + diem

print("Diem trung binh:", round(tong_diem / len(diem_mon_hoc), 2))


# =========================
# HOAT DONG 3
# DICTIONARY COMPREHENSION
# VA SET
# =========================

print("\n=== BAI 3.1 ===")

diem_mon_hoc = {
    "Toan": 8.0,
    "Ly": 7.5,
    "Hoa": 9.0,
    "Van": 6.5
}

diem_cong_diem = {
    mon: round(diem + 0.5, 2)
    for mon, diem in diem_mon_hoc.items()
}

print(diem_cong_diem)

ten_mon_viet_hoa = {
    mon.upper(): diem
    for mon, diem in diem_mon_hoc.items()
}

print(ten_mon_viet_hoa)


print("\n=== BAI 3.2 ===")

mon_hoc_ky1 = {"Toan", "Ly", "Hoa", "Van"}
mon_hoc_ky2 = {"Toan", "Anh", "Tin", "Van"}

print("Giao:", mon_hoc_ky1 & mon_hoc_ky2)
print("Hop:", mon_hoc_ky1 | mon_hoc_ky2)
print("Chi co o hoc ky 1:", mon_hoc_ky1 - mon_hoc_ky2)