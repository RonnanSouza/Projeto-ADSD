import random

import simpy

def cliente(env, name, caixaEletronico):
    print name + " chegou no instante %.2f minutos" % env.now
    with caixaEletronico.request() as caixa:
        yield caixa
        print name + " comecou atendimento no instante %.2f minutos" % env.now
        tempo_atendimento = random.uniform(15, 20)    
        yield env.timeout(tempo_atendimento)
        print name + " saiu do sistema no instante %.2f minutos" % env.now

def chegadaClientes(env, caixaEletronico):
    count = 0
    while True:
        nome = "Cliente "+str(count)
        c = cliente(env, nome, caixaEletronico)
        env.process(c)
        tempo = random.uniform(1, 2)
        yield env.timeout(tempo)
        count += 1



#Cria o ambiente e inicia os processos
print "Sistema Bancario"
env = simpy.Environment()
caixaEletronico = simpy.Resource(env, 2)
env.process(chegadaClientes(env, caixaEletronico))
env.run(until=50)