from playwright.sync_api import Page


class LoginPage:

    def __init__(self, page: Page):
        self.page = page

        self.signup_login_link = page.get_by_role(
            "link",
            name="Signup / Login"
        )

        self.email_input = page.locator(
            'input[data-qa="login-email"]'
        )

        self.password_input = page.locator(
            'input[data-qa="login-password"]'
        )

        self.login_button = page.get_by_role(
            "button",
            name="Login"
        )

        self.logged_in_text = page.get_by_text(
            "Logged in as"
        )

    def open_login_page(self):
        self.signup_login_link.click()

    def login(self, email, password):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()

    def verify_login_success(self):
        self.logged_in_text.wait_for()
        return self.logged_in_text.is_visible()