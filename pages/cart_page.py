from playwright.sync_api import Page


class CartPage:

    def __init__(self, page: Page):
        self.page = page

        # Actual cart contents section
        self.cart_items = page.locator("#cart_items")

        # Proceed to checkout button
        self.proceed_to_checkout_button = page.get_by_text(
            "Proceed To Checkout",
            exact=True
        )

    def open_cart(self):
        """
        Cart is already opened automatically from
        the View Cart popup after Add to Cart.
        """
        self.page.wait_for_url(
            "**/view_cart",
            timeout=15000
        )

        self.page.wait_for_load_state(
            "domcontentloaded"
        )

    def verify_cart_displayed(self):
        """
        Verify that the actual cart section is displayed.
        """
        return self.cart_items.is_visible()

    def proceed_to_checkout(self):
        """
        Click Proceed To Checkout.
        """

        self.proceed_to_checkout_button.wait_for(
            state="visible",
            timeout=15000
        )

        self.proceed_to_checkout_button.click()

        self.page.wait_for_load_state(
            "domcontentloaded"
        )