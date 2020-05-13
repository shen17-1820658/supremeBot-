from selenium import webdriver
import time

name = "Cj Shen"
email = "shen17@uw.edu"
tel = "1234567890"
address = "124 anytown"
apt_number = "1"
zip = "98105"
city = "Seattle"
state = "WA"
country = "USA"

number = "0000 0000 0000 0000"
expiration_month = "05"
expiration_year = "2022"
cvv = "123"

# Set website
chromedriver_location = "chromedriver.exe"
driver = webdriver.Chrome(chromedriver_location)
driver.get("https://www.supremenewyork.com/shop/accessories/nq5hkuef2/mt26hz7la")

# Add item to cart
add_to_cart = '//*[@id="add-remove-buttons"]/input'
driver.find_element_by_xpath(add_to_cart).click()

# Delay Execution
time.sleep(2)

checkout_button = '//*[@id="cart"]/a[2]'
driver.find_element_by_xpath(checkout_button).click()

name_xpath = '//*[@id="order_billing_name"]'
driver.find_element_by_xpath(name_xpath).send_keys(name)

email_xpath = '//*[@id="order_email"]'
driver.find_element_by_xpath(email_xpath).send_keys(email)

tel_xpath = '//*[@id="order_tel"]'
driver.find_element_by_xpath(tel_xpath).send_keys(tel)

address_xpath = '//*[@id="bo"]'
driver.find_element_by_xpath(address_xpath).send_key(address)

apt_xpath = '//*[@id="oba3"]'
driver.find_element_by_xpath(apt_xpath).send_keys(apt_number)

zip_xpath = '//*[@id="order_billing_zip"]'
driver.find_element_by_xpath(zip_xpath).send_keys(zip)

city_xpath = '//*[@id="order_billing_city"]'
driver.find_element_by_xpath(city_xpath).send_keys(city)

state_xpath = '//*[@id="order_billing_state]/option[56]'
driver.find_element_by_xpath(state_xpath).click()

number_xpath = '//*[@id="rnsnckrn"]'
driver.find_element_by_xpath(number_xpath).send_keys(number)

card_month_xpath = '//*[@id="credit_card_month"]/option[5]'
driver.find_element_by_xpath(card_month_xpath).click()

card_year_xpath = '//*[@id="credit_card_year"]/option[3]'
driver.find_element_by_xpath(card_year_xpath).click()

cvv_xpath = '//*[@id="orcer"]'
driver.find_element_by_xpath(cvv_xpath).send_keys(cvv)

i_agree_xpath = '//*[@id="cart-cc"]/fieldset/p[2]/label/div/ins'
driver.find_element_by_xpath(i_agree_xpath).click()

process_payment_xpath = '//*[@id="pay"]/input'
driver.find_element_by_xpath(process_payment_xpath).click()



print("Web Driver Run")
