import pytest
from dataconfig.testdata import *
from Tests.object_instance import ObjectInstances

@pytest.mark.usefixtures("setup_scope_function")
class TestLoginAddItemToCart(ObjectInstances):

    #@pytest.mark.smoke
    def test_add_1_item_to_cart(self):
        # Automate login flow, add 1 item to cart and verify that item is added to cart

        #product name that will be tested
        productname = "Sauce Labs Bike Light"

        #login and ensure login is successfully using assertion
        self.loginpage().login_with_standart_user()
        assert self.productpage().check_visibility_page_title_on_products_page(), "page title after login is not displayed properly"

        #add 1 item to cart and verify the cart badge icon should be changes 1
        self.productpage().add_product_to_cart(productname)
        assert self.productpage().get_count_on_cart_badge() == 1, "cart badge count is not correct after add item to cart"

        #navigate to cart page and verify the product item is success listed in the cart page as well.
        self.productpage().click_cart_icon()
        assert self.cartpage().check_visibility_item_in_cart(productname), "item is not listed in the cart page"

    @pytest.mark.parametrize("nama_produk", products_name)
    def test_add_more_than_1_item_to_cart(self, nama_produk):
        productname = "Sauce Labs Bike Light"

        # login and ensure login is successfully using assertion
        self.loginpage().login_with_standart_user()
        assert self.productpage().check_visibility_page_title_on_products_page(), "page title after login is not displayed properly"

        self.productpage().add_product_to_cart(nama_produk['nama_produk1'])
        assert self.productpage().get_count_on_cart_badge() == 1, "cart badge count is not correct after add item to cart"
        self.productpage().add_product_to_cart(nama_produk['nama_produk2'])
        assert self.productpage().get_count_on_cart_badge() == 2, "cart badge count is not correct after add item to cart"
        self.productpage().add_product_to_cart(nama_produk['nama_produk3'])
        assert self.productpage().get_count_on_cart_badge() == 3, "cart badge count is not correct after add item to cart"

        # navigate to cart page and verify the product item is success listed in the cart page as well.
        self.productpage().click_cart_icon()
        assert self.cartpage().check_visibility_item_in_cart(nama_produk['nama_produk1']), "item is not listed in the cart page"
        assert self.cartpage().check_visibility_item_in_cart(nama_produk['nama_produk2']), "item is not listed in the cart page"
        assert self.cartpage().check_visibility_item_in_cart(nama_produk['nama_produk3']), "item is not listed in the cart page"
        print("success assert 3 items in cart")

@pytest.mark.usefixtures("setup_scope_function")
class TestLoginAndNavigateAboutPage(ObjectInstances):

    @pytest.mark.parametrize("akun", accounts)
    def test_navigate_to_about_page(self, akun):
        # Automate login flow, click on hamburger button (top left), navigate to 'About' and verify if it successfully navigated or not.
        self.loginpage().login(akun['username'], akun['password'])
        self.productpage().navigate_to_about_via_hamburgermenu()
        assert self.aboutpage().check_visibility_subtext_in_aboutpage(), "failed to landing on about page"