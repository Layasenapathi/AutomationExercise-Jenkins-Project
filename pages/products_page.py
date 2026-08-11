from playwright.sync_api import Page


class ProductsPage:

    def __init__(self, page: Page):
        self.page = page

        self.products_link = page.get_by_role(
            "link",
            name="Products"
        )

        self.search_box = page.locator(
            "#search_product"
        )

        self.search_button = page.locator(
            "#submit_search"
        )

    def open_products(self):
        self.products_link.click()

        self.page.wait_for_url(
            "**/products",
            timeout=15000
        )

    def search_product(self, product_name):

        self.search_box.fill(product_name)

        self.search_button.click()

        # Wait for search results
        self.page.locator(
            ".product-image-wrapper"
        ).first.wait_for(
            state="visible",
            timeout=15000
        )

    def add_first_product_to_cart(self):

        # Select first product
        first_product = self.page.locator(
            ".product-image-wrapper"
        ).first

        # Scroll to product
        first_product.scroll_into_view_if_needed()

        # Hover over product so Add to Cart is available
        first_product.hover()

        # Select Add to Cart inside first product
        add_to_cart = first_product.locator(
            ".add-to-cart"
        ).first

        # Click Add to Cart
        add_to_cart.click(
            force=True
        )

        # Wait for confirmation popup
        added_message = self.page.get_by_text(
            "Your product has been added to cart.",
            exact=True
        )

        added_message.wait_for(
            state="visible",
            timeout=10000
        )

        # Automatically click View Cart
        view_cart = self.page.get_by_text(
            "View Cart",
            exact=True
        )

        view_cart.wait_for(
            state="visible",
            timeout=10000
        )

        view_cart.click()

        # Wait for Cart page
        self.page.wait_for_url(
            "**/view_cart",
            timeout=15000
        )

        self.page.wait_for_load_state(
            "domcontentloaded"
        )