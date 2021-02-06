import os

def file_size():
    totale = 0
    cartella = os.getcwd()
    for file in os.listdir(cartella):
        totale += os.path.getsize(os.path.join(cartella, file))
    print(f"La somma delle dimensioni dei file presenti nella cartella '{cartella}' è: {(totale/1048576):.2f}MB")