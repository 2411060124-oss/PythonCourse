danh_sach_sinh_vien = [
    {
        "ma_sv": "SV001",
        "ho_ten": "Nguyen Van An",
        "tuoi": 20,
        "diem_tb": 8.0
    },
    {
        "ma_sv": "SV002",
        "ho_ten": "Tran Thi Binh",
        "tuoi": 21,
        "diem_tb": 7.5
    }
]


def hien_thi_danh_sach():

    if len(danh_sach_sinh_vien) == 0:
        print("Danh sach sinh vien dang trong.")
        return

    print("\n===== DANH SACH SINH VIEN =====")

    print(
        f"{'Ma SV':<10}"
        f"{'Ho ten':<25}"
        f"{'Tuoi':<10}"
        f"{'Diem TB':<10}"
    )

    for sv in danh_sach_sinh_vien:

        print(
            f"{sv['ma_sv']:<10}"
            f"{sv['ho_ten']:<25}"
            f"{sv['tuoi']:<10}"
            f"{sv['diem_tb']:<10}"
        )


def tim_sinh_vien(ma_sv):

    for sv in danh_sach_sinh_vien:

        if sv["ma_sv"] == ma_sv:
            return sv

    return None


def nhap_tuoi():

    while True:

        try:

            tuoi = int(input("Nhap tuoi: "))

            if tuoi > 0:
                return tuoi

            print("Tuoi phai lon hon 0.")

        except ValueError:

            print(
                "Du lieu khong hop le, "
                "vui long nhap lai."
            )


def nhap_diem():

    while True:

        try:

            diem = float(
                input("Nhap diem trung binh: ")
            )

            if 0 <= diem <= 10:
                return diem

            print(
                "Diem phai nam trong "
                "khoang 0 den 10."
            )

        except ValueError:

            print(
                "Du lieu khong hop le, "
                "vui long nhap lai."
            )


def them_sinh_vien():

    print("\n===== THEM SINH VIEN =====")

    ma_sv = input(
        "Nhap ma sinh vien: "
    ).strip().upper()

    if tim_sinh_vien(ma_sv) is not None:

        print("Ma sinh vien da ton tai.")

        return

    ho_ten = input(
        "Nhap ho ten: "
    ).strip().title()

    tuoi = nhap_tuoi()

    diem_tb = nhap_diem()

    sinh_vien = {
        "ma_sv": ma_sv,
        "ho_ten": ho_ten,
        "tuoi": tuoi,
        "diem_tb": diem_tb
    }

    danh_sach_sinh_vien.append(
        sinh_vien
    )

    print(
        "Them sinh vien thanh cong."
    )


def tim_kiem():

    ma_sv = input(
        "Nhap ma sinh vien can tim: "
    ).strip().upper()

    sv = tim_sinh_vien(ma_sv)

    if sv is None:

        print("Khong tim thay sinh vien.")

    else:

        print("Ma sinh vien:", sv["ma_sv"])
        print("Ho ten:", sv["ho_ten"])
        print("Tuoi:", sv["tuoi"])
        print(
            "Diem trung binh:",
            sv["diem_tb"]
        )


def sua_sinh_vien():

    ma_sv = input(
        "Nhap ma sinh vien can sua: "
    ).strip().upper()

    sv = tim_sinh_vien(ma_sv)

    if sv is None:

        print("Khong tim thay sinh vien.")

        return

    sv["ho_ten"] = input(
        "Nhap ho ten moi: "
    ).strip().title()

    sv["tuoi"] = nhap_tuoi()

    sv["diem_tb"] = nhap_diem()

    print(
        "Cap nhat sinh vien thanh cong."
    )


def xoa_sinh_vien():

    ma_sv = input(
        "Nhap ma sinh vien can xoa: "
    ).strip().upper()

    sv = tim_sinh_vien(ma_sv)

    if sv is None:

        print("Khong tim thay sinh vien.")

        return

    danh_sach_sinh_vien.remove(sv)

    print("Xoa sinh vien thanh cong.")


def thong_ke():

    tong = len(
        danh_sach_sinh_vien
    )

    print(
        "Tong so sinh vien:",
        tong
    )

    if tong == 0:
        return

    tong_diem = 0

    for sv in danh_sach_sinh_vien:

        tong_diem += sv["diem_tb"]

    diem_tb = tong_diem / tong

    print(
        f"Diem trung binh chung: "
        f"{diem_tb:.2f}"
    )


def hien_thi_menu():

    print("\n===== QUAN LY SINH VIEN =====")
    print("1. Hien thi danh sach")
    print("2. Them sinh vien")
    print("3. Tim sinh vien")
    print("4. Sua sinh vien")
    print("5. Xoa sinh vien")
    print("6. Thong ke")
    print("0. Thoat")


def chay_chuong_trinh():

    while True:

        hien_thi_menu()

        lua_chon = input(
            "Nhap lua chon: "
        ).strip()

        if lua_chon == "1":

            hien_thi_danh_sach()

        elif lua_chon == "2":

            them_sinh_vien()

        elif lua_chon == "3":

            tim_kiem()

        elif lua_chon == "4":

            sua_sinh_vien()

        elif lua_chon == "5":

            xoa_sinh_vien()

        elif lua_chon == "6":

            thong_ke()

        elif lua_chon == "0":

            print("Tam biet!")

            break

        else:

            print(
                "Lua chon khong hop le."
            )


if __name__ == "__main__":
    chay_chuong_trinh()