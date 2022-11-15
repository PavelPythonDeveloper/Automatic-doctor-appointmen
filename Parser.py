from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from Auth import LOGIN, PASSWORD

from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(options=options)
driver.get("https://www.mos.ru/services/zapis-k-vrachu/")
driver.find_element(By.CLASS_NAME,
                    'src-pages-main-components-Lead-___styles-module__lead_action_button___1Rb23').click()
time.sleep(2)
driver.find_element(By.ID, 'login').send_keys(LOGIN)
driver.find_element(By.ID, 'password').send_keys(PASSWORD)
time.sleep(2)
driver.find_element(By.ID, 'bind').click()
time.sleep(5)
names = driver.find_element(By.CLASS_NAME,
                            'src-pages-dashboard-components-DashboardOmsFilter-___styles-module__filter_container___UI1Zl')
time.sleep(5)
names.find_elements(By.TAG_NAME, 'button')[2].click()
time.sleep(5)
# element = driver.find_element(By.CLASS_NAME, 'src-pages-dashboard-components-DashboardAppointmentsList-'
#                                              '___styles-module__list_container___1H4RN')
# element.find_element(By.TAG_NAME, 'button').click()
driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div[2]/div/div[3]/div/div[2]/button').click()
time.sleep(5)
driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div[2]/div/div[2]/div[1]/div[2]/div/div[2]/button').click()
time.sleep(5)
driver.close()
driver.quit()
time.sleep(5)
