from calculator import add, subtract, multiply, divide

def main():
    """Main function to demonstrate calculator operations."""
    a = 10
    b = 5
    print(f"Addition: {add(a, b)}")
    print(f"Subtraction: {subtract(a, b)}")
    print(f"Multiplication: {multiply(a, b)}")
    print(f"Division: {divide(a, b)}")

if __name__ == "__main__":
    main()