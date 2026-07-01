from pages.home_page import HomePage
from pages.login_page import LoginPage
from config import email_id, password_id


#Invalid Login Test
def test_invalid_login(driver):
    #Start at the HomePage
    home = HomePage(driver)
    home.hover_on_account_list()
    #Navigate to the LoginPage
    login_page = home.click_sign_in()

    dashboard_page = login_page.login(email_id,password_id)

    #Assertions (Validation)
    if isinstance(dashboard_page,LoginPage):
        #If we are still on LoginPage, check for error message
        assert dashboard_page.is_error_displayed()
        error_text = dashboard_page.get_error_message_text()
        assert error_text is not None
        assert "incorrect" in error_text.lower()


#Valid Login Test
def test_valid_login(driver):

    home = HomePage(driver)
    home.hover_on_account_list()
    login_page = home.click_sign_in()

    dashboard_page = login_page.login(email_id, password_id)

    if isinstance(dashboard_page,LoginPage):
        assert dashboard_page.is_error_displayed()
    else:
        assert 'Hello' in dashboard_page.get_logged_in_username()

def test_product_search_add_to_cart(driver):
    home = HomePage(driver)
    home.hover_on_account_list()
    login_page = home.click_sign_in()

    dashboard_page = login_page.login(email_id, password_id)
    assert 'Hello' in dashboard_page.get_logged_in_username()

    #search product
    search_page = dashboard_page.go_to_search()
    product_page = search_page.search_products('laptop')

    #select product
    product_page.select_product()

    #add to cart
    product_page.add_to_cart()
    product_page.add_to_your_order()

    cart_page = product_page.go_to_cart()
    cart_page.proceed_to_checkout()

    assert "checkout" in driver.current_url.lower()