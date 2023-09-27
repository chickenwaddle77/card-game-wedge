import pickle


def setup():
    
    global moneyPlayerA, moneyPlayerB, HOUSE, maxMoney, gameTurn, imageNumberList
    global maxNumber, minNumber
    global cardImage
    global gameTurnCompare
    global pressLock
    global timer
    global betBase
    global showMaxMin  
    global showMaxMinNumc
    global helpImage
    global font,  gameState
    global fileInput,  fileEntered,  directory,  saveName,  saveEntered,  wrong,  scoreList,  scrollinc,  loser
    
    size(1000, 1000)

    font= createFont("PressStart2P-Regular.ttf", 32)
    textFont(font)
    
    
    helpImage= loadImage("help.jpg")
    showMaxMin= False
    showMaxMinNum= 0
    
    gameState =  7
    
    betBase= 10
    timer= 0
    pressLock= False
    gameTurnCompare= 0
    gameTurn= 0
    
    moneyPlayerA= 500
    moneyPlayerB= 500
    HOUSE= 500
    
    maxMoney= 1000
    
    cardImage= [loadImage(str(i+1)+".png") for i in range(0, 52)]
    imageNumberList= [i for i in range(0, 52)]
    global playerAName, playerBName, nameLen
    playerAName= ""
    playerBName= ""
    nameLen= 6
    createVariable()
    
    wrong =  False
    scoreList =  []
    scrollinc =  0 
    fileEntered =  False
    fileInput =  "scoreboard1.txt"
    saveEntered =  False
    saveName =  fileInput
    loser =  ""
                
    directory =  sketchPath("") + "scores" 

def typeIN(enteredName, gameState, playerNOTequal, repeat, nameLen, gameGO, fileState):
    fileEntered =  False
    if (key) ==  ENTER:
            repeat =  isRepeat(scoreList, playerAName)
            if enteredName !=  " " and len(enteredName) > 0 and not repeat and playerNOTequal:
                if fileState: 
                    fileEntered =  True
                else: 
                    gameState =  gameGO
            
    elif key ==  BACKSPACE:
        if len(enteredName) > 0: 
            enteredName =  enteredName[:-1]
        
    elif (str(key).isdigit() or str(key).isalpha) and len(enteredName)<= nameLen:
        enteredName =  enteredName + str(key)
        enteredName =  enteredName.replace("65535", "")
            
    if fileState:
        return enteredName, fileEntered
    else: 
        return enteredName, gameState
            
            
def isRepeat(scoreList,  enteredName):
    for i in scoreList: 
        if i[0] ==  enteredName:
            return True
    return False
    
    
def buildBox(x1,  y1,  scoreList,  rank,  displayText):
    
    wid =  width/2 - 50
    hei =  height/12
    x2 =  x1 + wid 
    y2 =  y1 + hei
    
    strokeWeight(3)
    stroke(255)
    noFill()
    rectMode(CORNER)
    rect(x1,  y1,  wid,  hei)
    
    textAlign(CENTER,  CENTER)
    textSize(35)
    fill(255)
    
    if displayText: 
        text(scoreList[rank][0],  (x1 + x2)/2,  (y1 + y2)/2)
    else: 
        text(scoreList[rank][1],  (x1 + x2)/2,  (y1 + y2)/2)
        
def drawInputFile():
    global directory,  wrong,  gameState,  fileInput,  fileEntered,  scoreList
    
    background(155, 145, 165)
    textAlign(CENTER,  CENTER)
    textSize(30)
    fill(200, 190, 210)
    
    if not wrong:
        text("please input file name: ",  width/2,  height*2/4)
    else: 
        text("please input full file path: ",  width/2,  height*2/4)
        
    textSize(15)
    text(fileInput + "_",  width/2,  height*2/4 + 40)
    
    if fileEntered: 
        try:
            if not wrong:
                fileaddress =  os.path.join(directory,  fileInput)
                print(fileaddress)
                with open(fileaddress,  'rb') as f:
                    scoreData =  pickle.load(f)
            else: 
                with open(fileInput,  'rb') as f:
                    scoreData =  pickle.load(f)
            
            scoreList =  list(scoreData)
            scoreList =  sorting(scoreList)
            
            gameState =  0
        except: 
            fileEntered =  False
            wrong =  True
            
