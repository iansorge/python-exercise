from movies import Movies

movies = Movies('./movies.txt')


#defining a method to list all the movie names
def list_names():
    for k in movies._movies:
        print(k["name"])

#defining a method to search for movies with a search term in their name
def search_names(term):
    for k in movies._movies:
        if term.lower() in k["name"].lower():
            print(k["name"])

#defining a method to search for movies with a search term in their cast list
def search_cast(term):
    actors = []
    for k in movies._movies:
        for j in k["cast"]:
            if term.lower() in j.lower():
                print(k["name"])
                print("['", j.strip(), "']")


#printing the menu options
print("q: quit")
print("sn: search movie names")
print("sc: search cast")
print("list: print all the movie names")

#storing the user's input in a  variable
menu_input = input()


#if the user enters 'list' list all the movie names
if menu_input == "list":
    list_names()
    print()

#if the user enters 'sn' prompt the user for a search term then search for movies with that term in their names
if menu_input == "sn":
    print("Enter a search term: ")
    search_term = input()
    search_names(search_term)
    print()

#if the user enters 'sc' prompt the user for a search term then search for movies with that term in their cast list
if menu_input == "sc":
    print("Enter a search term: ")
    search_term = input()
    search_cast(search_term)
    print()


#using a while loop to repeatedly prompt the user for input until they enter 'q'
while(menu_input != "q"):
    print("q: quit")
    print("sn: search movie names")
    print("sc: search cast")
    print("list: print all the movie names")
    menu_input = input()

    if menu_input == "list":
        list_names()
        print()
    if menu_input == "sn":
        print("Enter a search term: ")
        search_term = input()
        search_names(search_term)
        print()
    if menu_input == "sc":
        print("Enter a search term: ")
        search_term = input()
        search_cast(search_term)
        print()
