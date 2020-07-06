import csv
import sys


from util import Node, StackFrontier, QueueFrontier
f=open("frontieranodieplorati.txt","w")
g=open("names.txt","w")
h=open("movies.txt","w")
l=open("people.txt","w")
# Maps names to a set of corresponding person_ids
names = {}

# Maps person_ids to a dictionary of: name, birth, movies (a set of movie_ids)
people = {}

# Maps movie_ids to a dictionary of: title, year, stars (a set of person_ids)
movies = {}


def load_data(directory):
    """
    Load data from CSV files into memory.
    """
    # Load people
    with open(f"{directory}/people.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            people[row["id"]] = {
                "name": row["name"],
                "birth": row["birth"],
                "movies": set()
            }
            if row["name"].lower() not in names:
                names[row["name"].lower()] = {row["id"]}
            else:
                names[row["name"].lower()].add(row["id"])
    print ('1',names)
    g.write(str(names))
    
    # Load movies
    with open(f"{directory}/movies.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies[row["id"]] = {
                "title": row["title"],
                "year": row["year"],
                "stars": set()
            }

    # Load stars
    with open(f"{directory}/stars.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                people[row["person_id"]]["movies"].add(row["movie_id"])
                movies[row["movie_id"]]["stars"].add(row["person_id"])
            except KeyError:
                pass
				
    print ('2',movies)
    h.write(str(movies))
    print ('3',people)
    l.write(str(people))

def main():
    if len(sys.argv) > 2:
        sys.exit("Usage: python degrees.py [directory]")
    directory = sys.argv[1] if len(sys.argv) == 2 else "small"

    # Load data from files into memory
    print("Loading data...")
    load_data(directory)
    print("Data loaded.")
    source0=input( "Name ")
    #print (source0)
    source = person_id_for_name(source0)
    if source is None: 
        sys.exit("Person not found.")
    #print ("1")	
    target = person_id_for_name(input("Name: "))
    if target is None:
	    
        sys.exit("Person not found.")
    
    path = shortest_path(source, target)
    print ('path ',path)
    if path is None:
        print ("Not connected.")
    else:
        degrees = len(path)
        print(f"{degrees} degrees of separation.")
        path = [(None, source)] + path
        for i in range(degrees):
            person1 = people[path[i][1]]["name"]
            person2 = people[path[i + 1][1]]["name"]
            movie = movies[path[i + 1][0]]["title"]
            print(f"{i + 1}: {person1} and {person2} starred in {movie}")


def shortest_path(source, target):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target.

    If no possible path, returns None.
    """
  
    frontier = QueueFrontier()
    frontier.add(Node(source, None, None))
    
    
    #print ("frontier",frontier)
    nodesExplored = set()
    if source == target:
        raise Exception("Can't choose the same actor twice!")
    while True:
        if frontier.empty():
            return None
        node = frontier.remove()
        f.write("rimosso ")
        f.write(str(node.state))
        f.write('\n')
        #print ("\n rimosso ",node)
        #print ("frontier-remove",node.state)
        if node.state == target:
            solutions = []
            while node.parent is not None:
                solutions.append((node.action, node.state))
                node = node.parent
            solutions.reverse()
            return solutions
        nodesExplored.add(node.state)
        #print (nodesExplored)
        #print (5*"-------","nodesexplored",nodesExplored)
        f.write("nodesexplored ")
        f.write(str(nodesExplored))
        f.write('\n')
        for movie_id, person_id in neighbors_for_person(node.state):
            if not (person_id in nodesExplored):
                child = Node(person_id, node, movie_id)
                #print (child.state)
                frontier.add(child)
                #print ('len',len (frontier.frontier))
                f.write("lunghezza frontiera ")
                f.write(str(len (frontier.frontier)))
                f.write('\n')
                for i in range(len(frontier.frontier)):
                  #print (i,' ',frontier.frontier[i].state)
                  f.write (str(i))
                  f.write (' ')
                  f.write (str(frontier.frontier[i].state))
                  f.write ('\n')
                #print ('stop')
                
        #print ("frontier",frontier.frontier)
    # TODO
    #raise NotImplementedError


def person_id_for_name(name):
    """
    Returns the IMDB id for a person's name,
    resolving ambiguities as needed.
    """
    #print (names[name.lower()])
    #print(names.get(name.lower()))
    person_ids = list(names.get(name.lower(),set()))
    
    if len(person_ids) == 0:
        return None
    elif len(person_ids) > 1:
        print(f"Which '{name}'?")
        for person_id in person_ids:
            person = people[person_id]
            name = person["name"]
            birth = person["birth"]
            print(f"ID: {person_id}, Name: {name}, Birth: {birth}")
        try:
            person_id = input("Intended Person ID: ")
            if person_id in person_ids:
                return person_id
        except ValueError:
            pass
        return None
    else:
        return person_ids[0]


def neighbors_for_person(person_id):
    """
    Returns (movie_id, person_id) pairs for people
    who starred with a given person.
    """
    movie_ids = people[person_id]["movies"]
    neighbors = set()
    for movie_id in movie_ids:
        for person_id in movies[movie_id]["stars"]:
            neighbors.add((movie_id, person_id))
    #print(neighbors)        
    return neighbors


if __name__ == "__main__":
    main()
