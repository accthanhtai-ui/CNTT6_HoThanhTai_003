class CourseRegistration:
    def __init__(self, id, student_name, course_name, tuition_fee, discount, extra_fee):
        self.id = id
        self.student_name = student_name
        self.course_name = course_name
        self.tuition_fee = tuition_fee
        self.discount = discount
        self.extra_fee = extra_fee
        self.total_fee = 0
        self.fee_type = ""

        self.calculate_total_fee()
        self.classify_fee()

    def calculate_total_fee(self):
        self.total_fee = self.tuition_fee - self.discount + self.extra_fee

    def classify_fee(self):
        if self.total_fee < 3000000:
            self.fee_type = "Thấp"
        elif self.total_fee < 7000000:
            self.fee_type = "Trung bình"
        elif self.total_fee < 15000000:
            self.fee_type = "Cao"
        else:
            self.fee_type = "Rất cao"


class CourseRegistrationManager:
    def __init__(self):
        self.registrations = []

    def add_registration(self):
        try:
            id = input("Nhập mã đăng ký: ").strip()
            if id == "":
                print("Mã không được để trống")
                return
            for registration in self.registrations:
                if registration.id == id:
                    print("Mã đã tồn tại")
                    return
            student_name = input("Nhập tên học viên: ").strip()
            if student_name == "":
                print("Tên học viên không được để trống")
                return
            if student_name.isdigit():
                print("tên không được nhập số")
                return
            course_name = input("Nhập tên khóa học: ").strip()
            if course_name == "":
                print("Tên khóa học không được để trống")
                return
            tuition_fee = float(input("Nhập học phí: "))
            if tuition_fee <= 0:
                print("Học phí phải lớn hơn 0")
                return
            if tuition_fee == "":
                print("không được để trống")
                return
            discount = float(input("Nhập giảm giá: "))
            if discount == "":
                print(" không được để trống")
                return
            if discount < 0:
                print("Giảm giá không được âm")
                return
            extra_fee = float(input("Nhập phụ phí: "))
            if extra_fee == "":
                print(" không được để trống")
                return
            if extra_fee < 0:
                print("Phụ phí không được âm")
                return

            new_registration = CourseRegistration(
                id,
                student_name,
                course_name,
                tuition_fee,
                discount,
                extra_fee
            )
            self.registrations.append(new_registration)
            print("Thêm thành công")

        except ValueError:
            print("Sai kiểu dữ liệu")

    def show_all(self):
        if len(self.registrations) == 0:
            print("Danh sách rỗng")
            return

        print("-" * 100)
        print(f"{'id':<5}|{'tên':<20}|{'khóa học':<20}|{'học phí gốc':<20}|{'giảm giá':<20}|{'phụ phí':<20}|{'tổng học phí':<20}|{'phân loại':<10}")
        for registration in self.registrations:
            print(f"{registration.id:<5}|{registration.student_name:<20}|{registration.course_name:<20}|{registration.tuition_fee:<20}|{registration.discount:<20}|{registration.extra_fee:<20}|{registration.total_fee:<20}|{registration.fee_type:<10}")

    def update_registration(self):
        if len(self.registrations) == 0:
            print("Danh sách rỗng")
            return

        id = input("Nhập mã cần sửa: ")

        for registration in self.registrations:
            if registration.id == id:
                try:
                    registration.tuition_fee = float(input("Nhập học phí mới: "))
                    registration.discount = float(input("Nhập giảm giá mới: "))
                    registration.extra_fee = float(input("Nhập phụ phí mới: "))

                    registration.calculate_total_fee()
                    registration.classify_fee()

                    print("Cập nhật thành công")
                    return

                except ValueError:
                    print("Sai kiểu dữ liệu")
                    return

        print("Không tìm thấy")
    
    def delete_registration(self):
        if len(self.registrations) == 0:
            print("Danh sách rỗng")
            return
        id = input("Nhập mã cần xóa: ")

        for registration in self.registrations:
            if registration.id == id:
                confirm = input("Bạn có chắc muốn xóa? (Y/N): ")

                if confirm.lower() == "y":
                    self.registrations.remove(registration)
                    print("Xóa thành công")
                else:
                    print("Đã hủy")

                return
        print("Không tìm thấy")
    def search_registration(self):
        if len(self.registrations) == 0:
            print("Danh sách rỗng")
            return
        keyword = input("Nhập tên học viên cần tìm: ").lower()
        found = False
        for registration in self.registrations:
            if keyword in registration.student_name.lower():
                found = True
                print(registration.id, registration.student_name, registration.course_name)
        if not found:
            print("Không tìm thấy")
def main():
    student = CourseRegistrationManager()
    student.registrations.append(
        CourseRegistration("001", "Nguyễn Văn An", "Python Basic", 1000000, 100000, 100000)
    )
    student.registrations.append(
        CourseRegistration("002", "Trần Thị Bình", "Python Web Service", 2000000, 200000, 200000)
    )

    student.registrations.append(
        CourseRegistration("003", "Lê Minh Cường", "Python OOP", 3000000, 300000, 300000)
        )
    while True:
        print("""
=======================MENU===================
1. Hiển thị danh sách đăng kí khóa học
2. Thêm đăng kí khóa học mới
3. Cập nhật học phí
4. Xóa đăng kí khóa học
5. Tìm kiếm đăng kí
6. Thoát
==============================================
""")
        choice = input("Nhập vào chức năng của bạn: ")
        match choice:
            case "1":
                student.show_all()
            case "2":
                student.add_registration()
            case "3":
                student.update_registration()
            case "4":
                student.delete_registration()
            case "5":
                student.search_registration()
            case "6":
                print("Thoát chương trình")
                break
            case _:
                print("Chọn không đúng chức năng, vui lòng chọn từ 1-6")

main()
