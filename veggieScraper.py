from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class Tomato:
    def __init__(self, name, price, unit_price):
        self.name = name
        self.price = price
        self.unit_price = unit_price

# create Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")

tomatoes = []

# create a new Chrome browser instance with the headless option
driver = webdriver.Chrome(options=chrome_options)

# BARBORA ###########################################
# navigate to the webpage
driver.get("https://www.barbora.ee/koogiviljad-puuviljad/koogiviljad-ja-aedviljad/tomatid-ja-kurgid")
print(driver.title)  # print the page title
# Identify the elements containing the product data
products = driver.find_elements(By.CSS_SELECTOR, '.b-product--wrap2')

# Iterate over the elements and print out the data
for product in products:
    try:
        product_name = product.find_element(By.CSS_SELECTOR, 'span[itemprop="name"]').text
        product_price = product.find_element(By.CSS_SELECTOR, 'span[itemprop="price"]').text
        product_price = product_price.replace('€', '')
        product_unit_price = product.find_element(By.CSS_SELECTOR, '.b-product-price--extra div').text
        product_unit_price = product_unit_price.replace('€', '').replace('/kg', '')
        if "tomat" in product_name.lower():
            price = float(product_price)
            unit_price = float(product_unit_price)
            tomato = Tomato(product_name, price, unit_price)
            tomatoes.append(tomato)
    except:
        # if the product is out of stock, the price is not displayed
        pass

# SELVER ###########################################
# navigate to the webpage
driver.get("https://www.selver.ee/puu-ja-koogiviljad/koogiviljad-juurviljad?product_segment=1848&page=1")
print(driver.title)  # print the page title

# # Identify the elements containing the product data
products = driver.find_elements(By.CSS_SELECTOR, '.ProductCard')

# # Iterate over the elements and print out the data
for product in products:
    product_name = product.find_element(By.CSS_SELECTOR, '.ProductCard__title a').text
    product_price = product.find_element(By.CSS_SELECTOR, '.ProductPrice').text.split('\n')[0]  # gets the price part
    product_price = product_price.replace(' €', '').replace(',', '.')
    product_unit_price = product.find_element(By.CSS_SELECTOR, '.ProductPrice__unit-price').text  # gets the unit price part
    price = float(product_price)
    unit_price = float(product_unit_price.replace(',', '.').split()[0])
    tomato = Tomato(product_name, price, unit_price)
    tomatoes.append(tomato)

# RIMI ###########################################
# navigate to the webpage
driver.get("https://www.rimi.ee/epood/ee/tooted/puuviljad-koogiviljad-lilled/juurviljad-ja-koogiviljad/tomat/c/SH-12-2-14")

# # Identify the elements containing the product data
products = driver.find_elements(By.CSS_SELECTOR, '.product-grid__item')

# # Iterate over the elements and print out the data
for product in products:
    product_name = product.find_element(By.CSS_SELECTOR, '.card__name').text
    product_price = product.find_element(By.CSS_SELECTOR, '.price-tag').text.split('\n')  # gets the price part
    price = float(product_price[0] + '.' + product_price[1])
    product_unit_price = float(product.find_element(By.CSS_SELECTOR, '.card__price-per').text.split(' ')[0].replace(',', '.'))  # gets the unit price part
    tomato = Tomato(product_name, price, product_unit_price)
    tomatoes.append(tomato)

tomatoes.sort(key=lambda x: x.unit_price)
for i, tomato in enumerate(tomatoes):
    print(f"{i+1}. {tomato.name} {tomato.price}€ {tomato.unit_price}€/kg")

# close the browser
driver.quit()