def sorting(scoreList):
    n =  len(scoreList)

    for i in range(1,  n):
        isSorted =  True
        for j in range(0,  n - i):
            if scoreList[j][1] < scoreList[j + 1][1]:
                scoreList[j],  scoreList[j + 1] =  scoreList[j + 1],  scoreList[j]
                isSorted =  False
        if isSorted:
            break
    return scoreList


def drawScoreListSave():
    global saveName,  saveEntered
    
    background(155, 145, 165)
    textAlign(CENTER,  CENTER)
    textSize(30)
    fill(200, 190, 210)
    text("please input savegame file: ",  width/2,  height*2/4)
    
    textSize(15)
    text(saveName,  width/2,  height*2/4 + 40)
        
    if saveEntered:
        address =  os.path.join(directory,  saveName)
    
        with open(address, 'wb') as file:
            pickle.dump(scoreList,  file)
        
        delay(500)
        exit()
        
        
def saveScore(moneyPlayerA,  moneyPlayerB):
    global playerAName,  playerBName,  scoreList
    
    newScoreA =  [playerAName,  moneyPlayerA]
    newScoreB =  [playerBName,  moneyPlayerB]
    scoreList.append(newScoreA)
    scoreList.append(newScoreB)
    scoreList =  sorting(scoreList)
    
    print(scoreList)
    
    
def resetVariable():
    
    global moneyPlayerA, moneyPlayerB, HOUSE, maxMoney, gameTurn, imageNumberList
    global maxNumber, minNumber
    global cardImage
    global gameTurnCompare
    global pressLock
    global timer
    global betBase
    global showMaxMin  
    global showMaxMinNum
    showMaxMin= False
    showMaxMinNum= 0
    betBase= 10
    timer= 0
    pressLock= False
    gameTurnCompare= 0
    gameTurn= 0
    moneyPlayerA= 100
    moneyPlayerB= 100
    HOUSE= 100
    maxMoney= 200
    global playerAName, playerBName, nameLen
    playerAName= ""
    playerBName= ""
    nameLen= 6
    global showMaxMinFlag
    showMaxMinFlag= 0
    
    
def createVariable():
    
    global gameImage
    global maxNumber, minNumber
    gameImage =  [-1, -1]
    randomImageList()
    
    minNumber= gameImage[0]/4+1
    maxNumber= gameImage[1]/4+1
    
    
def randomImageList():
    
    global gameImage    
    global showMaxMin
    global showMaxMinNum
    gameImage[0] =  floor(random(0, 52))
    gameImage[1] =  floor(random(0, 52))
    while(gameImage[1]== gameImage[0]):
        gameImage[1] =  floor(random(0, 52))
    temp0= gameImage[0]
    temp1= gameImage[1]
    gameImage[0]= min(temp0, temp1)
    gameImage[1]= max(temp0, temp1)
    if gameImage[0]<= 3:
        showMaxMin= True
        showMaxMinNum= 0
        
        
def draw():
    global gameState, difficulty
    
    if gameState== 0:
        drawStartPage()
    elif gameState== 1:
        drawGamePage()
    elif gameState== 2:
        drawEndPage()
    elif gameState== 3:
        drawMenuPage()
    elif gameState== 4:
        drawHistoryPage()
    elif gameState== 5:
        drawSetPlayerNameA()
    elif gameState== 6:
        drawSetPlayerNameB()
    elif gameState== 7:
        drawInputFile()
    elif gameState== 8:
        drawScoreListSave()
        
        
def drawSetPlayerNameA():
    global playerAName, playerBName
    background(155, 145, 165)
    textAlign(CENTER, CENTER)
    textSize(30)
    
    fill(200, 190, 210)
    text("Set name for A: " + playerAName + "_",  width/2,  height*2/4)
    
    
def drawSetPlayerNameB():
    global playerAName, playerBName
    background(155, 145, 165)
    textAlign(CENTER, CENTER)
    textSize(30)
    
    fill(200, 190, 210)
    text("Set name for B: " + playerBName + "_",  width/2,  height*2/4)
    
    
