#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 16:16:47 2024

@author: rileynickles

"""
#This is going to the generic script for the quantification data analysis. 
pip install scipy
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

# WHen inputing the data into the CSV you put the pulldown in column 1, and the binding partners in rows
#2,3, 4, etc. THere can be no text, only the numbers. Follow the excel template with comments for guidance. 

data_set = np.loadtxt('Quantification_test.csv',delimiter=',')
data_set = np.array(data_set)
data_set = np.transpose(data_set)

number_reps = int(input('How many Replicatates: '))
number_conditions = int((len(np.transpose(data_set)) + 1) / number_reps)
number_binding = int(input('How many binding partners: '))

conditions = []
for j in range(number_conditions):
    x = input('Input Experiment Conditon to be used in Graph: ')
    conditions.append(x)


offset = number_conditions


# THis will be the normalizations for the binding partner 1 lysates
for j in range(number_binding*2):
    Binding_Lysates =[]
    #This will set up the arrays that will be used in the rest of the function
    pulldown_lys_column = int(input('What column is the pulldown in? '))
    pulldown_lys = data_set[pulldown_lys_column]
    
    binding_lys_column = int(input('What column is the binding partner in? '))
    bind_lys = data_set[binding_lys_column]
    for i in range(number_reps):
        #This part will take the values above and normalize them. 
        pulldown_lysate = pulldown_lys[i*number_conditions:i*number_conditions+offset]
        binding_lysate = bind_lys[i*number_conditions:i*number_conditions+offset]
    
        norm_lys = binding_lysate/pulldown_lysate
        percent_lys_bound_pulldown = norm_lys / norm_lys[1]*100
        Binding_Lysates.append(percent_lys_bound_pulldown)
        Lysates = np.array(Binding_Lysates)
        if np.all(np.isinf(Lysates[:, 0])):
    # Set the entire first column to zero
            Lysates[:, 0] = 0
        if np.all(np.isnan(Lysates[:, 0])):
    # Set the entire first column to zero
            Lysates[:, 0] = 0
        #The following will generate the bar graph for the binding partner 1 lysates
        values_lys = []
    for i in range(number_conditions):
        avg = np.average(Lysates[:,i])
        if np.isinf(avg):
            avg = 0
        if np.isnan(avg):
            avg = 0
        values_lys.append(avg)
    #Calculate the error for hte error bars
    std_dev = np.std(np.transpose(Lysates),axis=1,ddof=1)
    color = input('Common colors are blue, green, lightgreen, red, orange, skyblue, turquoise, etc. \nChoose a color: ')
    condition_dict = {}
    
    for i, condition in enumerate(conditions):
        condition_dict[condition] = np.transpose(Lysates)[i].tolist()
#bars = ax.bar(conditions, means, yerr=errors, capsize=5, color='skyblue', edgecolor='black')
    fig, ax = plt.subplots()
    bars = ax.bar(conditions,values_lys, yerr=std_dev, capsize=5,edgecolor='black',color=color)
    
# This does the T-Test for statistical signifigance
    Stat_comp = int(input('How many Statistical comparisons do you want to do? '))
    for i in range(Stat_comp):
        t_stat, p_value = stats.ttest_ind(list1, list2)
        if p_values => 0.05:
            
    
    for bar in bars:
        category = bar.get_x() + bar.get_width() / 2
        height = bar.get_height()
        category_label = bar.get_x() + bar.get_width() / 2
        points = condition_dict[conditions[int(category_label)]]
        for point in points:
            ax.plot(category, point, 'o', color='black')  # Customize marker style as needed
       
#plt.xlabel('Categories', fontsize=14, fontweight='bold', family='Helvetica')
#plt.ylabel('Values', fontsize=14, fontweight='bold', family='Helvetica')
#plt.title('Bar Graph with Helvetica Font', fontsize=16, fontweight='bold', family='Helvetica')

    plt.title(input('Enter title: '), fontsize=16, fontweight='bold',family='helvetica')
    plt.ylabel(input('Enter Y-Axis Label: '),fontsize=14, fontweight='bold',family='helvetica')
    plt.xticks(fontsize=12, fontweight='bold', family='helvetica')
    plt.yticks(fontsize=12, fontweight='bold', family='helvetica')
    plt.show()

    