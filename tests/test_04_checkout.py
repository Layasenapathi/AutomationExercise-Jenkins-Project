from utils.config import BASE_URL
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_checkout(page):

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

    # Step 3: Open Products
    products_page = ProductsPage(page)

    products_page.open_products()

    # Step 4: Search product
    products_page.search_product("Blue Top")

    # Step 5: Add product to cart
    products_page.add_first_product_to_cart()

    # Step 6: Open Cart
    cart_page = CartPage(page)

    cart_page.open_cart()

    assert cart_page.verify_cart_displayed()

    # Step 7: Proceed to Checkout
    checkout_page = CheckoutPage(page)

    checkout_page.proceed_to_checkout()

    # Step 8: Verify Checkout page
    assert checkout_page.verify_checkout_page()

    page.wait_for_timeout(5000)