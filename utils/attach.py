import allure
from allure_commons.types import AttachmentType


def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')


def add_logs(browser):
    try:
        # Пробуем получить логи браузера (работает для Chrome/Chromium)
        log = "".join(f'{text}\n' for text in browser.driver.get_log(log_type='browser'))
        allure.attach(log, 'browser_logs', AttachmentType.TEXT, '.log')
    except Exception as e:
        # Если метод get_log не доступен, сохраняем сообщение об ошибке
        error_message = f"Browser logs not available: {str(e)}"
        allure.attach(error_message, 'browser_logs_error', AttachmentType.TEXT, '.log')

    # log = "".join(f'{text}\n' for text in browser.driver.get_log(log_type='browser'))  # Еcли оставить код таким, то будет ошибка "AttributeError: 'WebDriver' object has no attribute 'get_log'"
    # allure.attach(log, 'browser_logs', AttachmentType.TEXT, '.log')


def add_html(browser):
    html = browser.driver.page_source
    allure.attach(html, 'page_source', AttachmentType.HTML, '.html')


def add_video(browser):
    video_url = "https://selenoid.autotests.cloud/video/" + browser.driver.session_id + ".mp4"
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + video_url \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(html, 'video_' + browser.driver.session_id, AttachmentType.HTML, '.html')