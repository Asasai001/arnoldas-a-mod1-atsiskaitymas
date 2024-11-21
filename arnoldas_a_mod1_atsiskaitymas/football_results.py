from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

def footbal_results():
    website = 'https://www.adamchoi.co.uk/overs/detailed'
    path = 'C:\\Tools\\chromedriver\\chromedriver.exe'

    service = Service(path)
    driver = webdriver.Chrome(service=service)


    driver.get(website)


    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//label[@analytics-event="All matches"]'))
    ).click()


    date = []
    home_team = []
    score = []
    away_team = []


    matches = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.TAG_NAME, "tr"))
    )


    for match in matches:
        try:

            tds = match.find_elements(By.TAG_NAME, 'td')
            if len(tds) >= 4:
                date.append(tds[0].text)
                home_team.append(tds[1].text)
                score.append(tds[2].text)
                away_team.append(tds[3].text)
        except Exception as e:
            print(f"Skipping a row due to an error: {e}")


    for i in range(len(date)):
        print(f"Date: {date[i]}, Home Team: {home_team[i]}, Score: {score[i]}, Away Team: {away_team[i]}")


    driver.quit()

    data_frame = pd.DataFrame({'date': date, 'home_team': home_team, 'score': score, 'away_team': away_team})
    data_frame.to_csv('football_results.csv', index=False)
    print(data_frame)

