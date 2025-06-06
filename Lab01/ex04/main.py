from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()
while True:
    print("1. Nhap sinh vien")
    print("2. Cap nhat sinh vien boi ID")
    print("3. Xoa sinh vien boi ID")
    print("4. Tim kiem sinh vien theo ten")
    print("5. Sap xep sinh vien theo diem TB")
    print("6. Sap xep sinh vien theo theo ten")
    print("7. Hien thi danh sach sinh vien")
    print("0. Thoat")
    
    choice = int(input("Nhap lua chon: "))
    
    if choice == 1:
        print("\n1. Them sinh vien")
        qlsv.nhapSinhVien()
        print("\nDa nhap sinh vien thanh cong")
    elif choice == 2:
        if (qlsv.soLuongSinhVien() > 0):
            print("\n2. Cap nhat thong tin sinh vien ")
            print("\nNhap id sinh vien can cap nhat: ")
            ID = int(input())
            qlsv.updateSinhVien(ID)
            print("\nDa cap nhat sinh vien thanh cong")
        else:
            print("Khong co sinh vien nao trong danh sach")
    elif choice == 3:
        if (qlsv.soLuongSinhVien() > 0):
            print("\n3. Xoa sinh vien")
            print("\nNhap id sinh vien can xoa: ")
            ID = int(input())
            if qlsv.deleteByID(ID):
                print("\nDa xoa sinh vien co id = ", ID)
            else:
                print("\nKhong tim thay sinh vien co id = ", ID)
        else:
            print("Khong co sinh vien nao trong danh sach")
    elif choice == 4:
        if (qlsv.soLuongSinhVien() > 0):
            print("\n4. Tim kiem sinh vien")
            print("\nTim kiem theo ten:")
            name = input()
            searchResult = qlsv.findByName(name)
        else:
            print("Khong co sinh vien nao trong danh sach")
    elif choice == 5:
        if (qlsv.soLuongSinhVien() > 0):
            print("\n5. Sap xep sinh vien theo diem TB")
            qlsv.sortByDTB()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("Khong co sinh vien nao trong danh sach")
    elif choice == 6:
        if (qlsv.soLuongSinhVien() > 0):
            print("\n6. Sap xep sinh vien theo ten")
            qlsv.sortByName()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("Khong co sinh vien nao trong danh sach")
    elif choice == 7:
        if (qlsv.soLuongSinhVien() > 0):
            print("\n7. Hien thi danh sach sinh vien")
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("Khong co sinh vien nao trong danh sach")
    elif choice == 0:
        print("\nDang thoat chuong trinh...")
        break
    else:
        print("\nLua chon khong hop le, vui long nhap lai")