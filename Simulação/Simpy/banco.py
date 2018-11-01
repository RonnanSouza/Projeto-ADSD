#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import simpy

def cliente(env, nome, caixaEletronico, caixaInterno, gicheAtendimento):
    print "%s chegou no instante %.2f minutos" % (nome, env.now)
    interno_externo = random.random()
    if interno_externo <= 0.35:
        print "%s escolheu atendimento Interno no instante %.2f minutos" % (nome, env.now)
        caixa_giche = random.random()
        if caixa_giche <= 0.4:
            print "%s escolheu atendimento no caixa interno no instante %.2f minutos" % (nome, env.now)
            with caixaInterno.request() as caixa:
                yield caixa
                print "%s começou atendimento no caixa interno instante %.2f minutos" % (nome, env.now)
                tempo_atendimento = random.uniform(2, 5)    
                yield env.timeout(tempo_atendimento)
                print "%s saiu do sistema no instante %.2f minutos" % (nome,env.now)
        else:
            print "%s escolheu atendimento no gichê no instante %.2f minutos" % (nome, env.now)
            with gicheAtendimento.request() as giche:
                yield giche
                print "%s começou atendimento no gichê no instante %.2f minutos" % (nome, env.now)
                tempo_atendimento = random.uniform(2, 5)    
                yield env.timeout(tempo_atendimento)
                print "%s saiu do sistema no instante %.2f minutos" % (nome,env.now)
    else:
        print "%s escolheu atendimento Externo no instante %.2f minutos" % (nome, env.now)
        with caixaEletronico.request() as caixa:
            yield caixa
            print "%s começou atendimento no caixa eletrônico no instante %.2f minutos" % (nome, env.now)
            tempo_atendimento = random.uniform(2, 5)    
            yield env.timeout(tempo_atendimento)
            print "%s saiu do sistema no instante %.2f minutos" % (nome,env.now)

def chegadaClientes(env):
    nCliente = 0
    while True:
        nome = "Cliente "+str(nCliente)
        processoCliente = cliente(env, nome, caixaEletronico, caixaInterno, gicheAtendimento)
        env.process(processoCliente)
        proximaChegada = random.uniform(3, 8)
        nCliente += 1
        yield env.timeout(proximaChegada)
        



#Cria o ambiente e inicia os processos
print "########## Sistema Bancario ###########\n"
env = simpy.Environment()
caixaEletronico = simpy.Resource(env, 4)
caixaInterno = simpy.Resource(env, 1)
gicheAtendimento = simpy.Resource(env, 3)
env.process(chegadaClientes(env))
env.run(until=50)