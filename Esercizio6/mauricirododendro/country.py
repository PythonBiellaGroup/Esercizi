class Country:
    def __init__(self,name,population,area):
        self.name=name
        self.population=population
        self.area=area
    def is_larger(self,other):
        if self.area>other.area:
            return self.area
        elif self.area<other.area:
            return other.area
        else:
            return 1
    def population_density(self):
        return(self.population/area)
    def __str__(self):
        return self.name + " has a population of " + str(self.population) + " and is " + str(self.area) + " square km"
    def __repr__(self):
        return "Country({}, {},{})".format(self.name, self.population,self,area)
canada = Country('Canada', 34482779, 9984670)
usa = Country('United States of America', 313914040,9826675)
mexico = Country('Mexico', 112336538, 1943950)
print (canada)
