import requests
import datetime
import cfg

students = cfg.students
start_date = datetime.date(2022,9,5)
now_date = datetime.date.today()
days = int(str(now_date-start_date).split()[0])+1

ofset = 9
def get_nid(day):
    if day % 7 == 0:
        return None # если сегодня воскресение - не дежурить
    day -= day // 7 # убираем все воскресенья
    return (ofset + (day - 1)*4 )% 26 # по 4 человека начиная с 9
    
def get_next():
    s = []
    nid = get_nid(days)
    if nid:
        for i in range (4):
            s.append(students[(nid+i-1)%26])
        return f"Сегодня дежурят в столовой:\n{s[0]}, {s[1]}\nВ кабинетах:\n{s[2]}, {s[3]}\n"
    return nid

def send_msg(text):
    if text:
        results = requests.get(f"https://api.telegram.org/bot{cfg.token}/sendMessage?chat_id={cfg.chat_id}&text={text}" )
        print(results.json())



send_msg(get_next())