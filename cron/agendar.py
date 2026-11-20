import time
import schedule

def task():
    print("Executando tarefa agendada.")

# schedule.every().day.at("08:00").do(task)
# schedule.every().hour.do(task)
# schedule.every().monday.do(task)
# schedule.every().friday.at("18:00").do(task)
schedule.every(5).seconds.do(task)

while True:
    schedule.run_pending()
    time.sleep(1)