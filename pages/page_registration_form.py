import os
from selene import have
from selenium.webdriver import Keys
from locators.locators_form_registration import LocatorsPageRegistrationForm
from data.url import URL_FORM_REGISTRATIONS

class RegistrationFormMethods:

    def open_page(self, setup_browser):  # открытие страницы формы регистрации
        browser = setup_browser
        browser.open(URL_FORM_REGISTRATIONS)


class SimpleRegistration:

    def simple_registration(self, setup_browser, user):
        browser = setup_browser
        browser.element(LocatorsPageRegistrationForm.FIELD_INPUT_NAME).type(user.name)
        browser.element(LocatorsPageRegistrationForm.FIELD_INPUT_LAST_NAME).type(user.last_name)
        browser.element(LocatorsPageRegistrationForm.FIELD_INPUT_EMAIL).type(user.email)
        browser.element(LocatorsPageRegistrationForm.GENDER_MALE).click()
        browser.element(LocatorsPageRegistrationForm.FIELD_INPUT_MOBILE_NUMBER).type(user.mobile_number)
        browser.element(LocatorsPageRegistrationForm.FIELD_DATE_PICKER).press(Keys.CONTROL + 'a').type(
            user.date_of_birth).press_enter()
        browser.element(LocatorsPageRegistrationForm.FIELD_MULTISELECT_SUBJECT).type(user.math)
        browser.element(LocatorsPageRegistrationForm.VALUE_MULTISELECT_SUBJECT).click()
        browser.element(LocatorsPageRegistrationForm.CHECK_BOX_HOBBIES_SPORTS).click()
        browser.element(LocatorsPageRegistrationForm.FIELD_ADD_PICTURE).type(os.path.abspath('resources/qa-guru.jpg'))
        browser.element(LocatorsPageRegistrationForm.FIELD_CURRENT_ADDRESS).type(user.current_address)
        browser.element(LocatorsPageRegistrationForm.MULTISELECT_STATE).click()
        browser.element(LocatorsPageRegistrationForm.STATE_NCR).click()
        browser.element(LocatorsPageRegistrationForm.MULTISELECT_CITY).click()
        browser.element(LocatorsPageRegistrationForm.CITY_DELHI).click()
        browser.element(LocatorsPageRegistrationForm.BUTTON_SUBMIT).click()

    def assert_simple_registration(self, setup_browser):
        browser = setup_browser
        browser.all(LocatorsPageRegistrationForm.VALUE_MODAL_WINDOW_RESULT_SEND).should(have.texts(
            'Student Name Роман Гороховик\n'
            'Student Email roman_qa@gmail.com\n'
            'Gender Male\nMobile 9963334558\n'
            'Date of Birth 01 October,1996\n'
            'Subjects Maths\n'
            'Hobbies Sports\n'
            'Picture qa-guru.jpg\n'
            'Address Кемерово, ул. Советсткая, д.6\n'
            'State and City NCR Delhi'))
