from main import (
    wire_journeys,
    closest_shared_point,
)

import pytest

# Set input datapath
DATAPATH = "day_3/input.txt"

# Read each individual line of the txt file as a list
with open(DATAPATH) as f:
    lines = f.readlines()

# Set the wires to correspond with txt file lines    
WIRE_1 = lines[0].split(",")
WIRE_2 = lines[2].split(",")

def test_wire_journeys():
    wire_1_path, wire_2_path = wire_journeys()
    result = wire_journeys()
    # check that result starts at 0,0
    assert (0,0) in result[0]
    
    assert (1,0) in wire_1_path
    
    # Test known plot point in wire 1
    assert (1005,0) in wire_1_path
    
    # Test known way point in wire 1
    assert (1005,1) in wire_1_path
    
    # Check another step we'll know from input - first movement of second step
    assert (1005, 0) not in wire_2_path
    
     # Test known plot point in wire 2 
    assert (-1003,0) in wire_2_path
    
    # Test known way point in wire 2 
    assert (-1003,-1) in wire_2_path
    
    # check that the two wire paths are not identical
    assert wire_1_path != wire_2_path
    
    # check a letter other than U,D,L, R can't be in the input
    assert "T" not in WIRE_1
    assert "E" not in WIRE_2
    
    # check wire paths length at least length of the input list?
    assert len(wire_1_path) > len(WIRE_1)
    assert len(wire_2_path) > len(WIRE_2)
    
def test_closest_shared_point():
    shared_points, min_abs_distance = closest_shared_point()
    
    # test the list of shared points has a length > 1
    assert len(shared_points) >= 1
          
    # check the min_abs_distance == 1211
    assert min_abs_distance == 1211
