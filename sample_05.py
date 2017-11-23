#####################################################################################
#
# Sample 05 - This sample presents Tone
#
# Python 3.5.2
# 
# SDK 3dRudder
#
# Copyright (C) 2016-2017 3dRudder
#
#####################################################################################

import time
import platform

from enum import Enum
import ctypes
import sys
import msvcrt
import ctypes


STD_OUTPUT_HANDLE=-11


# 32 or 64 bit
val_max=platform.architecture()

print(val_max[0])
if (val_max[0]=='32bit') : 
    from win32.Python363.ns3DRudder import * #import SDk 3dRudder
else:
    from x64.Python363.ns3DRudder import * #import SDk 3dRudder




#-------------------------------------
#-------------------------------------        
class ConsoleColor(Enum):

	ccBlack = 0
	ccDarkBlue=1
	ccGreen=2
	ccGrayBlue=3
	ccBrown=4
	ccPurple=5
	ccKaki=6
	ccLightGray=7
	ccGray=8
	ccBlue=9
	ccFluorescentGreen=10
	ccTurquoise=11
	ccRed=12
	ccFluorescentPink=13
	ccFluorescentYellow=14
	ccWhite=15



std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)


#-------------------------------------
#-------------------------------------
class CEvent(IEvent):
    
    def __init__(self) :
        IEvent.__init__(self)
        printToConsol("Create Event",ConsoleColor.ccWhite.value)

    def OnConnect(self,nDeviceNumber):
       printToConsol("-> 3dRudder is Connected",ConsoleColor.ccGreen.value)
       
    def OnDisconnect(self,nDeviceNumber):
        printToConsol("-> 3dRudder is DisConnected",ConsoleColor.ccRed.value)

#-------------------------------------
#-------------------------------------  
def set_color(mycolor, handle=std_out_handle):
    
    bret = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, mycolor)
    return bret


#-------------------------------------
#-------------------------------------
def printToConsol(msg,color=-1):
    
    if color !=-1 :
        set_color(color)
    print(msg)    


