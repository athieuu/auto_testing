package com.vlu.phancong.pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

public class MajorManagementPage extends BasePage {

    // Locators for F.4.1 - F.4.5 (Major Management)
    private By majorMenu = By.xpath("//span[contains(text(),'Quản lý ngành') or contains(text(),'Ngành học')]");
    private By addMajorBtn = By.xpath("//button[contains(text(),'Thêm ngành') or contains(@id,'btnAddMajor')]");
    private By majorIdInput = By.id("MajorId");
    private By majorNameInput = By.id("MajorName");
    private By saveMajorBtn = By.id("btnSaveMajor");
    private By searchMajorInput = By.cssSelector("input[type='search']");

    public MajorManagementPage(WebDriver driver) {
        super(driver);
    }

    public void goToMajorManagement() {
        click(majorMenu);
    }

    public void createMajor(String majorId, String majorName) {
        click(addMajorBtn);
        enterText(majorIdInput, majorId);
        enterText(majorNameInput, majorName);
        click(saveMajorBtn);
    }

    public void searchMajor(String keyword) {
        enterText(searchMajorInput, keyword);
    }

    public boolean isMajorExists(String majorName) {
        searchMajor(majorName);
        return isElementDisplayed(By.xpath("//td[contains(text(),'" + majorName + "')]"));
    }
}
