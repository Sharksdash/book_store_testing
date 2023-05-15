            #2. Registration_login: регистрация аккаунта
import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
time.sleep(3)
my_account_btn =driver.find_element_by_css_selector("#menu-item-50 > a")
my_account_btn.click()
reg_email= driver.find_element_by_id("reg_email")
reg_email.send_keys("yourfavoritetester@gmail.com")
reg_password=driver.find_element_by_id("reg_password")
reg_password.send_keys("mypasswordishard")
register_btn = driver.find_element_by_name("register")
register_btn.click()
driver.quit()

        #3. Registration_login: логин в систему
import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
time.sleep(3)
my_account_btn =driver.find_element_by_css_selector("#menu-item-50 > a")
my_account_btn.click()
login_email= driver.find_element_by_id("username")
login_email.send_keys("yourfavoritetester@gmail.com")
log_password=driver.find_element_by_id("password")
log_password.send_keys("mypasswordishard")
login_btn = driver.find_element_by_name("login")
login_btn.click()
driver.quit()