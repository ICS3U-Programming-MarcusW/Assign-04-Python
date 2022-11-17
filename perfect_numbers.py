#!/usr/bin/env python3
# Created By: Marcus Wehbi
# Date: Nov 11, 2022
# This program asks the user for a minimum and a maximum as a range
# It then displays all of the perfect numbers that are within that range

import os

# Function to find number of perfect numbers between range
def powerOf(num, exp):
    sum = 1
    for p_index in range(exp):
        sum *= num
    return sum


# Function to find number of perfect numbers between range
def isPerfect(p_num):
    # set sum to 0
    p_sum = 0
    # As long as index is less than num, execute inside loop
    for p_index in range(1, p_num):
        # If the remainder of num by index is 0, then add it to the sum
        if p_num % p_index == 0:
            p_sum += p_index
    # Return the boolean expression back to the if statement
    return p_num == p_sum


def isArmstrong(a_num):
    # Set sum and number of proper divisors variables to 0
    a_sum = 0
    a_nod = 0
    # Set the counter to the num
    a_counter = a_num
    # While loop to find number of digits
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
        a_sum += powerOf(a_digit, a_nod)
        # Divide the counter by 10
        a_counter = int(a_counter / 10)
    return a_num == a_sum


def main():
    # Get start of range for perfect numbers
    per_min_str = input("Input the starting range or number : ")
    # Get end of range for perfect numbers
    per_max_str = input("Input the ending range of number : ")
    try:
        # Convert the parameters to integers
        per_min = int(per_min_str)
        per_max = int(per_max_str)
    except Exception:
        print("Strings and decimals are not acceptable for this program.")
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
                    # Print if the numbers are perfect
                    print(per_counter)

    # ...........................................

    # Get start of range for armstrong numbers
    arm_min_str = input("Input the starting range or number : ")
    # Get end of range for armstrong numbers
    arm_max_str = input("Input the ending range of number : ")

    try:
        # Convert the parameters to integers
        arm_min = int(arm_min_str)
        arm_max = int(arm_max_str)
    except Exception:
        print("Strings and decimals are not acceptable for this program.")
    else:
        # Make sure the start isn't greater than the max
        if arm_min > arm_max:
            print("The start of the range must be less than the end.")
        # Otherwise. make sure neither numbers are negative
        elif arm_min < 0 or arm_max < 0:
            print("Negative numbers are not accepted.")
        else:
            # Otherwise continue program to find all armstrong numbers within range
            # For when the counter is less than or equal to the range max
            for arm_counter in range(arm_min, arm_max + 1):
                # Get the boolean expression from the isPerfect function
                if isArmstrong(arm_counter):
                    # Print if the numbers are perfect
                    print(arm_counter)


if __name__ == "__main__":
    main()
