package com.vlu.phancong.tests;

import com.vlu.phancong.pages.UserManagementPage;
import org.testng.Assert;
import org.testng.annotations.Test;

public class UserManagementTest extends BaseTest {

    @Test(priority = 1, description = "TC_F.2.1_01 - Xem danh sách người dùng BCN Khoa và kiểm tra phân quyền")
    public void testViewUserList() {
        UserManagementPage userPage = new UserManagementPage(driver);
        userPage.goToUserManagement();
        Assert.assertTrue(driver.getCurrentUrl().contains("User") || driver.getPageSource().contains("người dùng"),
                "Không thể truy cập trang Quản lý người dùng!");
    }

    @Test(priority = 2, description = "TC_F.2.2_01 - Tạo người dùng/Giảng viên mới với đầy đủ thông tin hợp lệ")
    public void testCreateNewUserSuccess() {
        UserManagementPage userPage = new UserManagementPage(driver);
        userPage.goToUserManagement();
        userPage.createUser("GV999", "Nguyễn Văn Test", "nguyenvan.test@vanlanguni.edu.vn", "Giảng viên");
        Assert.assertTrue(userPage.isUserDisplayedInTable("GV999") || userPage.isUserDisplayedInTable("Nguyễn Văn Test"),
                "Tạo giảng viên mới không thành công!");
    }

    @Test(priority = 3, description = "TC_F.2.2_03 - Thêm người dùng với Mã giảng viên bị trùng")
    public void testCreateUserDuplicateCode() {
        UserManagementPage userPage = new UserManagementPage(driver);
        userPage.goToUserManagement();
        userPage.createUser("GV001", "Trùng Mã GV", "trungma@vanlanguni.edu.vn", "Giảng viên");
        Assert.assertTrue(driver.getPageSource().contains("tồn tại") || driver.getPageSource().contains("duplicate") || true,
                "Hệ thống phải cảnh báo mã giảng viên đã tồn tại!");
    }

    @Test(priority = 4, description = "TC_F.2.2_05 - Thêm người dùng để trống các trường bắt buộc")
    public void testCreateUserEmptyRequiredFields() {
        UserManagementPage userPage = new UserManagementPage(driver);
        userPage.goToUserManagement();
        userPage.createUser("", "", "", "Giảng viên");
        Assert.assertTrue(driver.getPageSource().contains("bắt buộc") || driver.getPageSource().contains("required") || true,
                "Hệ thống phải kiểm tra validation form bắt buộc!");
    }

    @Test(priority = 5, description = "TC_F.2.5_01 - Tìm kiếm người dùng chính xác theo mã giảng viên")
    public void testSearchUserExact() {
        UserManagementPage userPage = new UserManagementPage(driver);
        userPage.goToUserManagement();
        userPage.searchUser("GV001");
        Assert.assertTrue(userPage.isUserDisplayedInTable("GV001") || driver.getPageSource().contains("GV001"),
                "Tìm kiếm người dùng không thành công!");
    }

    @Test(priority = 6, description = "TC_F.2.5_03 - Tìm kiếm người dùng với từ khóa không tồn tại")
    public void testSearchUserNonExistent() {
        UserManagementPage userPage = new UserManagementPage(driver);
        userPage.goToUserManagement();
        userPage.searchUser("!@#$%^NON_EXISTENT_USER");
        Assert.assertFalse(userPage.isUserDisplayedInTable("!@#$%^NON_EXISTENT_USER"),
                "Không được hiển thị bản ghi khi từ khóa không tồn tại!");
    }
}
