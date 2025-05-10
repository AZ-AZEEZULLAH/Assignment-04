## Shorten

MAX_LENGTH : int = 3


def shorten_list(lst):
    
    while len(lst) > MAX_LENGTH:
        last_element = lst.pop()
        print(f"Removed {last_element} from the list")



def get_list():
    lst = []
    element = input("Enter an element to add to the list :")
    while element != "":
        lst.append(element)
        element = input("Enter an element to add to the list : ")
        return lst 
    

def main():
    lst = get_list()
    print("Original list: ", lst)
    shorten_list(lst)
    print("Shortened list: ", lst)

if __name__ == "__main__":
    main()


