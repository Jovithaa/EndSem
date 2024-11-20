import sys

def main():
    if len(sys.argv) != 4:
        print("Usage: python addition.py <num1> <num2> <op>")
        return

    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        op=sys.argv[3]
        if op=="add":
            print(f"The sum of is: {num1 + num2}")
        elif op=="sub":
            print(f"The diff is: {num1 - num2}")
        elif op=="mul":
            print(f"The prod is: {num1 * num2}")
        elif op=="div":
            print(f"The quotient is: {num1 / num2}")
    except ValueError:
        print("Error: Please provide valid numbers.")

if __name__ == "__main__":
    main()
