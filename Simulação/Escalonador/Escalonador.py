#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint

class Escalonador:
    def __init__(self):
        self.tam_fila1 = 0
        self.tam_fila2 = 0
        self.prox_chegada1 = 0
        self.prox_chegada2 = 0
        self.prox_atendimento = 0
        self.servidor_livre = True
        self.tempo = 0
        self.elemento_atendimento = 0

    def escalona(self):
        self.clock()
        if self.prox_chegada1 < 1:
            if self.servidor_livre:
                self.imprimeEvento('Chegada de Elemento da classe 1')
                self.iniciaAtendimento('1')
            else :
                self.tam_fila1 += 1
                self.imprimeEvento('Chegada de Elemento da classe 1')
            self.prox_chegada1 = self.geraNumero(1, 10)
            self.imprimeEvento('Proxima chegada de elemento da classe 1 agendando para ' + str(self.tempo + self.prox_chegada1) + ' segundos')
        if self.prox_chegada2 < 1:
            if self.servidor_livre:
                self.imprimeEvento('Chegada de Elemento da classe 2')
                self.iniciaAtendimento('2')
            else :
                self.tam_fila2 += 1
                self.imprimeEvento('Chegada de Elemento da classe 2')
            self.prox_chegada2 = self.geraNumero(1, 5)
            self.imprimeEvento('Proxima chegada de elemento da classe 2 agendando para ' + str(self.tempo + self.prox_chegada2) + ' segundos')
        if self.prox_atendimento < 1:
            self.finalizaAtendimento()
            if self.tam_fila1 > 0:
                self.tam_fila1 -= 1
                self.iniciaAtendimento('1')
            elif self.tam_fila2 > 0:
                self.tam_fila2 -= 1
                self.iniciaAtendimento('2')
            else:
                self.servidor_livre = True



    def geraNumero(self, inicio, fim):
        return randint(inicio, fim)

    def clock(self):
        self.tempo += 1
        if self.prox_chegada1 > 0:
            self.prox_chegada1 -= 1
        if self.prox_chegada2 > 0:
            self.prox_chegada2 -= 1
        if self.prox_atendimento > 0:
            self.prox_atendimento -= 1
    
    def imprimeEvento(self, tipo):
        print '----EVENTO----'
        print tipo 
        print 'Momento do Evento: ' + str(self.tempo) + ' segundos.'
        print 'Elementos na Fila 1: ' + str(self.tam_fila1)
        print 'Elementos na Fila 2: ' + str(self.tam_fila2)
        if self.servidor_livre:
            print 'Servidor Livre'
        else:
            print 'Elemento em Atendimento: ' + str(self.elemento_atendimento)

    def iniciaAtendimento(self, classe):
        self.servidor_livre = False
        self.prox_atendimento = self.geraNumero(3, 7)
        self.elemento_atendimento += 1
        self.imprimeEvento('Atendimento do elemento ' + str(self.elemento_atendimento) + ' (classe '+ classe +') iniciado (duração de ' + str(self.prox_atendimento) + ' segundos).')
    
    def finalizaAtendimento(self):
        self.servidor_livre = True
        self.imprimeEvento('Finalização do atendimento do elemento '+ str(self.elemento_atendimento))


scheduler = Escalonador()
for i in range(10):
    scheduler.escalona()


    
