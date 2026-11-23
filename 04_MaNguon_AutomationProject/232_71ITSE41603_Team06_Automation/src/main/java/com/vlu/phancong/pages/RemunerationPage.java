package com.vlu.phancong.pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

public class RemunerationPage extends BasePage {

    // Locators for F.7.1 - F.7.19 (Remuneration Management)
    private By remunerationMenu = By.xpath("//span[contains(text(),'Quản lý thù lao') or contains(text(),'Thù lao')]");
    private By remunerationTable = By.className("remuneration-table");
    private By exportRemunerationBtn = By.id("btnExportRemuneration");
    private By configCoefficientBtn = By.id("btnConfigCoefficient");
    private By termSelect = By.id("selectTerm");

    public RemunerationPage(WebDriver driver) {
        super(driver);
    }

    public void goToRemuneration() {
        click(remunerationMenu);
    }

    public void selectTerm(String termName) {
        if (isElementDisplayed(termSelect)) {
            driver.findElement(termSelect).sendKeys(termName);
        }
    }

    public void exportRemuneration() {
        click(exportRemunerationBtn);
    }

    public boolean isRemunerationTableDisplayed() {
        return isElementDisplayed(remunerationTable) || isElementDisplayed(By.tagName("table"));
    }
}
