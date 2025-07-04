from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
service = Service("C:\\Users\\Adrian De Guzman\\OneDrive - ateneo.edu\\Desktop\\College\\Admin\\APK\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")

driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://aisis.ateneo.edu/j_aisis/displayLogin.do")

driver.find_element(By.NAME, "userName").send_keys("221941")
driver.find_element(By.NAME, "password").send_keys("dreyan22")

driver.find_element(By.NAME, "submit").click()

wait = WebDriverWait(driver, 20)

evaluation_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "COURSE AND FACULTY EVALUATION")))
evaluation_link.click()

time.sleep(5)

wait.until(EC.presence_of_all_elements_located((By.XPATH, "//input[@type='radio' and @value='5']")))

checkboxes = driver.find_elements(By.XPATH, "//input[@type='radio' and @value='5']")
for box in checkboxes:
    try:
        if not box.is_selected():
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", box)
            time.sleep(0.2)
            driver.execute_script("arguments[0].click();", box)
    except Exception as e:
        print(f"Click failed: {e}")

        
text_inputs = {
    "Q195": "The workload was manageable.",
    "Q196": "None",
    "Q197": "None",
    "Q198": "I find online classes challenging due to the lack of face-to-face interaction with classmates and professor.",
    "Q200": "The teacher ensures to be there for the students in every step of the way.",
    "Q201": "None",
    "Q202": "Very cool teacher",
    "Q204": "The onsite discussions and groupworks were the most helpful for me.",
    "Q205": "hehe"
}

for name, value in text_inputs.items():
    try:
        textarea = driver.find_element(By.NAME, name)
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", textarea)
        time.sleep(0.2)
        textarea.clear()
        textarea.send_keys(value)
    except Exception as e:
        print(f"Failed to fill {name}: {e}")

input("Click mo enter para close ko na pre solid")
driver.quit()
