# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 10:26:52 2019

@author: Dmytro_Kushchov
"""
class Tank:
    def __init__(self, x, y, side) :
        self.x = x;
        self.y = y;
        self.side = side;
        
    def __str__(self) :
        print('Tank x - {} y - {}'.format(self.x, self.y));
    

class Eagle:
    def __init__(self, x, y, side) :
        self.x = x;
        self.y = y;
        self.side = side;
    
    def __str__(self) :
        print('Eagle x - {} y - {}'.format(self.x, self.y));

class Bullet:
    def __init__(self, x, y, ax = 0, ay = 0) :
        self.x = x;
        self.y = y;
        self.ax = ax;
        self.ay = ay;
        
def testFunction(message) :
    print("func");
    print(message);