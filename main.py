from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

login_time = 30  # Time for login (in seconds)
new_msg_time = 20  # Time for a new message (in seconds)
send_msg_time = 10  # Time for sending a message (in seconds)
country_code = 91  # Set your country code
action_time = 2  # Set time for button click action
image_path = 'D:\\pythonProject_whatsapp\\image\\image.jpg'  # Absolute path to your image

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

with open('message.txt', 'r') as file:
    msg = file.read()

link = 'https://web.whatsapp.com'
driver.get(link)
time.sleep(login_time)

with open('numbers.txt', 'r') as file:
    for n in file.readlines():
        num = n.rstrip()
        print(num)
        link = f'https://web.whatsapp.com/send/?phone={country_code}{num}'
        driver.get(link)
        time.sleep(new_msg_time)

        if(image_path):
            try:
                # attach_btn = driver.find_element(By.CSS_SELECTOR, "._1OT67")
                attach_btn = driver.find_element(By.CSS_SELECTOR, ".x11xpdln")
                image_btn = driver.find_element(By.CSS_SELECTOR, ".x1gja9t")

                attach_btn.click()
                time.sleep(action_time)

                image_btn.click()
                time.sleep(action_time)

                # msg_input = driver.find_elements(By.CSS_SELECTOR, "input[type='file']")
                msg_input = driver.find_elements(By.CSS_SELECTOR, "._ak1l")
                print('Message input clicked')
                msg_input.send_keys(image_path)
                time.sleep(action_time)
            except Exception as e:
                print("Error:", e)

        actions = ActionChains(driver)
        for line in msg.split('\n'):
            actions.send_keys(line)
            actions.key_down(Keys.SHIFT).send_keys(Keys.ENTER).key_up(Keys.SHIFT)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        time.sleep(send_msg_time)

driver.quit()