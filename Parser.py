from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from Auth import LOGIN, PASSWORD


def init_driver():
    print('Инициализация драйвера...............')
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-blink-features=AutomationControlled')
    driver = webdriver.Chrome(options=options)
    print('Драйвер инициализирован!')
    return driver


def get_page():
    print('Переход на страницу записи......')
    driver.get("https://www.mos.ru/services/zapis-k-vrachu/")
    print('Готово!')


def get_continue(driver):
    driver.find_element(By.CLASS_NAME,
                        'src-pages-main-components-Lead-___styles-module__lead_action_button___1Rb23').click()
    sleep(2)


def enter_login(driver):
    driver.find_element(By.ID, 'login').send_keys(LOGIN)
    print('Логин введен!')


def enter_password(driver):
    driver.find_element(By.ID, 'password').send_keys(PASSWORD)
    print('Паровль введен!')


def bind(driver):
    driver.find_element(By.ID, 'bind').click()
    print('Отправка формы......')

def get_appointment(driver):
    driver.find_element(By.XPATH,
                        "/html/body/div[3]/div[1]/div/div/div[2]/div/div[3]/div/div[2]/button").click()


def press_drop_down_list(driver):
    driver.find_element(By.XPATH,
                        "/html/body/div[3]/div[1]/div/div/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/div/span/div/div[1]/button").click()


def get_list_names(driver):
    x = driver.find_element(By.XPATH,
                            '/html/body/div[3]/div[1]/div/div/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/div/span/div/div[2]')

    return x


def select_patient(names):
    patients = names.find_elements(By.TAG_NAME, 'div')

    return patients


def doctor_specialization_click(driver):
    driver.find_element(By.XPATH,
                        '/html/body/div[3]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div/div[1]/button').click()


def find_doctors_list(driver):
    doctors = driver.find_element(By.XPATH,
                                  '/html/body/div[3]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div/div[2]')

    return doctors


if __name__ == "__main__":
    driver = init_driver()
    get_page()
    get_continue(driver)
    enter_password(driver)
    enter_login(driver)
    bind(driver)
    sleep(5)
    get_appointment(driver)
    press_drop_down_list(driver)
    names = get_list_names(driver)
    sleep(5)
    patients = select_patient(names)
    print('==============================')
    print('Авторизованные пациенты:')
    for number, name in enumerate(patients):
        print(f"{number}: {name.text}")
    print('==============================')
    patient_number = int(input('Введите номер пациента: '))
    print(f'Получение списка врачей для {patients[patient_number].text}...............')
    patients[patient_number].click()
    #===================================================================================================================
    sleep(5)
    driver.find_element(By.XPATH,
                        '/html/body/div[3]/div[1]/div/div/div[2]/div/div[2]/div[1]/div[2]/div/div[2]/button').click()
    #===================================================================================================================
    sleep(5)
    doctor_specialization_click(driver)
    print('Список врачей получен!')
    sleep(5)
    doctors = find_doctors_list(driver)
    x = doctors.find_elements(By.TAG_NAME, 'div')
    for number, i in enumerate(x):
        print(f'{number}: {i.text}')
    sleep(5)
    #===================================================================================================================
    doctor_number = int(input('Введите номер специалиста: '))
    x[doctor_number].click()
    sleep(5)
    x = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div[2]/div/div[2]/div[3]/div[2]/div[1]')
    x.find_elements(By.TAG_NAME, 'button')[1].click()
    sleep(5)
    appointment_table = driver.find_element(By.CLASS_NAME, 'src-pages-appointment-new-components-stepThree-components-common-TimeTable-___styles-module__table___1Zxhu')
    appointment_day = appointment_table.find_elements(By.TAG_NAME, 'span')
    
    driver.close()
    driver.quit()
    sleep(5)
