## Add Many Number



def add_number(numbers) ->int:
    num : int = 0

    for number in numbers : 
        num += number
    return num


def add_numbers_2():
    numbers = [1, 2, 3, 4, 5]
    
    sum :int = add_number(numbers)
    return sum 

if __name__ == "__main__":
    print(add_numbers_2())