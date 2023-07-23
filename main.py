import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains


class AutomateWebsites:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.driver.get("https://www.naukri.com/nlogin/login")

    def login(self, usr, pwrd):
        username = self.find_search_box("id", "usernameField", usr)
        pword = self.find_search_box("id", "passwordField", pwrd)
        login_button = self.find_search_box("xpath", "//button[normalize-space()='Login']")
        # self.driver.get("https://www.naukri.com/python-jobs?experience=1")
        # time.sleep(10)

    def search_job(self, job_name, exp=None, city=None):
        time.sleep(5)
        search_url = "https://www.naukri.com/{}-jobs?experience={}&cityTypeGid={}".format(job_name, str(exp), str(city))
        print(search_url)
        self.driver.get(search_url)
        if exp is not None:
            self.vary_experience()

        time.sleep(10)

    def vary_experience(self):
        slider = self.find_search_box("xpath", "//div[@class='inside']")
        # self.driver.find_element(By.CSS_SELECTOR("div[data-type='slider']"))
        # self.driver.execute_script('arguments[0].value = 1;', slider)
        # self.driver.execute_script('arguments[0].onchange();', slider)
        # ActionChains(self.driver).drag_and_drop_by_offset(slider, 250, 0).perform()

    def get_job_results(self):
        res = self.driver.find_elements(By.TAG_NAME, "article")
        # print(res)
        for i in res:
            try:
                apply_url = i.find_element(By.TAG_NAME, "a").get_attribute("href")
                print(apply_url)
                i.find_element(By.TAG_NAME, "a").click()
                # break
            except Exception as e:
                # print(e)
                pass

    def job_apply(self):
        p = self.driver.current_window_handle
        chwd = self.driver.window_handles

        for w in chwd:
            # switch focus to child window
            if w != p:
                self.driver.switch_to.window(w)
                print(self.driver.title)
                try:
                    self.driver.find_element(By.CSS_SELECTOR,
                                             "div[class='apply-button-container'] button[class='waves-effect waves-ripple btn apply-button']").click()
                    time.sleep(10)
                    print("Applied")
                    self.driver.close()
                except Exception as e:
                    print("Failed")
                    self.driver.close()
                    pass

    def find_search_box(self, item_name, item_val, key=None):
        try:
            if key is None:
                res = self.driver.find_element(item_name, item_val).click()
            else:
                res = self.driver.find_element(item_name, item_val).send_keys(key)
            return res
        except Exception as e:
            print(e)
            print("Finding {} Failed".format(item_name))
            pass

    def close_window(self):
        self.driver.quit()


user = "username/email"
pword = "password"
job_name = "Python Automation 2 year"
experience = "2"
city_code = "97"
automate_obj = AutomateWebsites()
automate_obj.login(user, pword)
automate_obj.search_job(job_name)
automate_obj.get_job_results()
automate_obj.job_apply()
# Link opens in a different tab, and clicking is happening in the first tab (need to solve by shifting tab or opening in the same tab)

automate_obj.close_window()
