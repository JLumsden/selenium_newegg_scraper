import time
import csv
from selenium import webdriver

with open('newegg_sales.csv', 'w') as f:
    f.write("Item, Price \n")

driver = webdriver.Chrome()
driver.get("https://www.newegg.com/DailyDeal.aspx?name=DailyDeal")

#infinite scroll solution
SPT = 1.0
c = 0
element = driver.find_element_by_class_name('shop-region')
while c < 6:
    driver.execute_script("arguments[0].scrollIntoView();", element)
    driver.execute_script("window.scrollBy(0, -420)")
    time.sleep(SPT)
    c += 1

#game time
l = []
name = driver.find_elements_by_xpath('//a[@class="item-title"]')
price = driver.find_elements_by_xpath('//li[@class="price-current"]')
for i in price:
    if '$' not in i.text:
        l.append("See site for pricing. Might be sold out.")
    else:
        l.append(i.text)

#write
with open('newegg_sales.csv', 'a') as f:
    for i in range(len(name)):
        product = name[i].text
        product = product.replace(',', '.')
        f.write(product + ',' + l[i] + '\n')

driver.close()