def PlayTheme(sdk,fPitch=0.0,numMusic=0):
    
    
    # Mario
    if(numMusic=='0'):
        listTone = [ Tone(660,10,15),Tone( 660,10,30),Tone(660,10,30),Tone(510,10,10),Tone(660,10,30),Tone(770,10,55),Tone(380,10,57),Tone(510,10,45),Tone(380,10,40),Tone(320,10,50),Tone(440,10,30),Tone(480,8,33),
                    Tone( 450,10,15 ),Tone( 430,10,30 ),Tone( 380,10,20 ),Tone( 660, 8,20 ),Tone( 760, 5,15 ),Tone( 860,10,30 ),Tone( 700, 8,15 ),Tone( 760, 5,35 ),Tone( 660, 8,30 ),Tone( 520, 8,15 ),Tone( 580, 8,15 ),Tone( 480, 8,50 ),
                    Tone( 510,10,45 ),Tone( 380,10,40 ),Tone( 320,10,50 ),Tone( 440,10,30 ),Tone( 480, 8,33 ),Tone( 450,10,15 ),Tone( 430,10,30 ),Tone( 380,10,20 ),Tone( 660, 8,20 ),Tone( 760, 5,15 ),Tone( 860,10,30 ),Tone( 700, 8,15 ),
                    Tone( 760, 5,35 ),Tone( 660, 8,30 ),Tone( 520, 8,15 ),Tone( 580, 8,15 ),Tone( 480, 8,50 ),Tone( 500,10,30 ),Tone( 760,10,10 ),Tone( 720,10,15 ),Tone( 680,10,15 ),Tone( 620,15,30 ),Tone( 650,15,30 ),Tone( 380,10,15 ),
                    Tone( 430,10,15 ),Tone( 500,10,30 ),Tone( 430,10,15 ),Tone( 500,10,10 ),Tone( 570,10,22 ),Tone( 500,10,30 ),Tone( 760,10,10 ),Tone( 720,10,15 ),Tone( 680,10,15 ),Tone( 620,15,30 ),Tone( 650,20,30 ),Tone( 1020,8,30 ),
                    Tone( 1020,8,15 ),Tone( 1020,8,30 ),Tone( 380,10,30 ),Tone( 500,10,30 ),Tone( 760,10,10 ),Tone( 720,10,15 ),Tone( 680,10,15 ),Tone( 620,15,30 ),Tone( 650,15,30 ),Tone( 380,10,15 ),Tone( 430,10,15 ),Tone( 500,10,30 ),
                    Tone( 430,10,15 ),Tone( 500,10,10 ),Tone( 570,10,42 ),Tone( 585,10,45 ),Tone( 550,10,42 ),Tone( 500,10,36 ),Tone( 380,10,30 ),Tone( 500,10,30 ),Tone( 500,10,15 ),Tone( 500,10,30 ),Tone( 500,10,30 ),Tone( 760,10,10 ),
                    Tone( 720,10,15 ),Tone( 680,10,15 ),Tone( 620,15,30 ),Tone( 650,15,30 ),Tone( 380,10,15 ),Tone( 430,10,15 ),Tone( 500,10,30 ),Tone( 430,10,15 ),Tone( 500,10,10 ),Tone( 570,10,22 ),Tone( 500,10,30 ),Tone( 760,10,10 ),
                    Tone( 720,10,15 ),Tone( 680,10,15 ),Tone( 620,15,30 ),Tone( 650,20,30 ),Tone( 1020,8,30 ),Tone( 1020,8,15 ),Tone( 1020,8,30 ),Tone( 380,10,30 ),Tone( 500,10,30 ),Tone( 760,10,10 ),Tone( 720,10,15 ),Tone( 680,10,15 ),
                    Tone( 620,15,30 ),Tone( 650,15,30 ),Tone( 380,10,15 ),Tone( 430,10,15 ),Tone( 500,10,30 ),Tone( 430,10,15 ),Tone( 500,10,10 ),Tone( 570,10,42 ),Tone( 585,10,45 ),Tone( 550,10,42 ),Tone( 500,10,36 ),Tone( 380,10,30 ),
                    Tone( 500,10,30 ),Tone( 500,10,15 ),Tone( 500,10,30 ),Tone( 500, 6,15 ),Tone( 500, 8,30 ),Tone( 500, 6,35 ),Tone( 500, 8,15 ),Tone( 580, 8,35 ),Tone( 660, 8,15 ),Tone( 500, 8,30 ),Tone( 430, 8,15 ),Tone( 380, 8,60 ),
                    Tone( 500, 6,15 ),Tone( 500, 8,30 ),Tone( 500, 6,35 ),Tone( 500, 8,15 ),Tone( 580, 8,15 ),Tone( 660, 8,55 ),Tone( 870, 8,32 ),Tone( 760, 8,60 ),Tone( 500, 6,15 ),Tone( 500, 8,30 ),Tone( 500, 6,35 ),Tone( 500, 8,15 ),
                    Tone( 580, 8,35 ),Tone( 660, 8,15 ),Tone( 500, 8,30 ),Tone( 430, 8,15 ),Tone( 380, 8,60 ),Tone( 660,10,15 ),Tone( 660,10,30 ),Tone( 660,10,30 ),Tone( 510,10,10 ),Tone( 660,10,30 ),Tone( 770,10,55 ),Tone( 380,10,57 ) 
                    ]
    # MI
    if(numMusic=='1'):
        listTone = [ Tone(784,15,30),
                    Tone(784,15,30 ),Tone(784,15,30 ),Tone(932,15,15 ),Tone( 1047,15,15 ),Tone( 784,15,30 ),Tone( 784,15,30 ),Tone( 699,15,15 ),Tone( 740,15,15 ),Tone( 784,15,30 ),Tone( 784,15,30),Tone( 932,15,15 ),Tone( 1047,15,15),
                    Tone( 784,15,30 ),Tone( 784,15,30),Tone( 699,15,15),Tone( 740,15,15 ),Tone( 932,15, 0 ),Tone( 784,15, 0 ),Tone( 587,120,7 ),Tone( 932,15, 0 ),Tone( 784,15, 0 ),Tone( 554,120,7),Tone( 932,15, 0 ),Tone( 784,15, 0 ),
                    Tone(523,120,15 ),Tone(466,15,0 ),Tone(523,150,0),
                    Tone(784,15,30 ),Tone(784,15,30),Tone(699,15,15 ),Tone(740,15,15 ),Tone(932,15, 0 ),Tone(784,15, 0 ),Tone(587,120,7 ),Tone(932,15, 0 ),Tone(784,15, 0 ),Tone(554,120,7 ),Tone( 932,15, 0 ),Tone( 784,15, 0),
                    Tone( 523,120,15 ),Tone( 466,15,0),Tone( 523,150,0) 
                    ]
        

    if(numMusic=='1' or  numMusic=='0'):
        if sdk.IsDeviceConnected(0):
            for i in range(0,len(listTone)) :
                if(fPitch!=0.0) :
                    listTone[i].m_nFrequency = listTone[i].m_nFrequency * (int)(2.0 * fPitch)
                sdk.PlaySndEx(0,1,listTone[i])

    
