## Appium 초기 설정

기본 환경 : Mac, Android Studio(SDK), 스크립트 Python(Visual Studio Code)

* Python 설치가 안되어 있을경우 먼저 설치

#### Appium 설치 및 연결

* 관련 설명 링크 : https://kitle.xyz/post/100/
* Appium 설치 
  * http://appium.io/ 에서 다운로드 후 설치
  * PC의 환경에 따라 맞는 설치 파일 다운로드
* Appium 구분
  * GUI 버전
    * 말그대로 GUI로 구성하여 실행하는 버전
    * 실행된 앱의 화면 구성  Source를 볼수 있음
    * 이 Source를 기반으로 스크립트  작성 : 어떤 Component인지 구분할 수 있는 값는 용도
    * 안드로이드의 경우 @+id/ 의 값이나 View의 Path 값(View hierarchy Path)을 찾을수 있음
  * Server 버전
    * 실제 자동화테스트가 돌아가는 서버
    * 작성된 스크립트가 Server에서 돌아감
* Appium 실행
  * Port 구분 필요(GUI, Server 2가지 같이 실행해야하므로)
* Appium-doctor, Appium-Python-Client 설치
  * 관련 설명 링크 : https://dejavuqa.tistory.com/225
* 예제 스크립트 작성
  * https://dejavuqa.tistory.com/225 링크 내용대로 앱을 실행하고 30초후 종료하는 스크립트 작성
* 스크립트 구성
  * 참고 링크 : https://dejavuqa.tistory.com/227
  * class 이름 : 테스트를 구분할수 있는 이름으로 작성
  * def setUp : 테스트를 시작하기전 설정, GUI 버전에서 작성했던 JSON 정보들을 기입
    * GUI 버전과 다른 Port 설정
    * 연결된 기기의 platformVersion 확인
    * adb devices 명령어를 통해 uuid 확인
    * autoGrantPermissions : 퍼미션 자동으로 허용 옵션, 쇼퍼의 경우 true로 하고 테스트 시작
  * def test_search_field : 실제 테스트 코드가 진행되는 부분
    * GUI 버전의 ID나 XPath를 확인해가며 스크립트 작성
    * WebDriverWait 를 잘 활용 : 해당 Component가 준비 될때까지 기다릴때 사용
      * WebDriverWait(driver, 20) : 20초 동안 기다리고 준비가 되지 않았을 경우 Error
      * send_keys("입력할 텍스트") : EditText 를 해당 Text로 채워줌
* 스크립트 실행
  * python test_script.py 또는 python3 test_script.py

