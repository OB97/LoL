# INTERACT
# Main Project Hub
# By: Alex O'Brien

import Calculate
import pprint


def main():
    calculator = Calculate.Calculate()
    data = calculator.getData()

    # main loop
    while True:

        inp = input("Enter Champion Name (x to exit): ")
        if inp == 'x':
            break

        pprint.pprint(calculator.getMax("hp"))


if __name__ == "__main__":
    main()
