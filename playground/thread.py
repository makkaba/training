#같은 thread 로 이름만 다르게 생성을 해서 
#http 요청을 생각하면서 해보자 
#목적: 멀티스레드는 어디까지 공유하고 충돌이 있다면 왜 충돌이 일어나고 어떻게 막고?

import threading
import time
import random 


MAX_NUM = 20
TRY_EACH = 10

shared_number = 0
lock = threading.Lock() 

def thread_1(number):
    global shared_number
    #print("1-> number = ",end=""), print(number)
    
    
    for i in range(number):
        lock.acquire() # thread_2 잠금
        print(shared_number, "<-- 영희")
        shared_number += 1
        lock.release() # thread_2 해제
        time.sleep(random.randrange(1,2))
        
    


def thread_2(number):
    global shared_number
    #print("number = ",end=""), print(number), print("<-2")

    for i in range(number):
        lock.acquire() # thread_2 잠금
        print("철수-->", shared_number)
        shared_number += 1
        lock.release() # thread_2 해제
        time.sleep(random.randrange(1,2))
        
    

if __name__ == "__main__":

    threads = [ ]

    start_time = time.time()
    t1 = threading.Thread( target= thread_1, args=(TRY_EACH,) )
    t1.start()
    print("t1 started.")
    threads.append(t1)

    t2 = threading.Thread( target= thread_2, args=(TRY_EACH,) )
    t2.start()
    print("t2 started")
    threads.append(t2)


    #각 스레드 끝날때까지 기다렸다가 실행 wait 존재
    for t in threads:
        t.join()

    print("--- %s seconds ---" % (time.time() - start_time))

    print("shared_number=",end=""), print(shared_number)
    print("end of main")
