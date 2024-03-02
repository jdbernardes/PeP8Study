from fila_normal import Filanormal
from fila_prioritaria import FilaPrioritaria

# fila_test = FilaNormal()
# fila_test.atualizafila()
# fila_test.atualizafila()
# fila_test.atualizafila()
# print(fila_test.chamacliente(12))
# print(fila_test.chamacliente(10))
# print(fila_test.chamacliente(2))

fila_test_2 = FilaPrioritaria()
fila_test_2.atualiza_fila()
fila_test_2.atualiza_fila()
fila_test_2.atualiza_fila()
print(fila_test_2.chama_cliente(10))
print(fila_test_2.chama_cliente(5))


print(fila_test_2.estatistica('10/01/1993', 215, 'detail'))
