# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 01:48:10 2020

@author: Peter
"""
import numpy as np
import pandas as pd

def dataLoad(filename):
    df = pd.read_csv('test.txt', delimiter = ' ')
#Adding headers
    df.columns=['Temperature', 'Growth rate', 'Bacteria species']

#Converting frame to array
    dataI = df.iloc[:,0:3].to_numpy()
#Creating bool from
    boolEval = np.ones((np.size(dataI, axis = 0), np.size(dataI,axis = 1)), dtype=bool)
    
# going through each row of the data matrix
    for y in range(np.size(dataI, 0)):
    
    # validation of the temperatures
        if ((dataI[y,0] < 10) or (dataI[y,0] > 60)):
            boolEval[y,0] = False

    # validation of the growth rates
        if (dataI[y,1] < 0):
            boolEval[y,1] = False
                 
    # validation of the bacteria species
        if ((dataI[y,2] < 1) or (dataI[y,2] > 4)):
            boolEval[y,2] = False
        
        y = y + 1

    #Error messasging for erroneous data    
    for x in range(np.size(dataI,0)):
    
    #All data
        if (boolEval[x,0] == False) and (boolEval[x,1] == False) and (boolEval[x,2] == False):
            print("Erroneous data found. All attributes out of bounds. Line {:.0f} deleted!".format(x))
    #Temp and growth
        elif (boolEval[x,0] == False) and (boolEval[x,1] == False):
            print("Erroneous data found. Temperature and growth rate out of bounds. Line {:.0f} deleted!".format(x))
    #Temp and bacteria
        elif (boolEval[x,0] == False) and (boolEval[x,2] == False):
            print("Erroneous data found. Temperature and bacteria species out of bounds. Line {:.0f} deleted!".format(x))
    #Growth and bacteria    
        elif (boolEval[x,1] == False) and (boolEval[x,2] == False):
            print("Erroneous data found. Growth rate and bacteria species out of bounds. Line {:.0f} deleted!".format(x))
    #Temp    
        elif (boolEval[x,0] == False):
            print("Erroneous data found. Temperature out of bounds. Line {:.0f} deleted!".format(x))
    #Growth    
        elif (boolEval[x,1] == False):
            print("Erroneous data found. Growth rate out of bounds. Line {:.0f} deleted!".format(x))
    #Bacteria    
        elif (boolEval[x,2] == False):
            print("Erroneous data found. Bacteria species out of bounds. {:.0f} Line deleted!".format(x))
            

# Indexing temperature and filtering erroneous data
    indexTemp = df[(df['Temperature'] > 60 ) | (df['Temperature'] < 10)].index
    data = df.drop(indexTemp)
# Indexing growth rate and filtering erroneous data    
    indexGrowth = data[(data['Growth rate'] < 0 )].index
    data = data.drop(indexGrowth)
# Indexing bacteria species and filtering erroneous data
    indexBact = data[(data['Bacteria species'] > 4 ) | (data['Bacteria species'] < 1)].index
    data = data.drop(indexBact)


#Write new txt file
    df.to_csv('data.txt', index=False, sep=' ')
    
    return data

