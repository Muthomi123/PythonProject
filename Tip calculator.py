def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    total_cost = dollars + tip
    print(f"Leave ${total_cost:.2f} including a ${tip:.2f} tip.")

def dollars_to_float(d):
    # Remove the leading '$' and convert to float
    return float(d[1:])

def percent_to_float(p):
    # Remove the trailing '%' and convert to float
    return float(p[:-1]) / 100

main()