# Simulação desenvolvida utilizando o framework Simpy

Nossa simulação consiste em um sistema de uma agencia bancária como a do Banco do Brasil da UFCG.
Consiste em um gerador de chegadas dos clientes, onde inicialmente cada cliente tem uma probabilidade de 0.35 de ir para o atendimento interno, e 0.65 de ir para os caixas eletronicos. Uma vez escolhido o atendimento interno, a probabilidade do cliente ir para a fila de resolução de problemas é de 0.6 e de 0.4 de ir para o caixa. No caixa o cliente irá ter um tempo de atendimento em torno de 2 minutos (uniforme de 1min~2min), enquanto no atendimento o tempo gira em torno de 5min (uniforme de 4min~7min).
No caso do cliente escolher o caixa eletrônico, o seu tempo de atendimento girará em torno dos 3 minutos (2min~5min).
Após isso o cliente tem uma probabilidade de 0.05 de fazer outra operação dentro da agência, caso contrario o cliente sai da agência.

Entidades:
 - Gerador de chegadas
 - 5 caixas eletrônicos
 - 1 caixa interno
 - 3 guichês de atendimento


