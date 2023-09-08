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

#go to mobile page category
element = driver.find_element(By.CSS_SELECTOR, 'div.widgetLeafCategory_WidgetLeafCategory__col__WGzM0:nth-child(1) > a:nth-child(1)')
driver.execute_script("arguments[0].scrollIntoView();",element)
driver.implicitly_wait(WAIT)
driver.execute_script("arguments[0].click();", element)
driver.implicitly_wait(WAIT)
print('mobile category')

# go to Samsung page
element = driver.find_element(By.CSS_SELECTOR, 'div.h-100.d-flex.flex-column.bg-000.ai-center div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.shrink-0 div.grow-1.bg-000.d-flex.flex-column.w-100.ai-center.styles_BaseLayoutDesktop__content__hfHD1.styles_BaseLayoutDesktop__content--fullWidth__A2vWI div.w-100.px-2.mx-auto.mt-4.container-md-w.container-xl-w-lg.my-4 div.w-full.d-flex.flex-column.jc-center.align-items.py-4.bg-000.radius-large-lg.border-200-lg div.d-flex.jc-between.jc-center-lg.ai-center.px-2.px-5-lg.pos-relative')
driver.execute_script("arguments[0].scrollIntoView();",element)
driver.implicitly_wait(WAIT)
driver.execute_script("arguments[0].click();", element)
driver.implicitly_wait(WAIT)
print('click on Samsung')

#go to a specific mobile page
element = driver.find_element(By.CSS_SELECTOR, 'div.product-list_ProductList__item__LiiNI:nth-child(2) > a:nth-child(1)')
href = element.get_attribute('href')
driver.get(href)
driver.implicitly_wait(WAIT)
print('specific mobile page')


#compare
element = driver.find_element(By.CSS_SELECTOR, 'div.z-1:nth-child(5) > div:nth-child(1) > a:nth-child(1)')
driver.execute_script("arguments[0].click();", element)
driver.implicitly_wait(WAIT)
print('compare')

#click on button
element = driver.find_element(By.CSS_SELECTOR, '.border-r > button:nth-child(1) > div:nth-child(2)')
print(element)
element.click()
driver.implicitly_wait(WAIT)
print("button")

#chose another mobile
element = driver.find_element(By.CSS_SELECTOR, 'div.border-l:nth-child(1) > a:nth-child(1)')
driver.execute_script("arguments[0].click();", element)
driver.implicitly_wait(WAIT)
print("Choose another mobile")

#chose one of the mobiles
element = driver.find_element(By.CSS_SELECTOR, 'div.mx-6:nth-child(1) > div:nth-child(2) > a:nth-child(1)')
href = element.get_attribute('href')
driver.get(href)
driver.implicitly_wait(WAIT)
print("Choose one")

#add mobile to basket
element = driver.find_element(By.CSS_SELECTOR, 'div.pos-relative:nth-child(8) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > button:nth-child(1)')
driver.execute_script("arguments[0].click();", element)
# element.click()
driver.implicitly_wait(WAIT)
print("Add to basket")

# element = driver.find_element(By.CSS_SELECTOR, 'button.styles_btn--outlined__7Tmy6:nth-child(2)')
# # driver.execute_script("arguments[0].click();", element)
# element.click()
# driver.implicitly_wait(WAIT)
# print("Choose one")

#see basket
element = driver.find_element(By.CSS_SELECTOR, 'div.pos-relative:nth-child(8) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(2) > div:nth-child(2) > a:nth-child(1)')
driver.execute_script("arguments[0].click();", element)
driver.implicitly_wait(WAIT)
print("See basket")

# elem.send_keys("selenium")
# elem.send_keys(Keys.RETURN)
# driver.implicitly_wait(20)
driver.close()

