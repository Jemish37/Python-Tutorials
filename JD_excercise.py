import time


lst = [1,2,3,4,5,6,7,8,9]
for i in range(1,100000):
    print(i)

    if(i/1000 in lst):
        time.sleep(2)