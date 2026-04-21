calculation_to_hours = 24
name_of_unit = "hours"

def day_to_unit(num_of_days):
        return f"{num_of_days} days are {num_of_days * calculation_to_hours} {name_of_unit}"

def validate_and_execute():
    if user_input.isdigit():
        user_input_number = int(user_input)
        if user_input_number > 0:
            calculated_value = day_to_unit(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("You enter 0. Please enter a valid positive number.")
        else:
            print("Please enter a positive number.")
    else:
        print("You enter wrong input. We can't convert it to hours.")

user_input = input("Enter the number of the day:\n")
validate_and_execute()
