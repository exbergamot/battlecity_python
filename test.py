# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 17:52:03 2019

@author: Dmytro_Kushchov
"""
from enum import Enum

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