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

        inp = input("Enter Input (x to exit): ")
        if inp == 'x':
            break

        #pprint.pprint(calculator.getData())
        #pprint.pprint(calculator.getByField("stats"))
        #pprint.pprint(calculator.sMax("hp"))
        pprint.pprint(calculator.sMin("armor"))


if __name__ == "__main__":
    main()
