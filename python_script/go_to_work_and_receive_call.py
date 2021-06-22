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
                'noReset': 'true',
                'appPackage': 'kst.macaron.chauffeur.dev',
                'appActivity': 'kst.macaron.chauffeur.ui.activity.SplashActivity',
                'newCommandTimeout': 300
            })

    def test_go_to_work_and_receive_call(self):
        driver = self.driver
        wait = WebDriverWait(driver, 60)

        # 자동로그인, 차량 등록된 상태 된 상태로 일단 테스트
        # 출근하기 버튼 클릭
        ui_go_to_work_btn = wait.until(EC.element_to_be_clickable((By.ID, 'kst.macaron.chauffeur.dev:id/btnStartWork')))
        ui_go_to_work_btn.click()

        # 콜 수락
        ui_receive_call = wait.until(EC.element_to_be_clickable((By.ID, 'kst.macaron.chauffeur.dev:id/btnAccept')))
        ui_receive_call.click()

        # 고객탑승 kst.macaron.chauffeur.dev:id/btnLoad
        ui_customer_ride = wait.until(EC.element_to_be_clickable((By.ID, 'kst.macaron.chauffeur.dev:id/btnLoad')))
        ui_customer_ride.click()

        # 요금 입력 화면 : BackKey
        sleep(10)
        driver.back()

        # 앱 결제 요금 입력 클릭
        ui_app_pay_input = wait.until(EC.element_to_be_clickable((By.ID, 'kst.macaron.chauffeur.dev:id/btnDestArr')))
        ui_app_pay_input.click()

        # 운행요금 입력
        ui_input_fare = wait.until(EC.element_to_be_clickable((By.ID, 'kst.macaron.chauffeur.dev:id/fare_amount')))
        ui_input_fare.send_keys('10')

        # 통행요금 입력
        ui_input_service_charge = wait.until(EC.element_to_be_clickable((By.ID, 'kst.macaron.chauffeur.dev:id/et_service_charge')))
        ui_input_service_charge.send_keys('0')

        # 앱 결제 요청 버튼 클릭
        ui_app_pay_request_btn = wait.until(EC.element_to_be_clickable((By.ID, 'kst.macaron.chauffeur.dev:id/btnReqPay')))
        ui_app_pay_request_btn.click()

        # 결제요청 팝업 '네' 버튼 클릭
        dialog_pay_request_yes = wait.until(EC.element_to_be_clickable((By.ID, 'kst.macaron.chauffeur.dev:id/btnPositive')))
        dialog_pay_request_yes.click()

        # 앱 결제 실패 화면 -> 결제 변경 버튼 클릭
        ui_offline_pay_btn = wait.until(EC.element_to_be_clickable((By.ID, 'kst.macaron.chauffeur.dev:id/btnOfflinePay')))
        ui_offline_pay_btn.click()

        # 직접결제받기 팝업 -> '네' 버튼 클릭
        dialog_offline_pay_yes = wait.until(EC.element_to_be_clickable((By.ID, 'kst.macaron.chauffeur.dev:id/btnPositive')))
        dialog_offline_pay_yes.click()

        # 직접결제 요청 화면 -> 요금 받았습니다. 클릭
        ui_offline_fare_complete = wait.until(EC.element_to_be_clickable((By.ID, 'kst.macaron.chauffeur.dev:id/btnOffAccept')))
        ui_offline_fare_complete.click()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MyTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)
