import json
import time
import random
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

KEYWORDS = ["junior developer", "fullstack", "backend", "frontend"]

with open('config.json', 'r') as file:
    config = json.load(file)

def human_delay(min_seconds=1, max_seconds=5):
    time.sleep(random.uniform(min_seconds, max_seconds))

def browser_setup():
    # -------- Configure Chrome Profile --------
    opts = webdriver.ChromeOptions()
    opts.add_argument(rf"--user-data-dir={config['chrome_user_data_dir']}")
    opts.add_argument(rf"--profile-directory={config['chrome_profile']}")

    opts.add_argument("--start-maximized")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--ignore-certificate-errors")
    opts.add_argument("--no-sandbox")
    # # Can be useful on Mac to disable GPU
    opts.add_argument("--disable-gpu")
    opts.add_experimental_option("excludeSwitches", ["enable-automation"]) 
    opts.add_experimental_option('useAutomationExtension', False)
    opts.add_argument("--remote-debugging-port=9222")

    # browser = webdriver.Firefox(options=opts)
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=opts)

    print("Chrome options configured.")
    return browser

def login(browser, username,password):
    browser.get("https://www.linkedin.com/login")
    try:
            user_field = browser.find_element("id","username").send_keys(username)
            # user_field = browser.find_element(By.ID,"username").send_keys(username)
            pw_field = browser.find_element("id","password").send_keys(password)
            time.sleep(2)
            login_button = browser.find_element(By.XPATH, "//button[@type='submit']").click()
            time.sleep(15)
    except Exception as e:
           print(f" Username/password field or login button not found, {e}")

def start_apply(browser):

    try:
        for keyword in config['keywords']:
            print(f"Searching for jobs with keyword: {keyword}")
            
            browser.get(f"https://www.linkedin.com/jobs/search/?keywords={keyword.replace(' ', '%20')}f_AL=true&location={config['location']}&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0") 
            human_delay(3, 7)
            # TODO: Finish the logic of job application
            
            # Lisf of jobs
            links = browser.find_elements(By.XPATH, "//div[@data-job-id]")
            print(f"Processing job listing: {links}")

            for job in links:
                try:
                    # Scroll to the job listing to make it visible
                    browser.execute_script("arguments[0].scrollIntoView();", job)
                    human_delay(1, 3)

                    # job_title_element = job.find_element(By.CSS_SELECTOR, "a.job-card-list__title")
                    # job_title_element.click()
                    # human_delay(2, 5)

                    # "Easy Apply" button
                    browser.find_element(By.ID,'jobs-apply-button-id').click()
                    human_delay(2, 4)
                    
                    # Click "Next" if it exists
                    next_button = browser.find_element(By.CSS_SELECTOR, "button[aria-label='Continue to next step']")
                    while next_button:
                        next_button.click()
                        human_delay(2, 5)
                        try:
                            next_button = browser.find_element(By.CSS_SELECTOR, "button[aria-label='Continue to next step']")
                        except:
                            next_button = None

                    # Review and submit
                    review_button = browser.find_element(By.CSS_SELECTOR, "button[aria-label='Review your application']")
                    review_button.click()
                    human_delay(2,5)

                    submit_button = browser.find_element(By.CSS_SELECTOR, "button[aria-label='Submit application']")
                    submit_button.click() # Uncomment to actually submit
                    print("Application submitted (simulation).")


                    # Close the application modal
                    close_button = browser.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
                    close_button.click()
                    human_delay(1, 2)

                except Exception as e:
                    print(f"Could not process a job listing: {e}")
                    try:
                        close_button = browser.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
                        close_button.click()
                        human_delay(1, 2)
                    except:
                        pass

    except Exception as e:
        print(f"Could not complete the search for keyword '{keyword}': {e}")

    # TODO: AI integration for cover letter generation or custome responses
    # Close browser after some time
    browser.quit()

def main():
    browser = browser_setup()
    print("Browser opened with profile")
     
    login(browser, config['username'], config['password'])
    start_apply(browser)


if __name__ == "__main__":
   main()