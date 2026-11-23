
package com.vlu.phancong.tests;

import java.io.File;
import java.net.HttpURLConnection;
import java.net.URL;
import java.time.Duration;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.testng.annotations.AfterSuite;
import org.testng.annotations.BeforeSuite;

public class BaseTest {

    protected static WebDriver driver;
    protected String baseUrl =
        "https://cntttest.vanlanguni.edu.vn:18081/Phancong02/";

    protected static boolean isAttached = false;

    private boolean isDebugPortOpen() {
        try {
            URL url = new URL("http://127.0.0.1:9222/json/version");
            HttpURLConnection conn =
                (HttpURLConnection) url.openConnection();
            conn.setConnectTimeout(1000);
            conn.setReadTimeout(1000);
            conn.connect();
            return conn.getResponseCode() == 200;
        } catch (Exception e) {
            return false;
        }
    }

    @BeforeSuite
    public void setUp() {

        if (driver != null) {
            return;
        }

        ChromeOptions options = new ChromeOptions();
        options.setAcceptInsecureCerts(true);

        if (isDebugPortOpen()) {

            System.out.println(
                ">>> Dang ket noi trinh duyet port 9222..."
            );

            options.setExperimentalOption(
                "debuggerAddress", "127.0.0.1:9222"
            );

            driver = new ChromeDriver(options);
            isAttached = true;

        } else {

            System.out.println(
                ">>> Khoi dong trinh duyet moi..."
            );

            String coccocPath =
                "C:\\Program Files\\CocCoc\\Browser\\Application\\browser.exe";

            if (new File(coccocPath).exists()) {
                options.setBinary(coccocPath);
            }

            options.addArguments("--remote-allow-origins=*");

            driver = new ChromeDriver(options);
            driver.manage().window().maximize();
            driver.get(baseUrl);
        }

        driver.manage().timeouts()
            .implicitlyWait(Duration.ofSeconds(10));
    }

    @AfterSuite
    public void tearDown() {

        if (driver != null && !isAttached) {
            driver.quit();
        }

        driver = null;
        isAttached = false;
    }
}
