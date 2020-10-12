from logic import *
from itertools import product
from itertools import zip_longest
def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return zip_longest(fillvalue=fillvalue, *args)

people = ["Giovanni", "Berto", "Laura"]
hotels = ["Beautiful", "Majestic", "Splendor"]
rooms = ["204", "305", "406"]

symbols = []
knowledge = And()

#SYMBOLS
for p in people:
    for h in hotels:
        for r in rooms:
            print(f"Adding {p}{h}{r}")
            symbols.append(Symbol(f"{p}{h}{r}"))

#KNOWLEDGE BASE
#One person, one hotel, one room
all_cobinations = [[i, j, k] for i in people  
                             for j in hotels 
                             for k in rooms]
symb = []
for phr in all_cobinations:
    p = phr[0]
    h = phr[1]
    r = phr[2]
    symb.append((f"{p}{h}{r}"))

for a, b, c, d, e, f, g, h, i in grouper(symb, 9):
    print(f"OR {a} {b} {c} {d} {e} {f} {g} {h} {i}")
    knowledge.add(Or(
        Symbol(a),
        Symbol(b),
        Symbol(c),
        Symbol(d),
        Symbol(e),
        Symbol(f),
        Symbol(g),
        Symbol(h),
        Symbol(i)
    ))

#SBAGLIATO
# Each person stays in only one room
#for p in people:
#    for h in hotels:
#        print(f"OR {p}{h}204 {p}{h}305 {p}{h}406")
#        knowledge.add(Or(
#            Symbol(f"{p}{h}204"),
#            Symbol(f"{p}{h}305"),
#            Symbol(f"{p}{h}406")
#        ))


#SBAGLIATO        
# Each person belongs to a hotel
#for p in people:
#    for r in rooms:
#        print(f"OR {p}Beautiful{r} {p}Majestic{r} {p}Splendor{r}")
#        knowledge.add(Or(
#            Symbol(f"{p}Beautiful{r}"),
#            Symbol(f"{p}Majestic{r}"),
#            Symbol(f"{p}Splendor{r}")
#        ))

#Only one hotel per person.
#RIDONDANTE
for p in people:
    for h1 in hotels:
        for h2 in hotels:
            if h1 != h2:
                for r in rooms:
                    print(f"Implication {p}{h1}{r}, Not {p}{h2}{r}")
                    knowledge.add(
                        Implication(Symbol(f"{p}{h1}{r}"), Not(Symbol(f"{p}{h2}{r}")))
                    )

# Only one person per house.
# RIDONDANTE
for h in hotels:
    for p1 in people:
        for p2 in people:
            if p1 != p2:
                for r in rooms:
                    print(f"Implication {p1}{h}{r}, Not {p2}{h}{r}")
                    knowledge.add(
                        Implication(Symbol(f"{p1}{h}{r}"), Not(Symbol(f"{p2}{h}{r}")))
                    )

# Only one person per room
# RIDONDANTE
for h in hotels:
    for r1 in rooms:
        for r2 in rooms:
            if r1 != r2:
                for p in people:
                    print(f"Implication {p}{h}{r1}, Not {p}{h}{r2}")
                    knowledge.add(
                        Implication(Symbol(f"{p}{h}{r1}"), Not(Symbol(f"{p}{h}{r2}")))
                    )

# Specific from text
knowledge.add(
    print(f"AND GiovanniSplendor305")
    (Symbol("GiovanniSplendor305"))
)

                
knowledge.add(
    print(f"OR BertoBeautiful204 BertoBeautiful305 BertoBeautiful406")
    Or(Symbol("BertoBeautiful204"), Symbol("BertoBeautiful305"), Symbol("BertoBeautiful406"))
)


knowledge.add(
    print(f"OR LauraBeautiful406 LauraMajestic406 LauraSplendor406")
    Or(Symbol("LauraBeautiful406"), Symbol("LauraMajestic406"), Symbol("LauraSplendor406"))
)

for symbol in symbols:
    if model_check(knowledge, symbol):
        print(symbol)
