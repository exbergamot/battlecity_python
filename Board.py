# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 11:03:49 2019

@author: Dmytro_Kushchov
"""
import numpy as np
from enum import Enum
from Tank import Tank, Eagle, Bullet

class Side(Enum) :
    TOP = 1;
    BOTTOM = 2;
    
class Action(Enum) :
    UP =    (0, 1, False);
    DOWN =  (0, -1, False);
    LEFT =  (-1, 0, False);
    RIGHT = (1, 0, False);
    UP_AND_SHOOT =    (0, 1, True);
    DOWN_AND_SHOOT =  (0, -1, True);
    LEFT_AND_SHOOT =  (-1, 0, True);
    RIGHT_AND_SHOOT = (1, 0, True);

class Board :
    walls = [
            [0,0,0,0,0,0,0],
            [0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0],
            [1,1,0,1,0,1,1],
            [0,0,0,0,0,0,0],
            [0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0],
    ];
    eagles = [Eagle(3,0,Side.TOP), Eagle(3,6,Side.BOTTOM)];
    tanks = [Tank(2,0,Side.TOP), Tank(4,0,Side.TOP), Tank(2,6,Side.BOTTOM), Tank(4,6,Side.BOTTOM)]
    bullets = []
    
    def toLayeredMap(self, tank) :
        result = np.zeros((10,7,7));
        #walls
        result[0] = self.walls;
        #eagles
            #ally
            for eagle in eagles :
                result[tank.side.value 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        