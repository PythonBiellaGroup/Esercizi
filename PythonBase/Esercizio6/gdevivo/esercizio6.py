class Country():
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area
        
    def is_larger(self, c2):
        if isinstance(c2, Country):
            return self.area > c2.area
        else:
            print("Not country.")

    def population_density(self):
        return self.population / self.area

    def __repr__(self):
        return "Country(\'%s\', %s, %s)" % (self.name, self.population, self.area) 
    
    def __str__(self):
        return "%s has a population of %s and is %s square km." % (self.name, self.population, self.area)

class Continent():
    def __init__(self, name, clist):
        for c in clist:
            if not isinstance(c, Country):
                raise Exception(str(c)+" not country.")
        self.name = name
        self.clist = clist

    def add_country(self, name):
        if not isinstance(name, Country):
            print(str(name)+" not country.")
        else:
            self.clist.append(name)

    def rm_country(self, name):
        if name in self.clist:
            self.clist.remove(name)
        else:
            print(str(name)+" not in list.")

    def total_population(self):
        self.__total = 0
        for i in self.clist:
            self.__total += i.population
        return self.__total

    def __str__(self):
        self.__info=self.name
        for c in self.clist:
            self.__info += "\n%s has a population of %s and is %s square km." % (c.name, c.population, c.area)
        return self.__info

canada = Country('Canada', 34482779, 9984670)
usa = Country('United States of America', 313914040, 9826675)
print(canada.is_larger(usa))
print(canada.population_density())
print(usa)
print([usa])

countries = [canada, usa]
north_america = Continent('North America', countries)
for country in north_america.clist:
    print(country)

mexico = Country('Mexico', 112336538, 1943950)
north_america.add_country(mexico)

print(north_america.total_population())

print(north_america)
