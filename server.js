const {Builder, By, Key, until} = require('selenium-webdriver');
const chrome = require('selenium-webdriver/chrome');

(async function example() {
    //console.log(chrome);
    var options = new chrome.Options();
    options.options_["debuggerAddress"] = "127.0.0.1:9222"

//     chrome_options.add_argument('--headless')
// chrome_options.add_argument('--no-sandbox')
    //withCapabilities(options.toCapabilities()).build();
    console.log(options);
    let driver = await new Builder()
    .forBrowser('chrome')
    .setChromeOptions(options)
    .build();
    try {
        // 네이버 실행
        await driver.get('https://www.nike.com/kr/launch/');
        
        const info_div = await driver.findElement(By.xpath('//*[@data-qa="top-nav-login-button"]')); 
        info_div.click();

        // function pbcopy(data) {
        //     var proc = require('child_process').spawn('pbcopy'); 
        //     proc.stdin.write(data); proc.stdin.end();
        // }

        // pbcopy("addddaddd");

        // driver.wait(function () {
        //     return driver.isElementPresent(webdriver.By.id("j_username"));
        // }, timeout);

        // driver.wait(until.elementLocated(By.id('j_username')), 5 * 1000).then(el => {
        //     el.sendKeys("aaaaa@gmail.com");
        //     driver.findElement(By.id("j_password")).sendKeys("123123");
        //     driver.findElement(By.className("uk-form-large")).submit();
        // });
    
        // const loginInput = await driver.findElement(By.css('#batBeacon389734363897')); 
        // console.log(loginInput);
        // await loginInput.sendKeys("email", "aaaaa@gmail.com");
        // const pwInput = await driver.findElement(By.id("j_password")); 
        // await pwInput.sendKeys("password", "123");
    }
    finally{
        setTimeout( () => {
            driver.quit();
        }
        , 10000);
    }
})();