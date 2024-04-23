import time

from driver.app_dervier import AppDriver


class Run:

    def exec(self, app_driver: AppDriver):
        # no need open app, because it's already opened
        # self.open_app()

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

        el_kw = app_driver.find_element_by_id('com.ss.android.ugc.aweme:id/et_search_kw')
        if el_kw:
            print("找到输入框")
            time.sleep(0.8)
            el_kw.send_keys('一千万粉丝')
        else:
            print("未找到输入框")

        time.sleep(1.2)

        el_search = app_driver.find_element_by_id('com.ss.android.ugc.aweme:id/zr=')
        if el_search:
            print("找到搜索按钮")
            el_search.click()
        else:
            print("未找到搜索按钮")


if __name__ == '__main__':
    run = Run()
    driver = AppDriver('emulator-5554')
    run.exec(driver)
    del run
