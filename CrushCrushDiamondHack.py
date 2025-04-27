from uniref import WinUniRef
import uniref
import os
def GetProcess(process_name : str):
    try:
        return WinUniRef(process_name)
    except AttributeError:
        print("Not Founded Process {}".format(process_name))
        os._exit(4421)

def SetDiamonds_Force(diamonds : int):
    process = GetProcess("CrushCrush.exe")
    utilities = process.find_class_in_image("Assembly-CSharp.dll", "Utilities")
    AwardDiamonds_Force = utilities.find_method("AwardDiamonds", param_count=2)
    if(AwardDiamonds_Force.is_static() is True):
        AwardDiamonds_Force(args=(diamonds, True))
    else:
        print("This Function is not Static!!!")