#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 22:50:29 2021

@author: tahashafique
"""

import re 


class read_write_textfile: 

  '''To read and write lists from text files'''
  
  @staticmethod
  def read_file(filename): 
    files = []


    with open(filename, 'r')as f: 
      lines = f.readlines()
    
    for line in lines: 
        
      if re.search(r'\n', line) != None:
        files.append(re.sub('\n','',line))

      else:
        files.append(line)

    f.close()

    return files 

  
  def write_file(filename, list_to_write): 
    textfile = open (filename, "w")

    for item in list_to_write: 
      textfile.write(item + "\n")

    textfile.close()