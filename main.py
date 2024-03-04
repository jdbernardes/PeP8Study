from fila_normal import FilaNormal
from fila_prioritaria import FilaPrioritaria

fila_test = FilaNormal()
fila_test.atualiza_fila()
fila_test.atualiza_fila()
fila_test.atualiza_fila()
print(fila_test.chama_cliente(12))
print(fila_test.chama_cliente(10))
print(fila_test.chama_cliente(2))

fila_test_2 = FilaPrioritaria()
fila_test_2.atualiza_fila()
fila_test_2.atualiza_fila()
fila_test_2.atualiza_fila()
print(fila_test_2.chama_cliente(10))
print(fila_test_2.chama_cliente(5))


print(fila_test_2.estatistica('10/01/1993', 215, 'detail'))
