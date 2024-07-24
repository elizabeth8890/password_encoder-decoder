#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 15:18:39 2024

@author: elizabethkallman
"""

def decode(password):
    list_password = list(password)
    
    password2 = []
    for i in range(len(list_password)):
        i_tmp = str(int(list_password[i]) - 3)
        password2.append(i_tmp)
        x = "".join(password2)
    
    return(x)


#pswd = '98765'
#print(decode(pswd))