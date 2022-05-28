import pyautogui as pg
import webbrowser as web
import time
import pandas as pd

country='55'
data = pd.read_csv(r"C: Escreva aqui endereço da planilha no computador ",
delimiter=r';', encoding="utf-8-sig")
data_dict = data.to_dict('list') 
leads = data_dict['leadnumber'] # Nome da coluna de numeros no excel
messages = data_dict['message'] # Nome da coluna de mensagens no excel
combo = zip(leads,messages)
first = True

for leads,messages in combo:
    time.sleep(4)
    web.open("https://web.whatsapp.com/send?phone="+country+str(leads)+"&text="+messages)
    if first:
        time.sleep(8)
        first = False
    width, height = pg.size()
    pg.click(width / 2, height / 2)
    time.sleep(10)
    pg.press('enter')
    pg.press('enter')
    time.sleep(5)
    pg.hotkey('ctrl', 'w')