from pages.loginpage_example import LoginPageAction
# from pages.aboutpage import AboutPageAction
# from pages.cartpage import CartPageAction
# from pages.productspage import ProductsPageAction


# Buat instansiasi object dari action method seperti pada loginpage dibawah ini
# agar lebih efektif saat penulisan di test case layer (tidak perlu object instantiation lagi)

class ObjectInstances:

    def loginpage(self):
        obj = LoginPageAction(self.driver)  #
        return obj

    # def productpage(self):
    #     obj = ProductsPageAction(self.driver)
    #     return obj
    #
    # def aboutpage(self):
    #     obj = AboutPageAction(self.driver)
    #     return obj
    #
    # def cartpage(self):
    #     obj = CartPageAction(self.driver)
    #     return obj