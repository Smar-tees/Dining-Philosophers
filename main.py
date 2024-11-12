import time
import threading


def eat(philosopher, fork1, fork2):
    arg = (fork1, fork2)
    thread = threading.Thread(target=philosopher.Eat, args=arg)

    if fork1.getStatus() == True or fork2.getStatus() == True:
        arg = (philosopher, fork1, fork2)
        thread_args.append(arg)
        return
    
    else:
        fork1.changeStatus()
        fork2.changeStatus()
        thread.start()


class Philosopher:

    def __init__(self, position, status):
        self.position = position
        self.status = status
        # When not eating it will be False and when eating it will be True

    def Eat(self, fork1, fork2):
        # This function is going to take in two forks and change the status of this philosopher while it's running to eating and change the status of the forks as being used
        self.status = True

        print(f'Philosopher {self.position} is eating with forks {fork1.whatPosition()} and {fork2.whatPosition()}')
        time.sleep(5)
        print(f'Philosopher {self.position} has finished eating with forks {fork1.whatPosition()} and {fork2.whatPosition()}')

        arg = (self, fork1, fork2)
        thread_args.append(arg)
        fork1.changeStatus()
        fork2.changeStatus()

class Fork:
    def __init__(self, position, status):
        self.position = position
        self.status = status
        # If it's being used then it's True and False if not
    
    def changeStatus(self):
        if self.status == True:
            self.status = False
        else:
            self.status = True

    def whatPosition(self):
        return self.position

    def getStatus(self):
        return self.status
        

if __name__ == '__main__':
    philosophers = {}
    forks = {}

    for i in range(5):
        philosophers[i] = Philosopher(i+1, False)

    for i in range(5):
        forks[i] = Fork(i+1, False)

    thread_args = []

    for i in range(len(philosophers.keys())):
        index = list(philosophers.keys())[i-1]
        arg = (philosophers[i], forks[index], forks[i])
        thread_args.append(arg)

    for arg in thread_args:
        eat(arg[0], arg[1], arg[2])
        time.sleep(0.1)