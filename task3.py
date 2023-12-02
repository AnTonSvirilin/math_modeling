import time 

M, N = int(input()), int(input())

starttimer = time.time()


for i in range(0, N):
    print(i)
    for k in range(0, M):
        print(k)
        time.sleep(1)

endtimer = time.time()

total = endtimer - starttimer
print(total)