#-------------------------------------
# my code here
#-------------------------------------
def main():
    
    
    printToConsol("----------------------------",ConsoleColor.ccBlue.value)
    printToConsol("3dRudder")
    printToConsol("----------------------------")
    printToConsol("Start Sample 05",ConsoleColor.ccWhite.value)
    printToConsol("Stop Sample : Ctrl + c ",ConsoleColor.ccFluorescentYellow.value)
   
    
    # 3dRudder settings
    nPortNumber=0
    myevent = CEvent()
	
    try:
        # Init SDk 3dRudder
        sdk=GetSDK()
        sdk.SetEvent(myevent)
        sdk.Init()
       
        printToConsol("Firmware Version : {:1x}".format(sdk.GetVersion(nPortNumber)),ConsoleColor.ccKaki.value)
        printToConsol("SDK Version : {:04x}".format(sdk.GetSDKVersion()),ConsoleColor.ccKaki.value)


        while True:
            
            if (sdk.IsDeviceConnected(nPortNumber)):
                printToConsol("press any key to play, 'Q' to quit,'+' or '-' to change the pitch, '0'(Mario) or '1' (MI) music",ConsoleColor.ccPurple.value)
                nPitch=0
                fPitch=0.0
                while True:
                    #choice = input()
                    choice = msvcrt.getwch()
                    print(choice)
                    if (choice == '+' or choice == '-'):
                        if choice == '+':
                            nPitch+=1
                        if choice == '-':
                            nPitch-=1
                        if nPitch >= 0:
                        
                            fPitch = nPitch
                            printToConsol("Pitch : {:1x}".format(fPitch),ConsoleColor.ccGray.value) 
                        if (nPitch < 0) :
                            fPitch = 1.0 / (-nPitch)*1.0
                            printToConsol("Pitch : 1/{:1x}".format(nPitch),ConsoleColor.ccGray.value)
                    else : break
                if (choice == 'Q' or choice == 'q'):
                    break
                if(choice=='0' or choice=='1'):
                    PlayTheme(sdk,fPitch,choice)
                else:
                    PlayTheme(sdk,fPitch)
            else:
                time.sleep(1)
        

    except KeyboardInterrupt as e:
        set_color(ConsoleColor.ccRed.value)
        print ("->Stop by User")
   
    except ValueError as err:
        set_color(ConsoleColor.ccRed.value)
        print ("Error : ",err )    
    finally:

        set_color(ConsoleColor.ccBlue.value)
        print("End Sample 05")
        print("----------------------------")
        set_color(ConsoleColor.ccWhite.value)


#-------------------------------------
#-------------------------------------
if(__name__ == "__main__"):
    main()



