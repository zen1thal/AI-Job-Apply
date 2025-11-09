from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time
import random

KEYWORDS = ["junior developer", "fullstack", "backend", "frontend"]

# Random delay to mimic human behavior
def human_delay(min_seconds=1, max_seconds=10):
    time.sleep(random.uniform(min_seconds, max_seconds))

# -------- Configure Firefox Profile --------
# Create a dedicated profile in Firefox (e.g., called "JobApply") and use its path here:
FIREFOX_PROFILE_PATH = "/Users/zviatos/Library/Application Support/Firefox/Profiles/l0tx736r.default-release"

opts = Options()
opts.profile = FIREFOX_PROFILE_PATH
opts.headless = False  # Keep False to see the browser

driver = webdriver.Firefox(options=opts)


# driver.get("https://www.linkedin.com/login")

# human_delay(2, 5)

# # Fill login form
# driver.find_element(By.ID, "username").send_keys(")
# human_delay()
# driver.find_element(By.ID, "password").send_keys("")
# human_delay()
# driver.find_element(By.XPATH, "//button[@type='submit']").click()


# human_delay(5, 20)


try:
        keyword = random.choice(KEYWORDS)
        print(f"Searching for jobs with keyword: {keyword}")
        
        driver.get(f"https://www.linkedin.com/jobs/search/?keywords={keyword.replace(' ', '%20')}&location=Madrid%2C%20Spain") 
        human_delay(3, 7)

        # Get a list of job listings
        job_listings = driver.browser.find_element(By.CLASS_NAME,"jobs-search-results-list")

        for job in job_listings:
            try:
                # Scroll to the job listing to make it visible
                driver.execute_script("arguments[0].scrollIntoView();", job)
                human_delay(1, 3)

                links = job.find_element(By.XPATH, "//div[@data-job-id]").click()
                print(f"Processing job listing: {links}")



                job_title_element = job.find_element(By.CSS_SELECTOR, "a.job-card-list__title")
                job_title_element.click()
                human_delay(2, 5)

                # Click the "Easy Apply" button
                easy_apply_button = driver.find_element("xpath",'//button[contains(@class, "jobs-apply-button")]')
                easy_apply_button.click()
                human_delay(2, 4)

                # --- Application filling logic ---
                # This is a simplified example. Real applications are more complex.
                
                # Click "Next" if it exists
                next_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Continue to next step']")
                while next_button:
                    next_button.click()
                    human_delay(2, 5)
                    # You would add logic here to fill out fields on each page
                    try:
                        next_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Continue to next step']")
                    except:
                        next_button = None

                # Review and submit
                review_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Review your application']")
                review_button.click()
                human_delay(2,5)

                submit_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Submit application']")
                # submit_button.click() # Uncomment to actually submit
                print("Application submitted (simulation).")


                # For now, just close the application modal to continue to the next job
                close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
                close_button.click()
                human_delay(1, 2)

            except Exception as e:
                print(f"Could not process a job listing: {e}")
                try:
                    close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
                    close_button.click()
                    human_delay(1, 2)
                except:
                    pass

except Exception as e:
    print(f"Could not complete the search for keyword '{keyword}': {e}")


# Close browser after some time
# human_delay(5, 10)
driver.quit()
