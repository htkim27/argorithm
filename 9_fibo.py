# 재귀함수 -> Stack : 메모리 비효율

from time import time

def fibo(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else: 
        return fibo(i-1) + fibo(i-2)



memory = {0:0, 1:1}
def fibo_opt(i):
    global memory
    if i in memory.keys():
        return memory[i]
    else:
        memory[i] = fibo_opt(i-1) + fibo_opt(i-2)
        return memory[i]

def helper(i, memory: dict={}):
    if i in memory.keys():
        return memory[i]
    else:
        memory[i] = helper(i-1, memory) + helper(i-2, memory)
        return memory[i]

def fibo_opt(n):
    memory = {0:0, 1:1}

    return helper(n, memory)
    

# for i in range(10):
#     ans = fibo_opt(i)
#     print(ans)
    

N = 30

start = time() * 1000
ans = fibo(N)
print(ans)
end = time() * 1000

print("[1] : ", end-start, "s")


start = time() * 1000
ans = fibo_opt(N)
print(ans)
end = time() * 1000

print("[2] : ", end-start, "s")