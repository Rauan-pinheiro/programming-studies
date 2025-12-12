import pyautogui
from time import sleep

pyautogui.PAUSE = 0.3
#abrir o gogle e procurar por spotify
sleep(2)
pyautogui.press('Win')
sleep(0.5)
pyautogui.write('Google')
sleep(0.5)
pyautogui.press('Enter')
pyautogui.write('Spotify')
pyautogui.press('Enter')
pyautogui.moveTo(x=520 , y=393 , duration= 1)
pyautogui.click()
sleep(5)
pyautogui.moveTo(x=149, y=399 , duration= 1 )
pyautogui.click()
sleep(1)

#adicionar e remover músicas
for musica in range(): # numero de músicas
    sleep(1)
    #clica nos 3 pontinhos e add a playlist
    pyautogui.moveTo(x=1405, y=685, duration= 0.5)
    pyautogui.click()
    pyautogui.moveTo(x=1546, y=190, duration= 0.5)
    pyautogui.moveTo(x=1145, y=291, duration= 0.5)
    pyautogui.click()
    sleep(1)
    # ------------------------------------------

    # seleciona o botão para tirar das músicas curtidas
    pyautogui.moveTo(x=1405, y=685, duration= 0.5)
    pyautogui.click()
    pyautogui.moveTo(x=1524, y=251, duration= 0.5)
    pyautogui.click()
    # ------------------------------------------
