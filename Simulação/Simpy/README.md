# Simulação desenvolvida utilizando o framework Simpy

Nossa simulação consiste em um sistema de uma agencia bancária como a do Banco do Brasil da UFCG.
Consiste em um gerador de chegadas dos clientes, onde inicialmente cada cliente tem uma probabilidade de 0.35 de ir para o atendimento interno, e 0.65 de ir para os caixas eletronicos. Uma vez escolhido o atendimento interno, a probabilidade do cliente ir para a fila de resolução de problemas é de 0.6 e de 0.4 de ir para o caixa. No caixa o cliente irá ter um tempo de atendimento em torno de 2 minutos (uniforme de 1min-2min), enquanto no atendimento o tempo gira em torno de 5min (uniforme de 4min-7min).
No caso do cliente escolher o caixa eletrônico, o seu tempo de atendimento girará em torno dos 3 minutos (2min~5min).
Após isso o cliente tem uma probabilidade de 0.05 de fazer outra operação dentro da agência, caso contrario o cliente sai da agência.

Entidades:
 - Gerador de chegadas
 - 5 caixas eletrônicos
 - 1 caixa interno
 - 3 guichês de atendimento



![proposta de adsd - simulacao](https://user-images.githubusercontent.com/8560905/48173022-d6da9100-e2e0-11e8-9849-133e0e6411db.png)

## Exemplo de Execução

########## Sistema Bancario ###########

Cliente 0 chegou no instante 0.00 minutos
Cliente 0 escolheu atendimento Interno no instante 0.00
Cliente 0 escolheu atendimento no guichê no instante 0.00
Cliente 0 começou atendimento no guichê no instante 0.00 após uma espera de 0.00
Cliente 1 chegou no instante 1.28 minutos
Cliente 1 escolheu atendimento Interno no instante 1.28
Cliente 1 escolheu atendimento no caixa interno no instante 1.28
Cliente 1 começou atendimento no caixa interno no instante 1.28 após uma espera de 0.00
Cliente 2 chegou no instante 2.87 minutos
Cliente 2 começou atendimento no caixa eletrônico no instante 2.87 após uma espera de 0.00
Cliente 3 chegou no instante 4.65 minutos
Cliente 3 começou atendimento no caixa eletrônico no instante 4.65 após uma espera de 0.00
Cliente 4 chegou no instante 6.48 minutos
Cliente 4 escolheu atendimento Interno no instante 6.48
Cliente 4 escolheu atendimento no guichê no instante 6.48
Cliente 4 começou atendimento no guichê no instante 6.48 após uma espera de 0.00
Cliente 5 chegou no instante 8.41 minutos
Cliente 5 começou atendimento no caixa eletrônico no instante 8.41 após uma espera de 0.00
Cliente 6 chegou no instante 9.96 minutos
Cliente 6 começou atendimento no caixa eletrônico no instante 9.96 após uma espera de 0.00
Cliente 2 saiu do sistema no instante 11.26
Cliente 7 chegou no instante 11.65 minutos
Cliente 7 começou atendimento no caixa eletrônico no instante 11.65 após uma espera de 0.00
Cliente 8 chegou no instante 13.13 minutos
Cliente 9 chegou no instante 14.47 minutos
Cliente 1 saiu do sistema no instante 15.19
Cliente 3 saiu do sistema no instante 15.75
Cliente 8 começou atendimento no caixa eletrônico no instante 15.75 após uma espera de 2.61
Cliente 10 chegou no instante 16.13 minutos
Cliente 5 finalizou atendimento mas decide realizar outra operação no instante 17.09
Cliente 5 escolheu atendimento Interno no instante 17.09
Cliente 5 escolheu atendimento no caixa interno no instante 17.09
Cliente 5 começou atendimento no caixa interno no instante 17.09 após uma espera de 0.00
Cliente 9 começou atendimento no caixa eletrônico no instante 17.09 após uma espera de 2.62
Cliente 11 chegou no instante 17.86 minutos
Cliente 12 chegou no instante 19.34 minutos
Cliente 6 finalizou atendimento mas decide realizar outra operação no instante 19.85
Cliente 10 começou atendimento no caixa eletrônico no instante 19.85 após uma espera de 3.72
Cliente 13 chegou no instante 20.59 minutos
Cliente 13 escolheu atendimento Interno no instante 20.59
Cliente 13 escolheu atendimento no guichê no instante 20.59
Cliente 13 começou atendimento no guichê no instante 20.59 após uma espera de 0.00
Cliente 7 saiu do sistema no instante 21.12
Cliente 11 começou atendimento no caixa eletrônico no instante 21.12 após uma espera de 3.27
Cliente 14 chegou no instante 21.63 minutos
Cliente 14 escolheu atendimento Interno no instante 21.63
Cliente 14 escolheu atendimento no guichê no instante 21.63
Cliente 15 chegou no instante 23.23 minutos
Cliente 15 escolheu atendimento Interno no instante 23.23
Cliente 15 escolheu atendimento no guichê no instante 23.23
Cliente 16 chegou no instante 24.56 minutos
Cliente 16 escolheu atendimento Interno no instante 24.56
Cliente 16 escolheu atendimento no caixa interno no instante 24.56
Cliente 0 saiu do sistema no instante 24.96
Cliente 14 começou atendimento no guichê no instante 24.96 após uma espera de 3.32
Cliente 17 chegou no instante 25.73 minutos
Cliente 4 saiu do sistema no instante 26.84
Cliente 15 começou atendimento no guichê no instante 26.84 após uma espera de 3.61
Cliente 8 saiu do sistema no instante 27.03
Cliente 12 começou atendimento no caixa eletrônico no instante 27.03 após uma espera de 7.69
Cliente 18 chegou no instante 27.08 minutos
Cliente 18 escolheu atendimento Interno no instante 27.08
Cliente 18 escolheu atendimento no caixa interno no instante 27.08
Cliente 9 saiu do sistema no instante 27.65
Cliente 6 começou atendimento no caixa eletrônico no instante 27.65 após uma espera de 7.81
Cliente 19 chegou no instante 28.51 minutos
Cliente 20 chegou no instante 29.93 minutos
Cliente 20 escolheu atendimento Interno no instante 29.93
Cliente 20 escolheu atendimento no caixa interno no instante 29.93
Cliente 5 saiu do sistema no instante 30.97
Cliente 16 começou atendimento no caixa interno no instante 30.97 após uma espera de 6.41
Cliente 21 chegou no instante 31.22 minutos
Cliente 11 finalizou atendimento mas decide realizar outra operação no instante 31.26
Cliente 17 começou atendimento no caixa eletrônico no instante 31.26 após uma espera de 5.54
Cliente 10 saiu do sistema no instante 31.61
Cliente 19 começou atendimento no caixa eletrônico no instante 31.61 após uma espera de 3.11
Cliente 22 chegou no instante 32.33 minutos
Cliente 23 chegou no instante 33.87 minutos
Cliente 23 escolheu atendimento Interno no instante 33.87
Cliente 23 escolheu atendimento no guichê no instante 33.87
Cliente 24 chegou no instante 35.41 minutos
Cliente 25 chegou no instante 36.43 minutos
Cliente 12 saiu do sistema no instante 37.90
Cliente 21 começou atendimento no caixa eletrônico no instante 37.90 após uma espera de 6.68
Cliente 13 saiu do sistema no instante 38.14
Cliente 23 começou atendimento no guichê no instante 38.14 após uma espera de 4.27
Cliente 26 chegou no instante 38.31 minutos
Cliente 6 saiu do sistema no instante 39.01
Cliente 11 começou atendimento no caixa eletrônico no instante 39.01 após uma espera de 7.75
Cliente 27 chegou no instante 39.99 minutos
Cliente 27 escolheu atendimento Interno no instante 39.99
Cliente 27 escolheu atendimento no guichê no instante 39.99
Cliente 19 saiu do sistema no instante 40.94
Cliente 22 começou atendimento no caixa eletrônico no instante 40.94 após uma espera de 8.60
Cliente 28 chegou no instante 41.45 minutos
Cliente 17 saiu do sistema no instante 41.63
Cliente 24 começou atendimento no caixa eletrônico no instante 41.63 após uma espera de 6.22
Cliente 16 saiu do sistema no instante 43.11
Cliente 18 começou atendimento no caixa interno no instante 43.11 após uma espera de 16.03
Cliente 29 chegou no instante 43.29 minutos
Cliente 30 chegou no instante 44.90 minutos
Cliente 15 saiu do sistema no instante 46.45
Cliente 27 começou atendimento no guichê no instante 46.45 após uma espera de 6.46
Cliente 31 chegou no instante 46.62 minutos
Cliente 32 chegou no instante 48.09 minutos
Cliente 14 saiu do sistema no instante 48.37
Cliente 21 saiu do sistema no instante 48.47
Cliente 25 começou atendimento no caixa eletrônico no instante 48.47 após uma espera de 12.04
Cliente 33 chegou no instante 49.51 minutos
Cliente 11 saiu do sistema no instante 49.53
Cliente 26 começou atendimento no caixa eletrônico no instante 49.53 após uma espera de 11.22
Cliente 22 saiu do sistema no instante 50.07
Cliente 28 começou atendimento no caixa eletrônico no instante 50.07 após uma espera de 8.62
Cliente 34 chegou no instante 51.21 minutos
Cliente 24 finalizou atendimento mas decide realizar outra operação no instante 51.93
Cliente 24 escolheu atendimento Interno no instante 51.93
Cliente 24 escolheu atendimento no guichê no instante 51.93
Cliente 24 começou atendimento no guichê no instante 51.93 após uma espera de 0.00
Cliente 29 começou atendimento no caixa eletrônico no instante 51.93 após uma espera de 8.64
Cliente 35 chegou no instante 52.41 minutos
Cliente 18 saiu do sistema no instante 53.29
Cliente 20 começou atendimento no caixa interno no instante 53.29 após uma espera de 23.36
Cliente 36 chegou no instante 53.56 minutos
Cliente 36 escolheu atendimento Interno no instante 53.56
Cliente 36 escolheu atendimento no caixa interno no instante 53.56
Cliente 37 chegou no instante 55.24 minutos
Cliente 38 chegou no instante 56.76 minutos
Cliente 38 escolheu atendimento Interno no instante 56.76
Cliente 38 escolheu atendimento no guichê no instante 56.76
Cliente 39 chegou no instante 58.37 minutos
Cliente 25 saiu do sistema no instante 59.39
Cliente 30 começou atendimento no caixa eletrônico no instante 59.39 após uma espera de 14.49
Cliente 29 finalizou atendimento mas decide realizar outra operação no instante 60.03
Cliente 31 começou atendimento no caixa eletrônico no instante 60.03 após uma espera de 13.41
Cliente 28 saiu do sistema no instante 60.15
Cliente 32 começou atendimento no caixa eletrônico no instante 60.15 após uma espera de 12.06
Cliente 40 chegou no instante 60.21 minutos
Cliente 40 escolheu atendimento Interno no instante 60.21
Cliente 40 escolheu atendimento no caixa interno no instante 60.21
Cliente 26 saiu do sistema no instante 60.44
Cliente 33 começou atendimento no caixa eletrônico no instante 60.44 após uma espera de 10.93
Cliente 41 chegou no instante 61.48 minutos
Cliente 27 saiu do sistema no instante 62.29
Cliente 38 começou atendimento no guichê no instante 62.29 após uma espera de 5.53
Cliente 42 chegou no instante 62.75 minutos
Cliente 23 saiu do sistema no instante 64.13
Cliente 20 saiu do sistema no instante 64.29
Cliente 36 começou atendimento no caixa interno no instante 64.29 após uma espera de 10.72
Cliente 43 chegou no instante 64.57 minutos
Cliente 44 chegou no instante 66.43 minutos
Cliente 45 chegou no instante 68.27 minutos
Cliente 45 escolheu atendimento Interno no instante 68.27
Cliente 45 escolheu atendimento no guichê no instante 68.27
Cliente 45 começou atendimento no guichê no instante 68.27 após uma espera de 0.00
Cliente 46 chegou no instante 69.56 minutos
Cliente 33 finalizou atendimento mas decide realizar outra operação no instante 69.62
Cliente 33 escolheu atendimento Interno no instante 69.62
Cliente 33 escolheu atendimento no caixa interno no instante 69.62
Cliente 34 começou atendimento no caixa eletrônico no instante 69.62 após uma espera de 18.41
Cliente 32 saiu do sistema no instante 70.21
Cliente 35 começou atendimento no caixa eletrônico no instante 70.21 após uma espera de 17.80
Cliente 47 chegou no instante 70.99 minutos
Cliente 31 saiu do sistema no instante 71.07
Cliente 37 começou atendimento no caixa eletrônico no instante 71.07 após uma espera de 15.83
Cliente 30 saiu do sistema no instante 71.12
Cliente 39 começou atendimento no caixa eletrônico no instante 71.12 após uma espera de 12.75
Cliente 48 chegou no instante 72.52 minutos
Cliente 48 escolheu atendimento Interno no instante 72.52
Cliente 48 escolheu atendimento no guichê no instante 72.52
Cliente 49 chegou no instante 73.65 minutos
Cliente 49 escolheu atendimento Interno no instante 73.65
Cliente 49 escolheu atendimento no caixa interno no instante 73.65
Cliente 24 saiu do sistema no instante 74.33
Cliente 48 começou atendimento no guichê no instante 74.33 após uma espera de 1.80
Cliente 36 saiu do sistema no instante 74.58
Cliente 40 começou atendimento no caixa interno no instante 74.58 após uma espera de 14.37
Cliente 50 chegou no instante 75.42 minutos
Cliente 39 saiu do sistema no instante 79.22
Cliente 29 começou atendimento no caixa eletrônico no instante 79.22 após uma espera de 19.19
Cliente 34 saiu do sistema no instante 79.35
Cliente 41 começou atendimento no caixa eletrônico no instante 79.35 após uma espera de 17.87
Cliente 37 saiu do sistema no instante 79.90
Cliente 42 começou atendimento no caixa eletrônico no instante 79.90 após uma espera de 17.15
Cliente 38 finalizou atendimento mas decide realizar outra operação no instante 81.03
Cliente 38 escolheu atendimento Interno no instante 81.03
Cliente 38 escolheu atendimento no caixa interno no instante 81.03
Cliente 35 saiu do sistema no instante 81.80
Cliente 43 começou atendimento no caixa eletrônico no instante 81.80 após uma espera de 17.23
Cliente 41 saiu do sistema no instante 87.83
Cliente 44 começou atendimento no caixa eletrônico no instante 87.83 após uma espera de 21.40
Cliente 40 saiu do sistema no instante 88.86
Cliente 33 começou atendimento no caixa interno no instante 88.86 após uma espera de 19.24
Cliente 48 saiu do sistema no instante 89.89
Cliente 42 saiu do sistema no instante 90.22
Cliente 46 começou atendimento no caixa eletrônico no instante 90.22 após uma espera de 20.66
Cliente 29 saiu do sistema no instante 91.21
Cliente 47 começou atendimento no caixa eletrônico no instante 91.21 após uma espera de 20.22
Cliente 43 finalizou atendimento mas decide realizar outra operação no instante 93.01
Cliente 50 começou atendimento no caixa eletrônico no instante 93.01 após uma espera de 17.59
Cliente 44 saiu do sistema no instante 97.10
Cliente 43 começou atendimento no caixa eletrônico no instante 97.10 após uma espera de 4.09
Cliente 45 saiu do sistema no instante 97.76
Cliente 33 saiu do sistema no instante 100.00
Cliente 49 começou atendimento no caixa interno no instante 100.00 após uma espera de 26.35
Cliente 50 saiu do sistema no instante 101.49
Cliente 46 saiu do sistema no instante 102.00
Cliente 47 saiu do sistema no instante 102.66
Cliente 43 saiu do sistema no instante 108.86
Cliente 49 saiu do sistema no instante 111.67
Cliente 38 começou atendimento no caixa interno no instante 111.67 após uma espera de 30.64
Cliente 38 saiu do sistema no instante 123.90



########## Dados da Simulação ###########


1. Tempo médio de espera em fila:
Caixa eletrônico: 9.93, com desvio padrão de 6.71
Caixa Interno: 14.71, com desvio padrão de 10.02
Guichê de Atendimento: 2.27, com desvio padrão de 2.36


2. Número médio de clientes em fila:
Caixa eletrônico: 3.63, com desvio padrão de 2.72
Caixa Interno: 0.96, com desvio padrão de 0.82
Guichê de Atendimento: 0.25, com desvio padrão de 0.48


3. Tempo de Médio de Resposta:
Caixa eletrônico: 10.23, com desvio padrão de 1.15
Caixa Interno: 12.07, com desvio padrão de 1.43
Guichê de Atendimento: 21.26, com desvio padrão de 4.21


4. Utilização média:
Caixa eletrônico: 0.84, com desvio padrão de 0.36
Caixa Interno: 0.94, com desvio padrão de 0.24
Guichê de Atendimento: 0.63, com desvio padrão de 0.48

