from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


#Set to headless so no GUI
options = Options()
options.add_argument('--headless')
options.add_argument("--window-size=1920, 1200")

#Path to Chrome driver
driver = webdriver.Chrome(options=options, executable_path= r"C:\Users\jarow\Downloads\chromedriver_win32\chromedriver.exe")

#Asking for user input
#webpage = input("What website do you want to check?: ")

#Which website
driver.get(f"https://www.reddit.com")

#Reddits login button
click_login = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/header/div/div[2]/div/div[1]/a").click()

#Reddits username/password fields
login_username = driver.find_element(By.XPATH, '//*[@id="loginUsername"]').send_keys(USERNAME)
login_password = driver.find_element(By.XPATH, '//*[@id="loginPassword"]').send_keys(PASSWORD)
submit_login = driver.find_element(By.XPATH, "/html/body/div/main/div[1]/div/div/form/fieldset[4]/button").click()

try:
    logout_button = driver.find_element(By.ID("logout"))
    print("Successfully logged in")
except NoSuchElementException:
    print("Login failed")

driver.quit()


