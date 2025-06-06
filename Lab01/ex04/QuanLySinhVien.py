from SinhVien import SinhVien

class QuanLySinhVien:
    def __init__(self):
        self.listSinhVien = []
    
    def generateID(self):
        maxId = 1
        if (self.soLuongSinhVien() > 0):
            maxId = self.listSinhVien[0]._id
            for sv in self.listSinhVien:
                if (maxId < sv._id):
                    maxId = sv._id
            maxId = maxId + 1
        return maxId
    
    def soLuongSinhVien(self):
        return self.listSinhVien.__len__()
    
    def nhapSinhVien(self):
        id = self.generateID()
        name = input("Nhap ten sinh vien: ")
        sex = input("Nhap gioi tinh sinh vien: ")
        major = input("Nhap nganh hoc sinh vien: ")
        diemTB = float(input("Nhap diem trung binh sinh vien: "))
        sv = SinhVien(id, name, sex, major, diemTB)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)
    
    def updateSinhVien(self, id):
        sv = self.findByID(id)
        if (sv != None):
            name = input("Nhap ten sinh vien: ")
            sex = input("Nhap gioi tinh sinh vien: ")
            major = input("Nhap nganh hoc sinh vien: ")
            diemTB = float(input("Nhap diem trung binh sinh vien: "))
            sv._name = name
            sv._sex = sex 
            sv._major = major
            sv._diemTB = diemTB
            self.xepLoaiHocLuc(sv)
        else:
            print("Khong tim thay sinh vien co id = ", id)
            
    def sortByID(self):
        self.listSinhVien.sort(key=lambda sv: sv._id, reverse=False) 
        #reverse = false la sort tang dan (1 -> n)
    def sortByName(self):
        self.listSinhVien.sort(key=lambda sv: sv._name, reverse=False) 
    def sortByDTB(self):
        self.listSinhVien.sort(key=lambda sv: sv._diemTB, reverse=False)
    def findByID(self, id):
        for sv in self.listSinhVien:
            if (sv._id == id):
                return sv
        return None
    def findByName(self, name):
        result = []
        for sv in self.listSinhVien:
            if (name.lower() in sv._name.lower()):
                result.append(sv)
        if len(result) > 0:
            print("Tim thay {} sinh vien:".format(len(result)))
            self.showSinhVien(result)
        else:
            print("Khong tim thay sinh vien nao co ten: ", name)
        return result
    def deleteByID(self, id):
        sv = self.findByID(id)
        if (sv != None):
            self.listSinhVien.remove(sv)
            return True
        else:
            return False
    def xepLoaiHocLuc(self, sv):
        if (sv._diemTB >= 8):
            sv._hocLuc = "Gioi"
        elif (sv._diemTB >= 6.5):
            sv._hocLuc = "Kha"
        elif (sv._diemTB >= 5.0):
            sv._hocLuc = "Trung binh"
        else:
            sv._hocLuc = "Yeu"
    def showSinhVien(self, listSV):
        print("{:<8} {:<18} {:<8} {:<15} {:<8} {:<15}"
              .format("ID", "Name", "Sex", "Major", "DTB", "Hoc Luc"))
        print("-" * 80)
        if (listSV.__len__() > 0):
            for sv in listSV:
                print("{:<8} {:<18} {:<8} {:<15} {:<8} {:<15}"
                      .format(sv._id, sv._name, sv._sex, sv._major, sv._diemTB, sv._hocLuc))
        print("\n")
    
    def getListSinhVien(self):
        return self.listSinhVien