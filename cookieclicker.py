from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_experimental_option('excludeSwitches', ['enable-logging'])

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://orteil.dashnet.org/cookieclicker/")

cookie_id = "bigCookie"
cookies_id = "cookies"
lang_id = "langSelect-EN"
product_id = "product"
prod_price_prefix = "productPrice"

lang_element = WebDriverWait(driver, 5).until(
	EC.presence_of_element_located((By.ID, lang_id))
)
lang_element.click()

while True:
	try:
		WebDriverWait(driver, 5).until(
			EC.presence_of_element_located((By.ID, cookie_id))
		)

		cookie = driver.find_element(By.ID, cookie_id)
		cookie.click()
		cookies_count = driver.find_element(By.ID, cookies_id).text.split(" ")[0]
		cookies_count = int(cookies_count.replace(",", ""))
		print(cookies_count)
	except:
		continue

	for i in range(4):
		try:
			prod_price = driver.find_element(By.ID, prod_price_prefix + str(i)).text.replace(",", "")

			if not prod_price.isdigit():	
				continue
			prod_price = int(prod_price)
			if cookies_count >= prod_price:
				prod = driver.find_element(By.ID, product_id + str(i))
				prod.click()
				print(f"Purchased product {i}")
				time.sleep(1)
				
		except Exception as e:
			print(e)
			continue
		