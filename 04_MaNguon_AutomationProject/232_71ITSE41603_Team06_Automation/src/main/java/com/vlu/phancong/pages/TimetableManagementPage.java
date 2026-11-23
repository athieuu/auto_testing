package com.vlu.phancong.pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

public class TimetableManagementPage extends BasePage {

    // Locators for F.5.1 - F.5.6 (Timetable Management)
    private By timetableMenu = By.xpath("//span[contains(text(),'Quản lý thời khóa biểu')]");
    private By importBtn = By.id("btnImportTimetable");
    private By fileInput = By.cssSelector("input[type='file']");
    private By submitImportBtn = By.id("btnSubmitImport");
    private By exportBtn = By.id("btnExportTimetable");
    private By assignLecturerSelect = By.cssSelector("select.lecturer-dropdown");
    private By saveAssignBtn = By.id("btnSaveAssign");

    public TimetableManagementPage(WebDriver driver) {
        super(driver);
    }

    public void goToTimetableManagement() {
        click(timetableMenu);
    }

    public void importTimetable(String filePath) {
        click(importBtn);
        driver.findElement(fileInput).sendKeys(filePath);
        click(submitImportBtn);
    }

    public void exportTimetable() {
        click(exportBtn);
    }

    public boolean isTimetableLoaded() {
        return isElementDisplayed(By.className("timetable-grid"));
    }
}
