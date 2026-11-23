# VLU Automation Testing

**Dự án kiểm thử tự động Website Quản lý Phân công – Nhóm 06**

![Java](https://img.shields.io/badge/Java-17-orange)
![Selenium](https://img.shields.io/badge/Selenium-4.25.0-green)
![TestNG](https://img.shields.io/badge/TestNG-Testing-red)
![Maven](https://img.shields.io/badge/Maven-Build-blue)
![POM](https://img.shields.io/badge/Design-Page_Object_Model-purple)

## 1. Giới thiệu dự án

Dự án được xây dựng nhằm tự động hóa quy trình kiểm thử chức năng của hệ thống quản lý phân công tại Trường Đại học Văn Lang.

Thông qua **Selenium WebDriver**, **TestNG** và mô hình thiết kế **Page Object Model (POM)**, dự án giúp giảm thao tác kiểm thử thủ công, nâng cao khả năng tái sử dụng mã nguồn và hỗ trợ phát hiện lỗi trong quá trình phát triển phần mềm.

## 2. Công nghệ sử dụng

| Công nghệ | Mục đích |
|---|---|
| Java 17 | Ngôn ngữ lập trình |
| Selenium WebDriver 4.25.0 | Tự động hóa thao tác trình duyệt |
| TestNG | Tổ chức và thực thi Test Cases |
| Maven | Quản lý thư viện và chạy kiểm thử |
| Page Object Model | Tổ chức mã nguồn kiểm thử |
| ChromeDriver | Thực thi kiểm thử trên Google Chrome |
| Git & GitHub | Quản lý phiên bản mã nguồn |

## 3. Chức năng kiểm thử

Dự án tập trung vào các nhóm chức năng chính:

### Kiểm thử đăng nhập
- Kiểm tra đăng nhập với tài khoản hợp lệ.
- Kiểm tra xử lý tài khoản hoặc mật khẩu không hợp lệ.
- Xác minh kết quả đăng nhập.

### Kiểm thử quản lý người dùng
- Truy cập chức năng quản lý người dùng.
- Tìm kiếm người dùng.
- Thêm người dùng mới.
- Kiểm tra dữ liệu nhập.
- Xác minh kết quả thực hiện thao tác.

Các kịch bản khác được triển khai tùy theo phạm vi chức năng và Test Cases của dự án.

## 4. Cấu trúc dự án

```text
VLU-Automation-Testing/
│
├── src/
│   ├── main/
│   │   └── java/
│   │       └── com/vlu/phancong/
│   │           └── pages/
│   │               ├── BasePage.java
│   │               └── UserManagementPage.java
│   │
│   └── test/
│       └── java/
│           └── com/vlu/phancong/
│               └── tests/
│                   └── LoginTest.java
│
├── pom.xml
├── .gitignore
└── README.md
```

*Đây là cấu trúc minh họa các thành phần chính; cấu trúc thực tế có thể bao gồm thêm Page Objects, Test Classes và file cấu hình.*

## 5. Cài đặt và chạy dự án

### Yêu cầu môi trường

- JDK 17
- Apache Maven
- Google Chrome
- Visual Studio Code hoặc IntelliJ IDEA

### Clone repository

```bash
git clone https://github.com/USERNAME/VLU-Automation-Testing.git
```

### Di chuyển vào thư mục dự án

```bash
cd VLU-Automation-Testing
```

### Cài đặt dependencies

```bash
mvn clean install -DskipTests
```

### Chạy kiểm thử tự động

```bash
mvn test
```

### Chạy riêng kiểm thử đăng nhập

```bash
mvn -Dtest=LoginTest test
```

## 6. Quy trình kiểm thử

1. Phân tích yêu cầu chức năng hệ thống.
2. Thiết kế Test Cases theo từng chức năng.
3. Xây dựng Page Objects để quản lý các phần tử giao diện.
4. Viết Test Scripts bằng Selenium và TestNG.
5. Thực thi kiểm thử tự động.
6. Phân tích kết quả và xác định nguyên nhân lỗi.
7. Điều chỉnh và chạy kiểm thử lại.

## 7. Báo cáo kết quả

Sau khi chạy kiểm thử bằng Maven, có thể xem kết quả tại:

```text
target/
└── surefire-reports/
```

Báo cáo hỗ trợ theo dõi:

- Tổng số Test Cases được chạy.
- Số lượng Test Cases thành công.
- Số lượng Test Cases thất bại.
- Thông tin lỗi và thời gian thực thi.

## 8. Mô hình Page Object Model

Dự án áp dụng mô hình **Page Object Model (POM)** nhằm tách biệt phần tương tác giao diện với phần kiểm thử.

- **BasePage:** Chứa các phương thức dùng chung để tương tác với trình duyệt.
- **Page Classes:** Quản lý các phần tử và hành động trên từng trang.
- **Test Classes:** Chứa các kịch bản kiểm thử và câu lệnh xác minh kết quả.

Ưu điểm:
- Dễ bảo trì mã nguồn.
- Hạn chế trùng lặp code.
- Dễ mở rộng Test Cases.
- Tăng khả năng tái sử dụng.

## 9. Thành viên thực hiện

**Nhóm 06 – Môn Kiểm thử tự động**

Trường Đại học Văn Lang (VLU)

## 10. Mục đích dự án

Dự án được thực hiện phục vụ mục đích học tập và nghiên cứu trong môn học Kiểm thử tự động, giúp nhóm vận dụng kiến thức Selenium WebDriver, TestNG, Maven và POM vào kiểm thử phần mềm thực tế.

---

**VLU Automation Testing | Group 06**
