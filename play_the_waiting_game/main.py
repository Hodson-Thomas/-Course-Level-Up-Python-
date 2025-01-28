from datetime import datetime
import random

def game():
    while True:
        target_time = random.randint(2, 10)
        print(f"You need to wait {target_time} seconds")
        input("Press any key when you are ready")       
        start = datetime.now()
        input("Waiting for input ...")
        now = datetime.now()
        print(f"You pressed at {now - start}")
        if (now - start).seconds == target_time:
            print("Well done !")
        else:
            print("Sorry, you failed !")
        match input("Press (q) to leave, press any other key to continue ..."):
            case "q":
                return
            case _:
                continue
                            
if __name__ == "__main__":
    game()