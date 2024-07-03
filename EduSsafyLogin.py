import base64

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.options import Options

def eduSsafy_login():
    # 브라우저 꺼짐 방지 옵션
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--start-maximized")



    # Chrome 웹 드라이버 설정
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # 웹 페이지 열기
    driver.get('https://edu.ssafy.com/comm/login/SecurityLoginForm.do')

    # 페이지 로드 대기
    time.sleep(1)

    decoded_id = base64.b64decode('YWxlbmpiQG5hdmVyLmNvbQ==').decode('utf-8')
    decoded_pw = base64.b64decode('ZGx3amRxbHMxNSE=').decode('utf-8')

    # userId 입력
    user_id_element = driver.find_element(By.ID, 'userId')
    user_id_element.clear()
    user_id_element.send_keys(decoded_id)
    # userPwd 입력
    password_element = driver.find_element(By.ID, 'userPwd')
    password_element.clear()
    password_element.send_keys(decoded_pw)

    # 로그인 버튼 클릭 (CSS Selector 사용)
    login_button = driver.find_element(By.CSS_SELECTOR, 'div.form-btn > a')
    login_button.click()
    time.sleep(1)
    close_button = driver.find_element(By.CSS_SELECTOR, 'div.pop-foot > button.btn.btn-wide.btn-md.btn-primary.pop-event-close')
    close_button.click()
