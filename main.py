import time
from plyer import notification


if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Please Drink Water Now!!" ,
            message = "The average daily water requirement for men is about 15.5 cups (3.7 liters) and 11.5 cups (2.7 liters) for women" ,
            app_icon = "D:\Practice Python\icon.icu.ico" ,
            timeout = 2 ,
        )
        time.sleep(60*60)
        
    
