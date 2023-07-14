import csv; 
import numpy as np; 
import collections; 

largeList = []; 
enemy_team = [1,32,36,16,23];

def lineReader(heroNum): 

    f = open("counterlist.csv", "r");
    csvin = csv.reader(f);
    count = 1 

    for row in csvin:
        if (count == heroNum):
            for item in row:
                largeList.append(item); 
        elif (count > heroNum):
            break; 
        count+=1;
        
def all_counters(enemyNum):

    for num in enemy_team: 
        lineReader(num);

def rank():
    all_counters(enemy_team);
    counters = collections.Counter(largeList); 

    print(counters.most_common(5)); 

rank(); 
