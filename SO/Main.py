from threading import Thread,Semaphore
from time import sleep

contador = 0
sem = Semaphore()
#Semaphore ele garante a sincronização dos valores, com exclusão mútua.

class Process(Thread): #Construtor da classe
    def __init__(self,p):
        super().__init__() #construtor da classe thread.
        self.p = p #Self = this.

    def run(self): #Overwrite
        global contador
        while True:
            sem.acquire()#Impede que outras threads acessem a area critica.
            print("O processo {0}, Entrou na sessão crítica,contador: {1}".format(self.p,contador))
            contador += 1 #área crítica, Memória compartilhada.
            print("O processo {0}, Saiu na sessão crítica,contador: {1}".format(self.p, contador))
            sem.release() #Destrava os processos.
            sleep(1) #Tempo de 1seg



for thread in range(10): #Cria 10 Threads
    p = Process(thread)
    p.start()


