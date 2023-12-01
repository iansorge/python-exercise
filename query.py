from movies import Movies

movies = Movies('./movies.txt')

def list_names():
    for k in movies._movies:
        print(k["name"])
    print("\n")


print("q: quit")
print("list: print all the movie names")
menu_input = input()

if menu_input == "list":
    list_names()

while(menu_input != "q"):
    print("q: quit")
    print("list: print all the movie names")
    menu_input = input()

    if menu_input == "list":
        list_names()
