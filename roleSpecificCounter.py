'''
07-15-2023 -- Kyle Gruen
A continuation of the original algorithm developed in counterScript.py
This script takes in the role you are playing and gives the best character
'''

#Imports#
import csv; 
import numpy as np; 
import collections; 

#Fields#
largeList = [];     #List of all counters pulled from csv
enemy_team = [1,32,36,16,23];   #Current Heros on enemy team
filePath = "";

#Methods# 

'''
Method lineReader(int): 
Takes in # specific to hero and adds all counters from that row
in our csv file to largeList array
'''
def lineReader(heroNum): 

    f = open(filePath, "r");
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

    print(counters.most_common(3)); #Number is how many heros show

'''
Method run():
Takes input of specific role being played and sets csv being read to that role
Then runs rank() method to created a top list of the best picks
'''
def run():
    role = input("What is your role?");

    global filePath;

    if (role == "TANK"):
        filePath = "./roleCounters/tankList.csv";
    elif (role == "SUPPORT"):
        filePath = "./roleCounters/supportList.csv";
    elif (role == "DPS"):
        filePath = "./roleCounters/supportList.csv";
    
    rank(); 

run(); 