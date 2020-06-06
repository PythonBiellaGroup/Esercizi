class Carta:
    SEMI = ["Fiori", "Quadri", "Cuori", "Picche"]
    # VALORI[0] è un valore arbitrario che non sarà mai usato
    VALORI = ["dummy", "Asso", "2", "3", "4", "5", "6", "7",
              "8", "9", "10", "Fante", "Donna", "Re"]

    def __init__(self, seme=0, valore=0):
        self.seme = seme
        self.valore = valore

    def __str__(self):
        return (self.VALORI[self.valore] + " di " + self.SEMI[self.seme])

    # Metodo privato utile per fare confronti tra carte
    # Arbitrariamente si da più importanza al seme
    def __cmp(self, other):
        # Controlla il seme
        if self.seme > other.seme:
            return 1
        if self.seme < other.seme:
            return -1
        # Se seme uguale, controlla il valore
        # Esercizio 8
        if (self.valore == 1 and other.valore == 1):
            return 0
        if self.valore == 1:
            return 1
        if other.valore == 1:
            return -1
        # Fine modifiche es. 8
        if self.valore > other.valore:
            return 1
        if self.valore < other.valore:
            return -1
        # Se ancora uguale, è un pareggio
        return 0

    def __eq__(self, other):
        return self.__cmp(other) == 0

    def __le__(self, other):
        return self.__cmp(other) <= 0

    def __ge__(self, other):
        return self.__cmp(other) >= 0

    def __gt__(self, other):
        return self.__cmp(other) > 0

    def __lt__(self, other):
        return self.__cmp(other) < 0

    def __ne__(self, other):
        return self.__cmp(other) != 0


class Mazzo:
    '''
    Mazzo di Carte
    '''

    def __init__(self):
        self.carte = []
        for seme in range(4):
            for valore in range(1, 14):
                self.carte.append(Carta(seme, valore))

    def __str__(self):
        s = ""
        for i in range(len(self.carte)):
            s = s + " " * i + str(self.carte[i]) + "\n"
        return s

    def visualizza_mazzo(self):
        for carta in self.carte:
            print(carta)

    def mischia(self):
        import random
        rng = random.Random()
        # Create a random generator
        num_carte = len(self.carte)
        # Metodo 2 più sintetico, equivalente a 1
        # rng.shuffle(self.carte)
        # Metodo 1
        for i in range(num_carte):
            j = rng.randrange(i, num_carte)
            # Scambio posizione tra carte usando tupla
            (self.carte[i], self.carte[j]) = (self.carte[j], self.carte[i])

    def rimuovi(self, carta):
        if carta in self.carte:
            self.carte.remove(carta)
            return True
        else:
            return False

    def pesca(self):
        # Anche se pesca dal fondo
        return self.carte.pop()

    def mazzo_vuoto(self):
        return self.carte == []
