from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

class sauceExam:
    # Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak "Epic sadface: Username is required" gösterilir.
    def emptyLogin(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        loginBtn = driver.find_element(By.ID,"login-button")
        loginBtn.click()
        sleep(2)
        errorMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        errorResult = errorMessage.text == "Epic sadface: Username is required"
        sleep(2)
        #Kullanıcı adı ve şifre alanları boş geçildiğinde bu iki inputun yanında da kırmızı "X" ikonu çıkmalıdır. Daha sonra aşağıda çıkan uyarı mesajının kapatma butonuna tıklandığında bu "X" ikonları kaybolmalıdır.
        errorX = driver.find_element(By.CLASS_NAME,"error-button")
        errorX.click()
        print(f"Test Sonucu: {errorX}")
        print(f"Test Sonucu: {errorResult}")
        sleep(1)

    def emptyPassword(self):
        # Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak "Epic sadface: Password is required" gösterilir.
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        username = driver.find_element(By.ID,"user-name")
        username.send_keys("1")
        loginBtn = driver.find_element(By.ID,"login-button")
        loginBtn.click()
        sleep(2)
        errorMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        errorResult = errorMessage.text == "Epic sadface: Password is required" 
        print(f"Test Sonucu: {errorResult}")
        sleep(1)

    def login(self):
        # Kullanıcı adı locked_out_user şifre alanı secret_sauce gönderildiğinde Epic sadface: Sorry, this user has been locked out. mesajı gösterilir
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(1)
        username = driver.find_element(By.ID,"user-name")
        username.send_keys("locked_out_user")
        password = driver.find_element(By.ID,"password")
        password.send_keys("secret_sauce")
        sleep(1)
        loginBtn = driver.find_element(By.ID,"login-button")
        loginBtn.click()
        errorMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        errorResult =errorMessage.text == "Epic sadface: Sorry, this user has been locked out." 
        print(f"Test Sonucu: {errorResult}")
        sleep(6)

    def pageLogin(self):
        # Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir.
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        username = driver.find_element(By.ID,"user-name")
        username.send_keys("standard_user")
        password = driver.find_element(By.ID,"password")
        password.send_keys("secret_sauce")
        sleep(1)
        loginBtn = driver.find_element(By.ID,"login-button")
        loginBtn.click()
        sleep(3)
        # Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır.
        driver = webdriver.Chrome()
        listOfCourse = driver.find_elements(By.CLASS_NAME,"inventory_item")
        print(f"Şu anda {len(listOfCourse)} adet ürün vardır.")
        sleep(2)


testClass = sauceExam()
testClass.emptyLogin()
testClass.emptyPassword()
testClass.login()
testClass.pageLogin()
