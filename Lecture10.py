from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_yahoo_search():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://search.yahoo.com/")
    driver.maximize_window()

    try:
        try:
            accept_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Accept')]"))
            )
            accept_button.click()
        except:
            pass

        search_box = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "yschsp"))
        )
        search_box.clear()
        search_box.send_keys("selenide")
        search_box.send_keys(Keys.RETURN)

        first_result = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[3]/div/div/div[1]/div/div/div/div/ol/li[1]/div/div[1]/a"))
        )
        first_result_link = first_result.get_attribute("href")

        assert "selenide.org" in first_result_link, f"Ожидалось selenide.org, получено: {first_result_link}"
        print("✓ Первый результат ведет на selenide.org")

        first_result_text = first_result.text

        images_tab = driver.find_element(By.XPATH, "//a[contains(text(), 'Images')]")
        images_tab.click()

        first_image = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/section/section/section/div/div[2]/section/div/ul/li[1]/div[1]"))
        )
        first_image_alt = first_image.get_attribute("title")

        assert "selenide" in first_image_alt.lower(), "Первое изображение не связано с selenide"
        print("✓ Первое изображение связано с selenide")

        all_tab = driver.find_element(By.XPATH, "//a[contains(text(), 'All')]")
        all_tab.click()

        new_first_result = WebDriverWait(driver, 5).until(
                 EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[3]/div/div/div[1]/div/div/div/div/ol/li[1]/div/div[1]/a"))
        )
        new_first_result_text = new_first_result.text

        assert first_result_text == new_first_result_text, f"Результаты не совпадают: было '{first_result_text}', стало '{new_first_result_text}'"
        print("✓ Первый результат остался неизменным")

    finally:
        time.sleep(2)
        driver.quit()

if __name__ == "__main__":
    test_yahoo_search()