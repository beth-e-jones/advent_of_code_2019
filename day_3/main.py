# %%
"""
Resources used: https://www.w3schools.com/python/ref_file_readlines.asp
"""

# %%
import pandas as pd

# %%
# Set input datapath
DATAPATH = "input.txt"

# %%
# Read each individual line of the txt file as a list
with open(DATAPATH) as f:
    lines = f.readlines()

# %%
# Set the wires to correspond with txt file lines    
WIRE_1 = lines[0].split(",")
WIRE_2 = lines[1].split(",")

# %%
def wire_journeys():
    """Plots the path of each wire, step by step

    Returns
    -------
    Wirepath_1: List of tuples
        This is the step-by-step route of the first wire based on directions
        provided (e.g., U23 is up 23 steps, L12 is left 12 steps). The tuples
        are the step-by-step movements.
    
    Wirepath_2: List of tuples
        This is the step-by-step route of the second wire based on directions
        provided. The tuples are the step-by-step movements.
    """
    # Set wire 1 x and y axes to 0, set the starting point of the path as 0,0
    wire_1_x_axis = 0
    wire_1_y_axis = 0
    wire_1_path=[(0,0)]
    
    # Set wire 2 x and y axes to 0, set the starting point of the path as 0,0
    wire_2_x_axis = 0
    wire_2_y_axis = 0
    wire_2_path=[(0,0)]

    # Calculate individual steps for wire 1
    for step in WIRE_1:
        if step[0] == "R": 
            """Identify using the input (index position removes the character
            at the beginning) and calculates points in the path for each 
            individual step in the set direction by adding on to the 0 x/y 
            axes starting point. Appends the step onto a list that contains 
            the full wire path. Range starts at 1 to avoid an entry where the
            path is stationary"""
            for wire_step in range(1, int(step[1:])+1):
                path_point = (wire_1_x_axis + wire_step,wire_1_y_axis) 
                wire_1_path.append(path_point)
            wire_1_x_axis += wire_step
        elif step[0]== "L": 
            for wire_step in range(1, int(step[1:])+1):
                # For movement to the left, calculated as 0 - number of steps
                path_point = (wire_1_x_axis - wire_step,wire_1_y_axis) 
                wire_1_path.append(path_point)
            wire_1_x_axis -= wire_step
        elif step[0] == "U":
            for wire_step in range(1, int(step[1:])+1):
                path_point = (wire_1_x_axis, wire_1_y_axis + wire_step) 
                wire_1_path.append(path_point)
            wire_1_y_axis += wire_step
        elif step[0] == "D":
            # For movement downward, calculated as 0 - number of steps
            for wire_step in range(1, int(step[1:])+1):
                path_point = (wire_1_x_axis, wire_1_y_axis - wire_step) 
                wire_1_path.append(path_point)
            wire_1_y_axis -= wire_step
            

    for step in WIRE_2:
        """Identify using the input (index position removes the character
            at the beginning) and calculates points in the path for each 
            individual step in the set direction by adding on to the 0 x/y 
            axes starting point. Appends the step onto a list that contains 
            the full wire pathRange starts at 1 to avoid an entry where the
            path is stationary"""
        if step[0] == "R":
            for wire_step in range(1, int(step[1:])+1):
                path_point = (wire_2_x_axis + wire_step,wire_2_y_axis) 
                wire_2_path.append(path_point)
            wire_2_x_axis += wire_step
        elif step[0]== "L": 
            # For movement to the left, calculated as 0 - number of steps
            for wire_step in range(1, int(step[1:])+1):
                path_point = (wire_2_x_axis - wire_step,wire_2_y_axis) 
                wire_2_path.append(path_point)
            wire_2_x_axis -= wire_step
        elif step[0] == "U":
            for wire_step in range(1, int(step[1:])+1):
                path_point = (wire_2_x_axis, wire_2_y_axis + wire_step) 
                wire_2_path.append(path_point)
            wire_2_y_axis += wire_step
        elif step[0] == "D":
            # For movement downward, calculated as 0 - number of steps
            for wire_step in range(1, int(step[1:])+1):
                path_point = (wire_2_x_axis, wire_2_y_axis - wire_step) 
                wire_2_path.append(path_point)
            wire_2_y_axis -= wire_step
    
    # Returns the list of tuples for each wire journey as function output        
    return wire_1_path, wire_2_path


# %%
# Call the function
wire_journeys()

#wire_1, wire_2 = wire_journeys()

# %%
def closest_shared_point():
    """Uses the two wire paths to identify where the wires intersect and 
    creates a list of points where the wires intersect. Then calculates the 
    Manhattan distance of all points and prints the lowest Manhattan distance.
    """
    
    # Use the outputs of the wire_journeys() function as inputs
    wire_1_path, wire_2_path = wire_journeys()
    
    # Generate list of shared set points by using set for both lists of points
    shared_points = set.intersection(set(wire_1_path), set(wire_2_path))
    
    #Create empty list of absolute distances
    list_absolute_distances = []
    
    # Calculate absolute value of the x and y axes for each point and sum them
    for point in shared_points:
        # Calculate Manhattan distances by summing the absolute values for x/y
        # axes for each point
        abs_distance = (abs(point[0]) + abs(point[1]))
        if abs_distance > 0:
        # Append the absolute distance for each point to the list of distances
            list_absolute_distances.append(abs_distance)
    
    # Identify lowest value from the list of absolute distances for each point
    min_abs_distance = min(list_absolute_distances)
    list_absolute_distances.sort
    
    # Print the dlosest intersection
    print(
        f"The closest intersection to the the central point is:", 
        {min_abs_distance}
    )
    

# %%

closest_shared_point()
# %%


# %%
