import threading
import time
class signal:
    def s_color(self):
        user='red'
        if user=='red':
            print('red')
            time.sleep(15)
            print('green')
            time.sleep(15)
            print('yellow')
            time.sleep(15)
       
s1=signal()
s1.s_color()