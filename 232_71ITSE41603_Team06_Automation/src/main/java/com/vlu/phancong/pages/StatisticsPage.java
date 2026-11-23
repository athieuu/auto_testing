package com.vlu.phancong.pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

public class StatisticsPage extends BasePage {

    // Locators for F.6.1 - F.6.3 (Statistics Management)
    private By statisticsMenu = By.xpath("//span[contains(text(),'Thống kê')]");
    private By hoursInTermTab = By.xpath("//a[contains(text(),'Giờ dạy theo học kỳ')]");
    private By hoursInYearTab = By.xpath("//a[contains(text(),'Giờ dạy theo năm')]");
    private By subjectsInTermTab = By.xpath("//a[contains(text(),'Môn học theo học kỳ')]");
    private By statsTable = By.className("statistics-table");

    public StatisticsPage(WebDriver driver) {
        super(driver);
    }

    public void goToStatistics() {
        click(statisticsMenu);
    }

    public void viewHoursInTerm() {
        click(hoursInTermTab);
    }

    public void viewHoursInYear() {
        click(hoursInYearTab);
    }

    public void viewSubjectsInTerm() {
        click(subjectsInTermTab);
    }

    public boolean isStatisticsDisplayed() {
        return isElementDisplayed(statsTable) || isElementDisplayed(By.tagName("table"));
    }
}
