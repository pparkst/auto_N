const {Builder, By, Key, until} = require('selenium-webdriver');

(async function example() {
    let driver = await new Builder()
    .forBrowser('chrome')
    .build();
    try {
        // 네이버 실행
        await driver.get('https://www.nike.com/kr/launch/');
        
        const info_div = await driver.findElement(By.xpath('//*[@data-qa="top-nav-login-button"]')); 
        info_div.click();
    
        const loginInput = await driver.findElement(By.id('#j_username')); 
        await loginInput.sendKeys("email", "aaaaa@gmail.com");
        const pwInput = await driver.findElement(By.id("#j_password")); 
        await pwInput.sendKeys("password", "123");
    }
    finally{
        setTimeout( () => {
            driver.quit();
        }
        , 10000);
    }
})();