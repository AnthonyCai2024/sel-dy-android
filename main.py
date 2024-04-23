import time

from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.touch_action import TouchAction


class Run:

    def __init__(self, i, b):
        self.i = i
        self.b = b

        # 链接移动设备必须的参数
        # desired_caps = {'deviceName': "127.0.0.1:62001"
        #     , 'platformName': "Android"
        #     , 'platformVersion': "7.1.2"
        #     , 'appPackage': "com.ss.android.ugc.aweme"
        #     , 'appActivity': ".splash.SplashActivity"}

        option = AppiumOptions()
        option.set_capability('deviceName', 'emulator-5554')
        option.set_capability('platformName', 'android')
        option.set_capability('platformVersion', '9')
        option.set_capability('appPackage', 'com.ss.android.ugc.aweme')
        option.set_capability('appActivity', '.splash.SplashActivity')

        # 当前要测试的设备名称

        # 系统

        # 系统的版本

        # 要启动的app的名称（包名）

        # 要启动app的那个界面

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=option)

    def __del__(self):
        print("完成，再见")

    # 滑动页面使可以找到其它元素
    def click(self):
        time.sleep(0.8)
        # # 点击桌面抖音
        # dy_app = self.driver.find_element(By.XPATH, '//*[@text = "抖音"]')
        # if dy_app:
        #     print("找到抖音桌面图标,clicking ....")
        #     dy_app.click()
        # else:
        #     print("未找到抖音桌面图标")
        #
        # # wait for 6 seconds
        # time.sleep(6)
        #
        # action = TouchAction(self.driver)
        # action.tap(x=200, y=550, count=1)
        # action.perform()

        # self.b = b
        # # 点击搜索元素
        # self.driver.find_element(By.XPATH, '//*[@resource-id = "com.ss.android.ugc.aweme:id/c0="]').click()
        # time.sleep(1)
        # # 点击输入框，并输入文字
        # self.driver.find_element(By.XPATH, '//*[@resource-id = "com.ss.android.ugc.aweme:id/et_search_kw"]').send_keys(
        #     b)
        # time.sleep(1)
        # # 输入成功后点击搜索
        # self.driver.find_element(By.XPATH, '//*[@resource-id = "com.ss.android.ugc.aweme:id/k4g"]').click()
        # time.sleep(2)

        # action.tap(x=200, y=550, count=1)
        # action.perform()
        # self.huadon()

    def huadon(self):
        self.i = i
        a = 0
        while i > a:
            a += 1
            print(f"运行次数{a}")

            time.sleep(3)
            action = TouchAction(self.driver)
            action.press(x=240, y=630).wait(200).move_to(x=266, y=200).release()
            action.perform()
            time.sleep(2)
            action.tap(x=505, y=616, count=1).perform()

    # # 关闭app
    # def guanbi(self):
    #     self.driver.close_app()
    #
    #     time.sleep(2)
    #     self.driver.quit()

    def main(self):
        print("正在运行，请稍等....")
        self.click()


if __name__ == '__main__':
    i = eval(input("输入刷视频次数："))
    b = input("输入要看的视频：")
    a = Run(i, b)
    a.main()
