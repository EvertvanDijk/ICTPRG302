"""
(c) 2025 Evert
Calculon - is a a module that we will use to demonstrate the __main__ block in Python.
"""

# These are global variables for colour formatting on he command line.
RED = '\033[31m'
RESET = '\033[0m' # Resets to default color and formatting

def add(x, y):
    """Adds two numbers."""
    return x + y

def subtract(x, y):
    """Subtracts second number from first."""
    return x - y

def multiply(x, y):
    """Multiplies two numbers."""
    return x * y

def divide(x, y):
    """Divides first number by second."""
    try:
        return x / y
    except Exception as e:
        print(f"{RED}Error: {e}.{RESET}")



# now we will use the __main__ block to demonstrate how this module can be used directly
if __name__ == "__main__":
    # Example usage of the module functions
    print("Welcome to Calculon!")
    a = 10
    b = 5
    print(f"Adding {a} and {b}: {add(a, b)}")
    print(f"Subtracting {b} from {a}: {subtract(a, b)}")
    print(f"Multiplying {a} and {b}: {multiply(a, b)}")
    print(f"Dividing {a} by {b}: {divide(a, b)}")
""" 
This block will only execute if the script is run directly, 
not when imported as a module.
This allows for testing or demonstration of the module's functionality.
"""