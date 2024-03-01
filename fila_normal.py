class FilaNormal:
    codigo:int = 0
    fila = []
    clientesatendidos = []
    senhatual:str = ""

    def gerasenhaatual(self)->None:
        self.senhatual = f'NM{self.codigo}'

    #Tipagem de métodos, eu utilizo "->" e informo se ele retorna alguma info, se for None, significa que não tem return, ele apenas executa algo internamente
    def resetafila(self)->None:
        if self.codigo>=100:
            self.codigo=0
        else:
            self.codigo+=1

    def atualizafila(self)->None:
        self.resetafila()
        self.gerasenhaatual()
        self.fila.append(self.senhatual)

    def chamacliente(self, caixa:int)->str:
        cliente_atual:str = self.fila.pop()
        self.clientesatendidos.append(cliente_atual)
        return(f'Cliente Atual: {cliente_atual}, dirija-se ao caixa {caixa}')