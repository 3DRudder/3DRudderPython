#####################################################################################
#
# Sample 01 - This sample presents the basic Function of the SDK.
#
# Python 3.5.2
# 
# SDK 3dRudder
#
# Copyright (C) 2010-2017 3dRudder
#
#####################################################################################
import platform
import time

# 32 or 64 bit
val_max=platform.architecture()



print(val_max[0])
if (val_max[0]=='32bit') : 
    from win32.Python352.ns3DRudder import * #import SDk 3dRudder
else:
    from x64.Python352.ns3DRudder import * #import SDk 3dRudder

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


#####################################################################################
#####################################################################################					
def OptionNomalized():
    #Get Axis Value NormalizedValue
    sdk.GetAxis(0,NormalizedValue,axis)
    print ("Axis NormalizedValue Value : [{:.2f},{:.2f},{:.2f},{:.2f}]".format(axis.m_aX,axis.m_aY,axis.m_aZ,axis.m_rZ)) 

	
#####################################################################################
#####################################################################################	
def OptionUserRefAngle():
    #Get Axis Value UserRefAngle
    sdk.GetAxis(0,UserRefAngle,axis)
    print ("Axis UserRefAngle Value : [{:.2f},{:.2f},{:.2f},{:.2f}]".format(axis.m_aX,axis.m_aY,axis.m_aZ,axis.m_rZ)) 


#####################################################################################
#####################################################################################
def OptionCustomerCurves():

    #Get Axis Value ValueWithCurve
    curves=CurveArray()

    #curves.InitLinear()

    #roll
    roll=Curve()
    roll.SetDeadZone(50.0)
    roll.SeXSat(1.0)
    roll.SetYMax(1.0)
    roll.SetExp(3.0)
    curves.SetCurve(CurveRoll,roll)

    #pitch
    pitch=Curve()
    pitch.SetDeadZone(50.0)
    pitch.SeXSat(1.0)
    pitch.SetYMax(1.0)
    pitch.SetExp(3.0)
    curves.SetCurve(CurvePitch,pitch)

    #upDown
    upDown=Curve()
    upDown.SetDeadZone(50.0)
    upDown.SeXSat(1.0)
    upDown.SetYMax(1.0)
    upDown.SetExp(3.0)
    curves.SetCurve(CurveUpDown,upDown)

    #yaw
    yaw=Curve()
    yaw.SetDeadZone(50.0)
    yaw.SeXSat(1.0)
    yaw.SetYMax(1.0)
    yaw.SetExp(3.0)
    curves.SetCurve(CurveYaw,yaw)

   
    sdk.GetAxis(0,ValueWithCurve,axis,curves)
    print ("Axis ValueWithCurve Value : [{:.2f},{:.2f},{:.2f},{:.2f}]".format(axis.m_aX,axis.m_aY,axis.m_aZ,axis.m_rZ)) 

   
	
#####################################################################################
#####################################################################################	
def OptionSetLinearCurves():	
    #Get Axis Value ValueWithCurve
    curves=CurveArray()
    curves.InitLinear()

    sdk.GetAxis(0,ValueWithCurve,axis,curves)
    print ("Axis ValueWithCurve - Linear Value : [{:.2f},{:.2f},{:.2f},{:.2f}]".format(axis.m_aX,axis.m_aY,axis.m_aZ,axis.m_rZ)) 

#####################################################################################
#####################################################################################	
def OptionSetFactoryCurves():	
    #Get Axis Value ValueWithCurve
    curves=CurveArray()
    curves.InitFactory()

    sdk.GetAxis(0,ValueWithCurve,axis,curves)
    print ("Axis ValueWithCurve - Factory Value : [{:.2f},{:.2f},{:.2f},{:.2f}]".format(axis.m_aX,axis.m_aY,axis.m_aZ,axis.m_rZ)) 


