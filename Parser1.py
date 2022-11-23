from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from Auth import LOGIN, PASSWORD


class Parser:
    def __init__(self):
        print('Инициализация драйвера...............')
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-blink-features=AutomationControlled')
        self.driver = webdriver.Chrome(options=options)
        print('Драйвер инициализирован!')

    @staticmethod
    def print_comment(text_before, text_after):
        def real_decorator(func):
            def wrapper(self):
                print(text_before)
                func(self)
                print(text_after)

            return wrapper

        return real_decorator

    @print_comment('Переход на страницу записи......', 'Готово!')
    def get_page(self):
        self.driver.get("https://www.mos.ru/services/zapis-k-vrachu/")

    def press_continue(self):
        self.driver.find_element(By.CLASS_NAME,
                                 'src-pages-main-components-Lead-___styles-module__lead_action_button___1Rb23').click()
        sleep(2)

    @print_comment('Ввод логина......', 'Логин введен!')
    def login(self):
        self.driver.find_element(By.ID, 'login').send_keys(LOGIN)

    @print_comment('Ввод пароля......', 'Пароль введен!')
    def password(self):
        self.driver.find_element(By.ID, 'password').send_keys(PASSWORD)

    @print_comment('Отправка формы......', 'Форма отправлена!')
    def enter(self):
        self.driver.find_element(By.ID, 'bind').click()

    def press_make_appointment(self):
        self.driver.find_element(By.XPATH,
                                 "/html/body/div[3]/div[1]/div/div/div[2]/div/div[3]/div/div[2]/button").click()

    def press_patients_listbox(self):
        self.driver.find_element(By.XPATH,
                                 "/html/body/div[3]/div[1]/div/div/div[2]/div/div[2]"
                                 "/div[1]/div[2]/div/div[1]/div/span/div/div[1]/button").click()

    def get_patients(self):
        patient_names = self.driver.find_element(By.XPATH,
                                                 '/html/body/div[3]/div[1]/div/div/div[2]/div/div[2]/'
                                                 'div[1]/div[2]/div/div[1]/div/span/div/div[2]')
        return patient_names.find_elements(By.TAG_NAME, 'div')

    # @print_comment('Список пациентов: ')
    def print_items(self, patients):
        for number, name in enumerate(patients):
            sleep(0.3)
            print(f"{number}: {name.text}")

    def choose_patient(self, patients):
        patients[int(input('Введите номер пациента: '))].click()

    def continue_to_doctors(self):
        self.driver.find_element(By.XPATH,
                                 '/html/body/div[3]/div[1]/div/div/div[2]/div/'
                                 'div[2]/div[1]/div[2]/div/div[2]/button').click()

    def doctor_specialization_click(self):
        self.driver.find_element(By.XPATH,
                                 '/html/body/div[3]/div[1]/div/div/div[2]/div/div[2]/div[2]'
                                 '/div[2]/div/div/div/div/div[1]/button').click()

    def get_doctors(self):
        doctors = self.driver.find_element(By.XPATH,
                                           '/html/body/div[3]/div[1]/div/div/div[2]/div/'
                                           'div[2]/div[2]/div[2]/div/div/div/div/div[2]')

        return doctors.find_elements(By.TAG_NAME, 'div')


if __name__ == '__main__':
    parser = Parser()
    try:
        parser.get_page()
        parser.press_continue()
        parser.login()
        parser.password()
        parser.enter()
        sleep(10)
        parser.press_make_appointment()
        sleep(5)
        parser.press_patients_listbox()
        sleep(5)
        patients = parser.get_patients()
        sleep(4)
        parser.print_items(patients)
        sleep(4)
        parser.choose_patient(patients)
        sleep(6)
        parser.continue_to_doctors()
        sleep(5)
        parser.doctor_specialization_click()
        sleep(4)
        doctors = parser.get_doctors()
        parser.print_items(doctors)
    except Exception as ex:
        print(ex)

    finally:
        parser.driver.close()
        parser.driver.quit()
