# TRƯỜNG ĐẠI HỌC VĂN LANG
## KHOA CÔNG NGHỆ THÔNG TIN
---

### BÁO CÁO ĐỒ ÁN NHÓM
**MÔN HỌC: KIỂM THỬ TỰ ĐỘNG (KHÓA 27)**
**ĐỀ TÀI: KIỂM THỬ TỰ ĐỘNG ỨNG DỤNG QUẢN LÝ PHÂN CÔNG GIẢNG DẠY (VAI TRÒ BCN KHOA)**

- **Lớp học phần**: `232_71ITSE41603_0102`
- **Tên nhóm**: `Team03`
- **Phần mềm kiểm thử**: Quản lý phân công giảng dạy (`https://cntttest.vanlanguni.edu.vn:18081/Phancong02/`)

---

## I. KẾ HOẠCH THỰC HIỆN ĐỒ ÁN NHÓM (PROJECT PLAN)

| Tuần | Công việc | Người thực hiện | Sản phẩm bàn giao |
|:---:|---|:---:|---|
| **Tuần 1** | Tìm hiểu yêu cầu đề bài, tài liệu `ProductBacklog.xlsx` & `UserGuide.pdf` | Cả nhóm | Tài liệu tổng quan scope |
| **Tuần 2** | Phân tích hệ thống thực tế, xác định các tính năng vai trò BCN Khoa | Thành viên 1 | Danh sách Test Scenarios |
| **Tuần 3** | Thiết kế kịch bản test thủ công (Test Cases) & Ma trận kiểm thử | Thành viên 2 | File Excel Test Cases |
| **Tuần 4** | Xây dựng khung kiểm thử tự động Selenium + TestNG (Page Object Model) | Thành viên 3 | Base Framework Setup |
| **Tuần 5** | Viết Automation Test Scripts cho Module User & Term Management | Thành viên 1 & 2 | Source code Module 1 |
| **Tuần 6** | Viết Automation Test Scripts cho Module Timetable & Remuneration | Thành viên 2 & 3 | Source code Module 2 |
| **Tuần 7** | Chạy kiểm thử tự động toàn bộ Suite, tổng hợp báo cáo & đóng gói bài nộp | Cả nhóm | File Word & File Zip mã nguồn |

---

## II. DANH SÁCH CÁC CHỨC NĂNG KIỂM THỬ TỰ ĐỘNG (BCN KHOA)

Dựa theo tài liệu phân công chức năng, nhóm tập trung xây dựng kịch bản kiểm thử tự động cho vai trò **BCN Khoa (Faculty Board)**:

### 1. Module Đăng nhập / Đăng xuất (Login / Logout)
- **`F.1.1`**: Đăng nhập / Đăng xuất hệ thống bằng tài khoản VLU được cấp quyền BCN Khoa.

### 2. Module Quản lý Người dùng (User Management)
- **`F.2.1`**: Xem danh sách người dùng trong Khoa.
- **`F.2.2`**: Thêm mới người dùng / giảng viên vào hệ thống.
- **`F.2.3`**: Cập nhật thông tin giảng viên.
- **`F.2.4`**: Xóa tài khoản người dùng.
- **`F.2.5`**: Tìm kiếm người dùng theo Mã GV / Tên / Email.
- **`F.2.6`**: Khóa tài khoản giảng viên.

### 3. Module Quản lý Học kỳ (Term Management)
- **`F.3.1`**: Xem danh sách học kỳ.
- **`F.3.2`**: Tạo mới học kỳ.
- **`F.3.3`**: Cập nhật học kỳ.
- **`F.3.4`**: Xóa học kỳ.
- **`F.3.5`**: Tìm kiếm học kỳ.
- **`F.3.6`**: Khóa học kỳ (ngăn chặn chỉnh sửa dữ liệu đã chốt).

### 4. Module Quản lý Ngành học (Major Management)
- **`F.4.1` – `F.4.5`**: Thêm, Sửa, Xóa, Tìm kiếm danh sách các ngành học thuộc Khoa.

### 5. Module Quản lý Thời khóa biểu (Timetable Management)
- **`F.5.1`**: Import thời khóa biểu từ tệp Excel.
- **`F.5.2`**: Export thời khóa biểu ra tệp Excel.
- **`F.5.3`**: Xem thời khóa biểu toàn khoa theo tuần.
- **`F.5.4`**: Phân công giảng viên giảng dạy lớp học phần.
- **`F.5.5`**: Xóa lớp học phần trên thời khóa biểu.
- **`F.5.6`**: Xem thời khóa biểu cá nhân của BCN Khoa.

### 6. Module Thống kê & Thù lao (Statistics & Remuneration)
- **`F.6.1` – `F.6.3`**: Thống kê số giờ dạy, môn học theo học kỳ và năm học.
- **`F.7.1` – `F.7.19`**: Quản lý học hàm/học vị, hệ số thù lao và xem bảng tính thù lao giảng dạy.

---

## III. MÃ NGUỒN CÁC KỊCH BẢN KIỂM THỬ TỰ ĐỘNG (PAGE OBJECT MODEL)

