# Matemática discreta é o estudo de estruturas matemáticas que são fundamentalmente discretas, em contraste com as estruturas contínuas.
# Conjuntos são uma das estruturas fundamentais na matemática discreta. Um conjunto é uma coleção de objetos distintos.

# Definindo a classe SetCalculator
class SetCalculator:
    def __init__(self):
        # Inicializando os conjuntos como listas vazias
        # Em matemática discreta, um conjunto pode ser pensado como uma coleção de elementos distintos.
        self.setA = []
        self.setB = []

    # Método para adicionar elementos aos conjuntos
    def add_elements(self, set_name, elements):
        if set_name == 'A':
            self.setA.extend(elements)
            self.setA = list(set(self.setA))  # Removendo duplicatas
        elif set_name == 'B':
            self.setB.extend(elements)
            self.setB = list(set(self.setB))  # Removendo duplicatas

    # Método para calcular a união dos conjuntos
    # A união de dois conjuntos A e B é o conjunto de elementos que estão em A, em B, ou em ambos.
    def union(self):
        return list(set(self.setA + self.setB))

    # Método para calcular a interseção dos conjuntos
    # A interseção de dois conjuntos A e B é o conjunto de elementos que estão em ambos A e B.
    def intersection(self):
        return [value for value in self.setA if value in self.setB]

    # Método para calcular a diferença dos conjuntos (A - B)
    # A diferença de dois conjuntos A e B (denotada por A - B) é o conjunto de elementos que estão em A mas não estão em B.
    def difference(self):
        return [value for value in self.setA if value not in self.setB]

# Exemplo de uso:
calc = SetCalculator()
calc.add_elements('A', [1, 2, 3, 4])
calc.add_elements('B', [3, 4, 5, 6])
print("União: ", calc.union())
print("Interseção: ", calc.intersection())
print("Diferença (A - B): ", calc.difference())
