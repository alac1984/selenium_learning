import os
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


op = ChromeOptions()
op.add_experimental_option("debuggerAddress", "localhost:8989")
os.environ["PATH"] += r"/home/andre/Projects/utils/selenium_drivers/"
driver = webdriver.Chrome(options=op)

# driver.get("https://professor.seduc.ce.gov.br/")

# login_btn = driver.find_element(By.CLASS_NAME, "btn-login")
# login_btn.click()

# username = driver.find_element(By.ID, "username")
# password = driver.find_element(By.ID, "password")
# submit = driver.find_element(By.XPATH, '//*[@id="formLogin"]/div[3]/div/button')

# username.send_keys("00184016355")
# password.send_keys("Lucent13@")
# submit.click()

diario = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="navbar"]/ul/li[5]/a/div/div[2]')
    )
)
diario.click()

aval = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="collapseSubMenuDiario"]/li[4]/a')
    )
)
aval.click()

# print(aval)

# el = WebDriverWait(driver, 10).until(
#     EC.visibility_of_element_located((By.XPATH, '//*[@id="overlay"]/div'))
# )
