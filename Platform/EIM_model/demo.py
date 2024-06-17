import argparse
from EIM import EIM

def main():
    parser = argparse.ArgumentParser(description="EIM_model - Custom Python Library")
    parser.add_argument("-i", "--input", help="Specify input method")
    parser.add_argument("-c", "--cache", help="Specify cache method")
    parser.add_argument("-s", "--solution", help="Specify solution method")
    parser.add_argument("-o", "--output", help="Specify output method")
    parser.add_argument("-file", "--input_file", help="input_file", default="./files/input.txt")
    parser.add_argument("-set", "--input_set", help="input_set ", default="./files/set.json")
    args = parser.parse_args()
    input="What is AI？"
    input="Ali has four $10 bills and six $20 bills that he saved after working for Mr. James on his farm. Ali gives her sister half of the total money he has and uses 3/5 of the remaining amount of money to buy dinner. Calculate the amount of money he has after buying the dinner."
    # input="A bakery has 40 less than seven times as many loaves of bread as Sam had last Friday. If Sam had seventy loaves of bread last Friday, how many loaves of bread does the bakery have?"
    # input="There are forty apples in one box. Uncle Franky ordered two boxes of apples. He is planning to pack the apples with eight apples in one pack. How many packs of apples can he make with the two boxes of apples?"
    eim = EIM(input_method=args.input, cache_method=args.cache, solution_method=args.solution, output_method=args.output, input=input, input_file = args.input_file)
    result=eim.process()
    print("--------------")
    print("result type:",type(result))
    print("--------------")
    for i in result:
        print(i,":",result[i])


if __name__ == "__main__":
    main()

