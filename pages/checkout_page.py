from playwright.sync_api import Page


class CheckoutPage:

    def __init__(self, page: Page):
        self.page = page

        self.checkout_page = page.locator(
            "#checkout_info"
        )

        self.place_order_button = page.get_by_text(
            "Place Order",
            exact=True
        )

    def proceed_to_checkout(self):
        """
        Click Proceed To Checkout from the cart
        and wait for the checkout page.
        """

        proceed_button = self.page.get_by_text(
            "Proceed To Checkout",
            exact=True
        )

        proceed_button.wait_for(
            state="visible",
            timeout=15000
        )

        proceed_button.click()

        self.page.wait_for_load_state(
            "domcontentloaded"
        )

        # Wait until checkout page is displayed
        self.page.get_by_text(
            "Address Details",
            exact=True
        ).wait_for(
            state="visible",
            timeout=15000
        )

    def verify_checkout_page(self):
        """
        Verify that the checkout page is displayed.
        """

        return self.page.get_by_text(
            "Address Details",
            exact=True
        ).is_visible()

    def place_order(self):
        """
        Click Place Order.
        """

        self.place_order_button.wait_for(
            state="visible",
            timeout=15000
        )

        self.place_order_button.click()