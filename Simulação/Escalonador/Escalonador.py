from random import randint

class Escalonador:
    def __init__(self):
        self.tam_fila1 = 0
        self.tam_fila2 = 0
        self.prox_chegada1 = 0
        self.prox_chegada2 = 0
        self.tempo = 0

    def escalona(self):
        if self.prox_chegada1 < 1:
            self.tam_fila1 += 1
            print 'Chegada na fila 1. Tamanho da fila: ' + str(self.tam_fila1) + '. Tempo: ' + str(self.tempo)
            self.prox_chegada1 = self.geraNumero(1, 10)
            print 'Proxima chegada na fila 1 agendado para : ' + str(self.tempo + self.prox_chegada1) + '. Tempo: ' + str(self.tempo)
        if self.prox_chegada2 < 1:
            self.tam_fila2 += 1
            print 'Chegada na fila 2. Tamanho da fila: ' + str(self.tam_fila2) + '. Tempo: ' + str(self.tempo)
            self.prox_chegada2 = self.geraNumero(1, 5)
            print 'Proxima chegada na fila 2 agendado para : ' + str(self.tempo + self.prox_chegada2) + '. Tempo: ' + str(self.tempo)

    def geraNumero(self, inicio, fim):
        return randint(inicio, fim)

    def clock(self):
        self.tempo += 1
        if self.prox_chegada1 > 0:
            self.prox_chegada1 -= 1
        if self.prox_chegada2 > 0:
            self.prox_chegada2 -= 1


scheduler = Escalonador()
for i in range(10):
    scheduler.clock()
    scheduler.escalona()


    
