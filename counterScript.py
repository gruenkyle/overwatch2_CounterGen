'''
07-15-2023 -- Kyle Gruen

This is the original algorithm made for the counter script project
I wanted to make sure I could make it functional before going deeper
into the open cv side of the project.

Takes in the enemy team characters and pulls the best counters for each number
Uses large array created to rank the most repeated characters.
'''

#Imports#

import csv; 
import numpy as np; 
import collections; 

#Fields#

largeList = [];     #List of all counters pulled from csv
enemy_team = [1,32,36,16,23];   #Current Heros on enemy team

#Methods# 

'''
Method lineReader(int): 
Takes in # specific to hero and adds all counters from that row
in our csv file to largeList array
'''
def lineReader(heroNum): 

    f = open("./roleCounters/counterlist.csv", "r");
    csvin = csv.reader(f);
    count = 1 

    for row in csvin:
        if (count == heroNum):
            for item in row:
                largeList.append(item); 
        elif (count > heroNum):
            break; 
        count+=1;

'''
Method all_counters(arr):
Takes array of enemy team and calls lineReader() method on each 
number present in array
'''       
def all_counters(enemyNum):

    for num in enemy_team: 
        lineReader(num);

'''
Method rank():
Puts all the pieces together creating the list of counters
then uses collections to rank the top counters 
'''
def rank():
    all_counters(enemy_team);   #Adds counter to largeList field
    counters = collections.Counter(largeList);  #Creates collections counter instance 

    print(counters.most_common(5)); #Number is how many heros show

#Executable#

rank(); 

