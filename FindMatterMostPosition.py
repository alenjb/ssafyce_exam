import pyautogui

print("ID 입력란 위에 마우스를 올려놓고 엔터 키를 누르세요.")
input()  # 엔터 키를 누를 때까지 대기

x, y = pyautogui.position()  # 현재 마우스 위치 좌표
print(f"ID 입력란 위치: ({x}, {y})")
