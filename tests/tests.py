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



    
    
#def test_ignoring_commands():
    
#def test_turn_on():
    

#def test_turn_off():

    
#def test_within_region(filename):
       
