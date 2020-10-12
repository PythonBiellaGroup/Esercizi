from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
knowledge0 = And(
    #Exclusive or between knight and kneave
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    # A says "I am both a knight and a knave."
    Implication(AKnight,And(AKnight, AKnave)),
    Implication(AKnave,Not(And(AKnight, AKnave)))
)

# Puzzle 1
knowledge1 = And(
    #Exclusive or between knight and kneave
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    # A says "We are both knaves."
    Implication(AKnight,And(AKnave, BKnave)),
    Implication(AKnave,Not(And(AKnave, BKnave)))
    # B says nothing.
)

# Puzzle 2
knowledge2 = And(
    #Exclusive or between knight and kneave
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    # A says "We are the same kind."
    Implication(AKnight,Or(And(AKnight, BKnight),And(AKnave, BKnave))),
    Implication(AKnave,Not(Or(And(AKnight, BKnight),And(AKnave, BKnave)))),
    # B says "We are of different kinds."
    Implication(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))),
    Implication(BKnave, Not(Or(And(AKnight, BKnave), And(AKnave, BKnight))))
)

# Puzzle 3
knowledge3 = And(
    #Exclusive or between knight and kneave
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    Or(CKnight, CKnave),
    Not(And(CKnight, CKnave)),
    # A says either "I am a knight." or "I am a knave.", but you don't know which.
    Implication(AKnight,Or(AKnight, AKnave)),
    Implication(AKnave,Not(Or(AKnight, AKnave))),
    # B says "A said 'I am a knave'."
    Implication(BKnight,AKnave),
    Implication(BKnave,Not(AKnave)),
    # B says "C is a knave."
    Implication(BKnight,CKnave),
    Implication(BKnave,Not(CKnave)),
    # C says "A is a knight."
    Implication(CKnight,AKnight),
    Implication(CKnave,Not(AKnight))
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
