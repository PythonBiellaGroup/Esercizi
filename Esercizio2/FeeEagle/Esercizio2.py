# Esercizio 2
# Autore: Pasquale
# Data: 20 aprile 2020

def CountWords():
    '''
    Funzione che conta le parole presenti in un file.txt
    e stampa a video un dizionario con le parole e le rispettive frequenze.
    Inoltre calcola il numero di parole, il numero di parole uniche e le
    parole con frequenza massima.
    '''
    
    answer = 'S'
    while answer == 'S':

        import os
        import re
        import chardet

        os.system('clear')

        print('')
        file_name = input(f'Inserisci il nome del file di testo: ')
        print('')

        lista_files = os.listdir()
        match = re.search('\\b'+file_name+'\\b', str(lista_files))

        if match:

            try:
                textraw = open(file_name, 'rb').read()
                encod = chardet.detect(textraw)
                text = open(file_name, 'r' , encoding = encod.get('encoding'))
                stringa_text = text.read()
            
                stringa_text_filtered = re.sub(r'[\.\,\'\[\]\"\?\!\*\:\;\n\-\(\)\{\}]', r' ', stringa_text, flags=re.MULTILINE).lower()
                lista_text_split = re.split(r'[\s]', stringa_text_filtered)
                lista_text_split = ' '.join(lista_text_split).split()

                unique_text_split = set(lista_text_split)
                dict_words = {}

                for words in unique_text_split : 
                        dict_words[words] = lista_text_split.count(words)

                dict_words_sorted = {k: v for k, v in sorted(dict_words.items(), key = lambda item: item[1])}
                print(dict_words_sorted)
                print('')
                print(f'Numero parole totali -> ', len(lista_text_split))
                print(f'Numero parole uniche -> ', len(unique_text_split))
                print('')
                print('Parole con frequenza massima:')
                print('')

                for k, v in dict_words_sorted.items():
                    if v == max(dict_words_sorted.values()):
                        print(k, ' -> ', v)

            except FileNotFoundError:
                print('Attenzione il file inserito non è presente!')

        else:
            print('')
            print('Attenzione il file inserito non è presente!')
            print('')

        print('')
        answer = input('Vuoi continuare? S/n: ')

CountWords()