from  ns3DRudder import *

sdk=GetSDK()

version=sdk.GetFirmwareVersion(0)
print ("{:02x}".format(version))

print (sdk.GetNumberOfConnectedDevice())

state = State()
sdk.Get3DRudderState(0,state)
print (state.status)

sdk.PlaySnd(0,1000,1000)

