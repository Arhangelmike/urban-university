import threading
import time,random



class Bank:

    def __init__(self):
        self.balance = random.randint(1,1000) # random?
        self.counter = 0
        self.transaction = 100
        self.lock = threading.Lock()
        print(f'Баланс:{self.balance}')


    def deposit(self):

        for i in range(self.transaction):
            incoming_transaction = random.randint(50, 500)
            # print(f'Положить надо: {incoming_transaction}.')
            # print(f'Баланс перед внесением: {self.balance}')
            if self.lock.locked() and self.balance >= 500:
                self.lock.release()
            self.balance += incoming_transaction
            time.sleep(0.001)
            print(f'Пополнение: {incoming_transaction}. Баланс:{self.balance}')
        self.transaction = 100



    def take(self):

        for i in range(self.transaction):
            outgoing_transaction = random.randint(50, 500)
            # print(f'Снять надо: {outgoing_transaction}.')
            # print(f'Баланс перед снятием: {self.balance}')
            if (self.balance >= outgoing_transaction):
                self.balance -= outgoing_transaction
                time.sleep(0.001)
                print(f'Снятие: {outgoing_transaction}. Баланс: {self.balance}')
            else:
                self.lock.acquire()
                time.sleep(0.001)
                print("Запрос отклонён, недостаточно средств.")
        self.transaction = 100


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')