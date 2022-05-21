import PySimpleGUI as sg
import cv2
import numpy as np

def main():
    sg.thme("LightGreen")

    #define the window layout
    layout = [
        [sg.Text("OpenCV Demo", size = (60,1), justification = "center")],
        [sg.Tmage(filename = "", key = "-IMAGE-")],
        