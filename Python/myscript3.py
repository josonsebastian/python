import argparse

parser = argparse.ArgumentParser(description="Basic Math")
parser.add_argument("-n1", type=int, help="Integer 1")
parser.add_argument("-n2", type=int, help="Integer 2")
parser.add_argument("-n3", type=int, help="Integer 3")
parser.add_argument("Calculation", help="Math Operation", choices=["add", "sub", "multiply"])

args = parser.parse_args()

n1=int(args.n1)
n2=int(args.n2)
n3=int(args.n3)
result=None

if args.Calculation == "multiply":
	result = n1*n2*n3
elif args.Calculation == "add":
	result = n1+n2+n3
elif args.Calculation == "sub":
	result = n1-n2-n3
else:
	result = print("Incorrect Option")

print(f"Final result {result}")