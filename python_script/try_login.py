import unittest
import os
from appium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4724/wd/hub',
            desired_capabilities={
                'platformName': 'Android',
                'platformVersion': '10',
                'udid': 'R59M705G59W',
                'autoGrantPermissions': 'true',
                'noReset': 'false',
                'appPackage': 'kst.macaron.chauffeur.dev',
                'appActivity': 'kst.macaron.chauffeur.ui.activity.SplashActivity',
                'newCommandTimeout': 300
            })

    def test_try_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 60)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MyTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)
