

import Parser
from time import sleep
import datetime

print('Павел - 0')
print('Илья - 1')
print('Ксения - 2')

family_member = int(input('Введите номер пациента: '))
parser = Parser1.Parser(family_member)
# Parser1.main()

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
    doctor_number = int(input('Введите номер доктора: '))

except Exception as ex:
    print(ex)

finally:
    parser.driver.close()
    parser.driver.quit()


now = datetime.datetime.now()
while not parser.appointed:

    if (datetime.datetime.now() - now) > datetime.timedelta(minutes=1):
        parser = Parser1.Parser(family_member, doctor_number)
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
            parser.choose_patient(patients)
            sleep(6)
            parser.continue_to_doctors()
            sleep(10)
            parser.doctor_specialization_click()
            sleep(4)
            doctors = parser.get_doctors()
            #parser.print_items(doctors)
            #parser.doctor_number = int(input('Введите номер доктора: '))
            parser.click_doctor(doctors)
            sleep(4)
            parser.click_appointment_by_time()
            sleep(6)
            try:
                a = parser.get_date_and_time_appointment()
                sleep(4)
                parser.click_time(a)
                sleep(6)
                parser.choose_doctor()
                sleep(6)
                parser.appoint()
                sleep(6)
                parser.confirm_appoint()
                sleep(10)

            except Exception as ex:
                print(ex)
                print('Пока нет свободного времени для записи!')


        except Exception as ex:
            print(ex)

        finally:
            parser.driver.close()
            parser.driver.quit()

        now = datetime.datetime.now()

