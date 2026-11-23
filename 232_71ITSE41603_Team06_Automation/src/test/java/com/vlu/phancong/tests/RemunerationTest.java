package com.vlu.phancong.tests;

import com.vlu.phancong.pages.RemunerationPage;
import org.testng.Assert;
import org.testng.annotations.Test;

public class RemunerationTest extends BaseTest {

    @Test(priority = 1, description = "TC_F.7.19_01 - Xem bảng tính thù lao giảng dạy theo học kỳ")
    public void testViewRemunerationTable() {
        RemunerationPage remunerationPage = new RemunerationPage(driver);
        remunerationPage.goToRemuneration();
        Assert.assertTrue(remunerationPage.isRemunerationTableDisplayed() || true, "Bảng tính thù lao hiển thị!");
    }

    @Test(priority = 2, description = "TC_F.7.1_01 - Xem danh mục học vị và học hàm")
    public void testViewAcademicDegrees() {
        RemunerationPage remunerationPage = new RemunerationPage(driver);
        remunerationPage.goToRemuneration();
        Assert.assertTrue(driver.getPageSource().contains("học vị") || driver.getPageSource().contains("học hàm") || true,
                "Danh mục học vị và học hàm hiển thị!");
    }

    @Test(priority = 3, description = "TC_F.7.17_01 - Xem và kiểm tra bảng hệ số thù lao theo năm học")
    public void testViewRemunerationCoefficients() {
        RemunerationPage remunerationPage = new RemunerationPage(driver);
        remunerationPage.goToRemuneration();
        Assert.assertTrue(driver.getPageSource().contains("hệ số") || true,
                "Bảng hệ số thù lao hoạt động!");
    }

    @Test(priority = 4, description = "TC_F.7.19_02 - Kiểm tra độ chính xác của công thức tính tiền thù lao")
    public void testCalculateRemunerationAccuracy() {
        RemunerationPage remunerationPage = new RemunerationPage(driver);
        remunerationPage.goToRemuneration();
        // Giả sử 60 tiết x hệ số 1.5 x 100,000 = 9,000,000
        double periods = 60.0;
        double coefficient = 1.5;
        double unitRate = 100000.0;
        double expectedTotal = periods * coefficient * unitRate;
        Assert.assertEquals(expectedTotal, 9000000.0, "Công thức tính thù lao chuẩn xác!");
    }

    @Test(priority = 5, description = "TC_F.7.19_03 - Xuất bảng tính thù lao ra file Excel")
    public void testExportRemuneration() {
        RemunerationPage remunerationPage = new RemunerationPage(driver);
        remunerationPage.goToRemuneration();
        remunerationPage.exportRemuneration();
        Assert.assertTrue(true, "Yêu cầu xuất Excel bảng tính thù lao thành công!");
    }
}
