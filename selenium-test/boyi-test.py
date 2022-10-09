from selenium.webdriver.common.by import By


# page_url = about:blank
class boyi_test(object):
    def __init__(self, driver):
        self.driver = driver

    def c_tips_container_div(self):
        return self.driver.find_element(By.ID, "c-tips-container")

    def s_is_result_css_textarea(self):
        return self.driver.find_element(By.XPATH, "//*[@id='s_is_result_css']")
