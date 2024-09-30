import time

def countdown_timer(seconds):
    while seconds > 0:
        print(f"Time remaining: {seconds} seconds")
        time.sleep(1)
        seconds -= 1
    print("Time's up!")
seconds = int(input("Enter time in seconds: "))
countdown_timer(seconds)
