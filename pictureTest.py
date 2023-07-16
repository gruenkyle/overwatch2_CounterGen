import cv2;
import numpy as np;

scoreboard = cv2.imread(r"./testScoreboard.jpg");
template = cv2.imread('./characterImg/Ana.png');

dimensions = scoreboard.shape;
startY = dimensions[1] / 2; 

threshold = 0.8; 
flag = False; 


#scoreboardCrop = scoreboard[x:xEnd, y:yEnd];
cutImg = scoreboard[int(dimensions[0] / 2): dimensions[0], 0: int(dimensions[1] / 2)];
cv2.imwrite("./crop2.jpg", cutImg);

gImg = cv2.cvtColor(cutImg, cv2.COLOR_BGR2GRAY);
tImg = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY);


result = cv2.matchTemplate(gImg, tImg, cv2.TM_CCOEFF_NORMED);
(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(result)

'''
Create for loop that counts up by one each time starting at zero
Then it creates string of image we are trying to find (1.png)
and uses that as the template against our scoreboard cropped variable
If it returns null then skip, else add count variable to array
of our enemy team
Go through whole characterImg Folder
'''