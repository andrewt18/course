from threading import Thread, Lock

class Account:
    def __init__(self, amount):
        self.balance = amount
        self.lock = Lock()

    def withdraw(self, amount):
        if isinstance(amount, int):
            self.lock.acquire()
            if amount > self.balance:
                self.lock.release()
                return False
            self.balance -= amount
            self.lock.release()
            return True
        else:
            return False

account = Account(1)

t1 = Thread(target=account.withdraw, args=("a",))
t2 = Thread(target=account.withdraw, args=(1,))
t1.start()
t2.start()
t1.join()
t2.join()