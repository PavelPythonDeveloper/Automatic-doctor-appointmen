from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from Auth import LOGIN, PASSWORD
import random
from playsound import playsound


class Parser:
    def __init__(self, patient_number, doctor_number=None):
        print('Инициализация драйвера...............')
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-blink-features=AutomationControlled')
        self.driver = webdriver.Chrome(options=options)
        self.patient_number = patient_number
        self.doctor_number = doctor_number
        self.appointed = False
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
        self.driver.implicitly_wait(10)

    @print_comment('Отправка формы......', 'Форма отправлена!')
    def enter(self):
        self.driver.find_element(By.ID, 'bind').click()
        self.driver.implicitly_wait(10)

    def press_make_appointment(self):
        self.driver.find_element(By.XPATH,
                                 "/html/body/div[3]/div[1]/div/div/div[2]/div/div[3]/div/div[2]/button").click()
        self.driver.implicitly_wait(10)

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
        patients[self.patient_number].click()

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

    def input_doctor_number(self, doctor_number):
        self.doctor_number = doctor_number

    def click_doctor(self, doct):
        doct[self.doctor_number].click()

    def click_appointment_by_time(self):
        x = self.driver.find_element(By.XPATH,
                                     '/html/body/div[3]/div[1]/div/div/div[2]/div/div[2]/div[3]/div[2]/div[1]')
        x.find_elements(By.TAG_NAME, 'button')[1].click()

    # /html/body/div[3]/div[1]/div/div/div[2]/div/div[2]/div[3]/div[2]/div[1]/button[2]
    # /html/body/div[3]/div[1]/div/div/div[2]/div/div[2]/div[3]/div[2]/div[1]
    def get_date_and_time_appointment(self):
        all_buttons = []

        appointment_days = self.driver.find_elements(By.CLASS_NAME,
                                                     'src-pages-appointment-new-components-stepThree-components-common-'
                                                     'TimeTable-components-TimeTableItem-___styles-module__table_item___1kSLj')

        for day in appointment_days:

            appointment_time = day.find_elements(By.TAG_NAME, 'button')
            for el in appointment_time:
                all_buttons.append(el)

        return all_buttons

    def click_time(self, times):
        if times:
            times[random.randint(0, len(times) - 1)].click()

    def choose_doctor(self):
        doctors = self.driver.find_elements(By.CLASS_NAME, 'css-mzuuyn-Button-Text-Box')
        if doctors:
            doctors[random.randint(0, len(doctors) - 1)].click()

    def appoint(self):
        self.driver.find_element(By.CLASS_NAME, 'css-12z5268-Button-Text-Box').click()

    def confirm_appoint(self):
        self.driver.find_element(By.CLASS_NAME, 'css-18zs39j-Button-Text-Box').click()
        self.alarm()

    def alarm(self):
        self.appointed = True
        playsound('alarm.mp3')


def main():
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
        # sleep(4)
        # parser.print_items(patients)
        sleep(4)
        parser.choose_patient(patients)
        sleep(6)
        parser.continue_to_doctors()
        sleep(10)
        parser.doctor_specialization_click()
        sleep(4)
        doctors = parser.get_doctors()
        parser.print_items(doctors)
        sleep(4)
        parser.click_appointment_by_time()
        sleep(6)
        buttons = parser.get_date_and_time_appointment()
        parser.click_time(buttons)
        sleep(6)
    except Exception as ex:
        print(ex)

    finally:
        parser.driver.close()
        parser.driver.quit()


if __name__ == '__main__':
    main()
