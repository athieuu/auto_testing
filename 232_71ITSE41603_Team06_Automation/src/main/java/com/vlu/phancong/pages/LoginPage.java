
package com.vlu.phancong.pages;

import java.time.Duration;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class LoginPage extends BasePage {

    private final By openIdLoginBtn = By.id("OpenIdConnect");

    // Microsoft SSO
    private final By emailField = By.id("i0116");
    private final By passwordField = By.id("i0118");
    private final By submitBtn = By.id("idSIButton9");

    // Trang chủ BCN Khoa
    private final By facultyBoardRole = By.xpath(
        "//*[contains(normalize-space(.), 'BCN khoa')]"
    );

    private final By logoutBtn =
        By.xpath("//a[contains(@href, 'Logout')]");

    public LoginPage(WebDriver driver) {
        super(driver);
    }

    public void navigateTo(String url) {
        driver.get(url);
    }

    public void login(String email, String password) {

        WebDriverWait wait =
            new WebDriverWait(driver, Duration.ofSeconds(30));

        // Mở Microsoft Login nếu có nút
        if (isElementDisplayed(openIdLoginBtn)) {
            wait.until(ExpectedConditions.elementToBeClickable(
                openIdLoginBtn)).click();
        }

        // Chờ màn hình Microsoft hoặc phiên đăng nhập sẵn có
        wait.until(d ->
            !d.findElements(emailField).isEmpty()
            || !d.findElements(passwordField).isEmpty()
            || isFacultyBoardLoggedIn()
        );

        if (isFacultyBoardLoggedIn()) {
            return;
        }

        // Nhập Email nếu Microsoft yêu cầu
        if (!driver.findElements(emailField).isEmpty()) {

            wait.until(ExpectedConditions.visibilityOfElementLocated(
                emailField)).sendKeys(email);

            wait.until(ExpectedConditions.elementToBeClickable(
                submitBtn)).click();
        }

        // Nhập mật khẩu
        wait.until(ExpectedConditions.visibilityOfElementLocated(
            passwordField)).sendKeys(password);

        wait.until(ExpectedConditions.elementToBeClickable(
            submitBtn)).click();

        // Chờ người dùng hoàn tất MFA nếu được yêu cầu
        // Không tự động vượt qua bước xác thực bảo mật

       // Chờ tối đa 120 giây để hoàn tất Microsoft SSO/MFA
        WebDriverWait loginWait =
            new WebDriverWait(driver, Duration.ofSeconds(180));

        loginWait.until(d -> isFacultyBoardLoggedIn());
    }

    public boolean isFacultyBoardLoggedIn() {
        return driver.getCurrentUrl().contains("Phancong02")
            && isElementDisplayed(facultyBoardRole);
    }

    public boolean isLoggedInSuccessfully() {
        return isFacultyBoardLoggedIn();
    }

    public void logout() {
        if (isElementDisplayed(logoutBtn)) {
            click(logoutBtn);
        }
    }
}
