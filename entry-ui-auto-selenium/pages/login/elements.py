from core.form_element import FormElement


class LoginLocators:
    lnk_My_Account = FormElement("XPATH", "//a[.='My Account']", "My Account")
    log_in_mail = FormElement("XPATH", "//*[@name='username']", "UserName")
    log_in_password = FormElement("XPATH", "//*[@id='password']", 'password')
    log_in_button = FormElement("XPATH", '//*[@name="login"]', 'button')
    Address_link = FormElement("XPATH", "//a[.='Addresses']", "Addresses link")
    Billing_address = FormElement("XPATH", "//*[@class='u-column1 col-1 woocommerce-Address']", "Billing Address")
    Shipping_address = FormElement("XPATH", "//*[@class='u-column2 col-2 woocommerce-Address']", "Shipping address")
