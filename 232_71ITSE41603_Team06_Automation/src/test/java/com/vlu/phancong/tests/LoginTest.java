
package com.vlu.phancong.tests;

import com.vlu.phancong.pages.LoginPage;
import org.testng.Assert;
import org.testng.annotations.Test;

public class LoginTest extends BaseTest {

    @Test(description = "TC_F.1.1_01 - Dang nhap BCN Khoa thanh cong")
    public void testLoginFacultyBoardSuccess() {

        LoginPage loginPage = new LoginPage(driver);

        String email = System.getenv("VLU_TEST_EMAIL");
        String password = System.getenv("VLU_TEST_PASSWORD");

        Assert.assertNotNull(email,
            "Chua cau hinh VLU_TEST_EMAIL");

        Assert.assertNotNull(password,
            "Chua cau hinh VLU_TEST_PASSWORD");

        loginPage.login(email, password);

        Assert.assertTrue(
            loginPage.isFacultyBoardLoggedIn(),
            "Dang nhap thanh cong nhung khong thay vai tro BCN khoa!"
        );
    }
}
