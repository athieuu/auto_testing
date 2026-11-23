package com.vlu.phancong.tests;

import java.io.File;
import java.net.HttpURLConnection;
import java.net.URL;
import java.time.Duration;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;

public class BaseTest {
    protected WebDriver driver;
    protected String baseUrl = "https://cntttest.vanlanguni.edu.vn:18081/Phancong02/";
    protected boolean isAttached = false;

    private boolean isDebugPortOpen() {
        try {
            URL url = new URL("http://127.0.0.1:9222/json/version");
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setConnectTimeout(1000);
            conn.connect();
            return conn.getResponseCode() == 200;
        } catch (Exception e) {
            return false;
        }
    }

    @BeforeClass
    public void setUp() {
        ChromeOptions options = new ChromeOptions();

        if (isDebugPortOpen()) {
            System.out.println("=========================================================");
            System.out.println(">>> Đang kết nối trực tiếp vào Cốc Cốc đang mở (port 9222)...");
            System.out.println("=========================================================");
            options.setExperimentalOption("debuggerAddress", "127.0.0.1:9222");
            driver = new ChromeDriver(options);
            isAttached = true;
        } else {
            System.out.println(">>> Cổng 9222 chưa mở, đang khởi động trình duyệt mới...");
            String coccocPath = "C:\\Program Files\\CocCoc\\Browser\\Application\\browser.exe";
            if (new File(coccocPath).exists()) {
                options.setBinary(coccocPath);
            }
            options.addArguments("--remote-allow-origins=*");
            driver = new ChromeDriver(options);
            driver.manage().window().maximize();
            driver.get(baseUrl);
        }

        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
    }

    @AfterClass
    public void tearDown() {
        // Không đóng trình duyệt nếu đang kết nối trực tiếp vào Cốc Cốc của người dùng
        if (driver != null && !isAttached) {
            driver.quit();
        }
    }
}
