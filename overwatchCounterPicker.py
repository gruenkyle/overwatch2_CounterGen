'''
07-16-2023 -- Kyle Gruen 

Taking all baseCode algorithms, this script specifically can determine what counter
picks for your whole team would be best to play with. 
Done by taking in a screenshot and template matching it with our folder of character images. 
'''

#Imports#

from collections import Counter; 
import cv2;
import csv;

#Fields#

templatePath = "";      #Directory Path Field that is filled with characterImg folder
scoreboardPath = "scoreboardTestOne.jpg";        #Directory Path of Screenshot of Enemy Team
enemy_team = [];         #Array that holds what players the enemy team is using
threshold = 0.75;        #Threshold that maxVal in matchTemplate must reach

dpsArr = [];    #List of best DPS counters in csv
supportArr = [];        #List of best Support counters in csv
tankArr = [];       #List of best Tank counters in csv 

#Methods#

'''
Method correlatingImage(str, str):
originalPth - Directory Path to Screenshot
templatePth - Directory Path to Template used to compare

Takes in each path and compares them using the matchtemplate function 
using TM_COEFF_NORMED then returns the maxVal of the result
'''
def correlatingImage(originalPth, templatePth):

    scoreboard = cv2.imread(originalPth);       #Creates Instance of Scoreboard Screenshot
    temp = cv2.imread(templatePth);         #Creates Instance of Character Image 

    dimensions = scoreboard.shape;      #Returns Height and Width values to Array

    cutImg = scoreboard[int(dimensions[0] / 2): dimensions[0], 0: int(dimensions[1] / 4)];  #Crops scoreboard into managable image

    oImg = cv2.cvtColor(cutImg, cv2.COLOR_BGR2GRAY);    #Converts Original Image to Grayscale
    tImg = cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY);    #Converts Original Image to Grayscale

    result = cv2.matchTemplate(oImg, tImg, cv2.TM_CCOEFF_NORMED);   #Template Match with both Images on COEFF_NORMED
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(result)        #Stores Values returned by result of Match

    return maxVal;      #Returns maxVal of if template is found within screenshot

'''
Method createCountList():

Appends specific heros on enemy team into array enemyTeam[]
Uses the characterImg folder to enter parameter into correlatingImage() function
'''
def createCounterList(): 

    for count in range(37):     #For loop for the 37 files within characterImg Folder
        global threshold;   

        count+=1;

        templatePath = ("./characterImg/" + str(count) + ".jpg");   #Defines Template Path based off Count

        if (correlatingImage(scoreboardPath, templatePath) >= threshold):   #Uses correlatingImage against threshold field
            enemy_team.append(count);    #Appends only if maxVal is greater than threshold

'''
Method lineReader(int, string): 
Takes in # specific to hero and adds all counters from that row
Takes in string to determine which array to add to from csv file
'''
def lineReader(heroNum, role): 

    #Determines what role csv file to use within appending rows
    if (role == "TANK"):
        filePath = "./roleCounters/tankList.csv";
    elif (role == "SUPPORT"):
        filePath = "./roleCounters/supportList.csv";
    elif (role == "DPS"):
        filePath = "./roleCounters/dpsList.csv"; 

    #Opens file with specific path determined above
    f = open(filePath, "r");
    csvin = csv.reader(f);
    count = 1 

    #Appends heros to specific arrays based on if they correlate with given hero counter
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

    #Calls line reader for every hero based on role to be ranked
    for num in enemy_team: 
        lineReader(num,role);

    return 0; 

'''
Method rank():
Puts all the pieces together creating the list of counters
adds to array fields at the top
'''
def rank():

    all_counters(enemy_team,"TANK"); 
    all_counters(enemy_team,"SUPPORT");
    all_counters(enemy_team,"DPS");

    return 0; 

'''
Method execute():

Calls on different methods used to determine best team 
the can counter the enemy squad. 
'''
def execute():

    createCounterList();    #Creates list of enemies present on other team from screenshot given

    global enemy_team       #Calls on enemy_team field 
    
    rank();     #Fills each array with large list of counters from each role

    dpsCount = Counter(dpsArr);
    supportCount = Counter(supportArr);         #These set counter function availability on array
    tankCount = Counter(tankArr); 

    print(tankCount.most_common(1));            #These get the most common found in each array and display them
    print(dpsCount.most_common(2));
    print(supportCount.most_common(2));


    return 0; 

#Executable#
execute(); 
