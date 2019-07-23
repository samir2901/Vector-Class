'''
Vector Class in python for doing vector math.
Vector2 is for making 2-D vectors.
'''
from math import *

class Vector:
    
    #initialising the vector
    def __init__(self,x=0,y=0,z=0):
        self.x = x
        self.y = y
        self.z = z

    def showVector(self):
        print((self.x,self.y,self.z))  #prints the vector as a tuple
    
    def mag(self):
        return sqrt(self.x**2 + self.y**2 + self.z**2)  #returns the magnitude of the vector

    

    def add(self,v):    #adds two vectors and assigns the value to self
        self.x = self.x + v.x
        self.y = self.y + v.y
        self.z = self.z + v.z
        
    def sub(self,v):    #subtracts two vectors and assigns the value to self
        self.x = self.x - v.x
        self.y = self.y - v.y
        

    def mul(self,k):    #multiplies the vector with a scalar
        self.x *= k
        self.y *= k 
    
    def div(self,k):    #divides each component with a scalar value
        self.x /= k
        self.y /= k

    def dot(self,v):
        return self.x*v.x + self.y*v.y      #gives the dot product of a vector

    def cross(self,v):
         a = self.y*v.z - self.z*v.y
         b = v.x*self.z - self.x*v.z
         c = self.x*v.y - self.y*v.x
         return Vector(a,b,c)

    def dir_x(self):
        pass


v1 = Vector(1,1,1)
v2 = Vector(1,1,1)
z = v1.cross(v2)
z.add(v1)
z.showVector()










