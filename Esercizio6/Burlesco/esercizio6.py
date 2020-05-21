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

    def total_population(self):
        population = 0
        for c in self.countries:
            population += c.population
        return population

    def __str__(self):
        ret_str = self.name
        for c in self.countries:
            ret_str = ret_str + "\n" + str(c)
        return ret_str