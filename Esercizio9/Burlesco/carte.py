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

    def distribuisci_carte(self, mani, num_carte=999):
        '''
        Metodo abbastanza generico perchè dipende dal tipo di gioco
        num_carte opzionale, se non è passato si distribuiscono tutte
        mani è una lista o tupla di oggetti Mano
        '''
        num_mani = len(mani)
        for i in range(num_carte):
            if self.mazzo_vuoto():
                break  # Esce se le carte sono finite
            carta = self.pesca()  # Prende la carta in cima
            mano = mani[i % num_mani]  # Di chi è il turno?
            mano.aggiungi(carta)  # Aggiunge la carta alla mano


class Mano(Mazzo):
    '''
    Mano di partita di carte
    '''
    def __init__(self, nome=""):
        self.carte = []
        self.nome = nome

    def __str__(self):
        s = "La mano di " + self.nome
        if self.mazzo_vuoto():
            s += " è vuota\n"
        else:
            s += " contiene\n"
        return s + Mazzo.__str__(self)

    def aggiungi(self, carta):
        self.carte.append(carta)


class ManoVecchiaZitella(Mano):
    '''
    Nel gioco VecchiaZitella gli accoppiamenti avvengono per valore e colore
    '''
    def rimuovi_accoppiamenti(self):
        contatore_accoppiamenti = 0
        # Copia delle carte per "percorrerla"; self.carte viene modificata
        carte_originali = self.carte[:]
        for carta in carte_originali:
            # SEMI = ["Fiori", "Quadri", "Cuori", "Picche"]
            # 3 - seme trasforma: Fiori (0) in Picche (3)
            # e Quadri (1) in Cuori (2)
            carta_gemella = Carta(3 - carta.seme, carta.valore)
            if carta_gemella in self.carte:
                self.carte.remove(carta)
                self.carte.remove(carta_gemella)
                print("Mano {0}: {1} si accoppia con {2}".format(
                      self.nome, carta, carta_gemella))
                contatore_accoppiamenti += 1
        return contatore_accoppiamenti


class ManoAsino(Mano):
    '''
    Nel gioco Asino gli accoppiamenti avvengono solo per valore
    '''
    def rimuovi_accoppiamenti(self):
        contatore_accoppiamenti = 0
        # Copia delle carte per "percorrerla"; self.carte viene modificata
        carte_originali = self.carte[:]
        for carta in carte_originali:
            # SEMI = ["Fiori", "Quadri", "Cuori", "Picche"]
            # 3 - seme trasforma: Fiori (0) in Picche (3)
            # e Quadri (1) in Cuori (2)
            carta_gemella = Carta(3 - carta.seme, carta.valore)
            if carta_gemella in self.carte:
                self.carte.remove(carta)
                self.carte.remove(carta_gemella)
                print("Mano {0}: {1} si accoppia con {2}".format(
                      self.nome, carta, carta_gemella))
                contatore_accoppiamenti += 1
        return contatore_accoppiamenti


class GiocoDiCarte:
    def __init__(self):
        self.mazzo = Mazzo()
        self.mazzo.mischia()


class VecchiaZitella(GiocoDiCarte):
    def gioca(self, nomi):
        # Rimuove la Regina di Fiori
        self.mazzo.rimuovi(Carta(0, 12))
        # Una mano per ciascun giocatore
        self.mani = []
        for n in nomi:
            self.mani.append(ManoVecchiaZitella(n))
        # Distribuisce tutte le carte tra i giocatori
        self.mazzo.distribuisci_carte(self.mani)
        print("---------- Carte distribuite")
        self.print_mani()
        # Gestisce accoppiamenti iniziali
        accoppiamenti = self.rimuovi_tutti_accoppiamenti()
        print("---------- Accoppiamenti effettuati, il gioco inizia...")
        self.print_mani()
        # Si gioca finchè tutte le 50 sono accoppiate
        turno = 0
        num_mani = len(self.mani)
        while accoppiamenti < 25:
            accoppiamenti += self.gioca_un_turno(turno)
            turno = (turno + 1) % num_mani
        print("---------- Game Over")
        self.print_mani()

    def rimuovi_tutti_accoppiamenti(self):
        contatore_accoppiamenti = 0
        for m in self.mani:
            contatore_accoppiamenti += m.rimuovi_accoppiamenti()
        return contatore_accoppiamenti

    def gioca_un_turno(self, i):
        if self.mani[i].mazzo_vuoto():
            return 0
        vicino = self.trova_vicino(i)
        carta_pescata = self.mani[vicino].pesca()
        self.mani[i].aggiungi(carta_pescata)
        print("Mano di", self.mani[i].nome, "pesca", carta_pescata)
        count = self.mani[i].rimuovi_accoppiamenti()
        self.mani[i].mischia()
        return count

    def trova_vicino(self, i):
        num_mani = len(self.mani)
        for next in range(1, num_mani):
            vicino = (i + next) % num_mani
            if not self.mani[vicino].mazzo_vuoto():
                return vicino

    def print_mani(self):
        # Esercizio 9.1
        for m in self.mani:
            print(m)


if __name__ == '__main__':
    game = VecchiaZitella()
    game.gioca(["Barbara", "Asbjorn", "Davide"])
