#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 19:53:06 2021

@author: tahashafique
"""

import numpy as np 
import pytessearct 
import layoutparser as lp
import re 




class image_parser: 
    
    def __init__(self): 
        self.ocr_agent = lp.TesseractAgent(languages='eng')
        
        
    def parse_image(self, image):
        if type(image) != np.ndarray: 
            image = np.asarray(image)
                        
        return self.ocr_agent.detect(image)
    
    def clean_text(self): 
        pass 
    
    

    
    
    
    
        