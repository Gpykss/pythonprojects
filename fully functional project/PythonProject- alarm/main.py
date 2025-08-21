import time
import datetime

def set_alarm(alarm_time):
    print(f"The alarm time is {alarm_time}")
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("WAKE UP!!...WAKE UP!!...WAKE UP!!...")
            is_running = False
        elif current_time > alarm_time:
            print(f"Its Past {alarm_time} already ")
            is_running = False
        else:
            print(current_time)
            print("~", end=" ")
            time.sleep(1)




if __name__ == "__main__":
    alarm_time = input("Enter alarm Time 00:00:00:   ")
    set_alarm(alarm_time)

