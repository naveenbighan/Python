import modules as mf
import time

mf.hello("naveen")

# a= mf.person1["age"]
# print(a)
# b= mf.person1["country"]
# print(b)

# current_time = time.time()
# print("Current Time in seconds since the Epoch:", current_time)

# print("starting sleeping")

# time.sleep(5)
# print("awake after 5 seconds")


start_time = time.time()

for i in range(10000):
  print(i)

print(time.time()-start_time)