# this is the Main file
import sys 
import urllib.request
import re


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
    '''takes the string return from file_exists and filters out any responses that aren't turn on/off or switch'''
    string = file_exists(filename)
    clean_string = re.findall(r".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*", string)
    return clean_string

def coordinates(string):
    '''takes in a string which is parsed from the output of string_convert and assigns coordinates to start and stop values, converts them to ints'''
    start = int(string[0])
    end = int(string[1])
    point = [start,end]
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
                    
                    
                    
def main(filename,N):
    lights = LightTester(N)
    instructions = parse_file(filename)
    for cmd in instruction:
        lights.apply(cmd)
        
    print("# occupied", light.count())   

    
     
        
    
            

#===============================================================================
#         
#     def apply(self,cmd):
#         if cmd is 'switch on':
#             #do something to switch it off
#         #elif cmd is 'switch off':
#             #do something to switch it on
#        # elif
#             #insert other if statements for other scenarios
#     
# 
#     def ignoring_commands(filename):
#     '''Ignore any commands which are not "turn on", "turn off" or "switch" '''
#     
#     
# 
#      def turn_off():
#      '''turns on lights given coordinates, if they are currently off'''
#     
#     
#     def within_region(filename):
#     '''Checks if coordinates given are outside grid, ignores points outside grid and lights up parts inside'''
#            
#         
#     def count(self):
#         return count
#         #this should count the number of lights that are on
#===============================================================================