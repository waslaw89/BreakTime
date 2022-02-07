from datetime import timedelta
from datetime import datetime
from os.path import exists

n = 37 #Width of column of text

# Log if exist
if exists("break_log.txt") == True:
	f = open("break_log.txt", "r")
	for x in f:
		pass
	try:
		lastLine=x
	except:
		lastLine=""
	f.close()	
else:
	f = open("break_log.txt", "w")
	f.write("Date|BrakeStart|BreakEnd|BreakTime")
	f.close()

header = n*"#"+"\n   Break Time App\n"+ n*"#"
print(header)

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current time:", current_time)
print(" Hit ENTER start new\n or end current break")
print(n*"-")

#begining
ToDo = input()
start = datetime.now()
start_time = start.strftime("%H:%M:%S")
arr_start_time = start_time.split(":")
print("->break start: ",start_time)

#ending
ToDo = input()
stop = datetime.now()
stop_time = stop.strftime("%H:%M:%S")

print("->break stop:  ",stop_time)
print("\n"+n*"-")

#only todays
date = now.strftime("%Y:%m:%d")
try:
	arr = lastLine.split("|")
	if arr[0] == date:
		break_today = arr[4]
	else:
		break_today = "00:00:00"
except:
	break_today = "00:00:00"


#current break cout
delta = stop - timedelta(hours=int(arr_start_time[0]), minutes=int(arr_start_time[1]), seconds=int(arr_start_time[2]))
break_now = delta.strftime("%H:%M:%S")
print("Current break time:  ",break_now)

#summary brak count
arr_break_today = break_today.split(":")
arr_break_now = break_now.split(":")
sum = timedelta(hours=int(arr_break_today[0]), minutes=int(arr_break_today[1]), seconds=int(arr_break_today[2])) + timedelta(hours=int(arr_break_now[0]), minutes=int(arr_break_now[1]), seconds=int(arr_break_now[2]))
break_sum  = str(sum)
if len(break_sum) == 7: break_sum = "0" + break_sum
print("Summary break time:  ",break_sum)
print(n*"+")

#save log
f = open("break_log.txt", "a")
log = "\n" + date + "|"+ start_time + "|" + stop_time+ "|" + break_now+ "|" + break_sum
f.write(log)
f.close()
ToDo = input("Hit ENTER to close")
