from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
from datetime import datetime
import winsound
matricula="5988GNM"
expected_title = "Miércoles\n12 Feb"

def openChrome():
	# Create a new instance of the Chrome driver
	options = webdriver.ChromeOptions()
	options.add_argument("--start-maximized")
	options.add_argument("--headless")
	options.add_argument("--disable-gpu")
	driver = webdriver.Chrome(options)
	return driver

def closeChrome(driver):
	driver.quit()

def searchITV(driver):
	wait = WebDriverWait(driver, 10)

	# Navigate to the website
	driver.get("https://www.sycitv.com/es/cita-previa-particulares/")


	element = driver.find_element(By.CSS_SELECTOR,'.avia-cookie-select-all')
	driver.execute_script("arguments[0].click();", element)

	input_matricula = driver.find_element(By.NAME,'matricula')
	input_matricula.send_keys(matricula)

	aceptar = driver.find_element(By.LINK_TEXT,'ACEPTAR')
	driver.execute_script("arguments[0].scrollIntoView(true)", aceptar)

	driver.execute_script("arguments[0].click()", aceptar)

	selectorFirstDay = '//*[@id="av_section_2"]/div/div/div/div/section/div/div/div[1]/div/ul/li[4]/article/div/div/div/div/div[2]/div[3]/div[1]/ul/li[2]'
	firstDay = wait.until(EC.element_to_be_clickable((By.XPATH, selectorFirstDay)))
	driver.execute_script("arguments[0].scrollIntoView(true)", firstDay)

	actual_title = firstDay.text

	if expected_title == actual_title:
		print(datetime.now(), "	Title validation successful! Waiting 30 sec...")
		return True
	else:
		print("---SUCCEEDED---")
		print(datetime.now(), "	Title validation failed. Expected:", expected_title, "Actual:", actual_title)
		return False

# Bucle infinito que ejecuta la función cada 30 segundos
driver = openChrome()
while searchITV(driver):
	time.sleep(30)
closeChrome(driver)

duration = 5000  # milliseconds
freq = 440  # Hz
winsound.Beep(freq, duration)