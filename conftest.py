import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None,
                     help="Choose page language for e.g.: ra, ar, es, en-gb")

# Список языков
language_list = [
            'ar', 'ca', 'cs',
            'da', 'de', 'en-gb',
            'el', 'es', 'fi',
            'fr', 'it', 'ko',
            'nl', 'pl', 'pt',
            'pt-br', 'ro', 'ru',
            'sk', 'uk', 'zh-cn'
]

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    language_property = request.config.getoption("language") 
    # выбрасываем исключение, если языка нет в списке
    if language_property not in language_list:
        raise pytest.UsageError("--language should some language that supported by page for e.g. en-gb")
    # установку языка осуществляем после того, как определили браузер
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = chrome_options()
        options.add_experimental_option('prefs', {'intl.accept_languages' : language_property})
        browser = webdriver.Chrome(options = options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        options = webdriver.FirefoxProfile()
        options.set_preference("intl.accept_languages" , language_property)
        browser = webdriver.Firefox(firefox_profile = options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()

