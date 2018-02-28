'''Main file'''
import sys 
import urllib.request


def main(filename,N):
    lights = LightTester(N)
    instructions = parse_file(filename)
    for cmd in instruction:
        lights.apply(cmd)
        
    print("# occupied", light.count())

def file_exists(filename):
    '''Checks if a file exists in the local address or a network address that is given'''
    if filename.startswith('http://'):
        returned_file = urllib.request.urlopen(filename)
    else:
        returned_file = open(filename, 'r')
    return returned_file



class LightTester():
    
    lights = None
    
    def __init__(self,N):
        ''' LED grid has N x N number of lights. All lights start as off'''
        self.lights = [[False]*N for _ in range(N)]
        self.size = N
        
   
        
        
    
            

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
# 
#     def ignoring_commands(filename):
#     '''Ignore any commands which are not "turn on", "turn off" or "switch" '''
#     
#     def turn_on():
#     '''turns on lights given coordinates, if they are currently off'''
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