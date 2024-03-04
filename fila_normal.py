from fila_base import FilaBase

from constants import CODIGO_NORMAL


class FilaNormal(FilaBase):
    def gera_senha_atual(self) -> None:
        self.senha_atual = f'${CODIGO_NORMAL}{self.codigo}'

    # Tipagem de métodos:
    # eu utilizo "->" e informo se ele retorna alguma info,
    # se for None, significa que não tem return,
    # ele apenas executa algo internamente

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual: str = self.fila.pop()
        self.clientes_atendidos.append(cliente_atual)
        return (f'Cliente Atual: {cliente_atual}, dirija-se ao caixa {caixa}')
