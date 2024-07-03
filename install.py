import subprocess
import sys

def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def set_package():
    # 필요한 패키지 목록
    packages = [
        "pyautogui",
        "selenium",
        "webdriver-manager"
    ]

    # 각 패키지를 설치
    for package in packages:
        install_package(package)
