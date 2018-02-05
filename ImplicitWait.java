package Tests;

import java.util.concurrent.TimeUnit;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromDriver;

public class syncchroniz {
    public static void main(String[] args){
        System.setProperty("webdriver.chrome.driver","C:\\selenium\\chromdriver.exe");
        WebDriver driver=new ChromeDriver();
        driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
        driver.get("http://alaskatrips.poweredbygps.com/g/pt/hotels?MDPCID=ALASKA-US.TPS.BRAND.Hotels.HOTEL");
        driver.findElement(By.id("H-destination")).sendKeys("nyc");
        driver.findElement(By.id("H-destination")).sendKeys(Keys.TAB);
        driver.findElement(By.id("H-fromDate")).sendKeys(Keys.ENTER);
        
    driver.findElement(By.xpath("//a[contains(@href,'New-York-Hotels-Days-Hotel')]")).click();
        
    }
}