from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pandas as pd

def book_info(book_info_csv = 'book_info.csv'):
    website = 'https://books.toscrape.com/'
    path = 'C:\\Tools\\chromedriver\\chromedriver.exe'

    service = Service(path)

    driver = webdriver.Chrome(service=service)

    driver.get(website)
#importuota TimeoutException, kad būtų galima patikrinti kas vyksta, jei neužkrautų tinklalapio

    try:

        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//article[@class="product_pod"]'))
        )
    except TimeoutException:
        return[]

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

    results = [{"book_title": t, "book_price": p, "book_rating": r}
               for t, p, r in zip(book_title, book_price, book_rating)]

    driver.quit()

    data_frame = pd.DataFrame(results)
    data_frame.to_csv(book_info_csv, index=False)

    return results

book_info()








