# SERBOI FLOREA-DAN 335CB

# importam acest modul pentru acces la parametri dati din linia de comanda
import sys


def compute_delta(pattern):
    
    delta = {}

    # starile sunt numerotate dupa lungimea prefixelor pattern-ului
    # initial, starea este 0, fiind corespunzatoare sirului vid
    # iar starea finala este chiar lungimea pattern-ului

    for state in range(len(pattern) + 1):
        for ch in range(65, 91):
            # daca litera este egala cu urmatorul caracter din pattern
            # inseamna ca ajungem intr-o stare 
            # corespunzatoare unui prefix cu o unitate mai lung
            if state != len(pattern) and chr(ch) == pattern[state]:
                delta[state, chr(ch)] = state + 1
            # altfel, caut subfixul de lungime maxima pentru prefixul curent
            # care concatenat cu caracterul curent e un prefix al pattern-ului
            else:
                # litera este primul caracter din pattern, pornesc din starea 1
                if chr(ch) == pattern[0]:
                    best_state = 1
                # altfel, din starea 0
                else:
                    best_state = 0
                idx = state - 1
                while idx >= 1:
                    if pattern[idx:state] + chr(ch) == pattern[0:state + 1 - idx]:
                        best_state = state + 1 - idx
                    idx = idx - 1
                delta[state, chr(ch)] = best_state

    return delta


def str_parser():
    
    # deschid fisierul de output
    output_file = open(output_filename, "w")

    # calculez matricea delta, 
    # reprezentata de un dictionar indexat cu perechi (stare, caracter)
    delta = compute_delta(string1)

    # initial sunt in starea 0
    current_state = 0

    # parcurg fiecare caracter din sirul in care se cauta pattern-ul
    # actualizand mereu starea curenta
    # cand ajung in starea finala, inseamna ca am gasit pattern-ul 
    # si scriu pozitia in fisier
    for i in range(len(string2)):
        current_state = delta[current_state, string2[i]]
        if current_state == len(string1):
            output_file.write(str(i - len(string1) + 1) + " ")

    output_file.write('\n')

    # inchid fisierul de output
    output_file.close()


if __name__ == '__main__':

    # extrag denumirile fisierelor de input si output date din linia de comanda
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    # deschid fisierul de input
    input_file = open(input_filename, "r")
    # citesc pattern-ul si string-ul in care se cauta
    string1 = input_file.readline().rstrip('\n')
    string2 = input_file.readline().rstrip('\n')
    # inchid fisierul de input
    input_file.close()

    # parcurg sirul in care se cauta si scriu pozitiile pattern-ului in fisier
    str_parser()
