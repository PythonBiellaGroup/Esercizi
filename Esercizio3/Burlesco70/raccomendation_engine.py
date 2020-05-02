# Raccomendation engine
import csv
from math import sqrt
import argparse
import logging

# Gets or creates a logger
logger = logging.getLogger("raccomendation_engine")  
# Set log level
# DEBUG: Detailed information, for diagnosing problems. Value=10.
# INFO: Confirm things are working as expected. Value=20.
# WARNING: Something unexpected happened, or indicative of some problem. But the software is still working as expected. Value=30.
# ERROR: More serious problem, the software is not able to perform some function. Value=40
# CRITICAL: A serious error, the program itself may be unable to continue running. Value=50
logger.setLevel(logging.DEBUG)

# define file handler and set formatter
file_handler = logging.FileHandler('logfile.log')
formatter    = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
file_handler.setFormatter(formatter)

# define stream handler
stream_handler = logging.StreamHandler()
stream_formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s')
stream_handler.setFormatter(stream_formatter)

# add file handlers to logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

class ReccomendationEngine():

    LISTA_PRODOTTI = ['patata','carota','sedano','broccolo','verza']
    

    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.__dizionario_clienti = {}
        self.__dizionario_clienti_dizionario_prodotti = {}
        #Crea dizionari da csv
        logger.info(f"Si elabora il file {self.csv_file}")
        with open(self.csv_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                #print(type(row))
                # Creo dizionario con chiave id cliente e valore la lista degli altri attributi
                self.__dizionario_clienti[row['ID_Cliente']]=[ row['sesso_M'], row['sesso_F'],
                                              row['patata'],row['carota'],
                                              row['sedano'], row['broccolo'], row['verza'] ]
                # Il valore del dizionario è un altro dizionario con chiave prodotto
                self.__dizionario_clienti_dizionario_prodotti[row['ID_Cliente']]={ 'patata': row['patata'],
                                                                                    'carota': row['carota'],
                                                                                    'sedano': row['sedano'],
                                                                                    'broccolo': row['broccolo'], 
                                                                                    'verza': row['verza'] }
        #print(self.__dizionario_clienti)
        #print(self.__dizionario_clienti_dizionario_prodotti)                                                                                    

    def __suggerisci_prodotto(self, prodotti_a, prodotti_b):
        for p in self.LISTA_PRODOTTI:
            #print(p, prodotti_a[p], prodotti_b[p])
            if int(prodotti_a[p]) and int(prodotti_b[p]):
                #print(f"Prodotto {p} presente in entrambi i clienti")
                pass
            elif int(prodotti_a[p]) and not int(prodotti_b[p]):
                logger.info(f"Prodotto {p} presente solo nel primo cliente")
            elif int(prodotti_b[p]) and not int(prodotti_a[p]):
                logger.info(f"Prodotto {p} presente solo nel secondo cliente")

    def __distanza_euclidea(self, lista_a, lista_b):
        # Unico controllo di congruenza, in realtà ne servirebbero tantissimi
        if len(lista_a) != len(lista_b):
            logger.error("Le liste di valori devono avere stessa lunghezza")
            raise ValueError("Le liste di valori devono avere stessa lunghezza")
        de = 0
        for i in range(len(lista_a)):
            de += (int(lista_a[i]) - int(lista_b[i]))**2
        #print(de)
        return sqrt(de)

    def raccomanda(self, cliente):
        ''' Cliente è il cliente con il quale calcolare distanza e suggerire '''
        logger.info(f"Si cerca il cliente più simile a {cliente}")
        # Inizializza i minimi: indice del cliente (mcli), distanza euclidea (mde)
        mcli = None
        mde = 1000000 #Un valore grande a piacere
        # Calcola la distanza euclidea con gli altri clienti
        for cli in self.__dizionario_clienti.keys():
            if cli != cliente:
                c, d = cli, self.__distanza_euclidea(self.__dizionario_clienti[cli], 
                                                     self.__dizionario_clienti[cliente])
                # Aggiorno il minimo
                if d < mde:
                    mcli, mde = c, d
        logger.info(f"Il cliente più vicino a {cliente} è {mcli}, con una distanza euclidea di {mde:.2f}")
        self.__suggerisci_prodotto(self.__dizionario_clienti_dizionario_prodotti[mcli], 
                                   self.__dizionario_clienti_dizionario_prodotti[cliente])

def main():
    parser = argparse.ArgumentParser(description="Reccomendation engine from csv file")
    parser.add_argument('csv_file', action="store", nargs="?", default="cli-prod.csv")
    parser.add_argument('cliente', action="store", nargs="?", choices=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'Z'], default="Z")
    args = parser.parse_args()
    logger.debug(f"Main called with parameters {args.csv_file} and {args.cliente}")
    re = ReccomendationEngine(args.csv_file)
    re.raccomanda(args.cliente)

if __name__ == '__main__': 
    main()