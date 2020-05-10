from datetime import datetime, timedelta
import schedule

def print_epta():
    print("Епта")

x = datetime.now() + timedelta(seconds=10)

schedule.every().day.at("13:57:20").do(print_epta)