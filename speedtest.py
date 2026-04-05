import speedtest as st

print(st.ping())
def Speed_Test():
    test = st.Speed_Test()
    down_speed = round(test.download() / 10**6, 2)
    print("Download Speed in Mbps:", down_speed)
    
    up_speed = round(test.upload() / 10**6, 2)
    print("Upload Speed in Mbps:", up_speed)
    
    ping = test.results.ping
    print("Ping:", ping)

Speed_Test()

