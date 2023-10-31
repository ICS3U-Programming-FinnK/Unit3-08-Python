#!/usr/bin/env python3
# Created by: Finn Kitor
# Created on: October 31st (halloween) 2023
# This program is a nested if statement about leap years


def main() -> None:
    # user inputs the leap year into the terminal
    leap_year = int(input("enter the leap year: "))
    print("")

    # the terminal will process if the user inputted a leap year
    if leap_year >= 2024:
        if leap_year < 2028:
            print("2024 is the upcoming leap year!.")
        else:
            print("2028 is the next upcoming leap year!.")
    else:
        print("error, not a leap year.")


if __name__ == "__main__":
    main()
