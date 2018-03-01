'''This is the test file'''

import sys
sys.path.append('.')

from ledGrid.main import *

def test_file_exists():
    test_file = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_d.txt"
    # give a test file for testing. Will return error if it's not a real link
    assert file_exists(test_file) != None
    # as per practical, assert and call the function in main with test file
    # test that the result isn't empty
    
def test_string_convert():
    test_file = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_d.txt"
    output = string_convert(test_file) 
    assert output[0] == ('switch', '109', '360', '331', '987') 

def test_coordinates():
    test_string = ('109','360')
    output = coordinates(test_string)
    assert output == [109,360]

def test_within_grid():
    '''test check if coordinates for a start and stop point that are outside the grid, convert to 0 or the size of grid if they are less or more than those figures'''
    grid = LightTester(1000)
    test_startstop = ([-123,123],[2000,1200])
    assert test_startstop == ([0,123],[1000,1000])


    
    
#def test_ignoring_commands():
    
#def test_turn_on():
    

#def test_turn_off():

    
#def test_within_region(filename):
       
