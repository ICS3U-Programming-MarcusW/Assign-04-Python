#!/usr/bin/env python3
# Created By: Marcus Wehbi
# Date: Nov 11, 2022
# This program asks the user for a minimum and a maximum to create a range
# It then displays all of the perfect numbers that are within that range
# Then it asks the user for a second range
# It then displays all of the Armstrong numbers that are within that range


# Function to calculate the power of two numbers passed through from the isArmstrong function
# The number is raised to the number of digits in that number
def powerOf(num, exp):
    # Set sum to 1
    sum = 1
    # Use a for loop to calculate the power
    for p_index in range(exp):
        sum *= num
    # Return the sum to the Armstrong function
    return sum


# Function (calculator) to se if a number is perfect
def isPerfect(p_num):
    # set the perfect number sum to 0
    p_sum = 0
    # As long as index is less than num, execute the code inside loop
    for p_index in range(1, p_num):
        # If the remainder of the current number modulus p_index
        # (number that finds all proper divisors)
        # Is equal to zero, add it to the sum
        if p_num % p_index == 0:
            p_sum += p_index
    # Return the boolean expression back to the if statement in
    # The isPerfect function
    return p_num == p_sum


# Function (calculator) to se if a number is an Armstrong number
def isArmstrong(a_num):
    # Set sum and number of proper divisors variables to 0
    a_sum = 0
    a_nod = 0
    # Set the counter to the number
    a_counter = a_num
    # While loop to find the quantity of digits in a number
    # While the counter is not 0
    while a_counter != 0:
        # Increment the number of divisors by 1
        a_nod += 1
        # Divide counter by 10 (get rid of endmost digit)
        a_counter = int(a_counter / 10)

    # While loop to Calculate sum of all digits raised to number of base digits
    # While the counter is not 0
    # Reset the counter to the num
    a_counter = a_num
    while a_counter != 0:
        # Add the endmost digit raised to the power of
        # how many base digits there are, to the sum
        a_digit = a_counter % 10
        # Use the power function to calculate
        a_sum += powerOf(a_digit, a_nod)
        # Divide the counter by 10 to git rid of the endmost digit
        a_counter = int(a_counter / 10)
    # Return the boolean expression back to the if statement in
    # The isArmstrong function
    return a_num == a_sum


def main():
    # Explain what a perfect number is
    print(
        "In Mathematics, a perfect number is a postive integer that is equal to the sum of its proper divisors."
    )
    print(" ")
    # Get the start of the range for perfect numbers identifier
    per_min_str = input(
        "Input the starting number for the perfect number identification: "
    )
    # Get the end of the range for perfect numbers identifier
    per_max_str = input(
        "Input the ending number for the perfect number identification: "
    )
    try:
        # Convert the parameters (start/end) to integers
        per_min = int(per_min_str)
        per_max = int(per_max_str)
    # For invalid error, display message
    except Exception:
        print("Strings and decimals are not allowed in this program.")
    else:
        # Make sure the start isn't greater than the max
        if per_min > per_max:
            print("The start of the range must be less than the end.")
        # Otherwise. make sure neither numbers are negative
        elif per_min < 0 or per_max < 0:
            print("Negative numbers are not accepted.")
        # Otherwise continue program to find all perfect numbers within range
        else:
            print(
                "The Perfect numbers in the range "
                + per_min_str
                + " to "
                + per_max_str
                + " are :"
            )
            # For when the counter is less than or equal to the range max
            for per_counter in range(per_min, per_max + 1):
                # Get the boolean expression from the isPerfect function
                if isPerfect(per_counter):
                    # Print all numbers that are perfect
                    print(per_counter)

    # Explain what an Armstrong number is
    print(
        "An Armstrong number is a narcissistic number that is equal to the sum of its own digits raised to the power of the number of digits."
    )
    print(" ")

    # Get the start of the range for Armstrong numbers
    arm_min_str = input(
        "Input the starting number for the Armstrong number identification: "
    )
    # Get the end of the range for Armstrong numbers
    arm_max_str = input(
        "Input the ending number for the Armstrong number identification: "
    )

    try:
        # Convert the parameters to integers
        arm_min = int(arm_min_str)
        arm_max = int(arm_max_str)
    except Exception:
        print("Strings and decimals are not allowed in this program.")
    else:
        # Make sure the start isn't greater than the max
        if arm_min > arm_max:
            print("The start of the range must be less than the end.")
        # Otherwise, make sure neither numbers are negative
        elif arm_min < 0 or arm_max < 0:
            print("Negative numbers are not accepted.")
        # Otherwise continue program to find all armstrong numbers within range
        else:
            print(
                "The armstrong numbers in the range "
                + arm_min_str
                + " to "
                + arm_max_str
                + " are :"
            )
            # For when the counter is less than or equal to the range max
            for arm_counter in range(arm_min, arm_max + 1):
                # Get the boolean expression from the isArmstrong function
                if isArmstrong(arm_counter):
                    # Print if the numbers are Armstrong numbers
                    print(arm_counter)


if __name__ == "__main__":
    main()
