import allure
from allure_commons.types import AttachmentType
from selenium import webdriver


def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')


def add_logs(browser):
    options = webdriver.ChromeOptions()
    options.set_capability("goog:loggingPrefs", {"browser": "ALL"})

    driver = webdriver.Chrome(options=options)
    driver.get('https://demoqa.com/automation-practice-form')

    # Capture browser console logs
    logs = driver.get_log('browser')

    for entry in logs:
        print(f"{entry['level']} - {entry['message']}")

    # try:
    #     log = "".join(f'{text}\n' for text in browser.driver.get_log(log_type='browser'))  # этот вариант не работает
    #     allure.attach(log, 'browser_logs', AttachmentType.TEXT, '.log')
    # except Exception as e:
    #     error_message = f"Browser logs not available: {str(e)}"
    #     allure.attach(error_message, 'browser_logs_error', AttachmentType.TEXT, '.log')

def add_html(browser):
    html = browser.driver.page_source
    allure.attach(html, 'page_source', AttachmentType.HTML, '.html')


def add_video(browser):
    video_url = "https://selenoid.autotests.cloud/video/" + browser.driver.session_id + ".mp4"
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + video_url \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(html, 'video_' + browser.driver.session_id, AttachmentType.HTML, '.html')
