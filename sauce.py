from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from Constants import globalConstants 

class Test_Sauce:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(globalConstants.URL)
        
    def test_invalid_login(self):
        # en fazla 5 sniye olacak şekilde user-name id'li elementin görünmesini bekle
        # locatorde verilen element görünür olduğunda(until) 5 saniye beklet 
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "user-name")))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "password")))
        passwordInput =self.driver.find_element(By.ID, "password")
        usernameInput.send_keys("1")
        passwordInput.send_keys("1")
        loginBtn = self.driver.find_element(By.ID, "login-button")  
        loginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
        print(f"TEST SONUCU: {testResult}")

    def test_valid_login(self):
        self.driver.get(globalConstants.URL)
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "user-name")))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "password")))
        passwordInput =self.driver.find_element(By.ID, "password")
        # Action Chains
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(usernameInput, "standard_user")
        actions.send_keys_to_element(passwordInput, "secret_sauce") 
        actions.perform()
        # usernameInput.send_keys("standard_user")
        # passwordInput.send_keys("secret_sauce")
        loginBtn = self.driver.find_element(By.ID, "login-button")  
        loginBtn.click()
        sleep(9)

        
   
testClass = Test_Sauce()
testClass.test_invalid_login()
testClass.test_valid_login()