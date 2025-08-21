import threading
import time

def first_work (first,last):
    time.sleep(5)
    print(f"this is for first job {first} {last}")

def second_job(sname):
    time.sleep(4)
    print(f"this is the second job for {sname}")

def third_job():
    time.sleep(2)
    print("this is the last job ")

job1 = threading.Thread(target=first_work, args=("grace", "john" ) )
job1.start()
job2 = threading.Thread(target=second_job, args=("sname",))
job2.start()
job3 =threading.Thread(target=third_job)
job3.start()

job1.join()
job2.join()
job3.join()

print("done this is multithreading which allows you to do multiple thinsg sat the same time ")