def drawHistoryPage():
    global playerAName,  playerBName,  gameState,  scoreList,  scrollinc
    
    heiinc =  height/10
    titlepos =  75
    hei =  titlepos + 75
    totaldisplay =  5
    background(200,  190,  210)
    
    textAlign(CENTER,  CENTER)
    textSize(45)
    fill(255)
    text("Scoreboard",  width/2,  titlepos)
    
    inc =  int(scrollinc)
    if totaldisplay + inc > len(scoreList):
        inc =  0 

    for i in range(0 + inc,  totaldisplay + inc):
        displayText =  True
        buildBox(50,  hei,  scoreList,  i,  displayText) 
        hei =  hei + heiinc
 
    hei =  titlepos + 75
    for k in range(0 + inc,  totaldisplay + inc):
        displayText =  False
        buildBox(width/2,  hei,  scoreList,  k,  displayText) 
        hei =  hei + heiinc
        
    if keyPressed and key ==  ENTER:
        gameState =  0    
    
    
def mouseWheel(event): 
    global gameState
    global betBase
    global moneyPlayerA, moneyPlayerB, gameTurn, HOUSE
    global finalHistory, logIndex
    
    if gameState== 1:
        betBase =  betBase+event.getCount()
        print(betBase)
        # if betBase<10:
        #     betBase= 10
        if gameTurn== 0:
            betBase =  ((betBase%min(moneyPlayerA, HOUSE+5)//5)*5)
        else:
            betBase =  ((betBase%min(moneyPlayerB, HOUSE+5)//5)*5)
            
    # keep value in range
    
    
def drawGamePage():
    background(155, 145, 165)
    global gameState
    global playerAName, playerBName
    global showMaxMin  
    global showMaxMinNum
    global timer
    global cardImage, gameImage, gameTurn
    global gameTurnCompare
    global pressLock
    global moneyPlayerA, moneyPlayerB, HOUSE, maxMoney, gameTurn, imageNumberList
    global betBase
    global maxNumber, minNumber
    global helpImage,  loser 
    
    
    if gameTurn== 0:
        if gameTurnCompare== 0:
            image(cardImage[gameImage[0]], 100, 0)
            image(cardImage[gameImage[1]], 550, 0)
        elif gameTurnCompare== 1:
            image(cardImage[gameImage[0]], 500-175, 0)
    elif gameTurn== 1:
        if gameTurnCompare== 0:
            image(cardImage[gameImage[0]], 100, 0)
            image(cardImage[gameImage[1]], 550, 0)
        elif gameTurnCompare== 1:
            image(cardImage[gameImage[0]], 500-175, 0)
    
    textAlign(CENTER, CENTER)
    rectMode(CENTER)
    textSize(20)
    if showMaxMin and gameTurnCompare== 0:
        
        if(mouseX>width*2/4-100/2 and mouseX<width*2/4+100/2 and mouseY>height*9/18-30/2 and mouseY<height*9/18+30/2):
            fill(190, 145, 165)
            if mousePressed and pressLock== False:
                pressLock= True
                showMaxMinNum= 1-showMaxMinNum
                
        else:
            fill(250, 200, 215)
        rect(width*2/4, height*9/18, 100, 30)
        fill(255, 230, 200)
        
        if showMaxMinNum== 0:
            
            minNumber= 1
            maxNumber= max((gameImage[0])/4+1, (gameImage[1])/4+1)
            temp0= gameImage[0]
            temp1= gameImage[1]
            gameImage[0]= min(temp0, temp1)
            gameImage[1]= max(temp0, temp1)
            text("Min", width*2/4, height*9/18)
            
        if showMaxMinNum== 1:
            
            minNumber= max((gameImage[0])/4+1, (gameImage[1])/4+1)
            maxNumber= 13
            temp0= gameImage[0]
            temp1= gameImage[1]
            gameImage[0]= max(temp0, temp1)
            gameImage[1]= min(temp0, temp1)
            text("Max", width*2/4, height*9/18)
            
        text("Click to Set A as:", width*3/6-260, height*9/18)
        
        
    fill(250, 200, 215)
    text("Scoll to change Bet: "+str(betBase), width/2, height*7/12)
    textSize(30)
    
    fill(200)
    if gameTurn== 0:
        fill(255, 230, 200)
        triangle(width/4, height*2/3+15, width/4-15, height*2/3+30+15, width/4+15, height*2/3+30+15)
    text(playerAName+":"+str(moneyPlayerA), width/4, height*2/3);
    
    fill(200)
    if gameTurn== 1:
        fill(255, 230, 200)
        triangle(width*3/4, height*2/3+15, width*3/4-15, height*2/3+30+15, width*3/4+15, height*2/3+30+15)
    text(playerBName+":"+str(moneyPlayerB), width*3/4, height*2/3);
    
    
    fill(250, 200, 215)
    text("HOUSE: "+str(HOUSE), width/2, height*7/9);
    
    rectMode(CENTER)
    heightButtonY= height*9/10
    heightButtonX= width*1/4
    heightButtonW= width*1/5
    heightButtonH= width*1/20
    
    
    if millis()-timer>3500 and gameTurnCompare== 1:
        gameTurnCompare= 0
        gameTurn= 1-gameTurn
        randomImageList()
        minNumber= (gameImage[0])/4+1
        maxNumber= (gameImage[1])/4+1
        if minNumber== 1 and maxNumber== 1:
            maxNumber= 13
        betBase= min(5, HOUSE, moneyPlayerA, moneyPlayerB)
        
        
    if(mouseX>heightButtonX-heightButtonW/2 and mouseX<heightButtonX+heightButtonW/2 and mouseY>heightButtonY-heightButtonH/2 and mouseY<heightButtonY+heightButtonH/2):
        fill(250, 200, 215)
        if mousePressed and pressLock== False:
            pressLock= True
            if gameTurnCompare== 0:
                gameTurnCompare= 1
                timer= millis()
                randomImageList()
                tempN= (gameImage[0])/4+1
                print(minNumber, maxNumber, tempN)
                showMaxMin= False
                if tempN>min(minNumber, maxNumber) and tempN<max(minNumber, maxNumber):
                    HOUSE= HOUSE-betBase
                    if gameTurn== 0:
                        print(gameTurn, "A0", moneyPlayerA)
                        moneyPlayerA= moneyPlayerA+betBase
                        print(gameTurn, "A1", moneyPlayerA)
                    else:
                        print(gameTurn, "B0", moneyPlayerB)
                        moneyPlayerB= moneyPlayerB+betBase
                        print(gameTurn, "B1", moneyPlayerB)
                else:
                    HOUSE= HOUSE+betBase
                    if gameTurn== 0:
                        print(gameTurn, "A0", moneyPlayerA)
                        moneyPlayerA= moneyPlayerA-betBase-5
                        print(gameTurn, "A1", moneyPlayerA)
                    else:
                        print(gameTurn, "B0", moneyPlayerB)
                        moneyPlayerB= moneyPlayerB-betBase-5
                        print(gameTurn, "B1", moneyPlayerB)
                    
                minNumber= (gameImage[0])/4+1
                maxNumber= (gameImage[1])/4+1
                    
    else:
        fill(190, 145, 165)
        
        
    rect(heightButtonX, heightButtonY, heightButtonW, heightButtonH)
    fill(255, 245, 215)
    textSize(20)
    text("Bet In", heightButtonX, heightButtonY)
    
    dW =  width/4
    
    if(mouseX>heightButtonX+dW-heightButtonW/2 and mouseX<heightButtonX+dW+heightButtonW/2 and mouseY>heightButtonY-heightButtonH/2 and mouseY<heightButtonY+heightButtonH/2):
        fill(250, 200, 215)
        if mousePressed and pressLock== False:
            pressLock= True
            if gameTurn== 0:
                moneyPlayerA= moneyPlayerA-5
            else:
                moneyPlayerB= moneyPlayerB-5
            gameTurn= 1-gameTurn
            randomImageList()
            betBase= 5
    else:
        fill(190, 145, 165)
    rect(heightButtonX+dW, heightButtonY, heightButtonW, heightButtonH)
    fill(255, 245, 215)
    textSize(20)
    text("No Bet", heightButtonX+dW, heightButtonY)
    
    rectMode(CENTER)
    
    if(mouseX>heightButtonX+width/2-heightButtonW/2 and mouseX<heightButtonX+width/2+heightButtonW/2 and mouseY>heightButtonY-heightButtonH/2 and mouseY<heightButtonY+heightButtonH/2):
        fill(250, 200, 215)
        image(helpImage, 1000, 1000)
        
    else:
        fill(190, 145, 165)
    rect(heightButtonX+width/2, heightButtonY, heightButtonW, heightButtonH)
    fill(255, 245, 215)
    textSize(20)
    text("Help", heightButtonX+width/2, heightButtonY)

    if moneyPlayerA <=  0:
        loser =  playerAName
        gameState =  2
    elif moneyPlayerB <=  0:
        gameState =  2
        loser =  playerBName
    elif HOUSE <=  0:
        loser =  "HOUSE"
        gameState =  2
            
            
def drawEndPage():
    global gameState, pressLock,  loser
    
    background(155, 145, 165)
    fill(250, 200, 215)
    textAlign(CENTER, CENTER)
    textSize(40)
    text("See ya soon!", width/2, height*2/5)
    
    if len(loser) > 0: 
        textSize(20)
        text(loser + " ran out of money. \n THAT'S UNLUCKY!",  width/2, height*1/2)
    
    fill(200, 200, 100)
    rectMode(CENTER)
    if(mouseX>width/2-width/12 and mouseX<width/2+width/12 and mouseY>height*3/4-height/16 and mouseY<height*3/4+height/16):
        fill(250, 200, 215)
        if mousePressed and pressLock ==  False:
            pressLock =  True
            saveScore(moneyPlayerA,  moneyPlayerB)
            resetVariable()
            gameState =  4
    else:
        fill(190, 145, 165)
    rect(width/2, height*3/4, width*2/5, height/20)
    fill(255, 245, 215)
    textSize(20)
    text("Back to Start", width/2, height*3/4)
    
    
def drawStartPage():
    global gameState, pressLock
    
    background(155, 145, 165)
    fill(250, 200, 215)
    textAlign(CENTER, CENTER)
    textSize(80)
    text("Wedge", width/2, height*3/10)
    fill(200, 200, 200)
    textSize(16)
    text("Press Space to Start or Backspace to Quit/Save ", width*1/2, height*6/8)
    text("You can always leave the game anytime \n by pressing BACKSPACE",  width*1/2,  height*8/9)
    
    rectMode(CENTER)
    if(mouseX>width/2-width/12 and mouseX<width/2+width/12 and mouseY>height*2/3-height/16 and mouseY<height*2/3+height/16):
        fill(250, 200, 215)
        if mousePressed and pressLock== False:
            pressLock= True
            gameState= 3
    else:
        fill(190, 145, 165)
    rect(width/2, height*2/3, width*2/5, height/20)
    fill(255, 245, 215)
    textSize(20)
    text("Set Ante", width/2, height*2/3)
    
    
    rectMode(CENTER)
    if(mouseX>width/2-width/12 and mouseX<width/2+width/12 and mouseY>height*5/9-height/16 and mouseY<height*5/9+height/16):
        fill(250, 200, 215)
        if mousePressed and pressLock== False:
            pressLock= True
            gameState= 4
    else:
        fill(190, 145, 165)
    rect(width/2, height*5/9, width*2/5, height/20)
    fill(255, 245, 215)
    textSize(20)
    text("Scoreboard", width/2, height*5/9)
    
    
def drawMenuPage():
    global moneyPlayerA, moneyPlayerB, maxMoney, HOUSE, pressLock
    global gameState
    
    background(155, 145, 165)
    textAlign(CENTER, CENTER)
    rectMode(CENTER)

    moneyPlayerA= moneyPlayerA//5*5
    moneyPlayerB= moneyPlayerB//5*5
    HOUSE= HOUSE//5*5
    
    noStroke()
    fill(255, 245, 215)
    text("Players", width/5, height/5-40)
    text("0", width/5, height/5+40)
    text(maxMoney, width*4/5, height/5+40)
    
    stroke(180, 199, 100)
    strokeWeight(10)
    line(width/5, height/5, width*4/5, height/5)
    
    text(int(moneyPlayerA), map(moneyPlayerA, 0, maxMoney, width/5, width*4/5), height/5-20)
    rect(map(moneyPlayerA, 0, maxMoney, width/5, width*4/5), height/5, 35, 20, 5)
    
    noStroke()
    fill(255, 245, 215)
    text("HOUSE", width/5, height/2-40)
    text("0", width/5, height/2+40)
    text(maxMoney, width*4/5, height/2+40)
    
    noStroke()
    fill(255, 245, 215)
    stroke(180, 199, 100)
    strokeWeight(10)
    line(width/5, height/2, width*4/5, height/2)
    
    text(int(HOUSE), map(HOUSE, 0, maxMoney, width/5, width*4/5), height/2-20)
    rect(map(HOUSE, 0, maxMoney, width/5, width*4/5), height/2, 35, 20, 5)
    
    noStroke()
    if(mouseX>width/2-width/8 and mouseX<width/2+width/8 and mouseY>height*6/9-20 and mouseY<height*6/9+20):
        if mousePressed and pressLock== False:
            pressLock= True
            gameState= 0
        fill(255, 225, 215)
    else:
        fill(155, 125, 115)
        
    rect(width/2, height*6/9, width/4, 40)
    textSize(20)
    fill(255, 255, 215)
    text("Finish", width*1/2, height*6/9)


def keyReleased():
    global moneyPlayerA, moneyPlayerB
    global playerAName, playerBName, nameLen
    global gameState
    global saveName,  saveEntered,  fileInput,  fileEntered,  scoreList
    
    if key== CODED or key== SHIFT:
        pass
        
    if gameState ==  0 and key ==  ' ':
        print("start")
        gameState =  5
        moneyPlayerA =  moneyPlayerA-5
        createVariable()
        
    if gameState ==  0 and key ==  BACKSPACE:
        print("exit game")
        gameState =  8
        
    elif gameState ==  1 and key ==  BACKSPACE:
        print("exit game")
        gameState =  2
        
    elif gameState ==  5:
        repeat =  isRepeat(scoreList,  playerAName)
        playerAName, gameState = typeIN(playerAName, gameState, True, repeat, nameLen, 6, False)
        
    elif gameState ==  6:
        repeat =  isRepeat(scoreList,  playerAName)
        playerBName, gameState = typeIN(playerBName, gameState, playerBName !=  playerAName, repeat, nameLen, 1, False)
            
    elif gameState ==  7:
        fileInput, fileEntered = typeIN(fileInput, gameState, True, False, 100, 0, True)
            
    elif gameState ==  8: 
        print("yes")
        saveName, saveEntered = typeIN(saveName, gameState, True, False, 100, 1, True)


def mouseReleased():
    global pressLock
    pressLock= False
    
    
def mouseDragged():
    global moneyPlayerA, moneyPlayerB, maxMoney, HOUSE
    global gameState,  scrollinc
    
    
    if gameState== 3 :
        if mouseX>= map(moneyPlayerA, 0, maxMoney, width/5, width*4/5)-15-50 and mouseX<= map(moneyPlayerA, 0, maxMoney, width/5, width*4/5)+15+50 and mouseY>height/5-20 and mouseY<height/5+20:
            moneyPlayerA= int(constrain(map(mouseX, width/5, width*4/5, 0, maxMoney), 0, maxMoney))
            moneyPlayerB= moneyPlayerA
        if mouseX>= map(HOUSE, 0, maxMoney, width/5, width*4/5)-15-50 and mouseX<= map(HOUSE, 0, maxMoney, width/5, width*4/5)+15+50 and mouseY>height/2-20 and mouseY<height/2+20:
            HOUSE= int(constrain(map(mouseX, width/5, width*4/5, 0, maxMoney), 0, maxMoney))
    
    elif gameState ==  4: 
        if pmouseY > mouseY: 
            scrollinc +=  0.05
        elif pmouseY < mouseY:
            if scrollinc > 0: 
                scrollinc -=  0.05
        if scrollinc > len(scoreList):
            scrollinc =  0  
        
