import termcolor

from logic import *

gio = Symbol("Giovanni")
ber = Symbol("Berto")
lau = Symbol("Laura")
characters = [gio, ber, lau]

dcq = Symbol("204")
tcc = Symbol("305")
qcs = Symbol("406")
rooms = [dcq, tcc, qcs]

spl = Symbol("Splendor")
maj = Symbol("Majestic")
bea = Symbol("Beautiful")
hotels = [spl, maj, bea]

symbols = characters + rooms + hotels


def check_knowledge(knowledge):
    for symbol in symbols:
        if model_check(knowledge, symbol):
            termcolor.cprint(f"{symbol}: YES", "green")
        elif not model_check(knowledge, Not(symbol)):
            print(f"{symbol}: MAYBE")


# There must be a person, room, and weapon.
knowledge = And(
    Or(gio, ber, lau),
    Or(dcq, tcc, qcs),
    Or(spl, maj, bea)
)

knowledge.add(And(
    spl, tcc
))

knowledge.add(And(
    ber, bea
))

knowledge.add(And(
    lau, qcs
))

check_knowledge(knowledge)
