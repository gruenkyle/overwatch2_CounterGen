import cv2;

scoreboard = cv2.imread(r"./testScoreboard.jpg");

dimensions = scoreboard.shape;
startY = dimensions[1] / 2; 

#scoreboardCrop = scoreboard[x:xEnd, y:yEnd];
cutImg = scoreboard[int(dimensions[0] / 2): dimensions[0], 0: int(dimensions[1] / 2)];
cv2.imwrite("./crop2.jpg", cutImg);