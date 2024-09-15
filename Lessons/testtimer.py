import threading
import time


# def task():
#     print("Timer object is getting executed...")
#
#
# if __name__ == '__main__':
#     t = threading.Timer(5, task)
#     print("Starting the timer object...")
#     t.start()  # after 5 seconds, task will be executed
#
#     # cancelling the timer object before start
#     print("cancelling the timer object")
#     t.cancel()

counter = 0
def printit():
    global counter
    if counter < 5:  # Ограничение на 5 повторений
        print("Hello, World!")
        counter += 1
        threading.Timer(1, printit).start()



printit()