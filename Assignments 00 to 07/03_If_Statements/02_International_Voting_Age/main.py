## International Voting Age


from re import A


PETURKSBOUIPO_AGE : int = 16
STANLAU_AGE : int = 25
MAYENGUA_AGE : int = 48


AGE :int = int(input("Enter the age of the person: "))


def voting_age():

    if AGE >= PETURKSBOUIPO_AGE:
        print(f"Your age is {AGE} and you can vote in Peturksbouipo.")

    else:
        print(f"Your age is {AGE} and you cannot vote in Peturksbouipo.")

    if AGE >= STANLAU_AGE:
        print(f"Your age is {AGE} and you can vote in Stanlau.")
    else:
        print(f"Your age is {AGE} and you cannot vote in Stanlau.")

    if AGE >= MAYENGUA_AGE:
        print(f"Your age is {AGE} and you can vote in Mayengua.")
    else:
        print(f"Your age is {AGE} and you cannot vote in Mayengua.")

if __name__ == "__main__":
    voting_age()