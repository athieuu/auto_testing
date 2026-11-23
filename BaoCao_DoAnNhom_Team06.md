# TRÆ¯á»œNG Äáº I Há»ŒC VÄ‚N LANG
## KHOA CĂ”NG NGHá»† THĂ”NG TIN
---

### BĂO CĂO Äá»’ ĂN NHĂ“M
**MĂ”N Há»ŒC: KIá»‚M THá»¬ Tá»° Äá»˜NG (KHĂ“A 27)**
**Äá»€ TĂ€I: KIá»‚M THá»¬ Tá»° Äá»˜NG á»¨NG Dá»¤NG QUáº¢N LĂ PHĂ‚N CĂ”NG GIáº¢NG Dáº Y (VAI TRĂ’ BCN KHOA)**

- **Lá»›p há»c pháº§n**: `232_71ITSE41603_0102`
- **TĂªn nhĂ³m**: `Team06`
- **Pháº§n má»m kiá»ƒm thá»­**: Quáº£n lĂ½ phĂ¢n cĂ´ng giáº£ng dáº¡y (`https://cntttest.vanlanguni.edu.vn:18081/Phancong02/`)

---

## I. Káº¾ HOáº CH THá»°C HIá»†N Äá»’ ĂN NHĂ“M (PROJECT PLAN)

| Tuáº§n | CĂ´ng viá»‡c | NgÆ°á»i thá»±c hiá»‡n | Sáº£n pháº©m bĂ n giao |
|:---:|---|:---:|---|
| **Tuáº§n 1** | TĂ¬m hiá»ƒu yĂªu cáº§u Ä‘á» bĂ i, tĂ i liá»‡u `ProductBacklog.xlsx` & `UserGuide.pdf` | Cáº£ nhĂ³m | TĂ i liá»‡u tá»•ng quan scope |
| **Tuáº§n 2** | PhĂ¢n tĂ­ch há»‡ thá»‘ng thá»±c táº¿, xĂ¡c Ä‘á»‹nh cĂ¡c tĂ­nh nÄƒng vai trĂ² BCN Khoa | ThĂ nh viĂªn 1 | Danh sĂ¡ch Test Scenarios |
| **Tuáº§n 3** | Thiáº¿t káº¿ ká»‹ch báº£n test thá»§ cĂ´ng (Test Cases) & Ma tráº­n kiá»ƒm thá»­ | ThĂ nh viĂªn 2 | File Excel Test Cases |
| **Tuáº§n 4** | XĂ¢y dá»±ng khung kiá»ƒm thá»­ tá»± Ä‘á»™ng Selenium + TestNG (Page Object Model) | ThĂ nh viĂªn 3 | Base Framework Setup |
| **Tuáº§n 5** | Viáº¿t Automation Test Scripts cho Module User & Term Management | ThĂ nh viĂªn 1 & 2 | Source code Module 1 |
| **Tuáº§n 6** | Viáº¿t Automation Test Scripts cho Module Timetable & Remuneration | ThĂ nh viĂªn 2 & 3 | Source code Module 2 |
| **Tuáº§n 7** | Cháº¡y kiá»ƒm thá»­ tá»± Ä‘á»™ng toĂ n bá»™ Suite, tá»•ng há»£p bĂ¡o cĂ¡o & Ä‘Ă³ng gĂ³i bĂ i ná»™p | Cáº£ nhĂ³m | File Word & File Zip mĂ£ nguá»“n |

---

## II. DANH SĂCH CĂC CHá»¨C NÄ‚NG KIá»‚M THá»¬ Tá»° Äá»˜NG (BCN KHOA)

Dá»±a theo tĂ i liá»‡u phĂ¢n cĂ´ng chá»©c nÄƒng, nhĂ³m táº­p trung xĂ¢y dá»±ng ká»‹ch báº£n kiá»ƒm thá»­ tá»± Ä‘á»™ng cho vai trĂ² **BCN Khoa (Faculty Board)**:

### 1. Module ÄÄƒng nháº­p / ÄÄƒng xuáº¥t (Login / Logout)
- **`F.1.1`**: ÄÄƒng nháº­p / ÄÄƒng xuáº¥t há»‡ thá»‘ng báº±ng tĂ i khoáº£n VLU Ä‘Æ°á»£c cáº¥p quyá»n BCN Khoa.

### 2. Module Quáº£n lĂ½ NgÆ°á»i dĂ¹ng (User Management)
- **`F.2.1`**: Xem danh sĂ¡ch ngÆ°á»i dĂ¹ng trong Khoa.
- **`F.2.2`**: ThĂªm má»›i ngÆ°á»i dĂ¹ng / giáº£ng viĂªn vĂ o há»‡ thá»‘ng.
- **`F.2.3`**: Cáº­p nháº­t thĂ´ng tin giáº£ng viĂªn.
- **`F.2.4`**: XĂ³a tĂ i khoáº£n ngÆ°á»i dĂ¹ng.
- **`F.2.5`**: TĂ¬m kiáº¿m ngÆ°á»i dĂ¹ng theo MĂ£ GV / TĂªn / Email.
- **`F.2.6`**: KhĂ³a tĂ i khoáº£n giáº£ng viĂªn.

