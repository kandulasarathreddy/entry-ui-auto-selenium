from pytest import mark
from core.data_classes import Config
from pages.login.objects import LoginPageObj


@mark.login
def test_login(config: Config):
    config.log.info("Test the Register")
    register = LoginPageObj(config)
    register.open()
    register.login("sarathreddy15@gmail.com", "sarathreddy@123")
    register.verify_page_title()
    register.verify_billing_address()
    register.verify_shipping_address()
