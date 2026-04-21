calculation_to_hours = 24
name_of_unit = "hours"

def day_to_unit(num_of_days):
    return (f"{num_of_days} days are {num_of_days * calculation_to_hours} {name_of_unit}")

user_input = input("Enter the number of the day:\n")
user_input_number = int(user_input)

calculated_value = day_to_unit(user_input_number)
print(calculated_value)
