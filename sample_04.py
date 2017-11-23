#####################################################################################
#
# Sample 04 - # Sample 05 - This sample presents Tone
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


#-------------------------------------
# my code here
#-------------------------------------
def main():
    
    
    printToConsol("----------------------------",ConsoleColor.ccBlue.value)
    printToConsol("3dRudder")
    printToConsol("----------------------------")
    printToConsol("Start Sample 04",ConsoleColor.ccWhite.value)
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
		
                sdk.PlaySndEx(0, "a4(500, 0)a4(500, 0)a4(500, 0)f4(350, 0)c5(150, 0)a4(500, 0)f4(350, 0)c5(150, 0)a4(650, 50)e5(500, 0)e5(500, 0)e5(500, 0)")
                sdk.PlaySndEx(0, "f5(350, 0)c5(150, 0)g#4(500, 0)f4(350, 0)c5(150, 0)a4(650, 50)")

                sdk.PlaySndEx(0, "a5(500, 0)a4(300, 0)a4(150, 0)a5(500, 0)g#5(325, 0)g5(175, 0)f#5(125, 0)f5(125, 0)f#5(250, 325)a#4(250, 0)d#5(500, 0)d5(325, 0)")
                sdk.PlaySndEx(0, "c#5(175,0)c5(125,0)b4(125,0)c5(250,350)")

                sdk.PlaySndEx(0, "f4(250, 0)g#4(500, 0)f4(350, 0)a4(125, 0)c5(500, 0)a4(375, 0)c5(125, 0)e5(650, 500)")

                sdk.PlaySndEx(0, "a5(500, 0)a4(300, 0)a4(150, 0)a5(500, 0)g#5(325, 0)g5(175, 0)f#5(125, 0)f5(125, 0)f#5(250, 325)a#4(250, 0)d#5(500, 0)d5(325, 0)")
                sdk.PlaySndEx(0, "c#5(175,0)c5(125,0)b4(125,0)c5(250,350)")

                sdk.PlaySndEx(0, "f4(250, 0)g#4(500, 0)f4(375, 0)c5(125, 0)a4(500, 0)f4(375, 0)c5(125, 0)a4(650, 650)")
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



