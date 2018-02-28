'''Main file'''

def main(filename,N):
    lights = LightTester(N)
    instructions = parse_file(filename)
    for cmd in instruction:
        lights.apply(cmd)
        
    print("# occupied", light.count())
    



class LightTester():
    
    lights = None
    
    def.__init__(self,N):
        self.lights = [[False]*size for _ in range(size)]
        
    def apply(self,cmd):
        if cmd is 'switch on':
            #do something to switch it off
        elif cmd is 'switch off':
            #do something to switch it on
        elif
            #insert other if statements for other scenarios
    
     def file_exists(filename):
    '''Checks if a file exists in the local address or a network address'''


    def ignoring_commands(filename):
    '''Ignore any commands which are not "turn on", "turn off" or "switch" '''
    
    def turn_on():
    '''turns on lights given coordinates, if they are currently off'''

     def turn_off():
     '''turns on lights given coordinates, if they are currently off'''
    
    
    def within_region(filename):
    '''Checks if coordinates given are outside grid, ignores points outside grid and lights up parts inside'''
           
        
    def count(self):
        return count
        #this should count the number of lights that are on