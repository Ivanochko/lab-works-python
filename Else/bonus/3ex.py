from datetime import datetime

today = datetime.now()

date_string = today.strftime("%Y-%m-%d %H:%M:%S")
print(date_string)
