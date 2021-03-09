import threading
import random
import time

class Filosofo(threading.Thread):
    running = True 

    def __init__(self, index, garfo_da_esquerda, garfo_da_direita):
        threading.Thread.__init__(self)
        self.index = index
        self.garfo_da_esquerda = garfo_da_esquerda
        self.garfo_da_direita = garfo_da_direita

    def run(self):
        while(self.running):
            time.sleep(random.randint(1,5))
            print ('\nFilosofo %s está com fome.' % self.index)
            self.jantar()

    def jantar(self):
        garfo1, garfo2 = self.garfo_da_esquerda, self.garfo_da_direita
        while self.running:
            garfo1.acquire()
            locked = garfo2.acquire(False) 
            if locked:
                break
            garfo1.release()
            print ('\nFilosofo %s trocou de garfos.' % self.index)
            garfo1, garfo2 = garfo2, garfo1
        else:
            return
        self.jantando()
        garfo2.release()
        garfo1.release()
 
    def jantando(self):           
        print ('\nFilosofo %s começou a comer.'% self.index)
        time.sleep(random.randint(1,5))
        print ('\nFilosofo %s terminou de comer e está pensando.' % self.index)

def main():
    garfos = [threading.Semaphore() for n in range(5)] #começa o array dos semáforos(garfos).
    Filosofos= [Filosofo(i, garfos[i%5], garfos[(i+1)%5])for i in range(5)]
    Filosofo.running = True
    for p in Filosofos: p.start()
    time.sleep(10)
    Filosofo.running = False
    print ("Terminando...")

if __name__ == "__main__":
    main()