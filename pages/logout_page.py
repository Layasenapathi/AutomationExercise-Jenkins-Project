from playwright.sync_api import Page


class LogoutPage:

    def __init__(self, page: Page):
        self.page = page

        self.logout_link = page.get_by_role(
            "link",
            name="Logout"
        )

        self.login_link = page.get_by_role(
            "link",
            name="Signup / Login"
        )

    def logout(self):
        self.logout_link.click()

    def verify_logout_success(self):
        return self.login_link.is_visible()