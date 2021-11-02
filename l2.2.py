from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")
    element = browser.find_element_by_css_selector("img[src=\"images/chest.png\"]")
    x_element = element.get_attribute('valuex')
    x = x_element
    y = calc(x)
    input1 = browser.find_element_by_css_selector("input[type=\"text\"]")
    input1.send_keys(y)
    option1 = browser.find_element_by_css_selector("input[type=\"checkbox\"]")
    option1.click()
    option1 = browser.find_element_by_css_selector("input[id=\"robotsRule\"]")
    option1.click()
    button = browser.find_element_by_css_selector('button[type="submit"]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем ос