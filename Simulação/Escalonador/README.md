#Escalonador

Escalonador de um sistema com duas filas, onde a fila 1 possui prioridade sobre a fila 2, ou seja, os elementos da fila 2 só serão atendidos quando não houver elemento na fila 1. Para atendimento dos elementos, temos um servidor que atende apenas 1 elemento por vez.
Quando ocorre uma chegada de um elemento (seja da classe 1 ou 2) é observado se o servidor está livre, se sim, o mesmo logo é colocado no servidor para ser atendido, em caso negativo o elemento é colocado na sua respectiva fila.