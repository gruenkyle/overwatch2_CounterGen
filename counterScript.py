import csv; 
largeList = []; 

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
        

characterNum = int(input("Hero Number?"));
lineReader(characterNum); 
print(largeList); 