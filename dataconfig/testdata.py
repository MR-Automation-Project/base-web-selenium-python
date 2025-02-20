class TestData:
    # base url :
    BASE_URL_TEST = "https://saucedemo.com"
    BASE_URL_STAG = ""
    BASE_URL_PROD = ""

    # credentials :
    STANDARD_USERNAME = "standard_user"
    GENERAL_PASSWORD = "secret_sauce"

# if you want to use parametrization
# example in login scenario & add some product to cart, below :

accounts = [
    {"username": "standard_zzzz", "password": "secret_sauc1"},
    {"username": "standard_user", "password": "secret_sauce"},
    {"username": "visual_user", "password": "secret_sauce"}
]

products_name = [
    {"nama_produk1": "Sauce Labs Bike Light",
     "nama_produk2": "Sauce Labs Fleece Jacket",
     "nama_produk3": "Sauce Labs Backpack"}
]