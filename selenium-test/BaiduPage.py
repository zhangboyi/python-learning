from selenium.webdriver.common.by import By


# page_url = https://hf.ke.com/ershoufang/
class BaiduPage(object):
    def __init__(self, driver):
        self.driver = driver

    def clear(self):
        return self.driver.find_element(By.XPATH, "//li[.//a[text()='大富山庄']]")

    def clear2(self):
        return self.driver.find_element(By.XPATH, "//li[.//a[text()='大富山庄']]")

    def clear3(self):
        return self.driver.find_element(By.XPATH, "//li[.//a[text()='罗兰德小区']]")
