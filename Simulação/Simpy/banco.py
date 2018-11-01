#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import simpy

def finalizaAtendimento(env, nome, chegada, caixaEletronico, caixaInterno, guicheAtendimento):
    """
    Finaliza o atendimento de um cliente onde as opções são fazer outra operação no banco (probabilidade de 10%) ou
    sair do sistema (probabilidade de 90%).
    """
    reentrada = random.random()
    if reentrada < 0.1:
        print "%s finalizou atendimento mas decide realizar outra operação no instante %.2f minutos" % (nome, env.now)
        processoCliente = cliente(env, nome, caixaEletronico, caixaInterno, guicheAtendimento, True)
        env.process(processoCliente)

    else:
        print "%s saiu do sistema no instante %.2f minutos" % (nome,env.now)

def cliente(env, nome, caixaEletronico, caixaInterno, guicheAtendimento, recorrente):
    """
    Um processo cliente é responsável por gerenciar todas as atividades de um cliente dentro do banco.
    Quando um processo cliente é instanciado, ele recebe um nome e os recursos de caixa eletrônico, caixa
    interno e guiches de atendimento do banco. Um cliente pode escolher entre ir para o atendimento nos caixas 
    eletrônicos (probabilidade de 65%) ou atendimento interno (probabilidade de 35%). Se o cliente escolher o 
    atendimento interno, ele terá de escolher entre o caixa de atendimento interno (probabilidade de 40%) ou os 
    guichês (probabilidade de 60%). Uma vez escolhido o tipo de atendimento do cliente, ele irá verificar se tem
    recursos disponíveis de não houver, o processo irá esperar até um recurso ser liberado para enfim iniciar 
    seu atendimento.    
    """
    chegada = env.now
    if not recorrente:
        print "%s chegou no instante %.2f minutos" % (nome, chegada)
    
    #Define a probabilidade do cliente escolher os caixas eletrôncios ou o atendimento interno
    interno_externo = random.random()
    
    if interno_externo <= 0.35:
        print "%s escolheu atendimento Interno no instante %.2f minutos" % (nome, env.now)

        #Define a probabilidade do cliente escolher o atendimento no caixa ou os guichês
        caixa_guiche = random.random()

        if caixa_guiche <= 0.4:
            print "%s escolheu atendimento no caixa interno no instante %.2f minutos" % (nome, env.now)
            with caixaInterno.request() as caixa:
                yield caixa
                print "%s começou atendimento no caixa interno instante %.2f minutos" % (nome, env.now)
                tempo_atendimento = random.uniform(2, 5)    
                yield env.timeout(tempo_atendimento)
                caixaInterno.release(caixa)
                finalizaAtendimento(env, nome, chegada, caixaEletronico, caixaInterno, guicheAtendimento)
        else:
            print "%s escolheu atendimento no guichê no instante %.2f minutos" % (nome, env.now)
            with guicheAtendimento.request() as guiche:
                yield guiche
                print "%s começou atendimento no guichê no instante %.2f minutos" % (nome, env.now)
                tempo_atendimento = random.uniform(2, 5)    
                yield env.timeout(tempo_atendimento)
                guicheAtendimento.release(guiche)
                finalizaAtendimento(env, nome, chegada, caixaEletronico, caixaInterno, guicheAtendimento)


    else:
        with caixaEletronico.request() as caixa:
            yield caixa
            print "%s começou atendimento no caixa eletrônico no instante %.2f minutos" % (nome, env.now)
            tempo_atendimento = random.uniform(2, 5)    
            yield env.timeout(tempo_atendimento)
            caixaEletronico.release(caixa)
            finalizaAtendimento(env, nome, chegada, caixaEletronico, caixaInterno, guicheAtendimento)

def chegadaClientes(env):
    """
        Este processo é responsável por gerar as chegadas dos clientes no sistema utilizando uma distribuição de 
        probabilidade uniforme para definir o tempo de chegada do próximo cliente ao sistema, definindo-o um nome
        diferente de todos os outros clientes no sistema.
    """
    nCliente = 0
    while True:
        nome = "Cliente "+str(nCliente)
        processoCliente = cliente(env, nome, caixaEletronico, caixaInterno, guicheAtendimento, False)
        env.process(processoCliente)
        proximaChegada = random.uniform(3, 8)
        nCliente += 1
        yield env.timeout(proximaChegada)


#Cria o ambiente e inicia os processos
print "########## Sistema Bancario ###########\n"
env = simpy.Environment()
caixaEletronico = simpy.Resource(env, 4)
caixaInterno = simpy.Resource(env, 1)
guicheAtendimento = simpy.Resource(env, 3)
env.process(chegadaClientes(env))
env.run(until=50)