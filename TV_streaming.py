"""
Month to year ratio for tv streaming service pricing
"""


# monthly_price = int(input("How much do you pay a month for your service: $"))
# yearly_price = monthly_price * 12
# print(f"You pay ${yearly_price} per year for that service.")

# income = int(input("income: "))
# tax_rate = float(input("Tax rate: "))
# gross_income = income - (income * tax_rate)
# print(gross_income)

# age = int(input("Age: "))
# if age <= 5:
#     category = "baby"
# elif age <= 18:
#     category = "child"
# elif age <= 66:
#     category = "adult"
# else:
#     category = "old"
#
# print(f"Your age {age} is considered {category}")

# total_age = 0
#
# number_of_people = int(input("Number of people: "))
# for people in range(number_of_people):
#     age = int(input("Age: "))
#     total_age += age
# average_age = total_age / number_of_people
# print(f"total age: {total_age}\naverage age: {average_age}")

# total_age = 0  # Corrects the exit condition altering the total age
# number_of_people = 0
#
# age = int(input("Age: "))
# while age != -1:
#     total_age += age
#     number_of_people += 1
#     age = int(input("Age: "))
# average_age = total_age / number_of_people
# print(f"total age: {total_age}\naverage age: {average_age}")

# import random
#
# length = int(input("Length: "))
# random_length = random.randint(1, length)
# area = length * random_length
# print(f"Area of {length} * {random_length} is {area}.")

# def main():
#     number_of_rows = int(input("Number of rows: "))
#     number_of_columns = int(input("Number of columns: "))
#     print_grid(number_of_rows, number_of_columns)
#
#
# def print_grid(number_of_rows, number_of_columns):
#     for row in range(number_of_rows):
#         for column in range(number_of_columns):
#             print("*", end="")
#         print("")
#
#
# main()


# def main():
#     print_menu_options()
#     choice = str(input("Choice: ")).lower()
#     while choice != "q":
#         if choice == 'a':
#             print("Getting valid name...")
#             get_valid_name()
#         elif choice == 'b':
#             print("You chose option 2")
#         elif choice == 'c':
#             print("You chose option 3")
#         else:
#             print("Invalid option")
#         print_menu_options()
#         choice = str(input("Choice: ")).lower()
#
#
# def print_menu_options():
#     print("Welcome to the main menu... see options below\n"
#           "(a)name\n"
#           "(b)second\n"
#           "(c)third\n")
#
#
# def get_valid_name():
#     name = str(input("Name: "))
#     while name == "":
#         print("Invalid name.")
#         name = str(input("Name: "))
#     return name
#
#
# main()

def main():
    print_greeting()


def print_greeting():
    print("adfnawnda")


main()
