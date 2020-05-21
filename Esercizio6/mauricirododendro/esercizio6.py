import country
#canada = Country('Canada', 34482779, 9984670)
#usa = Country('United States of America', 313914040,9826675)
#mexico = Country('Mexico', 112336538, 1943950)

#Define Continent with a constructor (method __init__) that has three parameters: a continent, its name, and its list of Country objects.
class Continent:
    def __init__(self,name,countries):
      self.name=name
      self.countries=countries
#method named total_population that returns the sum of the populations of the countries on this continent.
    def total_population(self):
        somma=0
        for i in self.countries:
            somma += i.population
        return somma
    def __str__(self):
        print(self.name)
        for i in self.countries:
            print(i)
canada = country.Country('Canada', 34482779, 9984670)

usa = country.Country('United States of America', 313914040,9826675)
mexico = country.Country('Mexico', 112336538, 1943950)
countries = [canada, usa, mexico]
north_america=Continent("North America",countries)
for country in north_america.countries:
    print(country)
print ("Total is ",str(north_america.total_population()))
