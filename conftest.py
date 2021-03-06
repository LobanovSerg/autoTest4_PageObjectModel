import pytest
from selenium import webdriver
from .pages.languages import languages

# список поддерживаемых браузеров
browsers_list = ['chrome', 'firefox']

# браузер и язык по умолчанию
default_browser, default_lang = 'chrome', 'en'


# передачa параметров через командную строку
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=default_browser,
                     help=f'Choose correct browser: {browsers_list}')
    parser.addoption('--language', action='store', default=default_lang,
                     help=f'Choose correct language: {languages.keys()}')


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption('browser_name')
    browser_lang = request.config.getoption('language')

    # создание исключения при неверном вводе языка
    if browser_lang not in languages:
        raise Exception(f'Wrong language! List languages: ' +
                        ' '.join(languages.keys()))

    # создание исключения при неверном вводе браузера
    if browser_name not in browsers_list:
        raise Exception(f'Wrong browser! List browsers: ' +
                        ' '.join(browsers_list))

    print(f'\nStart {browser_name} browser..')

    # выбор и запуск браузера
    if browser_name == 'chrome':
        lng_opt = webdriver.chrome.options.Options()
        lng_opt.add_experimental_option(
            'prefs', {'intl.accept_languages': browser_lang})
        browser = webdriver.Chrome(options=lng_opt)
    elif browser_name == 'firefox':
        lng_opt = webdriver.FirefoxProfile()
        lng_opt.set_preference("intl.accept_languages", browser_lang)
        browser = webdriver.Firefox(firefox_profile=lng_opt)

    yield browser
    print('\nQuit browser..')
    browser.quit()
