'''
07-15-2023 -- Kyle Gruen -- 
A continuation of the original algorithm developed in roleSpecificCounter.py
This script takes in the role you are playing and gives the best team

'''

#Imports#

import csv; 
import numpy as np; 

from collections import Counter; 

#Fields#

dpsArr = [];     #List of all counters pulled from csv
supportArr = [];
tankArr = []; 

enemy_team = [3, 17, 18, 30, 31];   #Current Heros on enemy team

#Methods# 

'''
Method lineReader(int, string): 
Takes in # specific to hero and adds all counters from that row
Takes in string to determine which array to add to from csv file
'''
def lineReader(heroNum, role): 

    if (role == "TANK"):
        filePath = "./roleCounters/tankList.csv";
    elif (role == "SUPPORT"):
        filePath = "./roleCounters/supportList.csv";
    elif (role == "DPS"):
        filePath = "./roleCounters/dpsList.csv"; 


    f = open(filePath, "r");
    csvin = csv.reader(f);
    count = 1 

    for row in csvin:
        if (count == heroNum):
            for item in row:
                if (role == "DPS"):
                    dpsArr.append(item);
                elif(role == "TANK"):
                    tankArr.append(item);
                elif(role == "SUPPORT"):
                    supportArr.append(item); 
        elif (count > heroNum):
            break; 
        count+=1;
    
    return 0; 

'''
Method all_counters(arr):
Takes array of enemy team and calls lineReader() method on each 
Takes role currently being determined
number present in array
'''       
def all_counters(enemyNum, role):

    for num in enemy_team: 
        lineReader(num,role);

    return 0; 

'''
Method rank():
Puts all the pieces together creating the list of counters
adds to array fields at the top
'''
def rank():

    all_counters(enemy_team,"TANK");   #Adds counter to largeList field
    all_counters(enemy_team,"SUPPORT");
    all_counters(enemy_team,"DPS");

    return 0; 

'''
Method run():
Takes input of specific role being played and sets csv being read to that role
Then runs rank() method to created a top list of the best picks
'''
def run():
    
    rank(); 

    dpsCount = Counter(dpsArr);
    supportCount = Counter(supportArr);
    tankCount = Counter(tankArr); 

    print(tankCount.most_common(1));
    print(dpsCount.most_common(2));
    print(supportCount.most_common(2));


#Executable#

run(); 