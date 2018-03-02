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
    test_startstop = grid.within_grid([-123,123],[2000,1200])
    assert test_startstop == ([0,123],[999,999])

def test_turn_on():
    '''test if area covered by given coordinates are converted to True'''
    test = LightTester(1000)
    #call the light tester class with N of size 1000
    test.turn_on([0,0],[100,100])
    # create a test area which has 101*101 lights on
    on = 0
    # going to count the lights on in this area, set count to 0
    for i in range (0, 1000):
        for j in range (0, 1000):
            #looping through each row and each columns in the grid
            if test.lights[i][j] == True:
                #if the test_grid function has returned true in one of these spaces, count it
                on += 1
    assert on == 10201
    # both counts should be = 101*101 = 10201
    
def test_turn_off():
    '''test if area covered by given coordinates are converted to False'''
    #same as test above for turn_on, just opposite
    test = LightTester(1000)
    test.turn_on([0,0],[100,100])
    off = 0
    for i in range (0, 1000):
        for j in range (0, 1000):
            if test.lights[i][j] == True:
                off += 1
    assert off == 10201
    # both counts should be = 101*101 = 10201

    
def test_switch():
    '''test if the switch function turns a true to a false and vice versa given cooridnates'''
    test = LightTester(1000)
    test.turn_on([0,0],[100,100])
    # run the same test as the test_turn_on, then call the function switch and see if all Trues have been reversed to false
    # check by counting all false in the 999 x 999 square
    test.switch([0,0],[100,100]) 
    switched = 0
    for i in range (0, 1000):
        for j in range (0, 1000):
            if test.lights[i][j] == False:
                switched += 1 
    assert switched == 1000000
    # 1000 * 1000 = 1000000
    
                             
def test_light_count():
    '''tests the light count function, runs turn_on function, then calls light_count to check if the counts are equal'''
    test = LightTester(1000)
    test.turn_on([0,0],[100,100])
    assert test.light_count() == 10201
    
  
    
    
    
    
    
    
