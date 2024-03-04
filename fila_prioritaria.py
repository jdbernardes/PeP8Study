from typing import Dict, List, Union


from fila_base import FilaBase
from constants import CODIGO_PRIORITARIO


class FilaPrioritaria(FilaBase):

    def gera_senha_atual(self) -> None:
        self.senha_atual = f'${CODIGO_PRIORITARIO}{self.codigo}'

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual = self.fila.pop()
        self.clientes_atendidos.append(cliente_atual)
        return (f'Cliente Atual: {cliente_atual}, dirija-se ao caixa {caixa}')

    def estatistica(self, dia: str, agencia: int, retorna_estatistica) -> dict:
        estatistica = retorna_estatistica(dia, agencia)

        return estatistica.roda_estatistica(self.clientes_atendidos)
