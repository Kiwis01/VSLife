from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def get_linkedin_info():
    
    options = Options()
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    service = Service("/usr/local/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=options)

    # Login
    driver.get("https://www.linkedin.com/login")
    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")
    username.send_keys("carlosespn2001@gmail.com")
    password.send_keys("Sasha2020")
    driver.find_element(By.XPATH, "//button[@aria-label='Sign in']").click()


    # verification_element = driver.find_element(By.ID, "input__email_verification_pin")
    # verification_pin = input("Enter verification pin: ")
    # verification_element.send_keys(verification_pin)
    # driver.find_element(By.ID, "email-pin-submit-button").click()

    driver.get("https://www.linkedin.com/in/carlos-quihuis-190b431aa/")

    # print(driver.page_source)
    print(driver.title)
    sections = driver.find_elements(By.TAG_NAME, 'section')
    for sec in sections:
        print(sec.text)


    input("Press Enter to close browser")
    driver.quit()

get_linkedin_info()
