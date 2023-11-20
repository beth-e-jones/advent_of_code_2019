"""The Elves quickly load you into a spacecraft and prepare to launch.

At the first Go / No Go poll, every Elf is Go until the Fuel Counter-Upper. 
They haven't determined the amount of fuel required yet.

Fuel required to launch a given module is based on its mass. Specifically, to 
find the fuel required for a module, take its mass, divide by three, round 
down, and subtract 2.

For example:

For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 
2.
For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel 
required is also 2.
For a mass of 1969, the fuel required is 654.
For a mass of 100756, the fuel required is 33583.
The Fuel Counter-Upper needs to know the total fuel requirement. To find it, 
individually calculate the fuel needed for the mass of each module (your puzzle
input), then add together all the fuel values.

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
        # redefine each mass as original
        fuel = (math.floor(mass / 3) - 2)
        fuel_list.append(fuel)
        print(fuel_list)
    # Returns the sum of all items in the new list, following the calculations

    
    """ Part 2
Apparently, you forgot to include additional fuel for the fuel you just added.

Fuel itself requires fuel just like a module - take its mass, divide by three, 
round down, and subtract 2. However, that fuel also requires fuel, and that 
fuel requires fuel, and so on. Any mass that would require negative fuel should
instead be treated as if it requires zero fuel; the remaining mass, if any, 
is instead handled by wishing really hard, which has no mass and is outside the
scope of this calculation.

So, for each module mass, calculate its fuel and add it to the total. Then, 
treat the fuel amount you just calculated as the input mass and repeat the 
process, continuing until a fuel requirement is zero or negative.

"""
    # Calculate fuel necessary for fuel
    fuel_for_fuel_list = []
    for fuel in fuel_list:
        fuel_for_fuel = (math.floor(fuel / 3) - 2)
        fuel_for_fuel_list.append(fuel_for_fuel)
        print(fuel_for_fuel_list)
    
    total_fuel_required = sum(fuel_list) + sum(fuel_for_fuel_list)

    return total_fuel_required



calculate_required_fuel(range(9,52))
