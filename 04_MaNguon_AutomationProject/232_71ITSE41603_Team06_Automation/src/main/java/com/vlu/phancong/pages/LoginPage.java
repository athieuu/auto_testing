package com.vlu.phancong.pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

public class LoginPage extends BasePage {

    // Locators
    private By openIdLoginBtn = By.id("OpenIdConnect");
    private By emailField = By.name("Email");
    private By passwordField = By.name("Password");
    private By submitBtn = By.cssSelector("button[type='submit']");
    private By userDisplayName = By.className("user-profile-name");
    private By logoutBtn = By.xpath("//a[contains(@href, 'Logout')]");

    public LoginPage(WebDriver driver) {
        super(driver);
    }

    public void navigateTo(String url) {
        driver.get(url);
    }

    public void login(String email, String password) {
        if (isElementDisplayed(openIdLoginBtn)) {
            click(openIdLoginBtn);
        }
        if (isElementDisplayed(emailField)) {
            enterText(emailField, email);
            enterText(passwordField, password);
            click(submitBtn);
        }
    }

    public boolean isLoggedInSuccessfully() {
        return isElementDisplayed(userDisplayName) || driver.getCurrentUrl().contains("Home");
    }

    public void logout() {
        if (isElementDisplayed(logoutBtn)) {
            click(logoutBtn);
        }
    }
}
