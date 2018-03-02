# this is the Main file
import sys 
import urllib.request
import re
from pip import commands


def file_exists(filename):
    '''Checks if a file exists in the local address or a network address that is given'''
    if filename.startswith('http://'):
        returned_file = urllib.request.urlopen(filename)
        contents_returned_file = returned_file.read().decode('utf-8') 
        #this reads the returned file and converts it into a string
    else:
        returned_file = open(filename, 'r')
        contents_returned_file = returned_file.read()
    return contents_returned_file


def string_convert(filename):
    '''takes the string returned from file_exists and filters out any responses that aren't turn on/off or switch, converts to one big array'''
    string = file_exists(filename)
    converted_string = re.findall(r".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*", string)
    return converted_string

def coordinates(string):
    '''takes in a string which is parsed from the output of string_convert and assigns coordinates to start and stop values, converts them to ints'''
    x = int(string[0])
    y = int(string[1])
    point = [x,y]
    return point

class LightTester():
    
    lights = []
    
    def __init__(self,N):
        ''' LED grid has N x N number of lights. All lights start as off'''
        #N will be defined in the main function when the LightTester is called.
        self.lights = [[False]*N for _ in range(N)]
        self.size = N
        
    def within_grid(self, start, stop):
        ''' this function checks if a stop or start point from instruction is within the size of the grid. If not, changes the value'''
        # use self.size -1 as its 1000*1000 square where the max value is 999
        
        if start[0] < 0:
            start[0] = 0
        if start[0] > self.size:
            start[0] = (self.size - 1)
            
        if start[1] < 0:
            start[1] = 0
        if start[1] > self.size:
            start[1] = (self.size - 1) 
        
        if stop[0] < 0:
            stop[0] = 0
        if stop[0] > self.size:
            stop[0] = (self.size - 1) 
            
        if stop[1] < 0:
            stop[1] = 0
        if stop[1] > self.size:
            stop[1] = (self.size - 1)
            
        return start, stop
    
    def turn_on(self, start, stop):
        '''turns on lights given the start and stop coordinates. True is on'''
        if start[0] <= stop[0] and start[1] <= stop[1]:
        #assumes that start points are below (to the left) of stop points of per assignment slides
            for i in range (start[0], (stop[0] + 1)):
                for j in range (start[1], (stop[1] + 1)):
                    self.lights[i][j] = True
                    
    def turn_off(self, start, stop):
        '''turns off lights given the start and stop coordinates. False is off'''
        if start[0] <= stop[0] and start[1] <= stop[1]:
        #assumes that start points are below (to the left) of stop points of per assignment slides
            for i in range (start[0], (stop[0] + 1)):
                for j in range (start[1], (stop[1] + 1)):
                    self.lights[i][j] = False
                    
    def switch(self, start, stop):
        '''checks to see if a light is on/off and switches it to off/on. Brings previous two functions together'''
        if start[0] <= stop[0] and start[1] <= stop[1]:
        #assumes that start points are below (to the left) of stop points of per assignment slides
            for i in range (start[0], (stop[0] + 1)):
                for j in range (start[1], (stop[1] + 1)):
                    if self.lights[i][j] == False:
                        self.lights[i][j] = True
                    else:
                         self.lights[i][j] = False
    
    def light_count(self):
        '''count all occurrences of true that after all commands have been dealt with by on off and switch function'''  
        count = 0
        #loop through all rows and columns and count Trues  
        start = [0,0]
        stop = [999,999] 
        for i in range (start[0], (stop[0] + 1)):
                for j in range (start[1], (stop[1] + 1)):
                    if self.lights[i][j] == True:
                        count +=1
        return count     
                  
                    
def main():
    if len(sys.argv) >= 3:     
        #index two of sys.argv is the file/http address
        commands_list = file_exists(sys.argv[2])
        # returns contents of file in a string
        commands_array = string_convert(filename)
        # converts that string to a structured array
        num_lights = commands_list.split('\n')[0]
        # this takes the first line of the commands, which is always the N number of lights in the grid
        lights = LightTester(num_lights)
        
        # now have number of lights and array with instructions
        # need to loop through each index and first extract the start and stop points
        # then extract the command, and call the relevant function using the stop and start points
        for i in range(0,num_lights):
            start_point = coordinates(commands_array[i][1:3]) 
            stop_point = coordinates(commands_array[i][3:5])
            command = commands_array[i][0]
             #The next three if statements call the necessary method with our start and stop points 
            if command == "turn on":
               lights.lightsturn_on(start_point, stop_point)                
            if command == "turn off":
                 lights.turn_off(start_point, stop_point)
            if command == "switch":
                 lights.switch(start_point, stop_point)
        
        #after these adjustments, need to count the lights which are on using the light_count function  
        print(lights.light_count())
        
    else:    
    # sys.argv is used to read arguments from the command line
        print("Please check parameters: third argument must be the input file") 
     
        
if __name__ == '__main__':
    main()
            

