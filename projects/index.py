# import speedtest
# wifi = speedtest.Speedtest()

# wifi.get_servers()
# wifi.get_best_server()
# print(wifi.download()/1000000)
# print(wifi.upload()/1000000)
# results = wifi.results.dict()

# # print(f"Download speed: {results['download'] / 10**6:.2f} Mbps")
# # print(f"Upload speed: {results['upload'] / 10**6:.2f} Mbps")
# # print(f"Ping: {results['ping']:.2f} ms")


a=[10,40,5,13,8,12,15,9,]
index=0
for x in a:
    if index<len(a):
        index=index+1
        print(f"Element at index {index} is {x}")
    