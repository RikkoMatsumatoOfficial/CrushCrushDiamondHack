import dearpygui.dearpygui as dpg
import os
import sys
from typing import Optional
import CrushCrushDiamondHack as diamondhack
def GetValue(value):
    return dpg.get_value(value)
def Set_Height(height : int):
    return int(height)
def Set_Width(width : int):
    return int(width)

def CallHackDiamond():
    diamondhack.SetDiamonds_Force(GetValue("diamondhackcrushcrush"))
class DPG_GUI:
    def DPG_Createcontext():
        return dpg.create_context()
    def DPG_CreateViewport(titlename : str, width_int : int, height_int : int, windowname: Optional[str]):
        dpg.create_viewport(title=titlename, width=width_int, height=height_int)
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.set_primary_window(windowname, True)
        dpg.start_dearpygui()
        dpg.destroy_context()
    def SetGUI():
        DPG_GUI.DPG_Createcontext()
        with dpg.window(label="CrushCrushDiamondHack by RikkoMatsumatoOfficial", tag="crushcrushwindowdiamond", height=Set_Height(800), width=Set_Width(800)):
            dpg.add_slider_int(label="Diamond to Hack!!!", min_value=0, max_value=45000000, tag="diamondhackcrushcrush")
            dpg.add_button(label="Set Diamond!!!", tag="buttonhackdiamond", callback=CallHackDiamond)
            dpg.add_text("This is My First Trying Hack Diamonds for Game Crush Crush(Developed by Sadpanda!!!)... \nSo Enjoy to use this!!!")
        DPG_GUI.DPG_CreateViewport("CrushCrushDiamondHack by RikkoMatsumatoOfficial", Set_Height(800), Set_Width(800), "crushcrushwindowdiamond")
