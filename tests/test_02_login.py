from utils.config import BASE_URL
from pages.login_page import LoginPage


def test_login(page):

    page.goto(BASE_URL)

    login_page = LoginPage(page)

    login_page.open_login_page()

    login_page.login(
        "layasenapathi303@gmail.com",
        "Slaya@123"
    )

    assert login_page.verify_login_success()

    page.wait_for_timeout(5000)