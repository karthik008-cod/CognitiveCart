import sys
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

search_query = sys.argv[1]

options = Options()

# ✅ Headless Mode (no window popup)
options.add_argument("--headless=new")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--disable-extensions")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")

# ✅ Disable images for faster loading
prefs = {
    "profile.managed_default_content_settings.images": 2
}
options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 8)

driver.get(f"https://www.flipkart.com/search?q={search_query}")

# Close login popup if present
try:
    close_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'✕')]"))
    )
    close_btn.click()
except:
    pass

# Wait for product links
wait.until(
    EC.presence_of_element_located((By.XPATH, "//a[contains(@href,'/p/')]"))
)

product_links = driver.find_elements(By.XPATH, "//a[contains(@href,'/p/')]")

results = []

for link in product_links[:5]:
    href = link.get_attribute("href")
    raw_text = link.text.strip()

    lines = [l.strip() for l in raw_text.split("\n") if l.strip()]

    title = "N/A"
    rating = "N/A"
    reviews = "N/A"

    # 🔥 Dynamic title detection
    for line in lines:
        if (
            "₹" not in line
            and "Ratings" not in line
            and "Add to Compare" not in line
            and "Pre Order" not in line
            and len(line) > 15
        ):
            title = line
            break

    # Extract rating & reviews
    for line in lines:
        if "Ratings" in line:
            rating = line.split(" ")[0][:3]
            reviews = line
            break

    # Extract price
    try:
        parent = link.find_element(By.XPATH, "..")
        price_element = parent.find_element(By.XPATH, ".//*[contains(text(),'₹')]")
        price = price_element.text.split("\n")[0]
    except:
        price = "N/A"

    # ✅ Extract image FIRST
    try:
        img = link.find_element(By.XPATH, ".//img").get_attribute("src")
    except:
        img = ""

    # ✅ THEN append
    results.append({
        "title": title,
        "price": price,
        "rating": rating,
        "reviews": reviews,
        "link": href,
        "image": img
    })
    
driver.quit()

print(json.dumps(results))
