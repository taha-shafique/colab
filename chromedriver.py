#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 23:04:12 2021

@author: tahashafique
"""

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains 


class chrome_driver: 
    
    def __init__(self, executable_path, max_window = True, window_size = None, incognito = True, headless = False):
        
        self.options = webdriver.ChromeOptions()
        
        self.driver = webdriver.Chrome(executable_path = executable_path ,options = self.options)
        
        
        
        self.options.add_argument("user-agent = Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36")
        
        if headless == True: 
            self.options.add_argument('--headless')
            
        if max_window == True:
            self.driver.maximize_window()
            
        if window_size != None: 
            self.options.add_argument(f"window-size={window_size[0]},{window_size[1]}")
            
        if incognito == True: 
            self.options.add_argument("--incognito")
            
    
    def close_driver(self):
        self.driver.quit()