from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# Initialize the browser
driver = webdriver.Chrome()

# Navigate to the webpage
driver.get("https://nagarithezzz.github.io/test_ipl/")

try:
    # Wait for page to load
    print("⏳ Waiting for page to load...")
    
    # Check if the timer element is present
    timer_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "timer"))
    )
    print("✅ Found timer element")
    
    # Monitor timer until it reaches 00:00:00
    print("⏳ Monitoring timer until it reaches 00:00:00...")
    
    while True:
        # Get the current timer value
        timer_value = timer_element.text
        print(f"Current timer: {timer_value}")
        
        # Check if timer has reached zero
        if timer_value == "00:00:00":
            print("⏳ Waiting for 'Book Now' button to be added...")
            
            # Wait for the "Book Now" button to appear (1.5s after timer reaches 00:00:00)
            book_button = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.ID, "bookBtn"))
            )
            print("✅ 'Book Now' button is now visible!")

            # Click the "Book Now" button
            driver.execute_script("arguments[0].click();", book_button)
            print("✅ Successfully clicked 'Book Now' button!")

            break  # Exit loop after clicking the button
        
        # Check frequently (every 10 milliseconds)
        time.sleep(0.01)
    
    # Keep the browser open for inspection
    print("Browser will remain open for a long time...")
    time.sleep(10000)

except Exception as e:
    print(f"❌ An error occurred: {e}")
    time.sleep(10000)  # Keep browser open for debugging

print("Script finished")
