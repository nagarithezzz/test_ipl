from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Open the IPL ticket booking page
driver.get("https://www.district.in/tata-ipl-2025-match-09-gujarat-titans-vs-mumbai-indians-in-ahmedabad-march29/event")

# Wait for the page to load
time.sleep(5)  

# Find the "Notify me" button by class name
try:
    notify_button = driver.find_element(By.CLASS_NAME, "css-12ju5bv")

    # Scroll to the button
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", notify_button)

    # Click the button
    time.sleep(2)  # Small delay before clicking
    notify_button.click()
    print("✅ Clicked 'Notify me' button successfully!")

except Exception as e:
    print("❌ Could not find or click the 'Notify me' button:", e)

# Keep browser open for 10 seconds (adju
