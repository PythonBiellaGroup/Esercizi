from kanren import var, lall, lany, membero, eq, run
people = var()
rules = lall(
    # There are 3 people: Giovanni, Berto, Laura
    (eq, (var(), var(), var()), people),
    # Giovanni's house is Splendor or Majestic
    lany(
        (membero, ("Giovanni", "Splendor", var()), people),
        (membero, ("Giovanni", "Majestic", var()), people),
    ),
    # Room 305 is in Splendor house
    (membero, (var(), "Splendor", "305"), people),
    # Berto's house is Beatiful
    (membero, ("Berto", "Beatiful", var()), people),
    # Laura lives in room 406
    (membero, ("Laura", var(), "406"), people),
    # Who lives in house Majestic?
    (membero, (var(), "Majestic", var()), people),
    # Who lives in room 204?
    (membero, (var(), var(), "204"), people),
)
solutions = run(0, people, rules)
solution = list({tuple(sorted(s)) for s in solutions})[0]
for s in solution:
    print(*s)