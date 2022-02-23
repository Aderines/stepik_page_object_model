import pytest
# import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


# доступные языки: ar, ca, cs, da, de, en-gb, el, es, fi, fr, it, ko, nl, pl, pt, pt-br, ro, ru, sk, uk, zh-hans
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("--language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    yield browser
    # time.sleep(5)