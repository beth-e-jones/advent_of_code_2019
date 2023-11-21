"""The Elves quickly load you into a spacecraft and prepare to launch.

At the first Go / No Go poll, every Elf is Go until the Fuel Counter-Upper. 
They haven't determined the amount of fuel required yet.

Fuel required to launch a given module is based on its mass. Specifically, to 
find the fuel required for a module, take its mass, divide by three, round 
down, and subtract 2.

What is the sum of the fuel requirements for all of the modules on your 
spacecraft?

Resources used
https://www.geeksforgeeks.org/floor-ceil-function-python/ [Accessed 20/11/23]

"""

import pandas as pd
import math

# Set datapath for the input data
DATAPATH = "adventofcode.com_2019_day_1_input.txt"

# Read in .txt file from the stored datapath
item_masses_df = pd.read_table(
    DATAPATH,
    # Avoid first item becoming column header
    header=None,
)

# Check data read in successfully
item_masses_df.head()

# Converts the first column in the dataframe to a list
item_masses_list = item_masses_df.iloc[:, 0].tolist()

def calculate_required_fuel(item_masses_list):
    """
    Takes a series of integers (masses of items) and calculates the fuel
    required to transport each item. Does this by dividing each integer by 3 
    (using the math.floor() function to round down if this is not a whole 
    number) and subtracts 2.  
    
    Parameters
    ----------
    item_masses_list : list
        This is an imported .txt file of integers representing the masses of
        items, converted into a list. 

    Returns
    -------
   sum(updated_masses_list): integer
        A summed total of all the fuel required, based on the calculations for 
        each individual items' mass.
    """
    # Perform calculation on every item in the list of masses
    fuel_list = []
    for mass in item_masses_list:
        # Follow calculates to determine fuel needed for each item
        fuel = (math.floor(mass / 3) - 2)
        # Appends the fuel required to the new list
        fuel_list.append(fuel)

    return sum(fuel_list)

"""Fuel itself requires fuel just like a module - take its mass, divide by three, 
round down, and subtract 2. However, that fuel also requires fuel, and that 
fuel requires fuel, and so on. Any mass that would require negative fuel should
instead be treated as if it requires zero fuel; the remaining mass, if any, 
is instead handled by wishing really hard, which has no mass and is outside the
scope of this calculation.

So, for each module mass, calculate its fuel and add it to the total. Then, 
treat the fuel amount you just calculated as the input mass and repeat the 
process, continuing until a fuel requirement is zero or negative."""
    
def calculate_fuel_for_fuel(item_masses_list):
    """_summary_

    Parameters
    ----------
    item_masses_list : list
        This is an imported .txt file of integers representing the masses of
        items, converted into a list.

    Returns
    -------
    sum(fuel_list): integer
        _description_
    """
    
    fuel_list = []
    for mass in item_masses_list:
        # Sets a list for an empty fuel total
        running_fuel_total = []
        # Set the mass to start
        last_mass = mass
        # Sets a default boolean value for requiring more fuel
        requires_more_fuel = True
        
        # While more fuel required, perform calculations on the fuel
        while requires_more_fuel == True:
            fuel = (math.floor(last_mass / 3) - 2)
           
           # if the fuel is below zero, no more fuel required for the item
            if fuel < 0:
                # Break the loop for the item
                requires_more_fuel = False
            # If fuel required is one or more, append it onto the running total 
            else:
                running_fuel_total.append(fuel)
                # Set the new last mass to be the fuel, to loop through
                last_mass = fuel
        # redefine each mass as original
        
        fuel_list.append(sum(running_fuel_total))
        
                
    return sum(fuel_list)


# Run the first function and print the result
print(f"The amount of fuel needed to transport the items is:",
    calculate_required_fuel(item_masses_list))

# Run the second function and print the result
print(f"The total amount of fuel required is:",
    calculate_fuel_for_fuel(item_masses_list))
