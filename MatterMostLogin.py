import base64

import pyautogui
import time
import subprocess


def MatterMost_login():
    # 프로그램 실행
    program_path = r'C:\Users\cobin\AppData\Local\Programs\mattermost-desktop\Mattermost.exe'
    subprocess.run([program_path])

    # 프로그램이 실행되고 로그인 화면이 뜰 때까지 잠시 대기 (필요에 따라 조정)
    time.sleep(0.5)

    # ID 입력란 위치 (예: (x, y) 좌표를 찾은 값으로 대체)
    id_position = (1092, 537)  # 여기에 실제 ID 입력란 좌표를 입력하세요
    password_position = (1110, 609)  # 여기에 실제 비밀번호 입력란 좌표를 입력하세요
    login_button_position = (1288, 719)  # 여기에 실제 로그인 버튼 좌표를 입력하세요

    # ID 입력란으로 마우스 이동 및 클릭
    pyautogui.click(id_position)

    # ID 입력
    decoded_id = base64.b64decode('YWxlbmpiQG5hdmVyLmNvbQ==').decode('utf-8')
    pyautogui.write(decoded_id)

    # 비밀번호 입력란으로 마우스 이동 및 클릭
    pyautogui.click(password_position)

    # 비밀번호 입력
    decoded_pw = base64.b64decode('ZGx3amRxbHMxNSFB').decode('utf-8')

    pyautogui.write(decoded_pw)

    # 로그인 버튼 클릭
    pyautogui.click(login_button_position)
