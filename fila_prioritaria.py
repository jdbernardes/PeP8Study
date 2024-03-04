from fila_base import FilaBase


class FilaPrioritaria(FilaBase):
    codigo: int = 0
    fila = []
    clientes_atendidos = []
    senha_atual: str = ""

    def gera_senha_atual(self) -> None:
        self.senha_atual = f'PR{self.codigo}'

    def atualiza_fila(self) -> None:
        self.reseta_fila()
        self.gera_senha_atual()
        self.fila.append(self.senha_atual)

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual = self.fila.pop()
        self.clientes_atendidos.append(cliente_atual)
        return (f'Cliente Atual: {cliente_atual}, dirija-se ao caixa {caixa}')

    def estatistica(self, dia: str, agencia: int, flag: str) -> dict:
        if flag != 'detail':
            estatistica = {f'{agencia} - {dia}': len(self.clientes_atendidos)}
        else:
            estatistica = {}
            estatistica['dia'] = dia
            estatistica['agencia'] = agencia
            estatistica['clientes_atentidos'] = self.clientes_atendidos
            estatistica['quantidade_clientes_atendidos'] = (
                len(self.clientes_atendidos)
            )
        return estatistica
