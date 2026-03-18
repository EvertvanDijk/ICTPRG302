""" (c) Evert van Dijk 2025
This example is to demonstrate how to create a log file to capture errors for badly entered data
"""
#in case we need to record the error
from datetime import datetime

#creating the function that asks for arguments a and b expecting numbers (float)
def addnumbers(a,b):
    try: # Try to process
        result = float(a) + float(b)
        return result
#        print(f"The result is: {result}") # Success
    except Exception as err: # if it fails
        # current date and time
        now = datetime.now() 
        date_time = now.strftime("%Y/%m/%d, %H:%M:%S")
        with open('mynewlog.log', 'a') as f: # Open the log file, in this example it already exists
            f.write(f"{date_time} error {err} caught\n") # write the error code
            f.write(f"the data entered was: {a}, {b}\n") # show the data that was entered. 
        return "Bad input data"

if __name__ == "__main__":
    # the next line will fail, check the data passed through
    print(f'I have added 5, 8 for you, this is the result: {addnumbers(5,8)}') 
    print(f'I have added 5, Bob for you, this is the result: {addnumbers(5,'Bob')}') 

