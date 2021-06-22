import unittest
import os
from time import sleep
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'platformName': 'Android',
                'platformVersion': '11',
                'udid': 'RF9N90010HR',
                'autoGrantPermissions': 'true',
                'noReset': 'true',
                'appPackage': 'kst.macaron.rider.dev',
                'appActivity': 'kst.macaron.rider.ui.intro.IntroActivity',
                'newCommandTimeout': 300
            })

    def test_no_ride_swipe(self):
        driver = self.driver
        wait = WebDriverWait(driver, 60)
        action = TouchAction(driver)

        # 지금타기 Swipe
        ui_seekbar_ride_type = wait.until(EC.element_to_be_clickable((By.ID, 'kst.macaron.rider.dev:id/slideBtnCall')))
        ui_now_ride_text = wait.until(EC.element_to_be_clickable((By.ID, 'kst.macaron.rider.dev:id/tvCallTitle')))

        action.press(ui_seekbar_ride_type).move_to(ui_now_ride_text).release().perform()

        # 등록된 목적지 Click
        ui_recent_search_word = wait.until(EC.visibility_of_element_located((By.ID, 'kst.macaron.rider.dev:id/tvBookmarkRecent1')))
        ui_recent_search_word.click()

        # 택시선택
        ui_select_taxi = wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.view.ViewGroup')))
        ui_select_taxi.click()

        # 호출하기
        ui_call_taxi = wait.until(EC.visibility_of_element_located((By.ID, 'kst.macaron.rider.dev:id/btnReservationStart')))
        ui_call_taxi.click()

        # 평가화면


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MyTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)
