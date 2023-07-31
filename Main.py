# INTERACT
# Main Project Hub
# By: Alex O'Brien

import Calculate
import GrabData
import pprint


def main():
    champDict = GrabData.setChamps()
    calculator = Calculate.Calculate(champDict)

    for obj in champDict.values():
        print(obj.statsAtLevel(4))


if __name__ == "__main__":
    main()
