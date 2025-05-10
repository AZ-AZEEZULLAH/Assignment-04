## Second in Year



DAYS_PER_YEAR: int = 365
HOURS_PER_DAY: int = 24
MIN_PER_HOUR: int = 60
SEC_PER_MIN: int = 60



def seconds_in_year():
    seconds: int = DAYS_PER_YEAR * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MIN
    print(f"There are {seconds} seconds in a year.")
    

if __name__ == "__main__":
    seconds_in_year()