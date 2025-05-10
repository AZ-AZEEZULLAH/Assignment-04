## Get List


def get_list():
    lst = []

    val = input("Enter a value to add to the list: ")


    while val :
        lst.append(val)
        val = input("Enter a value to add to the list: ")

        print("Current list: ", lst)

if __name__ == "__main__":
    get_list()