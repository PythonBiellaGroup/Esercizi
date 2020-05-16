class Country():
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area
    
    def is_larger(self, other_country):
        return self.area > other_country.area

    def population_density(self):
        return self.population / self.area

    def __str__(self):
        '''
        Rappresenta il valore di un oggetto, ma è più orientato all'utente finale.
        '''
        return f'{self.name} has a population of {self.population} and is {self.area} square km.'

    def __repr__(self):
        '''
        Metodo built-in utilizzato nella programmazione ad oggetti per rappresentare un oggetto come stringa. 
        Utilizzato principalmente per effettuare operazioni di debug.
        '''
        return f"Country('{self.name}', {self.population}, {self.area})"

class Continent():
    def __init__(self, name, countries):
        self.name = name
        self.countries = countries

    def __str__(self):
        ret_str = self.name
        for c in self.countries:
            ret_str = ret_str + "\n" + str(c)
        return ret_str

# To run test suite: pytest esercizio6.py

def test_country():
    canada = Country('Canada', 34482779, 9984670)
    assert canada.name == 'Canada'
    assert canada.population == 34482779
    assert canada.area == 9984670
  
def test_country_is_larger():
    canada = Country('Canada', 34482779, 9984670)
    usa = Country('United States of America', 313914040, 9826675)
    assert canada.is_larger(usa) == True
    assert usa.is_larger(canada) == False

def test_country_pop_density():
    canada = Country('Canada', 34482779, 9984670)
    assert canada.population_density() == 3.4535722262227995

def test_country_str():
    usa = Country('United States of America', 313914040, 9826675)
    assert str(usa) == "United States of America has a population of 313914040 and is 9826675 square km."

def test_country_repr():
    canada = Country('Canada', 34482779, 9984670)
    assert repr(canada) == "Country('Canada', 34482779, 9984670)"
    assert repr([canada]) == "[Country('Canada', 34482779, 9984670)]"

def test_continent():
    canada = Country('Canada', 34482779, 9984670)
    usa = Country('United States of America', 313914040,9826675)
    mexico = Country('Mexico', 112336538, 1943950)
    countries = [canada, usa, mexico]
    north_america = Continent('North America', countries)
    assert north_america.name == 'North America'

def test_contintent_str():
    canada = Country('Canada', 34482779, 9984670)
    usa = Country('United States of America', 313914040,9826675)
    mexico = Country('Mexico', 112336538, 1943950)
    countries = [canada, usa, mexico]
    north_america = Continent('North America', countries)
    assert str(north_america) == "North America\nCanada has a population of 34482779 and is 9984670 square km.\nUnited States of America has a population of 313914040 and is 9826675 square km.\nMexico has a population of 112336538 and is 1943950 square km."