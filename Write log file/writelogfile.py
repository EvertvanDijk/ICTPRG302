""" (c) Evert van Dijk 2025
This example is to demonstrate how to create a log file to capture errors for badly entered data
"""

#creating the function that asks for arguments a and b expecting numbers (float)
def addnumbers(a,b):
    try: # Try to process
        result = float(a) + float(b)
        print(f"The result is: {result}") # Success
    except Exception as err: # if it fails
        with open('mynewlog.log', 'a') as f: # Open the log file, in this example it already exists
            f.write(f"error {err} caught\n") # write the error code
            f.write(f"the data entered was: {a}, {b}\n") # show the data that was entered. 

if __name__ == "__main__":
    # the next line will fail, check the data passed through
    print(f'I have added 5, bob for you, this is the result: {addnumbers(5,'bob')}') 

