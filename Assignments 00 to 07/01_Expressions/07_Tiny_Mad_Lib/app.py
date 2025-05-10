### Tiny Mad Lib



def tiny_mad_lib():
    """
    This function generates a mad lib story based on user input.
    """

    noun1:str = input("Enter a noun: ")
    adjective:str = str (input("Enter an adjective: "))
    verb:str = str (input("Enter a verb: "))

    print(f"Do you {verb} your {adjective} {noun1}? That's hilarious!")
    
    
    
    
    
if __name__ == "__main__":
    tiny_mad_lib()