from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def findElementAndClick(css_selector, msg, wait=10):
    element = driver.find_element(By.CSS_SELECTOR, css_selector)
    driver.execute_script("arguments[0].scrollIntoView();",element)
    driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(wait)
    print(msg)
    return

def findElementAndhref(css_selector, msg, wait=10):
    element = driver.find_element(By.CSS_SELECTOR, css_selector)
    href = element.get_attribute('href')
    driver.get(href)
    # driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(wait)
    print(msg)
    return


WAIT = 10


driver = webdriver.Firefox()

driver.get("https://www.digikala.com/")
driver.implicitly_wait(WAIT)
print('Digikala')

#best selling products
element = driver.find_element(By.CSS_SELECTOR, 'a.relative:nth-child(2)')
driver.execute_script("arguments[0].scrollIntoView();",element)
driver.implicitly_wait(WAIT)
driver.execute_script("arguments[0].click();", element)
driver.implicitly_wait(WAIT)
print('mobile category')


#go to a product
element = driver.find_element(By.CSS_SELECTOR, 'div.product-list_ProductList__item__LiiNI:nth-child(1) > a:nth-child(1)')
href = element.get_attribute('href')
driver.get(href)
driver.implicitly_wait(WAIT)
print('specific mobile page')


# go to comments
element = driver.find_element(By.CSS_SELECTOR, 'div.mt-3:nth-child(2)')
driver.execute_script("arguments[0].scrollIntoView();",element)
driver.implicitly_wait(WAIT)
driver.execute_script("arguments[0].click();", element)
driver.implicitly_wait(WAIT)
print('mobile category')



