from playwright.sync_api import Page


class OrderSuccessPage:

    def __init__(self, page: Page):
        self.page = page

        self.success_message = page.get_by_text(
            "Order Placed!"
        )

    def verify_order_success(self):
        return self.success_message.is_visible()