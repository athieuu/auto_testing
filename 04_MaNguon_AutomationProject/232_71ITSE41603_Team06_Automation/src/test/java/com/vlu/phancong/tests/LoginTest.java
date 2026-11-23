package com.vlu.phancong.tests;

import com.vlu.phancong.pages.LoginPage;
import org.testng.Assert;
import org.testng.annotations.Test;

public class LoginTest extends BaseTest {

    @Test(priority = 1, description = "TC_F.1.1_01 - Đăng nhập tài khoản BCN Khoa với thông tin hợp lệ")
    public void testLoginFacultyBoardSuccess() {
        LoginPage loginPage = new LoginPage(driver);
        loginPage.login("bcnkhoa.cntt@vanlanguni.edu.vn", "Password123");
        Assert.assertTrue(loginPage.isLoggedInSuccessfully(), "Đăng nhập BCN Khoa không thành công!");
    }

    @Test(priority = 2, description = "TC_F.1.1_03 - Đăng nhập thất bại khi nhập sai mật khẩu")
    public void testLoginInvalidPassword() {
        LoginPage loginPage = new LoginPage(driver);
        loginPage.login("bcnkhoa.cntt@vanlanguni.edu.vn", "WrongPassword!@#");
        Assert.assertFalse(loginPage.isLoggedInSuccessfully(), "Hệ thống không được phép đăng nhập khi sai mật khẩu!");
    }

    @Test(priority = 3, description = "TC_F.1.1_04 - Đăng nhập thất bại với email không thuộc tên miền Văn Lang")
    public void testLoginInvalidDomainEmail() {
        LoginPage loginPage = new LoginPage(driver);
        loginPage.login("testuser@gmail.com", "Password123");
        Assert.assertFalse(loginPage.isLoggedInSuccessfully(), "Hệ thống chỉ cho phép email @vanlanguni.edu.vn!");
    }

    @Test(priority = 4, description = "TC_F.1.1_05 - Đăng nhập thất bại khi để trống trường Email và Mật khẩu")
    public void testLoginEmptyCredentials() {
        LoginPage loginPage = new LoginPage(driver);
        loginPage.login("", "");
        Assert.assertFalse(loginPage.isLoggedInSuccessfully(), "Hệ thống phải hiển thị validation yêu cầu nhập đầy đủ!");
    }

    @Test(priority = 5, description = "TC_F.1.1_08 - Đăng xuất tài khoản và xác nhận hủy phiên")
    public void testLogoutFlow() {
        LoginPage loginPage = new LoginPage(driver);
        loginPage.logout();
        Assert.assertTrue(driver.getCurrentUrl().contains("Login") || driver.getCurrentUrl().contains("Phancong02"),
                "Đăng xuất không chuyển hướng về trang đăng nhập!");
    }
}
