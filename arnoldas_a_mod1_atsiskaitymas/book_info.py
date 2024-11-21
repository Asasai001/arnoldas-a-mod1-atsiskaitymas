from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

website = 'https://books.toscrape.com/'
path = 'C:\\Tools\\chromedriver\\chromedriver.exe'

service = Service(path)

driver = webdriver.Chrome(service=service)

driver.get(website)

WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//article[@class="product_pod"]'))
)
all_books = driver.find_elements(By.XPATH, '//article[@class="product_pod"]')

book_title = []
book_price = []
book_rating = []


for book in all_books:
    title = book.find_element(By.TAG_NAME, 'h3').text
    price = book.find_element(By.CLASS_NAME, 'price_color').text
    rating_element = book.find_element(By.XPATH, './p[contains(@class, "star-rating")]')
    rating_class = rating_element.get_attribute('class')
    rating = rating_class.split()[-1]
    book_title.append(title)
    book_price.append(price)
    book_rating.append(rating)

data_frame = pd.DataFrame({'Title': book_title, 'Price': book_price, 'Rating': book_rating})

print(data_frame)

driver.quit()


data_frame.to_csv('book_info.csv', index=False)
print(data_frame)






