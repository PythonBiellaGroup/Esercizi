from logic import *

people = ["Giovanni", "Berto", "Laura"]
houses = ["Beatiful", "Majestic", "Splendor"]
rooms=["204","305","406"]

symbols = []

knowledge = And()


for person in people:
    for room in rooms:
	    for house in houses:
	   
	        symbols.append(Symbol(f"{person}{room}{house}"))  

		
print(symbols)  

# Each person belongs to a house and to a room.
for person in people:
    knowledge.add(Or(
        Symbol(f"{person}Beatiful204"),
		Symbol(f"{person}Beatiful305"),
		Symbol(f"{person}Beatiful406"),
        Symbol(f"{person}Majestic204"),
		Symbol(f"{person}Majestic305"),
		Symbol(f"{person}Majestic406"),
        Symbol(f"{person}Splendor204"),
		Symbol(f"{person}Splendor305"),
        Symbol(f"{person}Splendor406"),
        
        
    ))


# Only one house per person.
for person in people:
    for h1 in houses:
        for h2 in houses:
            if h1 != h2:
                knowledge.add(
                    Implication(Symbol(f"{person}{h1}204"), Not(Symbol(f"{person}{h2}305")))
                )
                knowledge.add(
                    Implication(Symbol(f"{person}{h1}204"), Not(Symbol(f"{person}{h2}406")))
					                )
                knowledge.add(
                    Implication(Symbol(f"{person}{h1}305"), Not(Symbol(f"{person}{h2}204")))
                )
                knowledge.add(
                    Implication(Symbol(f"{person}{h1}305"), Not(Symbol(f"{person}{h2}406")))
                )
                knowledge.add(
                    Implication(Symbol(f"{person}{h1}406"), Not(Symbol(f"{person}{h2}204")))
                )
                knowledge.add(
                    Implication(Symbol(f"{person}{h1}406"), Not(Symbol(f"{person}{h2}305")))
                )
				

	
			
				
knowledge.add(
    Or(Symbol("GiovanniSplendor204"), Symbol("GiovanniMajestic204"))
)

knowledge.add(Or(Symbol("Giovanni305Splendor"),Symbol("Laura305Splendor"))
    
)

knowledge.add(Or(
    Symbol("Berto204Beatiful"), Symbol("Berto305Beatiful")))
knowledge.add(Or(	
	Symbol("Laura406Majestic"),Symbol("Laura406Splendor")))
	
	
print("prima di model_check")    

i=0
for symbol in symbols:
    i += 1
    print (i)
    if model_check(knowledge, symbol):
        print(i,symbol)