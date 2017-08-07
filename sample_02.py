#####################################################################################
#
# Sample 02 - This sample presents the Custom Curves.
#
# Python 3.5.2
# 
# SDK 3dRudder
#
# Copyright (C) 2016-2017 3dRudder
#
#####################################################################################
import platform



# 32 or 64 bit
val_max=platform.architecture()

print(val_max[0])
if (val_max[0]=='32bit') : 
    from win32.ns3DRudder import * #import SDk 3dRudder
else:
    from x64.ns3DRudder import * #import SDk 3dRudder
import time



#define the Status of the 3dRudder
status_3dRudder = [ "None",
                    "Puts the 3DRudder on the floor",
                    "The 3dRudder initialize for about 2 seconds",
                    "Put your first feet on the 3dRudder",
                    "Put your second Foot on the 3dRudder",
                    "The user must wait still for half a second for calibration until a last short beep is heard from the device. The 3DRudder is ready to be used.",
                    "The 3dRudder is in use",
                    "The 3dRudder is in use and is fully operational with all the features enabled"
                    ]


#-------------------------------------
# My Curve
#-------------------------------------
class MyCurve (Curve):
    
    def __init__(self,fDeadZone,fxSat,fyMax,fExp):
        Curve.__init__(self,fDeadZone,fxSat,fyMax,fExp)
        pass

    def CalcCurveValue (self,fValue):
        return 0.2

 
#-------------------------------------
#-------------------------------------
def InitContex(sdk,nPortNb):
    
    # Init SDk 3dRudder
    sdk.Init()
    #Check that the 3dRudder 1 is connected
    while not sdk.IsDeviceConnected (nPortNb):
        print("3dRudder is not Connected")
        time.sleep(1)
    print("-> 3dRudder is Connected") 

    # Wait 3dRudder initialized
    while(sdk.GetStatus(nPortNb)<6):
        print ("Status 3dRudder : {:1} ".format(status_3dRudder[sdk.GetStatus(nPortNb)]))
        time.sleep(1)
    print("-> 3drudder init OK")
#-------------------------------------
# my code here
#-------------------------------------
def main():
    print("----------------------------")
    print("3dRudder")
    print("----------------------------")
    print("Start Sample")


    # 3dRudder settings
    nPortNumber=0

    try:

        sdk=GetSDK()
        InitContex(sdk,nPortNumber)
              
        curves=CurveArray()
        
        
        fDeadZone=0.0
        fxSat=1.0;
        fyMax=1.0;
        fExp=1.0;

        #Roll
        axis=Axis()
        roll=MyCurve(fDeadZone,fxSat,fyMax,fExp)
        curves.SetCurve(CurveRoll,roll)

        #pitch
        pitch=MyCurve(fDeadZone,fxSat,fyMax,fExp)
        curves.SetCurve(CurvePitch,pitch)

        #upDown
        upDown=MyCurve(fDeadZone,fxSat,fyMax,fExp)
        curves.SetCurve(CurveUpDown,upDown)

        #yaw
        yaw=MyCurve(fDeadZone,fxSat,fyMax,fExp)
        curves.SetCurve(CurveYaw,yaw)
        
        while True:
            #sdk.GetAxis(nPortNumber,ValueWithCurve,axis,curves)
            sdk.GetAxis(nPortNumber,ValueWithCurve,axis,curves)
            print ("Axis ValueWithCurve Value : [{:.2f},{:.2f},{:.2f},{:.2f}]".format(axis.m_aX,axis.m_aY,axis.m_aZ,axis.m_rZ))
            time.sleep(1) 

    except KeyboardInterrupt as e:
        print ("->Stop by User")
   
    except ValueError as err:
        print ("Error : ",err )    
    finally:
        print("End Sample")
        print("----------------------------")




#-------------------------------------
#-------------------------------------
if(__name__ == "__main__"):
    main()



