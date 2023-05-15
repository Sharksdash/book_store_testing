            #4. Shop: отображение страницы товара
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
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
shop_btn=driver.find_element_by_link_text("Shop")
shop_btn.click()
time.sleep(3)
book_btn =driver.find_element_by_css_selector(".post-181 > .button.product_type_simple")
book_btn.click()
title_of_book = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".product_title"), 'HTML5 Forms'))
driver.quit()

            #5. Shop: количество товаров в категории
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
shop_btn=driver.find_element_by_link_text("Shop")
shop_btn.click()
html_btn=driver.find_element_by_link_text("HTML")
html_btn.click()
three_items = driver.find_elements_by_css_selector("ul > li > a > h3")
if len(three_items) == 3:
    print("В категории HTML 3 товара")
else:
    print("Количество товара в категории HTML:" + str(len(three_items)))
driver.quit()

            #6. Shop: сортировка товаров
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
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
shop_btn=driver.find_element_by_link_text("Shop")
shop_btn.click()
items_selector = driver.find_element_by_css_selector(".orderby")
items_selector_default = items_selector.get_attribute("value")
if items_selector_default == "menu_order":
    print("Выбрана сортировка по умолчанию")
else:
    print("Не выбрана сортировка по умолчанию")
select = Select(items_selector)
select.select_by_value("price-desc")
items_selector = driver.find_element_by_css_selector(".orderby")
items_selector_desc = items_selector.get_attribute("value")
if items_selector_desc == "price-desc":
    print("Выбрана сортировка по убыванию")
else:
    print("Не выбрана сортировка по убыванию")
driver.quit()

            #7. Shop: отображение, скидка товара
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
shop_btn=driver.find_element_by_link_text("Shop")
shop_btn.click()
book_open=driver.find_element_by_css_selector(".post-169 > .button")
book_open.click()
book_old_price = driver.find_element_by_css_selector(".price > del > span")
book_old_price_text = book_old_price.text
assert book_old_price_text == "₹600.00"
book_new_price = driver.find_element_by_css_selector(".price > ins > span")
book_new_price_text = book_new_price.text
assert book_new_price_text == "₹450.00"
book_first_page = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".images .attachment-shop_single")))
book_first_page.click()
book_close = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")))
book_close.click()
driver.quit()

            #8. Shop: проверка цены в корзине
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
time.sleep(3)
shop_btn=driver.find_element_by_link_text("Shop")
shop_btn.click()
java_book_open=driver.find_element_by_css_selector(".post-165 > .button")
java_book_open.click()
how_many_books = driver.find_element_by_css_selector(".wpmenucart-contents .cartcontents")
how_many_books_text = how_many_books.text
assert how_many_books_text == "1 Item"
book_cost = driver.find_element_by_css_selector(".wpmenucart-contents > .amount")
book_cost_text = book_cost.text
assert book_cost_text == "₹350.00"
cart_btn=driver.find_element_by_css_selector(".wpmenucart-contents")
cart_btn.click()
subtotal = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal .woocommerce-Price-amount"), "₹350.00"))
total = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total .woocommerce-Price-amount"), "₹357.00"))
driver.quit()


            #9. Shop: работа в корзине
import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
time.sleep(3)
shop_btn=driver.find_element_by_link_text("Shop")
shop_btn.click()
driver.execute_script("window.scrollTo(0, 300)")
java_book_open=driver.find_element_by_css_selector(".post-165 > .button")
java_book_open.click()
time.sleep(3)
second_java_book_open=driver.find_element_by_css_selector(".post-165 > .button")
second_java_book_open.click()
cart_btn=driver.find_element_by_css_selector(".wpmenucart-contents")
cart_btn.click()
time.sleep(3)
remove_btn=driver.find_element_by_class_name("remove")
remove_btn.click()
undo_btn = driver.find_element_by_link_text("Undo?")
undo_btn.click()
three_books = driver.find_element_by_css_selector("tbody > .product-quantity > .input-text")
three_books.clear()
three_books.send_keys("3")
update_basket= driver.find_element_by_css_selector(".actions > .button")
update_basket.click()
books_value = driver.find_element_by_css_selector("tbody > .product-quantity > .input-text")
books_value_text = books_value.text
assert books_value_text == "3"
time.sleep(3)
apply_btn=driver.find_element_by_css_selector(".coupon > .button")
apply_btn.click()
error = driver.find_element_by_css_selector(".woocommerce-error")
error_text = error.text
assert error_text == "Please enter a coupon code."
driver.quit()

        #10. Shop: покупка товара
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
time.sleep(3)
shop_btn=driver.find_element_by_link_text("Shop")
shop_btn.click()
driver.execute_script("window.scrollTo(0, 300)")
java_book_open=driver.find_element_by_css_selector(".post-165 > .button")
java_book_open.click()
time.sleep(3)
cart_btn=driver.find_element_by_css_selector(".wpmenucart-contents")
cart_btn.click()
checkout_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "checkout-button")))
checkout_btn.click()
first_name = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "billing_first_name")))
first_name.send_keys("Romeo")
last_name = driver.find_element_by_id("billing_last_name")
last_name.send_keys("Gestron")
email = driver.find_element_by_id("billing_email")
email.send_keys("322343543frge@email.com")
phone = driver.find_element_by_id("billing_phone")
phone.send_keys("89543356744")
country = driver.find_element_by_id("s2id_billing_country")
country.click()
country_search = driver.find_element_by_id("s2id_autogen1_search")
country_search.send_keys("Russia")
country_second_field = driver.find_element_by_class_name("select2-match")
country_second_field.click()
address = driver.find_element_by_id("billing_address_1")
address.send_keys("Moscow")
city = driver.find_element_by_id("billing_city")
city.send_keys("Moscow")
state = driver.find_element_by_id("billing_state")
state.send_keys("Moscow district")
postcode = driver.find_element_by_id("billing_postcode")
postcode.send_keys("344214233")
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(5)
payment_check = driver.find_element_by_id("payment_method_cheque")
payment_check.click()
place_order_btn = driver.find_element_by_id("place_order")
place_order_btn.click()
success_message = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-thankyou-order-received"),
"Thank you. Your order has been received."))
payment_method_message = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tfoot > tr:nth-child(3) > td"), "Check Payments"))
driver.quit()