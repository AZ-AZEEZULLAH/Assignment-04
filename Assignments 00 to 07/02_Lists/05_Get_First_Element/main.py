## Get First Element




def get_first_element(lst):


    if lst :
        print("First element is: ", lst[0])
    else:
        print("List is empty")



def get_list():
    lst = []

    element : str = input("Enter an element to add to the list  ")

    while element != "":
        lst.append(element)
        element = input("Enter an element to add to the list (or press Enter to finsh:) ")
        break 
    return lst
    
def main():
    lst = get_list()
    get_first_element(lst)

if __name__ == "__main__":
    main()
