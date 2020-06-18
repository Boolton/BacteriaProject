# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 18:53:57 2020

@author: Peter
"""
from DataLoad import dataLoad
filename = "test.txt"

def dataPlot(data):
    import numpy as np
    import matplotlib.pyplot as plt

#Counting up the bacteria species by type
    bacNum, bacCount =  np.unique(data.iloc[:,2], return_counts=True)
    
#Setting bacteria labels
    bacName = ['Salmonella enterica', 'Bacillus cereus', 'Listeria', 'Brochothrix thermosphacta']

#Plotting bar graph
    fig = plt.gcf()
    fig.set_size_inches(10, 6)
    plt.bar(bacNum,bacCount, color=['#0b162a','#c83803','#97233f','#008e97'])
    plt.xticks(bacNum,(bacName),fontsize=8)
    plt.yticks()
    plt.title("Bacteria quantities",fontsize=18)
    plt.xlabel("Species of bacteria",fontsize=12)
    plt.ylabel("Number of bacteria",fontsize=12)
    for a,b in zip(bacNum, bacCount):
        plt.text(a, b, str(b))
    plt.savefig('BacteriaQuantities')
    plt.show()

#Split original dataframe into four, according to bacteria species
    data1 = data[data['Bacteria species'] == 1].sort_values(['Temperature'])
    data2 = data[data['Bacteria species'] == 2].sort_values(['Temperature'])
    data3 = data[data['Bacteria species'] == 3].sort_values(['Temperature'])
    data4 = data[data['Bacteria species'] == 4].sort_values(['Temperature'])

#Plotting growth rate over temperature
    fig = plt.gcf()
    fig.set_size_inches(10, 6)
    plt.plot('Temperature','Growth rate',data=data1, color='#0b162a')
    plt.plot('Temperature','Growth rate',data=data2, color='#c83803')
    plt.plot('Temperature','Growth rate',data=data3, color='#97233f')
    plt.plot('Temperature','Growth rate',data=data4, color='#008e97')
    plt.title("Growth rate by temperature",fontsize=18)
    plt.xlabel("Temperature",fontsize=12)
    plt.ylabel("Growth rate",fontsize=12)
    lgd=plt.legend(['Salmonella enterica', 'Bacillus cereus', 'Listeria', 'Brochothrix thermosphacta'],bbox_to_anchor=(1, 1), loc='upper left', ncol=1)
    plt.savefig('GrowthTemp', bbox_extra_artists=(lgd,), bbox_inches='tight')
    plt.show()