### 3. Module Quáº£n lĂ½ Há»c ká»³ (Term Management)
- **`F.3.1`**: Xem danh sĂ¡ch há»c ká»³.
- **`F.3.2`**: Táº¡o má»›i há»c ká»³.
- **`F.3.3`**: Cáº­p nháº­t há»c ká»³.
- **`F.3.4`**: XĂ³a há»c ká»³.
- **`F.3.5`**: TĂ¬m kiáº¿m há»c ká»³.
- **`F.3.6`**: KhĂ³a há»c ká»³ (ngÄƒn cháº·n chá»‰nh sá»­a dá»¯ liá»‡u Ä‘Ă£ chá»‘t).

### 4. Module Quáº£n lĂ½ NgĂ nh há»c (Major Management)
- **`F.4.1` â€“ `F.4.5`**: ThĂªm, Sá»­a, XĂ³a, TĂ¬m kiáº¿m danh sĂ¡ch cĂ¡c ngĂ nh há»c thuá»™c Khoa.

### 5. Module Quáº£n lĂ½ Thá»i khĂ³a biá»ƒu (Timetable Management)
- **`F.5.1`**: Import thá»i khĂ³a biá»ƒu tá»« tá»‡p Excel.
- **`F.5.2`**: Export thá»i khĂ³a biá»ƒu ra tá»‡p Excel.
- **`F.5.3`**: Xem thá»i khĂ³a biá»ƒu toĂ n khoa theo tuáº§n.
- **`F.5.4`**: PhĂ¢n cĂ´ng giáº£ng viĂªn giáº£ng dáº¡y lá»›p há»c pháº§n.
- **`F.5.5`**: XĂ³a lá»›p há»c pháº§n trĂªn thá»i khĂ³a biá»ƒu.
- **`F.5.6`**: Xem thá»i khĂ³a biá»ƒu cĂ¡ nhĂ¢n cá»§a BCN Khoa.

### 6. Module Thá»‘ng kĂª & ThĂ¹ lao (Statistics & Remuneration)
- **`F.6.1` â€“ `F.6.3`**: Thá»‘ng kĂª sá»‘ giá» dáº¡y, mĂ´n há»c theo há»c ká»³ vĂ  nÄƒm há»c.
- **`F.7.1` â€“ `F.7.19`**: Quáº£n lĂ½ há»c hĂ m/há»c vá»‹, há»‡ sá»‘ thĂ¹ lao vĂ  xem báº£ng tĂ­nh thĂ¹ lao giáº£ng dáº¡y.

---

## III. MĂƒ NGUá»’N CĂC Ká»CH Báº¢N KIá»‚M THá»¬ Tá»° Äá»˜NG (PAGE OBJECT MODEL)

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
    @Test(priority = 1, description = "F.1.1 - ÄÄƒng nháº­p tĂ i khoáº£n BCN Khoa thĂ nh cĂ´ng")
    public void testLoginFacultyBoardSuccess() {
        LoginPage loginPage = new LoginPage(driver);
        loginPage.login("bcnkhoa.cntt@vanlanguni.edu.vn", "Password123");
        Assert.assertTrue(loginPage.isLoggedInSuccessfully(), "ÄÄƒng nháº­p BCN Khoa khĂ´ng thĂ nh cĂ´ng!");
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
    private By userMenu = By.xpath("//span[contains(text(),'Quáº£n lĂ½ ngÆ°á»i dĂ¹ng')]");
    private By searchInput = By.cssSelector("input[type='search']");
    private By addUserBtn = By.xpath("//button[contains(text(),'ThĂªm ngÆ°á»i dĂ¹ng')]");
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
    @Test(priority = 1, description = "F.2.2 - ThĂªm giáº£ng viĂªn má»›i")
    public void testCreateNewUser() {
        UserManagementPage userPage = new UserManagementPage(driver);
        userPage.goToUserManagement();
        userPage.createUser("GV999", "Nguyá»…n VÄƒn Test", "nguyenvan.test@vanlanguni.edu.vn", "Giáº£ng viĂªn");
        Assert.assertTrue(userPage.isUserDisplayedInTable("GV999"), "Táº¡o giáº£ng viĂªn má»›i khĂ´ng thĂ nh cĂ´ng!");
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
    private By termMenu = By.xpath("//span[contains(text(),'Quáº£n lĂ½ há»c ká»³')]");
    private By addTermBtn = By.xpath("//button[contains(text(),'ThĂªm há»c ká»³')]");
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
    @Test(priority = 1, description = "F.3.2 - Táº¡o há»c ká»³ má»›i")
    public void testCreateNewTerm() {
        TermManagementPage termPage = new TermManagementPage(driver);
        termPage.goToTermManagement();
        termPage.createTerm("HK999", "Há»c ká»³ 3 NÄƒm há»c 2026-2027 (Test)");
        Assert.assertTrue(termPage.isTermExists("HK999"), "Táº¡o há»c ká»³ má»›i khĂ´ng thĂ nh cĂ´ng!");
    }
}
```

---

## IV. QUY Äá»NH Ná»˜P BĂ€I VĂ€ ÄĂ“NG GĂ“I

- **TĂªn thÆ° má»¥c ná»™p bĂ i**: `232_71ITSE41603_0102_Team06`
- **File BĂ¡o cĂ¡o Word**: `Team06_Ver1.0.docx` (LÆ°u tá»« file ná»™i dung trĂªn).
- **File MĂ£ nguá»“n (Zip)**: `Team06_Ver1.0.zip` (NĂ©n thÆ° má»¥c `232_71ITSE41603_Team06_Automation`).

