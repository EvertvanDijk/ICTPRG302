""" 
(c) Evert 2025
this application calls calculon.py to demonstrate the __main__ block in Python.

"""
#importing the calculon module to use its functions
import calculon
"""
we can also use 
from calculon import add
"""

print (f"Adding 5 and 10:  {calculon.add(5, 10)}")

print (f"removing 5 from 10:  {calculon.subtract(10, 5)}")

print (f"Dividing 5 and 10:  {calculon.divide(5, 10)}")

print (f"Dividing 5 and 0:  {calculon.divide(5, 0)}")

print (f"Multiplying 5 and 10:  {calculon.multiply(5, 10)}")
