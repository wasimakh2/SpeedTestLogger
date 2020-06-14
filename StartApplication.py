# Python program to test 
# internet speed 
#Build with pyinstaller StartApplication.py  

#pyinstaller -y --add-data "C:/Users/wasim.akhtar/Documents/GitProjects/SpeedTestTracker/client_secret.json";"."  "C:/Users/wasim.akhtar/Documents/GitProjects/SpeedTestTracker/StartApplication.py"

import speedtest
from WriteToGoogleSheet import AddSpeedResutltToGoogleSheet
from TelegramBot import  SendPhoto
def DoTest():
    st = speedtest.Speedtest()
    # option = int(input('''What speed do you want to test:   
    
    # 1) Download Speed   
    
    # 2) Upload Speed   
    
    # 3) Ping  
    
    # Your Choice: ''')) 


    print((st.download()/1000000))

    print(st.upload())

    servernames =[]
    st.get_servers(servernames)
    print(st.results.ping)
    st.results.share()

    results_dict = st.results.dict()
    AddSpeedResutltToGoogleSheet(results_dict)
    if results_dict['client']['isp']=="Excitel":
        if (st.download()/1000000)<10:
            SendPhoto(st.results.share())

DoTest()