#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint

class Escalonador:
    """
        Escalonador de um sistema com duas filas, onde a fila 1 possui prioridade sobre a fila 2, ou seja, os elementos da fila 2
        só serão atendidos quando não houver nenhum elemento na fila 1. Para atendimento dos elementos, temos um servidor que atende 
        apenas 1 elemento por vez.
        Quando ocorre uma chegada de um elemento (seja da classe 1 ou 2) é observado se o servidor está livre, se sim, o mesmo logo é
        colocado no servidor para ser atendido, em caso negativo o elemento é colocado na sua respectiva fila.
    """
    def __init__(self, duracao):
        """
            Ao iniciarmos o escalonador passamos como parametro o tempo de duração do mesmo, uma vez que o iniciamos temos as duas filas vazias,
            uma para cada classe de elementos e logo definimos quando será a chegada do primeiro elemento de cada classe (considerando que o tempo
            de chegada do proximo elemento de classe 1 segue a distribuição uniforme entre 1 e 10, enquanto a classe 2 é entre 1 e 5). Também temos
            o servidor livre, uma vez que não há nenhum elemento para ser atendido.
        """
        self.duracao = duracao
        self.tam_fila1 = 0
        self.tam_fila2 = 0
        self.prox_chegada1 = self.geraNumero(1, 10)
        self.prox_chegada2 = self.geraNumero(1, 5)
        self.prox_atendimento = 0
        self.servidor_livre = True
        self.tempo = 0
        self.elemento_em_atendimento = 'Sem elemento'
        self.run(self.duracao)


    def run(self, duracao):
        """
            É executado um loop com um ciclo referente a cada segundo de ducação do escalonador, e em cada ciclo o relógio do escalonador é atualizado e 
            é checado se há uma algum evento para esse instante.
        """
        for i in xrange(duracao):
           self.clock()
           self.escalona() 

    def escalona(self):
        """
            Em todo pulso de clock devemos executar o método escalona, onde o mesmo irá atualizar o relógio do escalonador e verificar se há algum evento agendado
            para esse instante.
            Caso haja a chegada de um elemento, o escalonador irá verificar se o servidor está livre, se sim ele atribui o novo elemento para o servidor e imprime o
            evento, se não, o elemento será colocado na sua respectiva fila. Após isso o escalonador irá agendar a próxima chegada de um novo elemento da mesma classe.
            Caso algum evento seja finalizado nesse instante, o escalonador irá imprimir que um atendimento foi finalizado e irá verificar se há algum elemento na fila 1,
            em caso positivo o seu atendimento será inciado e este evento será impresso; caso a fila 1 esteja vazia o mesmo irá repetir o processo para a fila 2 e caso a 
            mesma também esteja vazia, o servidor continuará livre até o proximo instante de tempo.
        """

        if self.prox_chegada1 < 1:
            if self.servidor_livre:
                self.imprimeEvento('Chegada de Elemento da classe 1')
                self.iniciaAtendimento('1')
            else :
                self.tam_fila1 += 1
                self.imprimeEvento('Chegada de Elemento da classe 1')
                self.escalonaProximaChegada('1')

        if self.prox_chegada2 < 1:
            if self.servidor_livre:
                self.imprimeEvento('Chegada de Elemento da classe 2')
                self.iniciaAtendimento('2')
            else :
                self.tam_fila2 += 1
                self.imprimeEvento('Chegada de Elemento da classe 2')
            self.escalonaProximaChegada('2')

        if self.prox_atendimento < 1:
            if (not self.servidor_livre):    
                self.finalizaAtendimento()
            if self.tam_fila1 > 0:
                self.iniciaAtendimento('1')
            elif self.tam_fila2 > 0:
                self.iniciaAtendimento('2')
            else:
                self.servidor_livre = True



    def geraNumero(self, inicio, fim):
        """
            Gera um número aleatório entre o intervalo de passado como parametro.
        """
        return randint(inicio, fim)

    def clock(self):
        """
            Gerencia o tempo no escalonador, ou seja, conta mais um segundo no tempo de execução do escalonador e 
            diminui uma unidade no tempo dos eventos agendados.
        """
        self.tempo += 1
        if self.prox_chegada1 > 0:
            self.prox_chegada1 -= 1
        if self.prox_chegada2 > 0:
            self.prox_chegada2 -= 1
        if self.prox_atendimento > 0:
            self.prox_atendimento -= 1

    def escalonaProximaChegada(self, tipo):
        if tipo == '1':
            self.prox_chegada1 = self.geraNumero(1, 10)
            self.imprimeEvento('Proxima chegada de elemento da classe 1 agendado para o instante ' + str(self.tempo + self.prox_chegada1) + ' segundos')
        else:
            self.prox_chegada2 = self.geraNumero(1, 5)
            self.imprimeEvento('Proxima chegada de elemento da classe 2 agendado para o instante ' + str(self.tempo + self.prox_chegada2) + ' segundos')
    
    def imprimeEvento(self, tipo):
        """
            Imprime um evento, mostrando seu tipo, o instante que ocorreu e o estado do sistema nesse instante (filas e servidor).
        """
        print '----EVENTO----'
        print tipo 
        print 'Momento do Evento: ' + str(self.tempo) + ' segundos'
        print 'Elementos na Fila 1: ' + str(self.tam_fila1)
        print 'Elementos na Fila 2: ' + str(self.tam_fila2)
        if self.servidor_livre:
            print 'Servidor Livre'
        else:
            print 'Elemento em Atendimento: ' + str(self.elemento_em_atendimento)

    def iniciaAtendimento(self, classe):
        """
            Inicia um atendimento. Esse evento só ocorre quando o servidor está livre e há um elemento da #classe no sistema.
            Quando isso ocorre, o servidor servidor passa a ser ocupado, é definido o tempo de serviço desse elemento e o evento é impresso.
        """
        if classe == '1':
            if self.tam_fila1 > 0:
                self.tam_fila1 -= 1
            self.elemento_em_atendimento = 'Elemento da classe 1'
        else:
            if self.tam_fila2 > 0:
                self.tam_fila2 -= 1
            self.elemento_em_atendimento = 'Elemento da classe 2'
        self.servidor_livre = False
        self.prox_atendimento = self.geraNumero(3, 7)
        self.imprimeEvento('Atendimento de um ' + self.elemento_em_atendimento + ' iniciado (duração de ' + str(self.prox_atendimento) + ' segundos).')
    
    def finalizaAtendimento(self):
        """
            Finaliza um atendimento. Esse evento ocorre quando o tempo do serviço é finalizado. O servidor é setado como livre e o evento é impresso.
        """
        self.servidor_livre = True
        self.imprimeEvento('Finalização do atendimento do elemento '+ str(self.elemento_em_atendimento))




    
