from appium import webdriver
from appium.options.common import AppiumOptions
from selenium.webdriver.common.by import By


class AppDriver:
    def __init__(self, device):
        option = AppiumOptions()
        option.set_capability('deviceName', 'emulator-5554')
        option.set_capability('platformName', 'android')
        option.set_capability('platformVersion', '9')
        option.set_capability('appPackage', 'com.ss.android.ugc.aweme')
        option.set_capability('appActivity', '.splash.SplashActivity')

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=option)

    def find_element_by_id(self, ele_id):
        try:
            return self.driver.find_element(By.ID, ele_id)
        except Exception as e:
            print(e)
            return None