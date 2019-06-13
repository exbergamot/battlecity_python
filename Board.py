# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 11:03:49 2019

@author: Dmytro_Kushchov
"""

from enum import Enum
from Tank import Tank, Eagle, Bullet

class Side(Enum) :
    TOP = 1;
    BOTTOM = 2;
    
class Action(Enum) :
    UP = 1;
    DOWN = 2;
    LEFT = 3;
    RIGHT = 4;
    UP_AND_SHOOT = 5;
    DOWN_AND_SHOOT = 6;
    LEFT_AND_SHOOT = 7;
    RIGHT_AND_SHOOT = 8;

class Board :
    walls = [
            [0,0,0,0,0,0,0]
            [0,0,1,1,1,0,0]
            [0,0,0,0,0,0,0]
            [1,1,0,1,0,1,1]
            [0,0,0,0,0,0,0]
            [0,0,1,1,1,0,0]
            [0,0,0,0,0,0,0]
    ];
    eagles = [Eagle(3,0,Side.TOP), Eagle(3,6,Side.BOTTOM)];
    tanks = [Tank(2,0,Side.TOP), Tank(4,0,Side.TOP), Tank(2,6,Side.BOTTOM), Tank(4,6,Side.BOTTOM)]
    bullets = []