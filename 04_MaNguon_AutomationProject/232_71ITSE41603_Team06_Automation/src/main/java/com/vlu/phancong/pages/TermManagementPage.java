package com.vlu.phancong.pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

public class TermManagementPage extends BasePage {

    // Locators for F.3.1 - F.3.6 (Term Management)
    private By termMenu = By.xpath("//span[contains(text(),'Quản lý học kỳ')]");
    private By addTermBtn = By.xpath("//button[contains(text(),'Thêm học kỳ')]");
    private By termIdInput = By.id("TermId");
    private By termNameInput = By.id("TermName");
    private By saveTermBtn = By.id("btnSaveTerm");
    private By lockTermBtn = By.xpath("//button[contains(@class, 'btn-lock-term')]");
    private By searchTermInput = By.cssSelector("input[type='search']");

    public TermManagementPage(WebDriver driver) {
        super(driver);
    }

    public void goToTermManagement() {
        click(termMenu);
    }

    public void createTerm(String termId, String termName) {
        click(addTermBtn);
        enterText(termIdInput, termId);
        enterText(termNameInput, termName);
        click(saveTermBtn);
    }

    public void searchTerm(String termName) {
        enterText(searchTermInput, termName);
    }

    public boolean isTermExists(String termName) {
        searchTerm(termName);
        return isElementDisplayed(By.xpath("//td[contains(text(),'" + termName + "')]"));
    }
}