#####################################################################################	
#####################################################################################	
def OptionGetParamsCurves():
    
    
    #yaw=Curve()
    #pitch=Curve()
    #roll=Curve()
    #upDown=Curve()

    #curves=CurveArray()
    sdk.GetAxis(0,NormalizedValue,axis)

    curves=CurveArray()

    roll = curves.GetCurve(CurveRoll)
    yaw = curves.GetCurve(CurveYaw)
    pitch = curves.GetCurve(CurvePitch)
    upDown = curves.GetCurve(CurveUpDown)


    #Get Curve Value Yaw
    #print ("Yaw Curve Value : [{:.2f},{:.2f},{:.2f},{:.2f}]".format(yaw.GetDeadZone(),yaw.GeXSat(),yaw.GetYMax(),yaw.GetExp())) 
    print ("Yaw Curve Value : [{:.2f},{:.2f},{:.2f},{:.2f}]".format(yaw.GetDeadZone(),yaw.GeXSat(),yaw.GetYMax(),yaw.GetExp())) 
    

    #Get Curve Value Pitch
    print ("Pitch Curve Value : [{:.2f},{:.2f},{:.2f},{:.2f}]".format(pitch.GetDeadZone(),pitch.GeXSat(),pitch.GetYMax(),pitch.GetExp())) 

    #Get Curve Value Roll
    print ("Roll Curve Value : [{:.2f},{:.2f},{:.2f},{:.2f}]".format(roll.GetDeadZone(),roll.GeXSat(),roll.GetYMax(),roll.GetExp())) 

    #Get Curve Value UpDown
    print ("UpDown Curve Value : [{:.2f},{:.2f},{:.2f},{:.2f}]".format(upDown.GetDeadZone(),upDown.GeXSat(),upDown.GetYMax(),upDown.GetExp())) 


#####################################################################################               
#####################################################################################               
def OptionDisplaySensors():
    
    #Get sensor value
    print ("Sensor  Value : [{:d},{:d},{:d},{:d},{:d},{:d}] ".format(sdk.GetSensor( nPortNumber ,0 ),sdk.GetSensor( nPortNumber , 1 ),sdk.GetSensor( nPortNumber , 2 ),sdk.GetSensor( nPortNumber , 3 ),sdk.GetSensor( nPortNumber , 4 ),sdk.GetSensor( nPortNumber , 5 )))


#####################################################################################
 # Main
#####################################################################################
print ("Start Sample.py")
print ("------------------------")



#Init
try:

    #Init SDk 3dRudder
    sdk=GetSDK()
    sdk.Init()

    # 3dRudder 1
    nPortNumber=0
	
	
    #Check that the 3dRudder 1 is connected
    while not sdk.IsDeviceConnected (nPortNumber):
        print("3dRudder is not Connected")
        time.sleep(1)
    
    #Get Version of SDK
    versionSdk=sdk.GetSDKVersion()
    print ("Version SDK : {:1x}".format(versionSdk))
    
    #Get Version of The Firmware
    version=sdk.GetVersion(nPortNumber)
    print ("Version FirmWare : {:1x}".format(version))

    #Get the number of the 3dRudder are connected
    print ("Get the Number the 3dRudder are connected : {:1x}".format(sdk.GetNumberOfConnectedDevice()))

    #Play a sound wih the 3dRudder
    sdk.PlaySnd(nPortNumber,1000,1000)


    # Wait 3dRudder initialized
    while(sdk.GetStatus(nPortNumber)<2):
        print("3drudder init...")
        time.sleep(1)

except KeyboardInterrupt as e:
    print ("->Stop by User")
   
   
except ValueError as err:
    print ("Error : ",err )


icontinue=1
while(icontinue==1):

    try:

        
        #  Select type curve 3drudder
        print("Select type curve 3drudder")
        print("1- NormalizedValue")
        print("2- UserRefAngle")
        print("3- ValueWithCurve (NormalizedValue)")
        print("4- ValueWithCurve / Lineaire Curves (NormalizedValue)")
        print("5- ValueWithCurve / Factory Curves (NormalizedValue)")
        print("6- Get Params Curves")
        print("7- Display Sensors Value")


        ch = input()    
        nn = int(ch)

        options= { 1:OptionNomalized,
                   2:OptionUserRefAngle,
                    3:OptionCustomerCurves,
                    4:OptionSetLinearCurves,
                    5:OptionSetFactoryCurves,
                    6:OptionGetParamsCurves,
                    7:OptionDisplaySensors
                }


        axis = Axis()


        while True:

            #Get Status of the 3dRudder
            print ("*****************************************************************")
            print ("Status 3dRudder : {:1} ".format(status_3dRudder[sdk.GetStatus(nPortNumber)]))


            options[nn]()
        
            
            time.sleep(1) #second

    except KeyboardInterrupt as e:
        print ("->Stop by User")
    
    
    except ValueError as err:
        print ("Error : ",err )

    finally:

        print("Continue Sample ? (1/0)")
        ch = input()    
        icontinue = int(ch)
        
print ("------------------------")
print ("End Sample.py")
	
