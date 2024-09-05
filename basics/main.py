def hello(b,c):
    return 6+b(c)
    


print(hello(lambda x:x*x,5))



# import time

# attempts=0
# max_retries=5
# wait_time=1
# while attempts<max_retries:
#     print(f"attempts-{attempts+1} wait-time={wait_time} seconds")
#     time.sleep(wait_time)
#     wait_time*=2
#     attempts+=1
    





