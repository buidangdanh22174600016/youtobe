
import time

time.sleep(5)
my_lst =["cat","dog","pig","chicken","duck","dolphin"]

for item in my_lst:
    pag.write(f"hello, you are a{item}!")
    pag.press("enter")
    time.sleep(0.5)