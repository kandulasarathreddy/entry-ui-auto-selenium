from pages.login.elements import LoginLocators
from core.data_classes import Config
from core.base_page import BaseScreen
from assertpy import assert_that


class LoginPageObj(BaseScreen):
    def __init__(self, config: Config):
        super().__init__(config)
        self.resource_url = "My Account"
        self.log_in_page_ele = LoginLocators

    def open(self):
        self.log.info(f"Open the {self.url} page")
        self.driver.get(self.url)

    def login(self, username, password):
        self.log.info("Logging in")
        self.log.info(f"entering username to register {self.log_in_page_ele.log_in_mail.name}")
        self.se_helper.get_element(self.log_in_page_ele.log_in_mail).send_keys(username)
        self.log.info(f"entering password to register {self.log_in_page_ele.log_in_password.name}")
        self.se_helper.get_element(self.log_in_page_ele.log_in_password).send_keys(password)
        self.log.info(f"clicking register button")
        self.se_helper.get_element(self.log_in_page_ele.log_in_button).click()

    def verify_page_title(self):
        title = self.driver.title
        assert_that(title).contains("Practice Site")

    def verify_billing_address(self):
        self.log.info(f"verifying billing address")
        self.log.info(f"clicking on{self.log_in_page_ele.lnk_My_Account.name}")
        self.se_helper.get_element(self.log_in_page_ele.lnk_My_Account).click()
        self.log.info(f"clicking on{self.log_in_page_ele.Address_link.name}")
        self.se_helper.get_element(self.log_in_page_ele.Address_link).click()
        billing_address_test = self.se_helper.get_element(self.log_in_page_ele.Billing_address).text
        assert_that(billing_address_test).contains("Billing Address")

    def verify_shipping_address(self):
        self.log.info(f"verifying shipping address")
        shipping_address_test = self.se_helper.get_element(self.log_in_page_ele.Shipping_address).text
        assert_that(shipping_address_test).contains("Shipping Address")

