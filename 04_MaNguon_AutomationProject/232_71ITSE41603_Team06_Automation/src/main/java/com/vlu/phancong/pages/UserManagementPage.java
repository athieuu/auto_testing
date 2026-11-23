package com.vlu.phancong.pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

public class UserManagementPage extends BasePage {

    // Locators for F.2.1 - F.2.6 (User Management)
    private By userMenu = By.xpath("//span[contains(text(),'Quản lý người dùng')]");
    private By searchInput = By.cssSelector("input[type='search']");
    private By addUserBtn = By.xpath("//button[contains(text(),'Thêm người dùng')]");
    private By userTable = By.id("user-table");
    private By userCodeInput = By.id("UserCode");
    private By fullNameInput = By.id("FullName");
    private By emailInput = By.id("UserEmail");
    private By roleSelect = By.id("RoleSelect");
    private By saveBtn = By.id("btnSaveUser");
    private By toastMessage = By.className("toast-message");

    public UserManagementPage(WebDriver driver) {
        super(driver);
    }

    public void goToUserManagement() {
        click(userMenu);
    }

    public void searchUser(String keyword) {
        enterText(searchInput, keyword);
    }

    public void createUser(String code, String name, String email, String role) {
        click(addUserBtn);
        enterText(userCodeInput, code);
        enterText(fullNameInput, name);
        enterText(emailInput, email);
        click(saveBtn);
    }

    public boolean isUserDisplayedInTable(String keyword) {
        searchUser(keyword);
        return isElementDisplayed(By.xpath("//td[contains(text(),'" + keyword + "')]"));
    }

    public String getToastMessage() {
        return getText(toastMessage);
    }
}
