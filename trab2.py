class Elemento:
    def __init__(self, dado):
        self.dado = dado
        self.prox = None
        self.ant = None


class ListaDuplamenteEncadeada:
    def __init__(self):
        self.comeco = None
        self.final = self.comeco
        self.tamanho = 0

    def print_lista(self):
        if self.comeco == None:
            print("LISTA VAZIA")
        else:
            elemento_atual = self.comeco
            while elemento_atual != None:
                print(elemento_atual.dado, end=' ')
                elemento_atual = elemento_atual.prox
        print()

    def add(self, dado):
        new_elemento = Elemento(dado)
        if self.comeco == None:
            self.comeco = new_elemento
            self.final = self.comeco
            self.tamanho += 1
            return
        else:
            new_elemento.ant = self.final
            self.final.prox = new_elemento
            self.final = new_elemento
            self.tamanho += 1
            return

    def add_comeco(self, dado):
        new_elemento = Elemento(dado)
        if self.comeco == None:
            self.comeco = new_elemento
            self.final = self.comeco
            self.tamanho += 1
            return
        else:
            new_elemento.prox = self.comeco
            self.comeco.ant = new_elemento
            self.comeco = new_elemento
            self.tamanho += 1
            return

    def inserir_na_posicao(self, posicao, dado):
        if posicao == 0:
            self.add_comeco(dado)
            return
        if posicao >= self.tamanho:
            self.add(dado)
            return
        else:
            new_elemento = Elemento(dado)
            elemento_atual = self.comeco
            for c in range(posicao - 1):
                elemento_atual = elemento_atual.prox
            new_elemento.ant = elemento_atual
            new_elemento.prox = elemento_atual.prox
            elemento_atual.prox = new_elemento
            new_elemento.prox.ant = new_elemento
            self.tamanho += 1
            return

    def deleta_por_valor(self, dado):
        if self.comeco == None:
            print("Lista vazia, não há nada para deletar")
            return
        elemento_atual = self.comeco
        if elemento_atual.dado == dado:
            self.comeco = self.comeco.prox
            if self.comeco == None or self.comeco.prox == None:
                self.final = self.comeco
            if self.comeco != None:
                self.comeco.ant = None
            self.final -= 1
            return
        try:
            while elemento_atual != None and elemento_atual.prox.dado != dado:
                elemento_atual = elemento_atual.prox
            if elemento_atual != None:
                elemento_atual.prox = elemento_atual.prox.prox
                if elemento_atual.prox != None:
                    elemento_atual.prox.ant = elemento_atual
                else:
                    self.final = elemento_atual
                self.tamanho -= 1
                return
        except AttributeError:
            print("Valor nao encontrado")
            return

    def deleta_por_posicao(self, posicao):
        if self.comeco == None:
            print("Lista vazia, nao há nada para deletar")

        if posicao == 0:
            self.comeco = self.comeco.prox
            if self.comeco == None or self.comeco.prox == None:
                self.final = self.comeco
            if self.comeco != None:
                self.comeco.ant = None
            self.tamanho -= 1
            return

        if posicao >= self.tamanho:
            posicao = self.tamanho - 1

        elemento_atual = self.comeco
        for c in range(posicao - 1):
            elemento_atual = elemento_atual.prox
        elemento_atual.prox = elemento_atual.prox.prox
        if elemento_atual.prox != None:
            elemento_atual.prox.ant = elemento_atual
        else:
            self.final = elemento_atual
        self.tamanho -= 1
        return

    def deleta_ultimo(self):
        if self.comeco == None:
            print("Lista vazia, não há elementos para deletar")
            return
        if self.comeco.prox == None:
            self.comeco = None
            return
        elemento_atual = self.comeco
        while elemento_atual.prox != None:
            elemento_atual = elemento_atual.prox
        elemento_atual.ant.prox = None







def main():
    lista = ListaDuplamenteEncadeada()
    lista.print_lista()

    lista.add(5)
    lista.add(2)
    lista.add(9)
    lista.print_lista()

    lista.add_comeco(4)
    lista.print_lista()

    lista.inserir_na_posicao(2, 7)
    lista.print_lista()

    lista.deleta_por_valor(5)
    lista.print_lista()

    lista.deleta_por_posicao(1)
    lista.print_lista()

    lista.deleta_por_valor(5)
    lista.deleta_ultimo()
    lista.print_lista()


main()










