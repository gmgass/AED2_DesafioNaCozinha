# CLASSE DA RECEITA
class Receita:
    def __init__(self, id, nome, tempo, nota):
        self.id = id
        self.nome = nome
        self.tempo = tempo
        self.nota = nota
        self.assinatura_original = self._gerar_assinatura()

    def _gerar_assinatura(self):
        return f"{self.nome} | {self.tempo} | {self.nota}"

    def verifica_assinatura(self):
        return self._gerar_assinatura() != self.assinatura_original
    
    def __str__(self):
        return f"[{self.id}] {self.nome} - {self.tempo} min. Avaliação: {self.nota}"


# TABELA DE RECEITAS
class TabelaHash:
    def __init__(self):
        self.tamanho = 10
        self.tabela = [[] for _ in range(self.tamanho)]

    def inserir(self, receita):
        indice = hash(receita.id) % self.tamanho
        self.tabela[indice].append(receita)

    def buscar_todas(self):
        todas = []
        for lista in self.tabela:
            todas.extend(lista)
        return todas


# BUSCA POR NOME
class Trie:
    def __init__(self):
        self.raiz = {}

    def inserir(self, nome, id_receita):
        nodo = self.raiz
        for letra in nome.lower():
            if letra not in nodo:
                nodo[letra] = {}
            nodo = nodo[letra]
        
        if "ids" not in nodo:
            nodo["ids"] = []
        nodo["ids"].append(id_receita)


# SISTEMA DA COZINHA DO JACQUIN
class CozinhaDoJacquin:
    def __init__(self):
        self.hash_table = TabelaHash()
        self.trie = Trie()

    def adicionar(self, receita):
        self.hash_table.inserir(receita)
        self.trie.inserir(receita.nome, receita.id)

    # MODO CHEF (Algoritmo Guloso)
    def montar_menu_guloso(self, tempo_max):
        receitas = self.hash_table.buscar_todas()
        receitas.sort(key=lambda r: (r.nota / r.tempo) if r.tempo > 0 else 0, reverse=True)
        
        menu = []
        tempo_gasto = 0
        
        for r in receitas:
            if tempo_gasto + r.tempo <= tempo_max:
                menu.append(r)
                tempo_gasto += r.tempo
                
        return menu, tempo_gasto

    # MODO INVESTIGAÇÃO
    def investigar(self):
        receitas = self.hash_table.buscar_todas()
        adulteradas = []
        
        for r in receitas:
            if r.verifica_assinatura():
                adulteradas.append(r)
                
        if not adulteradas:
            print("Jacquin feliz! Nenhuma receita foi adulterada.")
        else:
            for r in adulteradas:
                print(f"ALERTA: O Ratatouille alterou a receita '{r.nome}'  !")