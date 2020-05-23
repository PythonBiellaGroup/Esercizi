from tamagotchi import Pet, Cat, Dog, Bird, Lab, Poodle, Tiger, Retriever, whichone, whichtype

def test_pet():
    p = Pet()
    assert p.name == "Kitty"
    assert p.hunger <= Pet.hunger_threshold
    assert p.boredom <= Pet.boredom_threshold
    assert 'Mrrp' in p.sounds

def test_pet_clock_tick():
    p = Pet()
    before_boredom = p.boredom
    before_hunger = p.hunger
    p.clock_tick()
    assert p.boredom == before_boredom + 1
    assert p.hunger == before_hunger + 1

def test_pet_mood():
    p = Pet()
    while p.hunger < Pet.hunger_threshold:
        p.clock_tick()
    assert p.mood() != "happy"

# Large task to cover all the cases!!!
# To BE CONTINUED...

# Test the new part (excercise)

# capsys to caputure "print" output; captured is a namedtuple with "out" and "err"
def test_tiger(capsys):
    t = Tiger()
    t.roar()
    captured = capsys.readouterr()
    assert captured[0] == 'ROOOOOAR!\n'

def test_retriever():
    r = Retriever()
    assert r.fetch() == 'I found the tennis ball! I can fetch anything!'