import allure
from selene import browser
from pages.page_registration_form import RegistrationFormMethods, SimpleRegistration
from data.user import user_student


@allure.title("Successful fill form")
def test_send_form_part_2(setup_browser):
    user = user_student
    open_page_registrations = RegistrationFormMethods()
    simple_registrations = SimpleRegistration()
    open_page_registrations.open_page(setup_browser)  # открытие страницы регистрации
    browser.driver.execute_script("$('#fixedban').remove()")
    browser.driver.execute_script("$('footer').remove()")
    simple_registrations.simple_registration(setup_browser, user)  # регистрация нового пользователя
    simple_registrations.assert_simple_registration(setup_browser)  # проверка, что регистрация прошла успешно
