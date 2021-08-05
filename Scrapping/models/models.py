import time
import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = Options()
driver= webdriver.Chrome(executable_path=ChromeDriverManager().install(),chrome_options=options)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://webscraper.io/test-sites/e-commerce/scroll")
time.sleep(2)
products = []
deploy = driver.find_elements_by_xpath("//a[@class='category-link ']")

def extract_products():
    """Get products's names

    - return: list with all names 
    - rtype: list
    """    
    lista = []
    elements = driver.find_elements_by_xpath("//a[@title]")
    for i in range(len(elements)):  
        name = (elements[i].text)
        lista.append(name)
    return lista

def to_json(products):
    """Generate json file

    - param products: Product's names
    - type products: list
    - return: dictionary with all products
    - rtype: dictionary
    """    
    global deploy
    items = len(deploy)
    for i in range(items):
        driver.execute_script('arguments[0].click();', deploy[0])
        time.sleep(2)
        products.extend(extract_products())
        deploy = driver.find_elements_by_xpath("//a[@class='category-link ']")
        time.sleep(1)
    driver.close()
    dic = {'Products': products}
    with open('products.json','w') as f:
        json.dump(dic,f)
    return dic