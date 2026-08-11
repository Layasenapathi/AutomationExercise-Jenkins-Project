from playwright.sync_api import Page


class PaymentPage:

    def __init__(self, page: Page):
        self.page = page

        self.name_on_card = page.locator(
            '[data-qa="name-on-card"]'
        )

        self.card_number = page.locator(
            '[data-qa="card-number"]'
        )

        self.cvc = page.locator(
            '[data-qa="cvc"]'
        )

        self.expiry_month = page.locator(
            '[data-qa="expiry-month"]'
        )

        self.expiry_year = page.locator(
            '[data-qa="expiry-year"]'
        )

        self.pay_button = page.get_by_role(
            "button",
            name="Pay and Confirm Order"
        )

    def enter_payment_details(
        self,
        name,
        card_number,
        cvc,
        expiry_month,
        expiry_year
    ):
        self.name_on_card.fill(name)
        self.card_number.fill(card_number)
        self.cvc.fill(cvc)
        self.expiry_month.fill(expiry_month)
        self.expiry_year.fill(expiry_year)

    def place_order(self):
        self.pay_button.click()