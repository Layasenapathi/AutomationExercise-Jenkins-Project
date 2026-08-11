from utils.config import BASE_URL
from pages.login_page import LoginPage
from pages.logout_page import LogoutPage


def test_logout(page):

    # Step 1: Open website
    page.goto(BASE_URL)

    # Step 2: Login
    login_page = LoginPage(page)

    login_page.open_login_page()

    login_page.login(
        "layasenapathi303@gmail.com",
        "Slaya@123"
    )

    assert login_page.verify_login_success()

    # Step 3: Logout
    logout_page = LogoutPage(page)

    logout_page.logout()

    # Step 4: Verify logout
    assert logout_page.verify_logout_success()

    page.wait_for_timeout(5000)