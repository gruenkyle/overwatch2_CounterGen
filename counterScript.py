import csv; 
largeList = []; 
enemy_team = [2, 5, 3, 10];

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

all_counters(enemy_team);
print(largeList); 