### 1. `LoginPage.java` & `LoginTest.java`
```java
package com.vlu.phancong.pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

public class LoginPage extends BasePage {
    private By openIdLoginBtn = By.id("OpenIdConnect");
    private By emailField = By.name("Email");
    private By passwordField = By.name("Password");
    private By submitBtn = By.cssSelector("button[type='submit']");
    private By userDisplayName = By.className("user-profile-name");

    public LoginPage(WebDriver driver) { super(driver); }

    public void login(String email, String password) {
        if (isElementDisplayed(openIdLoginBtn)) { click(openIdLoginBtn); }
        if (isElementDisplayed(emailField)) {
            enterText(emailField, email);
            enterText(passwordField, password);
            click(submitBtn);
        }
    }

    public boolean isLoggedInSuccessfully() {
        return isElementDisplayed(userDisplayName) || driver.getCurrentUrl().contains("Home");
    }
}
```

```java
package com.vlu.phancong.tests;

import com.vlu.phancong.pages.LoginPage;
import org.testng.Assert;
import org.testng.annotations.Test;

public class LoginTest extends BaseTest {
    @Test(priority = 1, description = "F.1.1 - Đăng nhập tài khoản BCN Khoa thành công")
    public void testLoginFacultyBoardSuccess() {
        LoginPage loginPage = new LoginPage(driver);
        loginPage.login("bcnkhoa.cntt@vanlanguni.edu.vn", "Password123");
        Assert.assertTrue(loginPage.isLoggedInSuccessfully(), "Đăng nhập BCN Khoa không thành công!");
    }
}
```

---

### 2. `UserManagementPage.java` & `UserManagementTest.java`
```java
package com.vlu.phancong.pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

public class UserManagementPage extends BasePage {
    private By userMenu = By.xpath("//span[contains(text(),'Quản lý người dùng')]");
    private By searchInput = By.cssSelector("input[type='search']");
    private By addUserBtn = By.xpath("//button[contains(text(),'Thêm người dùng')]");
    private By userCodeInput = By.id("UserCode");
    private By fullNameInput = By.id("FullName");
    private By emailInput = By.id("UserEmail");
    private By saveBtn = By.id("btnSaveUser");

    public UserManagementPage(WebDriver driver) { super(driver); }

    public void goToUserManagement() { click(userMenu); }

    public void createUser(String code, String name, String email, String role) {
        click(addUserBtn);
        enterText(userCodeInput, code);
        enterText(fullNameInput, name);
        enterText(emailInput, email);
        click(saveBtn);
    }

    public boolean isUserDisplayedInTable(String keyword) {
        enterText(searchInput, keyword);
        return isElementDisplayed(By.xpath("//td[contains(text(),'" + keyword + "')]"));
    }
}
```

```java
package com.vlu.phancong.tests;

import com.vlu.phancong.pages.UserManagementPage;
import org.testng.Assert;
import org.testng.annotations.Test;

public class UserManagementTest extends BaseTest {
    @Test(priority = 1, description = "F.2.2 - Thêm giảng viên mới")
    public void testCreateNewUser() {
        UserManagementPage userPage = new UserManagementPage(driver);
        userPage.goToUserManagement();
        userPage.createUser("GV999", "Nguyễn Văn Test", "nguyenvan.test@vanlanguni.edu.vn", "Giảng viên");
        Assert.assertTrue(userPage.isUserDisplayedInTable("GV999"), "Tạo giảng viên mới không thành công!");
    }
}
```

---

### 3. `TermManagementPage.java` & `TermManagementTest.java`
```java
package com.vlu.phancong.pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

public class TermManagementPage extends BasePage {
    private By termMenu = By.xpath("//span[contains(text(),'Quản lý học kỳ')]");
    private By addTermBtn = By.xpath("//button[contains(text(),'Thêm học kỳ')]");
    private By termIdInput = By.id("TermId");
    private By termNameInput = By.id("TermName");
    private By saveTermBtn = By.id("btnSaveTerm");

    public TermManagementPage(WebDriver driver) { super(driver); }

    public void goToTermManagement() { click(termMenu); }

    public void createTerm(String termId, String termName) {
        click(addTermBtn);
        enterText(termIdInput, termId);
        enterText(termNameInput, termName);
        click(saveTermBtn);
    }

    public boolean isTermExists(String termName) {
        return isElementDisplayed(By.xpath("//td[contains(text(),'" + termName + "')]"));
    }
}
```

```java
package com.vlu.phancong.tests;

import com.vlu.phancong.pages.TermManagementPage;
import org.testng.Assert;
import org.testng.annotations.Test;

public class TermManagementTest extends BaseTest {
    @Test(priority = 1, description = "F.3.2 - Tạo học kỳ mới")
    public void testCreateNewTerm() {
        TermManagementPage termPage = new TermManagementPage(driver);
        termPage.goToTermManagement();
        termPage.createTerm("HK999", "Học kỳ 3 Năm học 2026-2027 (Test)");
        Assert.assertTrue(termPage.isTermExists("HK999"), "Tạo học kỳ mới không thành công!");
    }
}
```

---

## IV. QUY ĐỊNH NỘP BÀI VÀ ĐÓNG GÓI

- **Tên thư mục nộp bài**: `232_71ITSE41603_0102_Team03`
- **File Báo cáo Word**: `Team03_Ver1.0.docx` (Lưu từ file nội dung trên).
- **File Mã nguồn (Zip)**: `Team03_Ver1.0.zip` (Nén thư mục `232_71ITSE41603_Team03_Automation`).
