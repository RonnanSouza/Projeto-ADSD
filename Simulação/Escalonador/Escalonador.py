from random import randint

class Escalonador:
    def __init__(self):
        self.tam_fila1 = 0
        self.tam_fila2 = 0
        self.prox_chegada1 = 0
        self.prox_chegada2 = 0
        self.tempo = 0

    def escalona(self):
        self.clock()
        if self.prox_chegada1 < 1:
            self.tam_fila1 += 1
            self.imprimeEvento('Chegada na fila 1')
            self.prox_chegada1 = self.geraNumero(1, 10)
            self.imprimeEvento('Proxima chegada na fila 1 agendando para ' + str(self.tempo + self.prox_chegada1) + ' segundos')
        if self.prox_chegada2 < 1:
            self.tam_fila2 += 1
            self.imprimeEvento('Chegada na fila 2')
            self.prox_chegada2 = self.geraNumero(1, 5)
            self.imprimeEvento('Proxima chegada na fila 2 agendando para ' + str(self.tempo + self.prox_chegada2) + ' segundos')

    def geraNumero(self, inicio, fim):
        return randint(inicio, fim)

    def clock(self):
        self.tempo += 1
        if self.prox_chegada1 > 0:
            self.prox_chegada1 -= 1
        if self.prox_chegada2 > 0:
            self.prox_chegada2 -= 1
    
    def imprimeEvento(self, tipo):
        print '----EVENTO----'
        print tipo 
        print 'Momento do Evento: ' + str(self.tempo) + ' segundos.'
        print 'Elementos na Fila 1: ' + str(self.tam_fila1)
        print 'Elementos na Fila 2: ' + str(self.tam_fila2)

scheduler = Escalonador()
for i in range(10):
    scheduler.escalona()


    
