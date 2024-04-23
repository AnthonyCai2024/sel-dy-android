import time

from driver.app_dervier import AppDriver


class Run:

    def exec(self, app_driver: AppDriver):
        # open app
        self.open_app()

        time.sleep(3)

        # agree
        el_agree = app_driver.find_element_by_id('com.ss.android.ugc.aweme:id/dp4')
        if el_agree:
            print("找到同意按钮")
            el_agree.click()
        else:
            print("未找到同意按钮")

        time.sleep(1.2)

        print("exec")
        el_search = app_driver.find_element_by_id('com.ss.android.ugc.aweme:id/kmz')
        if el_search:
            print("找到搜索按钮")
            el_search.click()
        else:
            print("未找到搜索按钮")

        time.sleep(1.2)

    def open_app(self):
        time.sleep(0.8)
        # 点击桌面抖音
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
        #
        # time.sleep(1.5)


if __name__ == '__main__':
    run = Run()
    driver = AppDriver('emulator-5554')
    run.exec(driver)
    del run
