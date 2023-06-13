#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.1),
    on June 13, 2023, at 15:50
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

import psychopy
psychopy.useVersion('2023.1.1')


# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Run 'Before Experiment' code from Settings_
from datetime import datetime
current_date = datetime.now().strftime("%Y_%m_%d") #Sets current date for foldername


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2023.1.1'
expName = 'TCET'  # from the Builder filename that created this script
expInfo = {
    'Participant_ID': 'S00',
    'Version': ['Standard','Short'],
    'Language': ['EN','CN'],
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/TCET_%s_%s/TCET_%s_%s_%s_Tasklog' %(expInfo['Participant_ID'], current_date, expInfo['Participant_ID'], expInfo['date'], expInfo['Version']) 

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\tanlab1\\Desktop\\NAP Study (local)\\threat-conditioning-and-extinction-task\\TCET_Sharif_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='', color='black', colorSpace='rgb',
    backgroundImage='', backgroundFit='fill',
    blendMode='avg', useFBO=True)
win.mouseVisible = True
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}
ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='ptb')

# --- Initialize components for Routine "Settings" ---
# Run 'Begin Experiment' code from Settings_
import random
random.seed()  # Seeds the random number generator

# List of schedule files
schedule_files = ['1_PreCondition.xlsx', '2_Condition.xlsx', '3_Extinction.xlsx']

# If experiment version is 'Short', modify the filenames in the list
if expInfo['Version'] == 'Short':
    for i, filename in enumerate(schedule_files):
        schedule_files[i] = filename.replace('.xlsx', '_Short.xlsx')

# Print the schedule files being used
print("Schedule files used:", schedule_files)

skipPhases = False  # Flag to determine if phases should be skipped (only show instructions and ratings)

parallelTrigger = False  # Flag to determine if parallel triggering is enabled
lfpTrigger = False  # Flag to determine if LFP parallel triggering (for Jingyu device) is enabled

# If parallel triggering is enabled
if parallelTrigger:
    from psychopy import parallel
    port = parallel.ParallelPort(address=0x0378)  # Initialize parallel port
    port.setData(0)  # Set parallel port data to 0

    if lfpTrigger:  # If LFP triggering is also enabled
        lfpCtrlPort = parallel.ParallelPort(address=0x037A)  # Initialize LFP control parallel port
        lfpCtrlPort.setData(0)  # Set LFP control parallel port data to 0



# --- Initialize components for Routine "PreCondInst" ---
PreCondImage = visual.ImageStim(
    win=win,
    name='PreCondImage', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0.05], size=[0.45,0.9],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
PreCondImageOverview = visual.ImageStim(
    win=win,
    name='PreCondImageOverview', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0.05], size=[1.5,0.9],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
PreCondInstEN = visual.TextStim(win=win, name='PreCondInstEN',
    text='',
    font='Arial',
    pos=[0,0.7], height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
PreCondInstCN = visual.TextStim(win=win, name='PreCondInstCN',
    text='',
    font='PingFang SC',
    pos=[-0.3,0.7], height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
PreCondRespKey = keyboard.Keyboard()
PreCondMouse = event.Mouse(win=win)
x, y = [None, None]
PreCondMouse.mouseClock = core.Clock()
PreCondSubmitEN = visual.ButtonStim(win, 
    text='CONTINUE', font='Arial',
    pos=[0.7, -0.8],
    letterHeight=0.06,
    size=[0.3, 0.1], borderWidth=0.0,
    fillColor=[0.8824, 0.6392, 0.4432], borderColor=None,
    color='black', colorSpace='rgb',
    opacity=1.0,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='PreCondSubmitEN',
    depth=-6
)
PreCondSubmitEN.buttonClock = core.Clock()
PreCondSubmitCN = visual.ButtonStim(win, 
    text='继续', font='PingFang SC',
    pos=[0.7, -0.8],
    letterHeight=0.06,
    size=[0.3, 0.1], borderWidth=0.0,
    fillColor=[0.8824, 0.6392, 0.4432], borderColor=None,
    color='black', colorSpace='rgb',
    opacity=1.0,
    bold=False, italic=False,
    padding=None,
    anchor='center',
    name='PreCondSubmitCN',
    depth=-7
)
PreCondSubmitCN.buttonClock = core.Clock()

# --- Initialize components for Routine "trialPreCond" ---
imagePreCond = visual.ImageStim(
    win=win,
    name='imagePreCond', 
    image='default.png', mask=None, anchor='center',
    ori=0, pos=[0, 0], size=[2, 2],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
PreCondTriggMouse = event.Mouse(win=win)
x, y = [None, None]
PreCondTriggMouse.mouseClock = core.Clock()
PreCondTriggKey = keyboard.Keyboard()

# --- Initialize components for Routine "ITI" ---
FixCross = visual.ShapeStim(
    win=win, name='FixCross', vertices='cross',
    size=(0.05, 0.07),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# --- Initialize components for Routine "Rating" ---
image = visual.ImageStim(
    win=win,
    name='image', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0.1], size=[0.45,0.9],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
RatingInstEN = visual.TextStim(win=win, name='RatingInstEN',
    text='',
    font='Arial',
    pos=[0,0.7], height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
RatingInstCN = visual.TextStim(win=win, name='RatingInstCN',
    text='',
    font='PingFang SC',
    pos=[0,0.7], height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
Scale = visual.Slider(win=win, name='Scale',
    startValue=None, size=(1.3, 0.05), pos=(0, -0.5), units=win.units,
    labels=['– Negative', 'Positive +'], ticks=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='beige', lineColor='White', colorSpace='rgb',
    font='Arial', labelHeight=0.04,
    flip=False, ori=0.0, depth=-3, readOnly=False)
RatingKey = keyboard.Keyboard()
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
SubmitEN = visual.ButtonStim(win, 
    text='SUBMIT', font='Arial',
    pos=[0.7, -0.8],
    letterHeight=0.06,
    size=[0.3, 0.1], borderWidth=0.0,
    fillColor=[0.8824, 0.6392, 0.4432], borderColor=None,
    color='black', colorSpace='rgb',
    opacity=1.0,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='SubmitEN',
    depth=-6
)
SubmitEN.buttonClock = core.Clock()
SubmitCN = visual.ButtonStim(win, 
    text='提交', font='PingFang SC',
    pos=[0.7, -0.8],
    letterHeight=0.06,
    size=[0.3, 0.1], borderWidth=0.0,
    fillColor=[0.8824, 0.6392, 0.4432], borderColor=None,
    color='black', colorSpace='rgb',
    opacity=1.0,
    bold=False, italic=False,
    padding=None,
    anchor='center',
    name='SubmitCN',
    depth=-7
)
SubmitCN.buttonClock = core.Clock()

# --- Initialize components for Routine "CondInst" ---
CondImage = visual.ImageStim(
    win=win,
    name='CondImage', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0.05], size=[0.45,0.9],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
CondImageOverview = visual.ImageStim(
    win=win,
    name='CondImageOverview', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0.05], size=[1.5,0.9],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
CondInstEN = visual.TextStim(win=win, name='CondInstEN',
    text='',
    font='Arial',
    pos=[0,0.7], height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
CondInstCN = visual.TextStim(win=win, name='CondInstCN',
    text='',
    font='PingFang SC',
    pos=[-0.3,0.7], height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
CondRespKey = keyboard.Keyboard()
CondMouse = event.Mouse(win=win)
x, y = [None, None]
CondMouse.mouseClock = core.Clock()
CondSubmitEN = visual.ButtonStim(win, 
    text='CONTINUE', font='Arial',
    pos=[0.7, -0.8],
    letterHeight=0.06,
    size=[0.3, 0.1], borderWidth=0.0,
    fillColor=[0.8824, 0.6392, 0.4432], borderColor=None,
    color='black', colorSpace='rgb',
    opacity=1.0,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='CondSubmitEN',
    depth=-6
)
CondSubmitEN.buttonClock = core.Clock()
CondSubmitCN = visual.ButtonStim(win, 
    text='继续', font='PingFang SC',
    pos=[0.7, -0.8],
    letterHeight=0.06,
    size=[0.3, 0.1], borderWidth=0.0,
    fillColor=[0.8824, 0.6392, 0.4432], borderColor=None,
    color='black', colorSpace='rgb',
    opacity=1.0,
    bold=False, italic=False,
    padding=None,
    anchor='center',
    name='CondSubmitCN',
    depth=-7
)
CondSubmitCN.buttonClock = core.Clock()

# --- Initialize components for Routine "trialCond" ---
CS_image = visual.ImageStim(
    win=win,
    name='CS_image', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
CondTriggMouse = event.Mouse(win=win)
x, y = [None, None]
CondTriggMouse.mouseClock = core.Clock()
CondTriggKey = keyboard.Keyboard()

# --- Initialize components for Routine "UCS" ---
UCSBkg = visual.Rect(
    win=win, name='UCSBkg',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=1.0, depth=0.0, interpolate=True)
UCS_image = visual.ImageStim(
    win=win,
    name='UCS_image', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
sound_1 = sound.Sound('A', secs=1, stereo=True, hamming=True,
    name='sound_1')
sound_1.setVolume(0.3)

# --- Initialize components for Routine "ITI" ---
FixCross = visual.ShapeStim(
    win=win, name='FixCross', vertices='cross',
    size=(0.05, 0.07),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# --- Initialize components for Routine "Rating" ---
image = visual.ImageStim(
    win=win,
    name='image', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0.1], size=[0.45,0.9],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
RatingInstEN = visual.TextStim(win=win, name='RatingInstEN',
    text='',
    font='Arial',
    pos=[0,0.7], height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
RatingInstCN = visual.TextStim(win=win, name='RatingInstCN',
    text='',
    font='PingFang SC',
    pos=[0,0.7], height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
Scale = visual.Slider(win=win, name='Scale',
    startValue=None, size=(1.3, 0.05), pos=(0, -0.5), units=win.units,
    labels=['– Negative', 'Positive +'], ticks=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='beige', lineColor='White', colorSpace='rgb',
    font='Arial', labelHeight=0.04,
    flip=False, ori=0.0, depth=-3, readOnly=False)
RatingKey = keyboard.Keyboard()
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
SubmitEN = visual.ButtonStim(win, 
    text='SUBMIT', font='Arial',
    pos=[0.7, -0.8],
    letterHeight=0.06,
    size=[0.3, 0.1], borderWidth=0.0,
    fillColor=[0.8824, 0.6392, 0.4432], borderColor=None,
    color='black', colorSpace='rgb',
    opacity=1.0,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='SubmitEN',
    depth=-6
)
SubmitEN.buttonClock = core.Clock()
SubmitCN = visual.ButtonStim(win, 
    text='提交', font='PingFang SC',
    pos=[0.7, -0.8],
    letterHeight=0.06,
    size=[0.3, 0.1], borderWidth=0.0,
    fillColor=[0.8824, 0.6392, 0.4432], borderColor=None,
    color='black', colorSpace='rgb',
    opacity=1.0,
    bold=False, italic=False,
    padding=None,
    anchor='center',
    name='SubmitCN',
    depth=-7
)
SubmitCN.buttonClock = core.Clock()

# --- Initialize components for Routine "ExtInst" ---
ExtImage = visual.ImageStim(
    win=win,
    name='ExtImage', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0.05], size=[0.45,0.9],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
ExtImageOverview = visual.ImageStim(
    win=win,
    name='ExtImageOverview', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0.05], size=[1.5,0.9],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
ExtInstEN = visual.TextStim(win=win, name='ExtInstEN',
    text='',
    font='Arial',
    pos=[0,0.7], height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
ExtInstCN = visual.TextStim(win=win, name='ExtInstCN',
    text='',
    font='PingFang SC',
    pos=[-0.3,0.7], height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
ExtRespKey = keyboard.Keyboard()
ExtMouse = event.Mouse(win=win)
x, y = [None, None]
ExtMouse.mouseClock = core.Clock()
ExtSubmitEN = visual.ButtonStim(win, 
    text='CONTINUE', font='Arial',
    pos=[0.7, -0.8],
    letterHeight=0.06,
    size=[0.3, 0.1], borderWidth=0.0,
    fillColor=[0.8824, 0.6392, 0.4432], borderColor=None,
    color='black', colorSpace='rgb',
    opacity=1.0,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='ExtSubmitEN',
    depth=-6
)
ExtSubmitEN.buttonClock = core.Clock()
ExtSubmitCN = visual.ButtonStim(win, 
    text='继续', font='PingFang SC',
    pos=[0.7, -0.8],
    letterHeight=0.06,
    size=[0.3, 0.1], borderWidth=0.0,
    fillColor=[0.8824, 0.6392, 0.4432], borderColor=None,
    color='black', colorSpace='rgb',
    opacity=1.0,
    bold=False, italic=False,
    padding=None,
    anchor='center',
    name='ExtSubmitCN',
    depth=-7
)
ExtSubmitCN.buttonClock = core.Clock()

# --- Initialize components for Routine "trialExt" ---
Ext_image = visual.ImageStim(
    win=win,
    name='Ext_image', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
ExtTriggMouse = event.Mouse(win=win)
x, y = [None, None]
ExtTriggMouse.mouseClock = core.Clock()
ExtTriggKey = keyboard.Keyboard()

# --- Initialize components for Routine "ITI" ---
FixCross = visual.ShapeStim(
    win=win, name='FixCross', vertices='cross',
    size=(0.05, 0.07),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# --- Initialize components for Routine "Rating" ---
image = visual.ImageStim(
    win=win,
    name='image', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0.1], size=[0.45,0.9],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
RatingInstEN = visual.TextStim(win=win, name='RatingInstEN',
    text='',
    font='Arial',
    pos=[0,0.7], height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
RatingInstCN = visual.TextStim(win=win, name='RatingInstCN',
    text='',
    font='PingFang SC',
    pos=[0,0.7], height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
Scale = visual.Slider(win=win, name='Scale',
    startValue=None, size=(1.3, 0.05), pos=(0, -0.5), units=win.units,
    labels=['– Negative', 'Positive +'], ticks=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='beige', lineColor='White', colorSpace='rgb',
    font='Arial', labelHeight=0.04,
    flip=False, ori=0.0, depth=-3, readOnly=False)
RatingKey = keyboard.Keyboard()
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
SubmitEN = visual.ButtonStim(win, 
    text='SUBMIT', font='Arial',
    pos=[0.7, -0.8],
    letterHeight=0.06,
    size=[0.3, 0.1], borderWidth=0.0,
    fillColor=[0.8824, 0.6392, 0.4432], borderColor=None,
    color='black', colorSpace='rgb',
    opacity=1.0,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='SubmitEN',
    depth=-6
)
SubmitEN.buttonClock = core.Clock()
SubmitCN = visual.ButtonStim(win, 
    text='提交', font='PingFang SC',
    pos=[0.7, -0.8],
    letterHeight=0.06,
    size=[0.3, 0.1], borderWidth=0.0,
    fillColor=[0.8824, 0.6392, 0.4432], borderColor=None,
    color='black', colorSpace='rgb',
    opacity=1.0,
    bold=False, italic=False,
    padding=None,
    anchor='center',
    name='SubmitCN',
    depth=-7
)
SubmitCN.buttonClock = core.Clock()

# --- Initialize components for Routine "EndBlock" ---
Bkg_Light = visual.Rect(
    win=win, name='Bkg_Light',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor=[0.8824, 0.6392, 0.4432],
    opacity=1.0, depth=0.0, interpolate=True)
EndTxtEN = visual.TextStim(win=win, name='EndTxtEN',
    text='',
    font='Arial',
    pos=[0, 0], height=0.2, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
EndTxtCN = visual.TextStim(win=win, name='EndTxtCN',
    text='',
    font='PingFang SC',
    pos=[-0.3, 0], height=0.2, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "Settings" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
SettingsComponents = []
for thisComponent in SettingsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Settings" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in SettingsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Settings" ---
for thisComponent in SettingsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Settings" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
PreCondInstText = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('0_Instructions.xlsx', selection='0:5'),
    seed=None, name='PreCondInstText')
thisExp.addLoop(PreCondInstText)  # add the loop to the experiment
thisPreCondInstText = PreCondInstText.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPreCondInstText.rgb)
if thisPreCondInstText != None:
    for paramName in thisPreCondInstText:
        exec('{} = thisPreCondInstText[paramName]'.format(paramName))

for thisPreCondInstText in PreCondInstText:
    currentLoop = PreCondInstText
    # abbreviate parameter names if possible (e.g. rgb = thisPreCondInstText.rgb)
    if thisPreCondInstText != None:
        for paramName in thisPreCondInstText:
            exec('{} = thisPreCondInstText[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "PreCondInst" ---
    continueRoutine = True
    # update component parameters for each repeat
    PreCondImage.setImage(PreCondInstTextImage)
    PreCondImageOverview.setImage(PreCondInstTextImage)
    PreCondInstEN.setText(PreCondInstTextEN)
    PreCondInstCN.setText(PreCondInstTextCN)
    PreCondRespKey.keys = []
    PreCondRespKey.rt = []
    _PreCondRespKey_allKeys = []
    # setup some python lists for storing info about the PreCondMouse
    PreCondMouse.x = []
    PreCondMouse.y = []
    PreCondMouse.leftButton = []
    PreCondMouse.midButton = []
    PreCondMouse.rightButton = []
    PreCondMouse.time = []
    gotValidClick = False  # until a click is received
    # reset PreCondSubmitEN to account for continued clicks & clear times on/off
    PreCondSubmitEN.reset()
    # reset PreCondSubmitCN to account for continued clicks & clear times on/off
    PreCondSubmitCN.reset()
    # keep track of which components have finished
    PreCondInstComponents = [PreCondImage, PreCondImageOverview, PreCondInstEN, PreCondInstCN, PreCondRespKey, PreCondMouse, PreCondSubmitEN, PreCondSubmitCN]
    for thisComponent in PreCondInstComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "PreCondInst" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *PreCondImage* updates
        
        # if PreCondImage is starting this frame...
        if PreCondImage.status == NOT_STARTED and PreCondInstTextImage=="Stimuli/Raw_Trig.BMP":
            # keep track of start time/frame for later
            PreCondImage.frameNStart = frameN  # exact frame index
            PreCondImage.tStart = t  # local t and not account for scr refresh
            PreCondImage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PreCondImage, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'PreCondImage.started')
            # update status
            PreCondImage.status = STARTED
            PreCondImage.setAutoDraw(True)
        
        # if PreCondImage is active this frame...
        if PreCondImage.status == STARTED:
            # update params
            pass
        
        # *PreCondImageOverview* updates
        
        # if PreCondImageOverview is starting this frame...
        if PreCondImageOverview.status == NOT_STARTED and PreCondInstTextImage=="Stimuli/Raw_3Faces.BMP":
            # keep track of start time/frame for later
            PreCondImageOverview.frameNStart = frameN  # exact frame index
            PreCondImageOverview.tStart = t  # local t and not account for scr refresh
            PreCondImageOverview.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PreCondImageOverview, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'PreCondImageOverview.started')
            # update status
            PreCondImageOverview.status = STARTED
            PreCondImageOverview.setAutoDraw(True)
        
        # if PreCondImageOverview is active this frame...
        if PreCondImageOverview.status == STARTED:
            # update params
            pass
        
        # *PreCondInstEN* updates
        
        # if PreCondInstEN is starting this frame...
        if PreCondInstEN.status == NOT_STARTED and expInfo['Language'] == 'EN':
            # keep track of start time/frame for later
            PreCondInstEN.frameNStart = frameN  # exact frame index
            PreCondInstEN.tStart = t  # local t and not account for scr refresh
            PreCondInstEN.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PreCondInstEN, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'PreCondInstEN.started')
            # update status
            PreCondInstEN.status = STARTED
            PreCondInstEN.setAutoDraw(True)
        
        # if PreCondInstEN is active this frame...
        if PreCondInstEN.status == STARTED:
            # update params
            pass
        
        # *PreCondInstCN* updates
        
        # if PreCondInstCN is starting this frame...
        if PreCondInstCN.status == NOT_STARTED and expInfo['Language'] == 'CN':
            # keep track of start time/frame for later
            PreCondInstCN.frameNStart = frameN  # exact frame index
            PreCondInstCN.tStart = t  # local t and not account for scr refresh
            PreCondInstCN.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PreCondInstCN, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'PreCondInstCN.started')
            # update status
            PreCondInstCN.status = STARTED
            PreCondInstCN.setAutoDraw(True)
        
        # if PreCondInstCN is active this frame...
        if PreCondInstCN.status == STARTED:
            # update params
            pass
        
        # *PreCondRespKey* updates
        waitOnFlip = False
        
        # if PreCondRespKey is starting this frame...
        if PreCondRespKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            PreCondRespKey.frameNStart = frameN  # exact frame index
            PreCondRespKey.tStart = t  # local t and not account for scr refresh
            PreCondRespKey.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PreCondRespKey, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'PreCondRespKey.started')
            # update status
            PreCondRespKey.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(PreCondRespKey.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(PreCondRespKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if PreCondRespKey.status == STARTED and not waitOnFlip:
            theseKeys = PreCondRespKey.getKeys(keyList=['space'], waitRelease=False)
            _PreCondRespKey_allKeys.extend(theseKeys)
            if len(_PreCondRespKey_allKeys):
                PreCondRespKey.keys = _PreCondRespKey_allKeys[-1].name  # just the last key pressed
                PreCondRespKey.rt = _PreCondRespKey_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        # *PreCondMouse* updates
        
        # if PreCondMouse is starting this frame...
        if PreCondMouse.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            PreCondMouse.frameNStart = frameN  # exact frame index
            PreCondMouse.tStart = t  # local t and not account for scr refresh
            PreCondMouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PreCondMouse, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('PreCondMouse.started', t)
            # update status
            PreCondMouse.status = STARTED
            PreCondMouse.mouseClock.reset()
            prevButtonState = PreCondMouse.getPressed()  # if button is down already this ISN'T a new click
        if PreCondMouse.status == STARTED:  # only update if started and not finished!
            buttons = PreCondMouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    x, y = PreCondMouse.getPos()
                    PreCondMouse.x.append(x)
                    PreCondMouse.y.append(y)
                    buttons = PreCondMouse.getPressed()
                    PreCondMouse.leftButton.append(buttons[0])
                    PreCondMouse.midButton.append(buttons[1])
                    PreCondMouse.rightButton.append(buttons[2])
                    PreCondMouse.time.append(PreCondMouse.mouseClock.getTime())
        # *PreCondSubmitEN* updates
        
        # if PreCondSubmitEN is starting this frame...
        if PreCondSubmitEN.status == NOT_STARTED and expInfo['Language'] == 'EN':
            # keep track of start time/frame for later
            PreCondSubmitEN.frameNStart = frameN  # exact frame index
            PreCondSubmitEN.tStart = t  # local t and not account for scr refresh
            PreCondSubmitEN.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PreCondSubmitEN, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'PreCondSubmitEN.started')
            # update status
            PreCondSubmitEN.status = STARTED
            PreCondSubmitEN.setAutoDraw(True)
        
        # if PreCondSubmitEN is active this frame...
        if PreCondSubmitEN.status == STARTED:
            # update params
            pass
            # check whether PreCondSubmitEN has been pressed
            if PreCondSubmitEN.isClicked:
                if not PreCondSubmitEN.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    PreCondSubmitEN.timesOn.append(PreCondSubmitEN.buttonClock.getTime())
                    PreCondSubmitEN.timesOff.append(PreCondSubmitEN.buttonClock.getTime())
                elif len(PreCondSubmitEN.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    PreCondSubmitEN.timesOff[-1] = PreCondSubmitEN.buttonClock.getTime()
                if not PreCondSubmitEN.wasClicked:
                    # end routine when PreCondSubmitEN is clicked
                    continueRoutine = False
                if not PreCondSubmitEN.wasClicked:
                    # run callback code when PreCondSubmitEN is clicked
                    pass
        # take note of whether PreCondSubmitEN was clicked, so that next frame we know if clicks are new
        PreCondSubmitEN.wasClicked = PreCondSubmitEN.isClicked and PreCondSubmitEN.status == STARTED
        # *PreCondSubmitCN* updates
        
        # if PreCondSubmitCN is starting this frame...
        if PreCondSubmitCN.status == NOT_STARTED and expInfo['Language'] == 'CN':
            # keep track of start time/frame for later
            PreCondSubmitCN.frameNStart = frameN  # exact frame index
            PreCondSubmitCN.tStart = t  # local t and not account for scr refresh
            PreCondSubmitCN.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PreCondSubmitCN, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'PreCondSubmitCN.started')
            # update status
            PreCondSubmitCN.status = STARTED
            PreCondSubmitCN.setAutoDraw(True)
        
        # if PreCondSubmitCN is active this frame...
        if PreCondSubmitCN.status == STARTED:
            # update params
            pass
            # check whether PreCondSubmitCN has been pressed
            if PreCondSubmitCN.isClicked:
                if not PreCondSubmitCN.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    PreCondSubmitCN.timesOn.append(PreCondSubmitCN.buttonClock.getTime())
                    PreCondSubmitCN.timesOff.append(PreCondSubmitCN.buttonClock.getTime())
                elif len(PreCondSubmitCN.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    PreCondSubmitCN.timesOff[-1] = PreCondSubmitCN.buttonClock.getTime()
                if not PreCondSubmitCN.wasClicked:
                    # end routine when PreCondSubmitCN is clicked
                    continueRoutine = False
                if not PreCondSubmitCN.wasClicked:
                    # run callback code when PreCondSubmitCN is clicked
                    pass
        # take note of whether PreCondSubmitCN was clicked, so that next frame we know if clicks are new
        PreCondSubmitCN.wasClicked = PreCondSubmitCN.isClicked and PreCondSubmitCN.status == STARTED
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PreCondInstComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "PreCondInst" ---
    for thisComponent in PreCondInstComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if PreCondRespKey.keys in ['', [], None]:  # No response was made
        PreCondRespKey.keys = None
    PreCondInstText.addData('PreCondRespKey.keys',PreCondRespKey.keys)
    if PreCondRespKey.keys != None:  # we had a response
        PreCondInstText.addData('PreCondRespKey.rt', PreCondRespKey.rt)
    # store data for PreCondInstText (TrialHandler)
    PreCondInstText.addData('PreCondMouse.x', PreCondMouse.x)
    PreCondInstText.addData('PreCondMouse.y', PreCondMouse.y)
    PreCondInstText.addData('PreCondMouse.leftButton', PreCondMouse.leftButton)
    PreCondInstText.addData('PreCondMouse.midButton', PreCondMouse.midButton)
    PreCondInstText.addData('PreCondMouse.rightButton', PreCondMouse.rightButton)
    PreCondInstText.addData('PreCondMouse.time', PreCondMouse.time)
    PreCondInstText.addData('PreCondSubmitEN.numClicks', PreCondSubmitEN.numClicks)
    if PreCondSubmitEN.numClicks:
       PreCondInstText.addData('PreCondSubmitEN.timesOn', PreCondSubmitEN.timesOn)
       PreCondInstText.addData('PreCondSubmitEN.timesOff', PreCondSubmitEN.timesOff)
    else:
       PreCondInstText.addData('PreCondSubmitEN.timesOn', "")
       PreCondInstText.addData('PreCondSubmitEN.timesOff', "")
    PreCondInstText.addData('PreCondSubmitCN.numClicks', PreCondSubmitCN.numClicks)
    if PreCondSubmitCN.numClicks:
       PreCondInstText.addData('PreCondSubmitCN.timesOn', PreCondSubmitCN.timesOn)
       PreCondInstText.addData('PreCondSubmitCN.timesOff', PreCondSubmitCN.timesOff)
    else:
       PreCondInstText.addData('PreCondSubmitCN.timesOn', "")
       PreCondInstText.addData('PreCondSubmitCN.timesOff', "")
    # the Routine "PreCondInst" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1.0 repeats of 'PreCondInstText'


# set up handler to look after randomisation of conditions etc
PreCond = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(schedule_files[0]),
    seed=None, name='PreCond')
thisExp.addLoop(PreCond)  # add the loop to the experiment
thisPreCond = PreCond.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPreCond.rgb)
if thisPreCond != None:
    for paramName in thisPreCond:
        exec('{} = thisPreCond[paramName]'.format(paramName))

for thisPreCond in PreCond:
    currentLoop = PreCond
    # abbreviate parameter names if possible (e.g. rgb = thisPreCond.rgb)
    if thisPreCond != None:
        for paramName in thisPreCond:
            exec('{} = thisPreCond[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "trialPreCond" ---
    continueRoutine = True
    # update component parameters for each repeat
    imagePreCond.setImage(PreCondName)
    # Run 'Begin Routine' code from EachTrial
    # If skipPhases is True, end the current routine and break the loop
    if skipPhases:
        continueRoutine = False  # Set continueRoutine to False to end the routine
        PreCond.finished = True  # Set PreCond.finished to True to break the loop
    
    # If parallelTrigger is True, perform parallel triggering
    if parallelTrigger:
        ParaleData = 50  # Value to be set on the parallel port
        port.setData(ParaleData)  # Set the parallel port data to ParaleData
        if lfpTrigger:  # If lfpTrigger is also True
            lfpCtrlPort.setData(1)  # Set the LFP control parallel port data to 1
        core.wait(0.02)  # Wait for 0.02 seconds
        port.setData(0)  # Set the parallel port data back to 0
        if lfpTrigger:  # If lfpTrigger is True
            lfpCtrlPort.setData(0)  # Set the LFP control parallel port data back to 0
    # setup some python lists for storing info about the PreCondTriggMouse
    PreCondTriggMouse.x = []
    PreCondTriggMouse.y = []
    PreCondTriggMouse.leftButton = []
    PreCondTriggMouse.midButton = []
    PreCondTriggMouse.rightButton = []
    PreCondTriggMouse.time = []
    gotValidClick = False  # until a click is received
    PreCondTriggMouse.mouseClock.reset()
    PreCondTriggKey.keys = []
    PreCondTriggKey.rt = []
    _PreCondTriggKey_allKeys = []
    # keep track of which components have finished
    trialPreCondComponents = [imagePreCond, PreCondTriggMouse, PreCondTriggKey]
    for thisComponent in trialPreCondComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "trialPreCond" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 6.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *imagePreCond* updates
        
        # if imagePreCond is starting this frame...
        if imagePreCond.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imagePreCond.frameNStart = frameN  # exact frame index
            imagePreCond.tStart = t  # local t and not account for scr refresh
            imagePreCond.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imagePreCond, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imagePreCond.started')
            # update status
            imagePreCond.status = STARTED
            imagePreCond.setAutoDraw(True)
        
        # if imagePreCond is active this frame...
        if imagePreCond.status == STARTED:
            # update params
            pass
        
        # if imagePreCond is stopping this frame...
        if imagePreCond.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 6-frameTolerance:
                # keep track of stop time/frame for later
                imagePreCond.tStop = t  # not accounting for scr refresh
                imagePreCond.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imagePreCond.stopped')
                # update status
                imagePreCond.status = FINISHED
                imagePreCond.setAutoDraw(False)
        # *PreCondTriggMouse* updates
        
        # if PreCondTriggMouse is starting this frame...
        if PreCondTriggMouse.status == NOT_STARTED and PreCondName=="Stimuli/Trig.BMP":
            # keep track of start time/frame for later
            PreCondTriggMouse.frameNStart = frameN  # exact frame index
            PreCondTriggMouse.tStart = t  # local t and not account for scr refresh
            PreCondTriggMouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PreCondTriggMouse, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'PreCondTriggMouse.started')
            # update status
            PreCondTriggMouse.status = STARTED
            prevButtonState = PreCondTriggMouse.getPressed()  # if button is down already this ISN'T a new click
        
        # if PreCondTriggMouse is stopping this frame...
        if PreCondTriggMouse.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 6-frameTolerance:
                # keep track of stop time/frame for later
                PreCondTriggMouse.tStop = t  # not accounting for scr refresh
                PreCondTriggMouse.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'PreCondTriggMouse.stopped')
                # update status
                PreCondTriggMouse.status = FINISHED
        if PreCondTriggMouse.status == STARTED:  # only update if started and not finished!
            buttons = PreCondTriggMouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    x, y = PreCondTriggMouse.getPos()
                    PreCondTriggMouse.x.append(x)
                    PreCondTriggMouse.y.append(y)
                    buttons = PreCondTriggMouse.getPressed()
                    PreCondTriggMouse.leftButton.append(buttons[0])
                    PreCondTriggMouse.midButton.append(buttons[1])
                    PreCondTriggMouse.rightButton.append(buttons[2])
                    PreCondTriggMouse.time.append(PreCondTriggMouse.mouseClock.getTime())
                    
                    continueRoutine = False  # end routine on response
        
        # *PreCondTriggKey* updates
        waitOnFlip = False
        
        # if PreCondTriggKey is starting this frame...
        if PreCondTriggKey.status == NOT_STARTED and PreCondName=="Stimuli/Trig.BMP":
            # keep track of start time/frame for later
            PreCondTriggKey.frameNStart = frameN  # exact frame index
            PreCondTriggKey.tStart = t  # local t and not account for scr refresh
            PreCondTriggKey.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PreCondTriggKey, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'PreCondTriggKey.started')
            # update status
            PreCondTriggKey.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(PreCondTriggKey.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(PreCondTriggKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if PreCondTriggKey is stopping this frame...
        if PreCondTriggKey.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 6-frameTolerance:
                # keep track of stop time/frame for later
                PreCondTriggKey.tStop = t  # not accounting for scr refresh
                PreCondTriggKey.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'PreCondTriggKey.stopped')
                # update status
                PreCondTriggKey.status = FINISHED
                PreCondTriggKey.status = FINISHED
        if PreCondTriggKey.status == STARTED and not waitOnFlip:
            theseKeys = PreCondTriggKey.getKeys(keyList=['space'], waitRelease=False)
            _PreCondTriggKey_allKeys.extend(theseKeys)
            if len(_PreCondTriggKey_allKeys):
                PreCondTriggKey.keys = _PreCondTriggKey_allKeys[-1].name  # just the last key pressed
                PreCondTriggKey.rt = _PreCondTriggKey_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialPreCondComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trialPreCond" ---
    for thisComponent in trialPreCondComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for PreCond (TrialHandler)
    PreCond.addData('PreCondTriggMouse.x', PreCondTriggMouse.x)
    PreCond.addData('PreCondTriggMouse.y', PreCondTriggMouse.y)
    PreCond.addData('PreCondTriggMouse.leftButton', PreCondTriggMouse.leftButton)
    PreCond.addData('PreCondTriggMouse.midButton', PreCondTriggMouse.midButton)
    PreCond.addData('PreCondTriggMouse.rightButton', PreCondTriggMouse.rightButton)
    PreCond.addData('PreCondTriggMouse.time', PreCondTriggMouse.time)
    # check responses
    if PreCondTriggKey.keys in ['', [], None]:  # No response was made
        PreCondTriggKey.keys = None
    PreCond.addData('PreCondTriggKey.keys',PreCondTriggKey.keys)
    if PreCondTriggKey.keys != None:  # we had a response
        PreCond.addData('PreCondTriggKey.rt', PreCondTriggKey.rt)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-6.000000)
    
    # --- Prepare to start Routine "ITI" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    ITIComponents = [FixCross]
    for thisComponent in ITIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ITI" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *FixCross* updates
        
        # if FixCross is starting this frame...
        if FixCross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            FixCross.frameNStart = frameN  # exact frame index
            FixCross.tStart = t  # local t and not account for scr refresh
            FixCross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FixCross, 'tStartRefresh')  # time at next scr refresh
            # update status
            FixCross.status = STARTED
            FixCross.setAutoDraw(True)
        
        # if FixCross is active this frame...
        if FixCross.status == STARTED:
            # update params
            pass
        
        # if FixCross is stopping this frame...
        if FixCross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > FixCross.tStartRefresh + random.uniform(0, 2)+6-frameTolerance:
                # keep track of stop time/frame for later
                FixCross.tStop = t  # not accounting for scr refresh
                FixCross.frameNStop = frameN  # exact frame index
                # update status
                FixCross.status = FINISHED
                FixCross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ITI" ---
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'PreCond'

# get names of stimulus parameters
if PreCond.trialList in ([], [None], None):
    params = []
else:
    params = PreCond.trialList[0].keys()
# save data for this loop
PreCond.saveAsExcel(filename + '.xlsx', sheetName='PreCond',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# set up handler to look after randomisation of conditions etc
RatingPreCond = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('4_Rating.xlsx'),
    seed=None, name='RatingPreCond')
thisExp.addLoop(RatingPreCond)  # add the loop to the experiment
thisRatingPreCond = RatingPreCond.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRatingPreCond.rgb)
if thisRatingPreCond != None:
    for paramName in thisRatingPreCond:
        exec('{} = thisRatingPreCond[paramName]'.format(paramName))

for thisRatingPreCond in RatingPreCond:
    currentLoop = RatingPreCond
    # abbreviate parameter names if possible (e.g. rgb = thisRatingPreCond.rgb)
    if thisRatingPreCond != None:
        for paramName in thisRatingPreCond:
            exec('{} = thisRatingPreCond[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Rating" ---
    continueRoutine = True
    # update component parameters for each repeat
    image.setImage(CondName)
    RatingInstEN.setText(FearRatingInstTextEN)
    RatingInstCN.setText(FearRatingInstTextCN)
    Scale.reset()
    RatingKey.keys = []
    RatingKey.rt = []
    _RatingKey_allKeys = []
    # setup some python lists for storing info about the mouse
    mouse.x = []
    mouse.y = []
    mouse.leftButton = []
    mouse.midButton = []
    mouse.rightButton = []
    mouse.time = []
    gotValidClick = False  # until a click is received
    # reset SubmitEN to account for continued clicks & clear times on/off
    SubmitEN.reset()
    # reset SubmitCN to account for continued clicks & clear times on/off
    SubmitCN.reset()
    # keep track of which components have finished
    RatingComponents = [image, RatingInstEN, RatingInstCN, Scale, RatingKey, mouse, SubmitEN, SubmitCN]
    for thisComponent in RatingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Rating" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        
        # if image is starting this frame...
        if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image.started')
            # update status
            image.status = STARTED
            image.setAutoDraw(True)
        
        # if image is active this frame...
        if image.status == STARTED:
            # update params
            pass
        
        # *RatingInstEN* updates
        
        # if RatingInstEN is starting this frame...
        if RatingInstEN.status == NOT_STARTED and expInfo['Language'] == 'EN':
            # keep track of start time/frame for later
            RatingInstEN.frameNStart = frameN  # exact frame index
            RatingInstEN.tStart = t  # local t and not account for scr refresh
            RatingInstEN.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RatingInstEN, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'RatingInstEN.started')
            # update status
            RatingInstEN.status = STARTED
            RatingInstEN.setAutoDraw(True)
        
        # if RatingInstEN is active this frame...
        if RatingInstEN.status == STARTED:
            # update params
            pass
        
        # *RatingInstCN* updates
        
        # if RatingInstCN is starting this frame...
        if RatingInstCN.status == NOT_STARTED and expInfo['Language'] == 'CN':
            # keep track of start time/frame for later
            RatingInstCN.frameNStart = frameN  # exact frame index
            RatingInstCN.tStart = t  # local t and not account for scr refresh
            RatingInstCN.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RatingInstCN, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'RatingInstCN.started')
            # update status
            RatingInstCN.status = STARTED
            RatingInstCN.setAutoDraw(True)
        
        # if RatingInstCN is active this frame...
        if RatingInstCN.status == STARTED:
            # update params
            pass
        
        # *Scale* updates
        
        # if Scale is starting this frame...
        if Scale.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Scale.frameNStart = frameN  # exact frame index
            Scale.tStart = t  # local t and not account for scr refresh
            Scale.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Scale, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Scale.started')
            # update status
            Scale.status = STARTED
            Scale.setAutoDraw(True)
        
        # if Scale is active this frame...
        if Scale.status == STARTED:
            # update params
            pass
        
        # *RatingKey* updates
        waitOnFlip = False
        
        # if RatingKey is starting this frame...
        if RatingKey.status == NOT_STARTED and Scale.rating:
            # keep track of start time/frame for later
            RatingKey.frameNStart = frameN  # exact frame index
            RatingKey.tStart = t  # local t and not account for scr refresh
            RatingKey.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RatingKey, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'RatingKey.started')
            # update status
            RatingKey.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(RatingKey.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(RatingKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if RatingKey.status == STARTED and not waitOnFlip:
            theseKeys = RatingKey.getKeys(keyList=['space'], waitRelease=False)
            _RatingKey_allKeys.extend(theseKeys)
            if len(_RatingKey_allKeys):
                RatingKey.keys = _RatingKey_allKeys[-1].name  # just the last key pressed
                RatingKey.rt = _RatingKey_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        # *mouse* updates
        
        # if mouse is starting this frame...
        if mouse.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse.started', t)
            # update status
            mouse.status = STARTED
            mouse.mouseClock.reset()
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
        if mouse.status == STARTED:  # only update if started and not finished!
            buttons = mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    x, y = mouse.getPos()
                    mouse.x.append(x)
                    mouse.y.append(y)
                    buttons = mouse.getPressed()
                    mouse.leftButton.append(buttons[0])
                    mouse.midButton.append(buttons[1])
                    mouse.rightButton.append(buttons[2])
                    mouse.time.append(mouse.mouseClock.getTime())
        # *SubmitEN* updates
        
        # if SubmitEN is starting this frame...
        if SubmitEN.status == NOT_STARTED and Scale.rating and expInfo['Language'] == 'EN':
            # keep track of start time/frame for later
            SubmitEN.frameNStart = frameN  # exact frame index
            SubmitEN.tStart = t  # local t and not account for scr refresh
            SubmitEN.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(SubmitEN, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'SubmitEN.started')
            # update status
            SubmitEN.status = STARTED
            SubmitEN.setAutoDraw(True)
        
        # if SubmitEN is active this frame...
        if SubmitEN.status == STARTED:
            # update params
            pass
            # check whether SubmitEN has been pressed
            if SubmitEN.isClicked:
                if not SubmitEN.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    SubmitEN.timesOn.append(SubmitEN.buttonClock.getTime())
                    SubmitEN.timesOff.append(SubmitEN.buttonClock.getTime())
                elif len(SubmitEN.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    SubmitEN.timesOff[-1] = SubmitEN.buttonClock.getTime()
                if not SubmitEN.wasClicked:
                    # end routine when SubmitEN is clicked
                    continueRoutine = False
                if not SubmitEN.wasClicked:
                    # run callback code when SubmitEN is clicked
                    pass
        # take note of whether SubmitEN was clicked, so that next frame we know if clicks are new
        SubmitEN.wasClicked = SubmitEN.isClicked and SubmitEN.status == STARTED
        # *SubmitCN* updates
        
        # if SubmitCN is starting this frame...
        if SubmitCN.status == NOT_STARTED and Scale.rating and expInfo['Language'] == 'CN':
            # keep track of start time/frame for later
            SubmitCN.frameNStart = frameN  # exact frame index
            SubmitCN.tStart = t  # local t and not account for scr refresh
            SubmitCN.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(SubmitCN, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'SubmitCN.started')
            # update status
            SubmitCN.status = STARTED
            SubmitCN.setAutoDraw(True)
        
        # if SubmitCN is active this frame...
        if SubmitCN.status == STARTED:
            # update params
            pass
            # check whether SubmitCN has been pressed
            if SubmitCN.isClicked:
                if not SubmitCN.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    SubmitCN.timesOn.append(SubmitCN.buttonClock.getTime())
                    SubmitCN.timesOff.append(SubmitCN.buttonClock.getTime())
                elif len(SubmitCN.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    SubmitCN.timesOff[-1] = SubmitCN.buttonClock.getTime()
                if not SubmitCN.wasClicked:
                    # end routine when SubmitCN is clicked
                    continueRoutine = False
                if not SubmitCN.wasClicked:
                    # run callback code when SubmitCN is clicked
                    pass
        # take note of whether SubmitCN was clicked, so that next frame we know if clicks are new
        SubmitCN.wasClicked = SubmitCN.isClicked and SubmitCN.status == STARTED
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RatingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Rating" ---
    for thisComponent in RatingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    RatingPreCond.addData('Scale.response', Scale.getRating())
    RatingPreCond.addData('Scale.rt', Scale.getRT())
    # check responses
    if RatingKey.keys in ['', [], None]:  # No response was made
        RatingKey.keys = None
    RatingPreCond.addData('RatingKey.keys',RatingKey.keys)
    if RatingKey.keys != None:  # we had a response
        RatingPreCond.addData('RatingKey.rt', RatingKey.rt)
    # store data for RatingPreCond (TrialHandler)
    RatingPreCond.addData('mouse.x', mouse.x)
    RatingPreCond.addData('mouse.y', mouse.y)
    RatingPreCond.addData('mouse.leftButton', mouse.leftButton)
    RatingPreCond.addData('mouse.midButton', mouse.midButton)
    RatingPreCond.addData('mouse.rightButton', mouse.rightButton)
    RatingPreCond.addData('mouse.time', mouse.time)
    RatingPreCond.addData('SubmitEN.numClicks', SubmitEN.numClicks)
    if SubmitEN.numClicks:
       RatingPreCond.addData('SubmitEN.timesOn', SubmitEN.timesOn)
       RatingPreCond.addData('SubmitEN.timesOff', SubmitEN.timesOff)
    else:
       RatingPreCond.addData('SubmitEN.timesOn', "")
       RatingPreCond.addData('SubmitEN.timesOff', "")
    RatingPreCond.addData('SubmitCN.numClicks', SubmitCN.numClicks)
    if SubmitCN.numClicks:
       RatingPreCond.addData('SubmitCN.timesOn', SubmitCN.timesOn)
       RatingPreCond.addData('SubmitCN.timesOff', SubmitCN.timesOff)
    else:
       RatingPreCond.addData('SubmitCN.timesOn', "")
       RatingPreCond.addData('SubmitCN.timesOff', "")
    # the Routine "Rating" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'RatingPreCond'

# get names of stimulus parameters
if RatingPreCond.trialList in ([], [None], None):
    params = []
else:
    params = RatingPreCond.trialList[0].keys()
# save data for this loop
RatingPreCond.saveAsExcel(filename + '.xlsx', sheetName='RatingPreCond',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# set up handler to look after randomisation of conditions etc
CondInstText = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('0_Instructions.xlsx', selection='0:5'),
    seed=None, name='CondInstText')
thisExp.addLoop(CondInstText)  # add the loop to the experiment
thisCondInstText = CondInstText.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisCondInstText.rgb)
if thisCondInstText != None:
    for paramName in thisCondInstText:
        exec('{} = thisCondInstText[paramName]'.format(paramName))

for thisCondInstText in CondInstText:
    currentLoop = CondInstText
    # abbreviate parameter names if possible (e.g. rgb = thisCondInstText.rgb)
    if thisCondInstText != None:
        for paramName in thisCondInstText:
            exec('{} = thisCondInstText[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "CondInst" ---
    continueRoutine = True
    # update component parameters for each repeat
    CondImage.setImage(CondInstTextImage)
    CondImageOverview.setImage(CondInstTextImage)
    CondInstEN.setText(CondInstTextEN)
    CondInstCN.setText(CondInstTextCN)
    CondRespKey.keys = []
    CondRespKey.rt = []
    _CondRespKey_allKeys = []
    # setup some python lists for storing info about the CondMouse
    CondMouse.x = []
    CondMouse.y = []
    CondMouse.leftButton = []
    CondMouse.midButton = []
    CondMouse.rightButton = []
    CondMouse.time = []
    gotValidClick = False  # until a click is received
    # reset CondSubmitEN to account for continued clicks & clear times on/off
    CondSubmitEN.reset()
    # reset CondSubmitCN to account for continued clicks & clear times on/off
    CondSubmitCN.reset()
    # keep track of which components have finished
    CondInstComponents = [CondImage, CondImageOverview, CondInstEN, CondInstCN, CondRespKey, CondMouse, CondSubmitEN, CondSubmitCN]
    for thisComponent in CondInstComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "CondInst" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *CondImage* updates
        
        # if CondImage is starting this frame...
        if CondImage.status == NOT_STARTED and CondInstTextImage=="Stimuli/Raw_Trig.BMP":
            # keep track of start time/frame for later
            CondImage.frameNStart = frameN  # exact frame index
            CondImage.tStart = t  # local t and not account for scr refresh
            CondImage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CondImage, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'CondImage.started')
            # update status
            CondImage.status = STARTED
            CondImage.setAutoDraw(True)
        
        # if CondImage is active this frame...
        if CondImage.status == STARTED:
            # update params
            pass
        
        # *CondImageOverview* updates
        
        # if CondImageOverview is starting this frame...
        if CondImageOverview.status == NOT_STARTED and CondInstTextImage=="Stimuli/Raw_3Faces.BMP":
            # keep track of start time/frame for later
            CondImageOverview.frameNStart = frameN  # exact frame index
            CondImageOverview.tStart = t  # local t and not account for scr refresh
            CondImageOverview.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CondImageOverview, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'CondImageOverview.started')
            # update status
            CondImageOverview.status = STARTED
            CondImageOverview.setAutoDraw(True)
        
        # if CondImageOverview is active this frame...
        if CondImageOverview.status == STARTED:
            # update params
            pass
        
        # *CondInstEN* updates
        
        # if CondInstEN is starting this frame...
        if CondInstEN.status == NOT_STARTED and expInfo['Language'] == 'EN':
            # keep track of start time/frame for later
            CondInstEN.frameNStart = frameN  # exact frame index
            CondInstEN.tStart = t  # local t and not account for scr refresh
            CondInstEN.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CondInstEN, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'CondInstEN.started')
            # update status
            CondInstEN.status = STARTED
            CondInstEN.setAutoDraw(True)
        
        # if CondInstEN is active this frame...
        if CondInstEN.status == STARTED:
            # update params
            pass
        
        # *CondInstCN* updates
        
        # if CondInstCN is starting this frame...
        if CondInstCN.status == NOT_STARTED and expInfo['Language'] == 'CN':
            # keep track of start time/frame for later
            CondInstCN.frameNStart = frameN  # exact frame index
            CondInstCN.tStart = t  # local t and not account for scr refresh
            CondInstCN.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CondInstCN, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'CondInstCN.started')
            # update status
            CondInstCN.status = STARTED
            CondInstCN.setAutoDraw(True)
        
        # if CondInstCN is active this frame...
        if CondInstCN.status == STARTED:
            # update params
            pass
        
        # *CondRespKey* updates
        waitOnFlip = False
        
        # if CondRespKey is starting this frame...
        if CondRespKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            CondRespKey.frameNStart = frameN  # exact frame index
            CondRespKey.tStart = t  # local t and not account for scr refresh
            CondRespKey.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CondRespKey, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'CondRespKey.started')
            # update status
            CondRespKey.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(CondRespKey.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(CondRespKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if CondRespKey.status == STARTED and not waitOnFlip:
            theseKeys = CondRespKey.getKeys(keyList=['space'], waitRelease=False)
            _CondRespKey_allKeys.extend(theseKeys)
            if len(_CondRespKey_allKeys):
                CondRespKey.keys = _CondRespKey_allKeys[-1].name  # just the last key pressed
                CondRespKey.rt = _CondRespKey_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        # *CondMouse* updates
        
        # if CondMouse is starting this frame...
        if CondMouse.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            CondMouse.frameNStart = frameN  # exact frame index
            CondMouse.tStart = t  # local t and not account for scr refresh
            CondMouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CondMouse, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('CondMouse.started', t)
            # update status
            CondMouse.status = STARTED
            CondMouse.mouseClock.reset()
            prevButtonState = CondMouse.getPressed()  # if button is down already this ISN'T a new click
        if CondMouse.status == STARTED:  # only update if started and not finished!
            buttons = CondMouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    x, y = CondMouse.getPos()
                    CondMouse.x.append(x)
                    CondMouse.y.append(y)
                    buttons = CondMouse.getPressed()
                    CondMouse.leftButton.append(buttons[0])
                    CondMouse.midButton.append(buttons[1])
                    CondMouse.rightButton.append(buttons[2])
                    CondMouse.time.append(CondMouse.mouseClock.getTime())
        # *CondSubmitEN* updates
        
        # if CondSubmitEN is starting this frame...
        if CondSubmitEN.status == NOT_STARTED and expInfo['Language'] == 'EN':
            # keep track of start time/frame for later
            CondSubmitEN.frameNStart = frameN  # exact frame index
            CondSubmitEN.tStart = t  # local t and not account for scr refresh
            CondSubmitEN.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CondSubmitEN, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'CondSubmitEN.started')
            # update status
            CondSubmitEN.status = STARTED
            CondSubmitEN.setAutoDraw(True)
        
        # if CondSubmitEN is active this frame...
        if CondSubmitEN.status == STARTED:
            # update params
            pass
            # check whether CondSubmitEN has been pressed
            if CondSubmitEN.isClicked:
                if not CondSubmitEN.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    CondSubmitEN.timesOn.append(CondSubmitEN.buttonClock.getTime())
                    CondSubmitEN.timesOff.append(CondSubmitEN.buttonClock.getTime())
                elif len(CondSubmitEN.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    CondSubmitEN.timesOff[-1] = CondSubmitEN.buttonClock.getTime()
                if not CondSubmitEN.wasClicked:
                    # end routine when CondSubmitEN is clicked
                    continueRoutine = False
                if not CondSubmitEN.wasClicked:
                    # run callback code when CondSubmitEN is clicked
                    pass
        # take note of whether CondSubmitEN was clicked, so that next frame we know if clicks are new
        CondSubmitEN.wasClicked = CondSubmitEN.isClicked and CondSubmitEN.status == STARTED
        # *CondSubmitCN* updates
        
        # if CondSubmitCN is starting this frame...
        if CondSubmitCN.status == NOT_STARTED and expInfo['Language'] == 'CN':
            # keep track of start time/frame for later
            CondSubmitCN.frameNStart = frameN  # exact frame index
            CondSubmitCN.tStart = t  # local t and not account for scr refresh
            CondSubmitCN.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CondSubmitCN, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'CondSubmitCN.started')
            # update status
            CondSubmitCN.status = STARTED
            CondSubmitCN.setAutoDraw(True)
        
        # if CondSubmitCN is active this frame...
        if CondSubmitCN.status == STARTED:
            # update params
            pass
            # check whether CondSubmitCN has been pressed
            if CondSubmitCN.isClicked:
                if not CondSubmitCN.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    CondSubmitCN.timesOn.append(CondSubmitCN.buttonClock.getTime())
                    CondSubmitCN.timesOff.append(CondSubmitCN.buttonClock.getTime())
                elif len(CondSubmitCN.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    CondSubmitCN.timesOff[-1] = CondSubmitCN.buttonClock.getTime()
                if not CondSubmitCN.wasClicked:
                    # end routine when CondSubmitCN is clicked
                    continueRoutine = False
                if not CondSubmitCN.wasClicked:
                    # run callback code when CondSubmitCN is clicked
                    pass
        # take note of whether CondSubmitCN was clicked, so that next frame we know if clicks are new
        CondSubmitCN.wasClicked = CondSubmitCN.isClicked and CondSubmitCN.status == STARTED
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in CondInstComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "CondInst" ---
    for thisComponent in CondInstComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if CondRespKey.keys in ['', [], None]:  # No response was made
        CondRespKey.keys = None
    CondInstText.addData('CondRespKey.keys',CondRespKey.keys)
    if CondRespKey.keys != None:  # we had a response
        CondInstText.addData('CondRespKey.rt', CondRespKey.rt)
    # store data for CondInstText (TrialHandler)
    CondInstText.addData('CondMouse.x', CondMouse.x)
    CondInstText.addData('CondMouse.y', CondMouse.y)
    CondInstText.addData('CondMouse.leftButton', CondMouse.leftButton)
    CondInstText.addData('CondMouse.midButton', CondMouse.midButton)
    CondInstText.addData('CondMouse.rightButton', CondMouse.rightButton)
    CondInstText.addData('CondMouse.time', CondMouse.time)
    CondInstText.addData('CondSubmitEN.numClicks', CondSubmitEN.numClicks)
    if CondSubmitEN.numClicks:
       CondInstText.addData('CondSubmitEN.timesOn', CondSubmitEN.timesOn)
       CondInstText.addData('CondSubmitEN.timesOff', CondSubmitEN.timesOff)
    else:
       CondInstText.addData('CondSubmitEN.timesOn', "")
       CondInstText.addData('CondSubmitEN.timesOff', "")
    CondInstText.addData('CondSubmitCN.numClicks', CondSubmitCN.numClicks)
    if CondSubmitCN.numClicks:
       CondInstText.addData('CondSubmitCN.timesOn', CondSubmitCN.timesOn)
       CondInstText.addData('CondSubmitCN.timesOff', CondSubmitCN.timesOff)
    else:
       CondInstText.addData('CondSubmitCN.timesOn', "")
       CondInstText.addData('CondSubmitCN.timesOff', "")
    # the Routine "CondInst" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1.0 repeats of 'CondInstText'


# set up handler to look after randomisation of conditions etc
Cond = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(schedule_files[1]),
    seed=None, name='Cond')
thisExp.addLoop(Cond)  # add the loop to the experiment
thisCond = Cond.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisCond.rgb)
if thisCond != None:
    for paramName in thisCond:
        exec('{} = thisCond[paramName]'.format(paramName))

for thisCond in Cond:
    currentLoop = Cond
    # abbreviate parameter names if possible (e.g. rgb = thisCond.rgb)
    if thisCond != None:
        for paramName in thisCond:
            exec('{} = thisCond[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "trialCond" ---
    continueRoutine = True
    # update component parameters for each repeat
    CS_image.setImage(CSName)
    # Run 'Begin Routine' code from EachTrial_2
    # If skipPhases is True, end the current routine and break the loop
    if skipPhases:
        continueRoutine = False  # Set continueRoutine to False to end the routine
        Cond.finished = True  # Set Cond.finished to True to break the loop
    
    # If parallelTrigger is True, perform parallel triggering
    if parallelTrigger:
        ParaleData = 50  # Value to be set on the parallel port
        port.setData(ParaleData)  # Set the parallel port data to ParaleData
        if lfpTrigger:  # If lfpTrigger is also True
            lfpCtrlPort.setData(1)  # Set the LFP control parallel port data to 1
        core.wait(0.02)  # Wait for 0.02 seconds
        port.setData(0)  # Set the parallel port data back to 0
        if lfpTrigger:  # If lfpTrigger is True
            lfpCtrlPort.setData(0)  # Set the LFP control parallel port data back to 0
    # setup some python lists for storing info about the CondTriggMouse
    CondTriggMouse.x = []
    CondTriggMouse.y = []
    CondTriggMouse.leftButton = []
    CondTriggMouse.midButton = []
    CondTriggMouse.rightButton = []
    CondTriggMouse.time = []
    gotValidClick = False  # until a click is received
    CondTriggMouse.mouseClock.reset()
    CondTriggKey.keys = []
    CondTriggKey.rt = []
    _CondTriggKey_allKeys = []
    # keep track of which components have finished
    trialCondComponents = [CS_image, CondTriggMouse, CondTriggKey]
    for thisComponent in trialCondComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "trialCond" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 6.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *CS_image* updates
        
        # if CS_image is starting this frame...
        if CS_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            CS_image.frameNStart = frameN  # exact frame index
            CS_image.tStart = t  # local t and not account for scr refresh
            CS_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CS_image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'CS_image.started')
            # update status
            CS_image.status = STARTED
            CS_image.setAutoDraw(True)
        
        # if CS_image is active this frame...
        if CS_image.status == STARTED:
            # update params
            pass
        
        # if CS_image is stopping this frame...
        if CS_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > CS_image.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                CS_image.tStop = t  # not accounting for scr refresh
                CS_image.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'CS_image.stopped')
                # update status
                CS_image.status = FINISHED
                CS_image.setAutoDraw(False)
        # *CondTriggMouse* updates
        
        # if CondTriggMouse is starting this frame...
        if CondTriggMouse.status == NOT_STARTED and CSName=="Stimuli/Trig.BMP":
            # keep track of start time/frame for later
            CondTriggMouse.frameNStart = frameN  # exact frame index
            CondTriggMouse.tStart = t  # local t and not account for scr refresh
            CondTriggMouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CondTriggMouse, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'CondTriggMouse.started')
            # update status
            CondTriggMouse.status = STARTED
            prevButtonState = CondTriggMouse.getPressed()  # if button is down already this ISN'T a new click
        
        # if CondTriggMouse is stopping this frame...
        if CondTriggMouse.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 6-frameTolerance:
                # keep track of stop time/frame for later
                CondTriggMouse.tStop = t  # not accounting for scr refresh
                CondTriggMouse.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'CondTriggMouse.stopped')
                # update status
                CondTriggMouse.status = FINISHED
        if CondTriggMouse.status == STARTED:  # only update if started and not finished!
            buttons = CondTriggMouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    x, y = CondTriggMouse.getPos()
                    CondTriggMouse.x.append(x)
                    CondTriggMouse.y.append(y)
                    buttons = CondTriggMouse.getPressed()
                    CondTriggMouse.leftButton.append(buttons[0])
                    CondTriggMouse.midButton.append(buttons[1])
                    CondTriggMouse.rightButton.append(buttons[2])
                    CondTriggMouse.time.append(CondTriggMouse.mouseClock.getTime())
                    
                    continueRoutine = False  # end routine on response
        
        # *CondTriggKey* updates
        waitOnFlip = False
        
        # if CondTriggKey is starting this frame...
        if CondTriggKey.status == NOT_STARTED and CSName=="Stimuli/Trig.BMP":
            # keep track of start time/frame for later
            CondTriggKey.frameNStart = frameN  # exact frame index
            CondTriggKey.tStart = t  # local t and not account for scr refresh
            CondTriggKey.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CondTriggKey, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'CondTriggKey.started')
            # update status
            CondTriggKey.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(CondTriggKey.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(CondTriggKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if CondTriggKey is stopping this frame...
        if CondTriggKey.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 6-frameTolerance:
                # keep track of stop time/frame for later
                CondTriggKey.tStop = t  # not accounting for scr refresh
                CondTriggKey.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'CondTriggKey.stopped')
                # update status
                CondTriggKey.status = FINISHED
                CondTriggKey.status = FINISHED
        if CondTriggKey.status == STARTED and not waitOnFlip:
            theseKeys = CondTriggKey.getKeys(keyList=['space'], waitRelease=False)
            _CondTriggKey_allKeys.extend(theseKeys)
            if len(_CondTriggKey_allKeys):
                CondTriggKey.keys = _CondTriggKey_allKeys[-1].name  # just the last key pressed
                CondTriggKey.rt = _CondTriggKey_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialCondComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trialCond" ---
    for thisComponent in trialCondComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for Cond (TrialHandler)
    Cond.addData('CondTriggMouse.x', CondTriggMouse.x)
    Cond.addData('CondTriggMouse.y', CondTriggMouse.y)
    Cond.addData('CondTriggMouse.leftButton', CondTriggMouse.leftButton)
    Cond.addData('CondTriggMouse.midButton', CondTriggMouse.midButton)
    Cond.addData('CondTriggMouse.rightButton', CondTriggMouse.rightButton)
    Cond.addData('CondTriggMouse.time', CondTriggMouse.time)
    # check responses
    if CondTriggKey.keys in ['', [], None]:  # No response was made
        CondTriggKey.keys = None
    Cond.addData('CondTriggKey.keys',CondTriggKey.keys)
    if CondTriggKey.keys != None:  # we had a response
        Cond.addData('CondTriggKey.rt', CondTriggKey.rt)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-6.000000)
    
    # --- Prepare to start Routine "UCS" ---
    continueRoutine = True
    # update component parameters for each repeat
    UCS_image.setImage(UCSName)
    sound_1.setSound(SoundName, secs=1, hamming=True)
    sound_1.setVolume(0.3, log=False)
    # keep track of which components have finished
    UCSComponents = [UCSBkg, UCS_image, sound_1]
    for thisComponent in UCSComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "UCS" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *UCSBkg* updates
        
        # if UCSBkg is starting this frame...
        if UCSBkg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            UCSBkg.frameNStart = frameN  # exact frame index
            UCSBkg.tStart = t  # local t and not account for scr refresh
            UCSBkg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(UCSBkg, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'UCSBkg.started')
            # update status
            UCSBkg.status = STARTED
            UCSBkg.setAutoDraw(True)
        
        # if UCSBkg is active this frame...
        if UCSBkg.status == STARTED:
            # update params
            pass
        
        # if UCSBkg is stopping this frame...
        if UCSBkg.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > UCSBkg.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                UCSBkg.tStop = t  # not accounting for scr refresh
                UCSBkg.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'UCSBkg.stopped')
                # update status
                UCSBkg.status = FINISHED
                UCSBkg.setAutoDraw(False)
        
        # *UCS_image* updates
        
        # if UCS_image is starting this frame...
        if UCS_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            UCS_image.frameNStart = frameN  # exact frame index
            UCS_image.tStart = t  # local t and not account for scr refresh
            UCS_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(UCS_image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'UCS_image.started')
            # update status
            UCS_image.status = STARTED
            UCS_image.setAutoDraw(True)
        
        # if UCS_image is active this frame...
        if UCS_image.status == STARTED:
            # update params
            pass
        
        # if UCS_image is stopping this frame...
        if UCS_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > UCS_image.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                UCS_image.tStop = t  # not accounting for scr refresh
                UCS_image.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'UCS_image.stopped')
                # update status
                UCS_image.status = FINISHED
                UCS_image.setAutoDraw(False)
        # start/stop sound_1
        
        # if sound_1 is starting this frame...
        if sound_1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            sound_1.frameNStart = frameN  # exact frame index
            sound_1.tStart = t  # local t and not account for scr refresh
            sound_1.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('sound_1.started', tThisFlipGlobal)
            # update status
            sound_1.status = STARTED
            sound_1.play(when=win)  # sync with win flip
        
        # if sound_1 is stopping this frame...
        if sound_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_1.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                sound_1.tStop = t  # not accounting for scr refresh
                sound_1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sound_1.stopped')
                # update status
                sound_1.status = FINISHED
                sound_1.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in UCSComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "UCS" ---
    for thisComponent in UCSComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_1.stop()  # ensure sound has stopped at end of routine
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    
    # --- Prepare to start Routine "ITI" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    ITIComponents = [FixCross]
    for thisComponent in ITIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ITI" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *FixCross* updates
        
        # if FixCross is starting this frame...
        if FixCross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            FixCross.frameNStart = frameN  # exact frame index
            FixCross.tStart = t  # local t and not account for scr refresh
            FixCross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FixCross, 'tStartRefresh')  # time at next scr refresh
            # update status
            FixCross.status = STARTED
            FixCross.setAutoDraw(True)
        
        # if FixCross is active this frame...
        if FixCross.status == STARTED:
            # update params
            pass
        
        # if FixCross is stopping this frame...
        if FixCross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > FixCross.tStartRefresh + random.uniform(0, 2)+6-frameTolerance:
                # keep track of stop time/frame for later
                FixCross.tStop = t  # not accounting for scr refresh
                FixCross.frameNStop = frameN  # exact frame index
                # update status
                FixCross.status = FINISHED
                FixCross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ITI" ---
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'Cond'

# get names of stimulus parameters
if Cond.trialList in ([], [None], None):
    params = []
else:
    params = Cond.trialList[0].keys()
# save data for this loop
Cond.saveAsExcel(filename + '.xlsx', sheetName='Cond',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# set up handler to look after randomisation of conditions etc
RatingCond = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('4_Rating.xlsx'),
    seed=None, name='RatingCond')
thisExp.addLoop(RatingCond)  # add the loop to the experiment
thisRatingCond = RatingCond.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRatingCond.rgb)
if thisRatingCond != None:
    for paramName in thisRatingCond:
        exec('{} = thisRatingCond[paramName]'.format(paramName))

for thisRatingCond in RatingCond:
    currentLoop = RatingCond
    # abbreviate parameter names if possible (e.g. rgb = thisRatingCond.rgb)
    if thisRatingCond != None:
        for paramName in thisRatingCond:
            exec('{} = thisRatingCond[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Rating" ---
    continueRoutine = True
    # update component parameters for each repeat
    image.setImage(CondName)
    RatingInstEN.setText(FearRatingInstTextEN)
    RatingInstCN.setText(FearRatingInstTextCN)
    Scale.reset()
    RatingKey.keys = []
    RatingKey.rt = []
    _RatingKey_allKeys = []
    # setup some python lists for storing info about the mouse
    mouse.x = []
    mouse.y = []
    mouse.leftButton = []
    mouse.midButton = []
    mouse.rightButton = []
    mouse.time = []
    gotValidClick = False  # until a click is received
    # reset SubmitEN to account for continued clicks & clear times on/off
    SubmitEN.reset()
    # reset SubmitCN to account for continued clicks & clear times on/off
    SubmitCN.reset()
    # keep track of which components have finished
    RatingComponents = [image, RatingInstEN, RatingInstCN, Scale, RatingKey, mouse, SubmitEN, SubmitCN]
    for thisComponent in RatingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Rating" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        
        # if image is starting this frame...
        if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image.started')
            # update status
            image.status = STARTED
            image.setAutoDraw(True)
        
        # if image is active this frame...
        if image.status == STARTED:
            # update params
            pass
        
        # *RatingInstEN* updates
        
        # if RatingInstEN is starting this frame...
        if RatingInstEN.status == NOT_STARTED and expInfo['Language'] == 'EN':
            # keep track of start time/frame for later
            RatingInstEN.frameNStart = frameN  # exact frame index
            RatingInstEN.tStart = t  # local t and not account for scr refresh
            RatingInstEN.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RatingInstEN, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'RatingInstEN.started')
            # update status
            RatingInstEN.status = STARTED
            RatingInstEN.setAutoDraw(True)
        
        # if RatingInstEN is active this frame...
        if RatingInstEN.status == STARTED:
            # update params
            pass
        
        # *RatingInstCN* updates
        
        # if RatingInstCN is starting this frame...
        if RatingInstCN.status == NOT_STARTED and expInfo['Language'] == 'CN':
            # keep track of start time/frame for later
            RatingInstCN.frameNStart = frameN  # exact frame index
            RatingInstCN.tStart = t  # local t and not account for scr refresh
            RatingInstCN.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RatingInstCN, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'RatingInstCN.started')
            # update status
            RatingInstCN.status = STARTED
            RatingInstCN.setAutoDraw(True)
        
        # if RatingInstCN is active this frame...
        if RatingInstCN.status == STARTED:
            # update params
            pass
        
        # *Scale* updates
        
        # if Scale is starting this frame...
        if Scale.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Scale.frameNStart = frameN  # exact frame index
            Scale.tStart = t  # local t and not account for scr refresh
            Scale.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Scale, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Scale.started')
            # update status
            Scale.status = STARTED
            Scale.setAutoDraw(True)
        
        # if Scale is active this frame...
        if Scale.status == STARTED:
            # update params
            pass
        
        # *RatingKey* updates
        waitOnFlip = False
        
        # if RatingKey is starting this frame...
        if RatingKey.status == NOT_STARTED and Scale.rating:
            # keep track of start time/frame for later
            RatingKey.frameNStart = frameN  # exact frame index
            RatingKey.tStart = t  # local t and not account for scr refresh
            RatingKey.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RatingKey, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'RatingKey.started')
            # update status
            RatingKey.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(RatingKey.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(RatingKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if RatingKey.status == STARTED and not waitOnFlip:
            theseKeys = RatingKey.getKeys(keyList=['space'], waitRelease=False)
            _RatingKey_allKeys.extend(theseKeys)
            if len(_RatingKey_allKeys):
                RatingKey.keys = _RatingKey_allKeys[-1].name  # just the last key pressed
                RatingKey.rt = _RatingKey_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        # *mouse* updates
        
        # if mouse is starting this frame...
        if mouse.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse.started', t)
            # update status
            mouse.status = STARTED
            mouse.mouseClock.reset()
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
        if mouse.status == STARTED:  # only update if started and not finished!
            buttons = mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    x, y = mouse.getPos()
                    mouse.x.append(x)
                    mouse.y.append(y)
                    buttons = mouse.getPressed()
                    mouse.leftButton.append(buttons[0])
                    mouse.midButton.append(buttons[1])
                    mouse.rightButton.append(buttons[2])
                    mouse.time.append(mouse.mouseClock.getTime())
        # *SubmitEN* updates
        
        # if SubmitEN is starting this frame...
        if SubmitEN.status == NOT_STARTED and Scale.rating and expInfo['Language'] == 'EN':
            # keep track of start time/frame for later
            SubmitEN.frameNStart = frameN  # exact frame index
            SubmitEN.tStart = t  # local t and not account for scr refresh
            SubmitEN.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(SubmitEN, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'SubmitEN.started')
            # update status
            SubmitEN.status = STARTED
            SubmitEN.setAutoDraw(True)
        
        # if SubmitEN is active this frame...
        if SubmitEN.status == STARTED:
            # update params
            pass
            # check whether SubmitEN has been pressed
            if SubmitEN.isClicked:
                if not SubmitEN.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    SubmitEN.timesOn.append(SubmitEN.buttonClock.getTime())
                    SubmitEN.timesOff.append(SubmitEN.buttonClock.getTime())
                elif len(SubmitEN.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    SubmitEN.timesOff[-1] = SubmitEN.buttonClock.getTime()
                if not SubmitEN.wasClicked:
                    # end routine when SubmitEN is clicked
                    continueRoutine = False
                if not SubmitEN.wasClicked:
                    # run callback code when SubmitEN is clicked
                    pass
        # take note of whether SubmitEN was clicked, so that next frame we know if clicks are new
        SubmitEN.wasClicked = SubmitEN.isClicked and SubmitEN.status == STARTED
        # *SubmitCN* updates
        
        # if SubmitCN is starting this frame...
        if SubmitCN.status == NOT_STARTED and Scale.rating and expInfo['Language'] == 'CN':
            # keep track of start time/frame for later
            SubmitCN.frameNStart = frameN  # exact frame index
            SubmitCN.tStart = t  # local t and not account for scr refresh
            SubmitCN.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(SubmitCN, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'SubmitCN.started')
            # update status
            SubmitCN.status = STARTED
            SubmitCN.setAutoDraw(True)
        
        # if SubmitCN is active this frame...
        if SubmitCN.status == STARTED:
            # update params
            pass
            # check whether SubmitCN has been pressed
            if SubmitCN.isClicked:
                if not SubmitCN.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    SubmitCN.timesOn.append(SubmitCN.buttonClock.getTime())
                    SubmitCN.timesOff.append(SubmitCN.buttonClock.getTime())
                elif len(SubmitCN.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    SubmitCN.timesOff[-1] = SubmitCN.buttonClock.getTime()
                if not SubmitCN.wasClicked:
                    # end routine when SubmitCN is clicked
                    continueRoutine = False
                if not SubmitCN.wasClicked:
                    # run callback code when SubmitCN is clicked
                    pass
        # take note of whether SubmitCN was clicked, so that next frame we know if clicks are new
        SubmitCN.wasClicked = SubmitCN.isClicked and SubmitCN.status == STARTED
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RatingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Rating" ---
    for thisComponent in RatingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    RatingCond.addData('Scale.response', Scale.getRating())
    RatingCond.addData('Scale.rt', Scale.getRT())
    # check responses
    if RatingKey.keys in ['', [], None]:  # No response was made
        RatingKey.keys = None
    RatingCond.addData('RatingKey.keys',RatingKey.keys)
    if RatingKey.keys != None:  # we had a response
        RatingCond.addData('RatingKey.rt', RatingKey.rt)
    # store data for RatingCond (TrialHandler)
    RatingCond.addData('mouse.x', mouse.x)
    RatingCond.addData('mouse.y', mouse.y)
    RatingCond.addData('mouse.leftButton', mouse.leftButton)
    RatingCond.addData('mouse.midButton', mouse.midButton)
    RatingCond.addData('mouse.rightButton', mouse.rightButton)
    RatingCond.addData('mouse.time', mouse.time)
    RatingCond.addData('SubmitEN.numClicks', SubmitEN.numClicks)
    if SubmitEN.numClicks:
       RatingCond.addData('SubmitEN.timesOn', SubmitEN.timesOn)
       RatingCond.addData('SubmitEN.timesOff', SubmitEN.timesOff)
    else:
       RatingCond.addData('SubmitEN.timesOn', "")
       RatingCond.addData('SubmitEN.timesOff', "")
    RatingCond.addData('SubmitCN.numClicks', SubmitCN.numClicks)
    if SubmitCN.numClicks:
       RatingCond.addData('SubmitCN.timesOn', SubmitCN.timesOn)
       RatingCond.addData('SubmitCN.timesOff', SubmitCN.timesOff)
    else:
       RatingCond.addData('SubmitCN.timesOn', "")
       RatingCond.addData('SubmitCN.timesOff', "")
    # the Routine "Rating" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'RatingCond'

# get names of stimulus parameters
if RatingCond.trialList in ([], [None], None):
    params = []
else:
    params = RatingCond.trialList[0].keys()
# save data for this loop
RatingCond.saveAsExcel(filename + '.xlsx', sheetName='RatingCond',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# set up handler to look after randomisation of conditions etc
ExtInstText = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('0_Instructions.xlsx', selection='0:5'),
    seed=None, name='ExtInstText')
thisExp.addLoop(ExtInstText)  # add the loop to the experiment
thisExtInstText = ExtInstText.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisExtInstText.rgb)
if thisExtInstText != None:
    for paramName in thisExtInstText:
        exec('{} = thisExtInstText[paramName]'.format(paramName))

for thisExtInstText in ExtInstText:
    currentLoop = ExtInstText
    # abbreviate parameter names if possible (e.g. rgb = thisExtInstText.rgb)
    if thisExtInstText != None:
        for paramName in thisExtInstText:
            exec('{} = thisExtInstText[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "ExtInst" ---
    continueRoutine = True
    # update component parameters for each repeat
    ExtImage.setImage(ExtInstTextImage)
    ExtImageOverview.setImage(ExtInstTextImage)
    ExtInstEN.setText(ExtInstTextEN)
    ExtInstCN.setText(ExtInstTextCN)
    ExtRespKey.keys = []
    ExtRespKey.rt = []
    _ExtRespKey_allKeys = []
    # setup some python lists for storing info about the ExtMouse
    ExtMouse.x = []
    ExtMouse.y = []
    ExtMouse.leftButton = []
    ExtMouse.midButton = []
    ExtMouse.rightButton = []
    ExtMouse.time = []
    gotValidClick = False  # until a click is received
    # reset ExtSubmitEN to account for continued clicks & clear times on/off
    ExtSubmitEN.reset()
    # reset ExtSubmitCN to account for continued clicks & clear times on/off
    ExtSubmitCN.reset()
    # keep track of which components have finished
    ExtInstComponents = [ExtImage, ExtImageOverview, ExtInstEN, ExtInstCN, ExtRespKey, ExtMouse, ExtSubmitEN, ExtSubmitCN]
    for thisComponent in ExtInstComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ExtInst" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ExtImage* updates
        
        # if ExtImage is starting this frame...
        if ExtImage.status == NOT_STARTED and ExtInstTextImage=="Stimuli/Raw_Trig.BMP":
            # keep track of start time/frame for later
            ExtImage.frameNStart = frameN  # exact frame index
            ExtImage.tStart = t  # local t and not account for scr refresh
            ExtImage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ExtImage, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ExtImage.started')
            # update status
            ExtImage.status = STARTED
            ExtImage.setAutoDraw(True)
        
        # if ExtImage is active this frame...
        if ExtImage.status == STARTED:
            # update params
            pass
        
        # *ExtImageOverview* updates
        
        # if ExtImageOverview is starting this frame...
        if ExtImageOverview.status == NOT_STARTED and ExtInstTextImage=="Stimuli/Raw_3Faces.BMP":
            # keep track of start time/frame for later
            ExtImageOverview.frameNStart = frameN  # exact frame index
            ExtImageOverview.tStart = t  # local t and not account for scr refresh
            ExtImageOverview.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ExtImageOverview, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ExtImageOverview.started')
            # update status
            ExtImageOverview.status = STARTED
            ExtImageOverview.setAutoDraw(True)
        
        # if ExtImageOverview is active this frame...
        if ExtImageOverview.status == STARTED:
            # update params
            pass
        
        # *ExtInstEN* updates
        
        # if ExtInstEN is starting this frame...
        if ExtInstEN.status == NOT_STARTED and expInfo['Language'] == 'EN':
            # keep track of start time/frame for later
            ExtInstEN.frameNStart = frameN  # exact frame index
            ExtInstEN.tStart = t  # local t and not account for scr refresh
            ExtInstEN.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ExtInstEN, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ExtInstEN.started')
            # update status
            ExtInstEN.status = STARTED
            ExtInstEN.setAutoDraw(True)
        
        # if ExtInstEN is active this frame...
        if ExtInstEN.status == STARTED:
            # update params
            pass
        
        # *ExtInstCN* updates
        
        # if ExtInstCN is starting this frame...
        if ExtInstCN.status == NOT_STARTED and expInfo['Language'] == 'CN':
            # keep track of start time/frame for later
            ExtInstCN.frameNStart = frameN  # exact frame index
            ExtInstCN.tStart = t  # local t and not account for scr refresh
            ExtInstCN.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ExtInstCN, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ExtInstCN.started')
            # update status
            ExtInstCN.status = STARTED
            ExtInstCN.setAutoDraw(True)
        
        # if ExtInstCN is active this frame...
        if ExtInstCN.status == STARTED:
            # update params
            pass
        
        # *ExtRespKey* updates
        waitOnFlip = False
        
        # if ExtRespKey is starting this frame...
        if ExtRespKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ExtRespKey.frameNStart = frameN  # exact frame index
            ExtRespKey.tStart = t  # local t and not account for scr refresh
            ExtRespKey.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ExtRespKey, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ExtRespKey.started')
            # update status
            ExtRespKey.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(ExtRespKey.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(ExtRespKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if ExtRespKey.status == STARTED and not waitOnFlip:
            theseKeys = ExtRespKey.getKeys(keyList=['space'], waitRelease=False)
            _ExtRespKey_allKeys.extend(theseKeys)
            if len(_ExtRespKey_allKeys):
                ExtRespKey.keys = _ExtRespKey_allKeys[-1].name  # just the last key pressed
                ExtRespKey.rt = _ExtRespKey_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        # *ExtMouse* updates
        
        # if ExtMouse is starting this frame...
        if ExtMouse.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            ExtMouse.frameNStart = frameN  # exact frame index
            ExtMouse.tStart = t  # local t and not account for scr refresh
            ExtMouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ExtMouse, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('ExtMouse.started', t)
            # update status
            ExtMouse.status = STARTED
            ExtMouse.mouseClock.reset()
            prevButtonState = ExtMouse.getPressed()  # if button is down already this ISN'T a new click
        if ExtMouse.status == STARTED:  # only update if started and not finished!
            buttons = ExtMouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    x, y = ExtMouse.getPos()
                    ExtMouse.x.append(x)
                    ExtMouse.y.append(y)
                    buttons = ExtMouse.getPressed()
                    ExtMouse.leftButton.append(buttons[0])
                    ExtMouse.midButton.append(buttons[1])
                    ExtMouse.rightButton.append(buttons[2])
                    ExtMouse.time.append(ExtMouse.mouseClock.getTime())
        # *ExtSubmitEN* updates
        
        # if ExtSubmitEN is starting this frame...
        if ExtSubmitEN.status == NOT_STARTED and expInfo['Language'] == 'EN':
            # keep track of start time/frame for later
            ExtSubmitEN.frameNStart = frameN  # exact frame index
            ExtSubmitEN.tStart = t  # local t and not account for scr refresh
            ExtSubmitEN.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ExtSubmitEN, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ExtSubmitEN.started')
            # update status
            ExtSubmitEN.status = STARTED
            ExtSubmitEN.setAutoDraw(True)
        
        # if ExtSubmitEN is active this frame...
        if ExtSubmitEN.status == STARTED:
            # update params
            pass
            # check whether ExtSubmitEN has been pressed
            if ExtSubmitEN.isClicked:
                if not ExtSubmitEN.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    ExtSubmitEN.timesOn.append(ExtSubmitEN.buttonClock.getTime())
                    ExtSubmitEN.timesOff.append(ExtSubmitEN.buttonClock.getTime())
                elif len(ExtSubmitEN.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    ExtSubmitEN.timesOff[-1] = ExtSubmitEN.buttonClock.getTime()
                if not ExtSubmitEN.wasClicked:
                    # end routine when ExtSubmitEN is clicked
                    continueRoutine = False
                if not ExtSubmitEN.wasClicked:
                    # run callback code when ExtSubmitEN is clicked
                    pass
        # take note of whether ExtSubmitEN was clicked, so that next frame we know if clicks are new
        ExtSubmitEN.wasClicked = ExtSubmitEN.isClicked and ExtSubmitEN.status == STARTED
        # *ExtSubmitCN* updates
        
        # if ExtSubmitCN is starting this frame...
        if ExtSubmitCN.status == NOT_STARTED and expInfo['Language'] == 'CN':
            # keep track of start time/frame for later
            ExtSubmitCN.frameNStart = frameN  # exact frame index
            ExtSubmitCN.tStart = t  # local t and not account for scr refresh
            ExtSubmitCN.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ExtSubmitCN, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ExtSubmitCN.started')
            # update status
            ExtSubmitCN.status = STARTED
            ExtSubmitCN.setAutoDraw(True)
        
        # if ExtSubmitCN is active this frame...
        if ExtSubmitCN.status == STARTED:
            # update params
            pass
            # check whether ExtSubmitCN has been pressed
            if ExtSubmitCN.isClicked:
                if not ExtSubmitCN.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    ExtSubmitCN.timesOn.append(ExtSubmitCN.buttonClock.getTime())
                    ExtSubmitCN.timesOff.append(ExtSubmitCN.buttonClock.getTime())
                elif len(ExtSubmitCN.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    ExtSubmitCN.timesOff[-1] = ExtSubmitCN.buttonClock.getTime()
                if not ExtSubmitCN.wasClicked:
                    # end routine when ExtSubmitCN is clicked
                    continueRoutine = False
                if not ExtSubmitCN.wasClicked:
                    # run callback code when ExtSubmitCN is clicked
                    pass
        # take note of whether ExtSubmitCN was clicked, so that next frame we know if clicks are new
        ExtSubmitCN.wasClicked = ExtSubmitCN.isClicked and ExtSubmitCN.status == STARTED
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ExtInstComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ExtInst" ---
    for thisComponent in ExtInstComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if ExtRespKey.keys in ['', [], None]:  # No response was made
        ExtRespKey.keys = None
    ExtInstText.addData('ExtRespKey.keys',ExtRespKey.keys)
    if ExtRespKey.keys != None:  # we had a response
        ExtInstText.addData('ExtRespKey.rt', ExtRespKey.rt)
    # store data for ExtInstText (TrialHandler)
    ExtInstText.addData('ExtMouse.x', ExtMouse.x)
    ExtInstText.addData('ExtMouse.y', ExtMouse.y)
    ExtInstText.addData('ExtMouse.leftButton', ExtMouse.leftButton)
    ExtInstText.addData('ExtMouse.midButton', ExtMouse.midButton)
    ExtInstText.addData('ExtMouse.rightButton', ExtMouse.rightButton)
    ExtInstText.addData('ExtMouse.time', ExtMouse.time)
    ExtInstText.addData('ExtSubmitEN.numClicks', ExtSubmitEN.numClicks)
    if ExtSubmitEN.numClicks:
       ExtInstText.addData('ExtSubmitEN.timesOn', ExtSubmitEN.timesOn)
       ExtInstText.addData('ExtSubmitEN.timesOff', ExtSubmitEN.timesOff)
    else:
       ExtInstText.addData('ExtSubmitEN.timesOn', "")
       ExtInstText.addData('ExtSubmitEN.timesOff', "")
    ExtInstText.addData('ExtSubmitCN.numClicks', ExtSubmitCN.numClicks)
    if ExtSubmitCN.numClicks:
       ExtInstText.addData('ExtSubmitCN.timesOn', ExtSubmitCN.timesOn)
       ExtInstText.addData('ExtSubmitCN.timesOff', ExtSubmitCN.timesOff)
    else:
       ExtInstText.addData('ExtSubmitCN.timesOn', "")
       ExtInstText.addData('ExtSubmitCN.timesOff', "")
    # the Routine "ExtInst" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1.0 repeats of 'ExtInstText'


# set up handler to look after randomisation of conditions etc
Ext = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(schedule_files[2]),
    seed=None, name='Ext')
thisExp.addLoop(Ext)  # add the loop to the experiment
thisExt = Ext.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisExt.rgb)
if thisExt != None:
    for paramName in thisExt:
        exec('{} = thisExt[paramName]'.format(paramName))

for thisExt in Ext:
    currentLoop = Ext
    # abbreviate parameter names if possible (e.g. rgb = thisExt.rgb)
    if thisExt != None:
        for paramName in thisExt:
            exec('{} = thisExt[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "trialExt" ---
    continueRoutine = True
    # update component parameters for each repeat
    Ext_image.setImage(ExtName)
    # Run 'Begin Routine' code from EachTrial_3
    # If skipPhases is True, end the current routine and break the loop
    if skipPhases:
        continueRoutine = False  # Set continueRoutine to False to end the routine
        Ext.finished = True  # Set PreCond.finished to True to break the loop
    
    # If parallelTrigger is True, perform parallel triggering
    if parallelTrigger:
        ParaleData = 50  # Value to be set on the parallel port
        port.setData(ParaleData)  # Set the parallel port data to ParaleData
        if lfpTrigger:  # If lfpTrigger is also True
            lfpCtrlPort.setData(1)  # Set the LFP control parallel port data to 1
        core.wait(0.02)  # Wait for 0.02 seconds
        port.setData(0)  # Set the parallel port data back to 0
        if lfpTrigger:  # If lfpTrigger is True
            lfpCtrlPort.setData(0)  # Set the LFP control parallel port data back to 0
    # setup some python lists for storing info about the ExtTriggMouse
    ExtTriggMouse.x = []
    ExtTriggMouse.y = []
    ExtTriggMouse.leftButton = []
    ExtTriggMouse.midButton = []
    ExtTriggMouse.rightButton = []
    ExtTriggMouse.time = []
    gotValidClick = False  # until a click is received
    ExtTriggMouse.mouseClock.reset()
    ExtTriggKey.keys = []
    ExtTriggKey.rt = []
    _ExtTriggKey_allKeys = []
    # keep track of which components have finished
    trialExtComponents = [Ext_image, ExtTriggMouse, ExtTriggKey]
    for thisComponent in trialExtComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "trialExt" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 6.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Ext_image* updates
        
        # if Ext_image is starting this frame...
        if Ext_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Ext_image.frameNStart = frameN  # exact frame index
            Ext_image.tStart = t  # local t and not account for scr refresh
            Ext_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Ext_image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Ext_image.started')
            # update status
            Ext_image.status = STARTED
            Ext_image.setAutoDraw(True)
        
        # if Ext_image is active this frame...
        if Ext_image.status == STARTED:
            # update params
            pass
        
        # if Ext_image is stopping this frame...
        if Ext_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Ext_image.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                Ext_image.tStop = t  # not accounting for scr refresh
                Ext_image.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Ext_image.stopped')
                # update status
                Ext_image.status = FINISHED
                Ext_image.setAutoDraw(False)
        # *ExtTriggMouse* updates
        
        # if ExtTriggMouse is starting this frame...
        if ExtTriggMouse.status == NOT_STARTED and ExtName=="Stimuli/Trig.BMP":
            # keep track of start time/frame for later
            ExtTriggMouse.frameNStart = frameN  # exact frame index
            ExtTriggMouse.tStart = t  # local t and not account for scr refresh
            ExtTriggMouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ExtTriggMouse, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ExtTriggMouse.started')
            # update status
            ExtTriggMouse.status = STARTED
            prevButtonState = ExtTriggMouse.getPressed()  # if button is down already this ISN'T a new click
        
        # if ExtTriggMouse is stopping this frame...
        if ExtTriggMouse.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 6-frameTolerance:
                # keep track of stop time/frame for later
                ExtTriggMouse.tStop = t  # not accounting for scr refresh
                ExtTriggMouse.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ExtTriggMouse.stopped')
                # update status
                ExtTriggMouse.status = FINISHED
        if ExtTriggMouse.status == STARTED:  # only update if started and not finished!
            buttons = ExtTriggMouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    x, y = ExtTriggMouse.getPos()
                    ExtTriggMouse.x.append(x)
                    ExtTriggMouse.y.append(y)
                    buttons = ExtTriggMouse.getPressed()
                    ExtTriggMouse.leftButton.append(buttons[0])
                    ExtTriggMouse.midButton.append(buttons[1])
                    ExtTriggMouse.rightButton.append(buttons[2])
                    ExtTriggMouse.time.append(ExtTriggMouse.mouseClock.getTime())
                    
                    continueRoutine = False  # end routine on response
        
        # *ExtTriggKey* updates
        waitOnFlip = False
        
        # if ExtTriggKey is starting this frame...
        if ExtTriggKey.status == NOT_STARTED and ExtName=="Stimuli/Trig.BMP":
            # keep track of start time/frame for later
            ExtTriggKey.frameNStart = frameN  # exact frame index
            ExtTriggKey.tStart = t  # local t and not account for scr refresh
            ExtTriggKey.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ExtTriggKey, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ExtTriggKey.started')
            # update status
            ExtTriggKey.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(ExtTriggKey.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(ExtTriggKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if ExtTriggKey is stopping this frame...
        if ExtTriggKey.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 6-frameTolerance:
                # keep track of stop time/frame for later
                ExtTriggKey.tStop = t  # not accounting for scr refresh
                ExtTriggKey.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ExtTriggKey.stopped')
                # update status
                ExtTriggKey.status = FINISHED
                ExtTriggKey.status = FINISHED
        if ExtTriggKey.status == STARTED and not waitOnFlip:
            theseKeys = ExtTriggKey.getKeys(keyList=['space'], waitRelease=False)
            _ExtTriggKey_allKeys.extend(theseKeys)
            if len(_ExtTriggKey_allKeys):
                ExtTriggKey.keys = _ExtTriggKey_allKeys[-1].name  # just the last key pressed
                ExtTriggKey.rt = _ExtTriggKey_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialExtComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trialExt" ---
    for thisComponent in trialExtComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for Ext (TrialHandler)
    Ext.addData('ExtTriggMouse.x', ExtTriggMouse.x)
    Ext.addData('ExtTriggMouse.y', ExtTriggMouse.y)
    Ext.addData('ExtTriggMouse.leftButton', ExtTriggMouse.leftButton)
    Ext.addData('ExtTriggMouse.midButton', ExtTriggMouse.midButton)
    Ext.addData('ExtTriggMouse.rightButton', ExtTriggMouse.rightButton)
    Ext.addData('ExtTriggMouse.time', ExtTriggMouse.time)
    # check responses
    if ExtTriggKey.keys in ['', [], None]:  # No response was made
        ExtTriggKey.keys = None
    Ext.addData('ExtTriggKey.keys',ExtTriggKey.keys)
    if ExtTriggKey.keys != None:  # we had a response
        Ext.addData('ExtTriggKey.rt', ExtTriggKey.rt)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-6.000000)
    
    # --- Prepare to start Routine "ITI" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    ITIComponents = [FixCross]
    for thisComponent in ITIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ITI" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *FixCross* updates
        
        # if FixCross is starting this frame...
        if FixCross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            FixCross.frameNStart = frameN  # exact frame index
            FixCross.tStart = t  # local t and not account for scr refresh
            FixCross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FixCross, 'tStartRefresh')  # time at next scr refresh
            # update status
            FixCross.status = STARTED
            FixCross.setAutoDraw(True)
        
        # if FixCross is active this frame...
        if FixCross.status == STARTED:
            # update params
            pass
        
        # if FixCross is stopping this frame...
        if FixCross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > FixCross.tStartRefresh + random.uniform(0, 2)+6-frameTolerance:
                # keep track of stop time/frame for later
                FixCross.tStop = t  # not accounting for scr refresh
                FixCross.frameNStop = frameN  # exact frame index
                # update status
                FixCross.status = FINISHED
                FixCross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ITI" ---
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'Ext'

# get names of stimulus parameters
if Ext.trialList in ([], [None], None):
    params = []
else:
    params = Ext.trialList[0].keys()
# save data for this loop
Ext.saveAsExcel(filename + '.xlsx', sheetName='Ext',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# set up handler to look after randomisation of conditions etc
RatingExt = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('4_Rating.xlsx'),
    seed=None, name='RatingExt')
thisExp.addLoop(RatingExt)  # add the loop to the experiment
thisRatingExt = RatingExt.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRatingExt.rgb)
if thisRatingExt != None:
    for paramName in thisRatingExt:
        exec('{} = thisRatingExt[paramName]'.format(paramName))

for thisRatingExt in RatingExt:
    currentLoop = RatingExt
    # abbreviate parameter names if possible (e.g. rgb = thisRatingExt.rgb)
    if thisRatingExt != None:
        for paramName in thisRatingExt:
            exec('{} = thisRatingExt[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Rating" ---
    continueRoutine = True
    # update component parameters for each repeat
    image.setImage(CondName)
    RatingInstEN.setText(FearRatingInstTextEN)
    RatingInstCN.setText(FearRatingInstTextCN)
    Scale.reset()
    RatingKey.keys = []
    RatingKey.rt = []
    _RatingKey_allKeys = []
    # setup some python lists for storing info about the mouse
    mouse.x = []
    mouse.y = []
    mouse.leftButton = []
    mouse.midButton = []
    mouse.rightButton = []
    mouse.time = []
    gotValidClick = False  # until a click is received
    # reset SubmitEN to account for continued clicks & clear times on/off
    SubmitEN.reset()
    # reset SubmitCN to account for continued clicks & clear times on/off
    SubmitCN.reset()
    # keep track of which components have finished
    RatingComponents = [image, RatingInstEN, RatingInstCN, Scale, RatingKey, mouse, SubmitEN, SubmitCN]
    for thisComponent in RatingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Rating" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        
        # if image is starting this frame...
        if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image.started')
            # update status
            image.status = STARTED
            image.setAutoDraw(True)
        
        # if image is active this frame...
        if image.status == STARTED:
            # update params
            pass
        
        # *RatingInstEN* updates
        
        # if RatingInstEN is starting this frame...
        if RatingInstEN.status == NOT_STARTED and expInfo['Language'] == 'EN':
            # keep track of start time/frame for later
            RatingInstEN.frameNStart = frameN  # exact frame index
            RatingInstEN.tStart = t  # local t and not account for scr refresh
            RatingInstEN.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RatingInstEN, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'RatingInstEN.started')
            # update status
            RatingInstEN.status = STARTED
            RatingInstEN.setAutoDraw(True)
        
        # if RatingInstEN is active this frame...
        if RatingInstEN.status == STARTED:
            # update params
            pass
        
        # *RatingInstCN* updates
        
        # if RatingInstCN is starting this frame...
        if RatingInstCN.status == NOT_STARTED and expInfo['Language'] == 'CN':
            # keep track of start time/frame for later
            RatingInstCN.frameNStart = frameN  # exact frame index
            RatingInstCN.tStart = t  # local t and not account for scr refresh
            RatingInstCN.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RatingInstCN, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'RatingInstCN.started')
            # update status
            RatingInstCN.status = STARTED
            RatingInstCN.setAutoDraw(True)
        
        # if RatingInstCN is active this frame...
        if RatingInstCN.status == STARTED:
            # update params
            pass
        
        # *Scale* updates
        
        # if Scale is starting this frame...
        if Scale.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Scale.frameNStart = frameN  # exact frame index
            Scale.tStart = t  # local t and not account for scr refresh
            Scale.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Scale, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Scale.started')
            # update status
            Scale.status = STARTED
            Scale.setAutoDraw(True)
        
        # if Scale is active this frame...
        if Scale.status == STARTED:
            # update params
            pass
        
        # *RatingKey* updates
        waitOnFlip = False
        
        # if RatingKey is starting this frame...
        if RatingKey.status == NOT_STARTED and Scale.rating:
            # keep track of start time/frame for later
            RatingKey.frameNStart = frameN  # exact frame index
            RatingKey.tStart = t  # local t and not account for scr refresh
            RatingKey.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RatingKey, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'RatingKey.started')
            # update status
            RatingKey.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(RatingKey.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(RatingKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if RatingKey.status == STARTED and not waitOnFlip:
            theseKeys = RatingKey.getKeys(keyList=['space'], waitRelease=False)
            _RatingKey_allKeys.extend(theseKeys)
            if len(_RatingKey_allKeys):
                RatingKey.keys = _RatingKey_allKeys[-1].name  # just the last key pressed
                RatingKey.rt = _RatingKey_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        # *mouse* updates
        
        # if mouse is starting this frame...
        if mouse.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse.started', t)
            # update status
            mouse.status = STARTED
            mouse.mouseClock.reset()
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
        if mouse.status == STARTED:  # only update if started and not finished!
            buttons = mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    x, y = mouse.getPos()
                    mouse.x.append(x)
                    mouse.y.append(y)
                    buttons = mouse.getPressed()
                    mouse.leftButton.append(buttons[0])
                    mouse.midButton.append(buttons[1])
                    mouse.rightButton.append(buttons[2])
                    mouse.time.append(mouse.mouseClock.getTime())
        # *SubmitEN* updates
        
        # if SubmitEN is starting this frame...
        if SubmitEN.status == NOT_STARTED and Scale.rating and expInfo['Language'] == 'EN':
            # keep track of start time/frame for later
            SubmitEN.frameNStart = frameN  # exact frame index
            SubmitEN.tStart = t  # local t and not account for scr refresh
            SubmitEN.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(SubmitEN, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'SubmitEN.started')
            # update status
            SubmitEN.status = STARTED
            SubmitEN.setAutoDraw(True)
        
        # if SubmitEN is active this frame...
        if SubmitEN.status == STARTED:
            # update params
            pass
            # check whether SubmitEN has been pressed
            if SubmitEN.isClicked:
                if not SubmitEN.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    SubmitEN.timesOn.append(SubmitEN.buttonClock.getTime())
                    SubmitEN.timesOff.append(SubmitEN.buttonClock.getTime())
                elif len(SubmitEN.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    SubmitEN.timesOff[-1] = SubmitEN.buttonClock.getTime()
                if not SubmitEN.wasClicked:
                    # end routine when SubmitEN is clicked
                    continueRoutine = False
                if not SubmitEN.wasClicked:
                    # run callback code when SubmitEN is clicked
                    pass
        # take note of whether SubmitEN was clicked, so that next frame we know if clicks are new
        SubmitEN.wasClicked = SubmitEN.isClicked and SubmitEN.status == STARTED
        # *SubmitCN* updates
        
        # if SubmitCN is starting this frame...
        if SubmitCN.status == NOT_STARTED and Scale.rating and expInfo['Language'] == 'CN':
            # keep track of start time/frame for later
            SubmitCN.frameNStart = frameN  # exact frame index
            SubmitCN.tStart = t  # local t and not account for scr refresh
            SubmitCN.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(SubmitCN, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'SubmitCN.started')
            # update status
            SubmitCN.status = STARTED
            SubmitCN.setAutoDraw(True)
        
        # if SubmitCN is active this frame...
        if SubmitCN.status == STARTED:
            # update params
            pass
            # check whether SubmitCN has been pressed
            if SubmitCN.isClicked:
                if not SubmitCN.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    SubmitCN.timesOn.append(SubmitCN.buttonClock.getTime())
                    SubmitCN.timesOff.append(SubmitCN.buttonClock.getTime())
                elif len(SubmitCN.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    SubmitCN.timesOff[-1] = SubmitCN.buttonClock.getTime()
                if not SubmitCN.wasClicked:
                    # end routine when SubmitCN is clicked
                    continueRoutine = False
                if not SubmitCN.wasClicked:
                    # run callback code when SubmitCN is clicked
                    pass
        # take note of whether SubmitCN was clicked, so that next frame we know if clicks are new
        SubmitCN.wasClicked = SubmitCN.isClicked and SubmitCN.status == STARTED
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RatingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Rating" ---
    for thisComponent in RatingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    RatingExt.addData('Scale.response', Scale.getRating())
    RatingExt.addData('Scale.rt', Scale.getRT())
    # check responses
    if RatingKey.keys in ['', [], None]:  # No response was made
        RatingKey.keys = None
    RatingExt.addData('RatingKey.keys',RatingKey.keys)
    if RatingKey.keys != None:  # we had a response
        RatingExt.addData('RatingKey.rt', RatingKey.rt)
    # store data for RatingExt (TrialHandler)
    RatingExt.addData('mouse.x', mouse.x)
    RatingExt.addData('mouse.y', mouse.y)
    RatingExt.addData('mouse.leftButton', mouse.leftButton)
    RatingExt.addData('mouse.midButton', mouse.midButton)
    RatingExt.addData('mouse.rightButton', mouse.rightButton)
    RatingExt.addData('mouse.time', mouse.time)
    RatingExt.addData('SubmitEN.numClicks', SubmitEN.numClicks)
    if SubmitEN.numClicks:
       RatingExt.addData('SubmitEN.timesOn', SubmitEN.timesOn)
       RatingExt.addData('SubmitEN.timesOff', SubmitEN.timesOff)
    else:
       RatingExt.addData('SubmitEN.timesOn', "")
       RatingExt.addData('SubmitEN.timesOff', "")
    RatingExt.addData('SubmitCN.numClicks', SubmitCN.numClicks)
    if SubmitCN.numClicks:
       RatingExt.addData('SubmitCN.timesOn', SubmitCN.timesOn)
       RatingExt.addData('SubmitCN.timesOff', SubmitCN.timesOff)
    else:
       RatingExt.addData('SubmitCN.timesOn', "")
       RatingExt.addData('SubmitCN.timesOff', "")
    # the Routine "Rating" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'RatingExt'

# get names of stimulus parameters
if RatingExt.trialList in ([], [None], None):
    params = []
else:
    params = RatingExt.trialList[0].keys()
# save data for this loop
RatingExt.saveAsExcel(filename + '.xlsx', sheetName='RatingExt',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# set up handler to look after randomisation of conditions etc
EndText = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('0_Instructions.xlsx', selection='0:1'),
    seed=None, name='EndText')
thisExp.addLoop(EndText)  # add the loop to the experiment
thisEndText = EndText.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisEndText.rgb)
if thisEndText != None:
    for paramName in thisEndText:
        exec('{} = thisEndText[paramName]'.format(paramName))

for thisEndText in EndText:
    currentLoop = EndText
    # abbreviate parameter names if possible (e.g. rgb = thisEndText.rgb)
    if thisEndText != None:
        for paramName in thisEndText:
            exec('{} = thisEndText[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "EndBlock" ---
    continueRoutine = True
    # update component parameters for each repeat
    EndTxtEN.setText(EndTextEN)
    EndTxtCN.setText(EndTextCN)
    # keep track of which components have finished
    EndBlockComponents = [Bkg_Light, EndTxtEN, EndTxtCN]
    for thisComponent in EndBlockComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "EndBlock" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Bkg_Light* updates
        
        # if Bkg_Light is starting this frame...
        if Bkg_Light.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Bkg_Light.frameNStart = frameN  # exact frame index
            Bkg_Light.tStart = t  # local t and not account for scr refresh
            Bkg_Light.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Bkg_Light, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Bkg_Light.started')
            # update status
            Bkg_Light.status = STARTED
            Bkg_Light.setAutoDraw(True)
        
        # if Bkg_Light is active this frame...
        if Bkg_Light.status == STARTED:
            # update params
            pass
        
        # if Bkg_Light is stopping this frame...
        if Bkg_Light.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Bkg_Light.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                Bkg_Light.tStop = t  # not accounting for scr refresh
                Bkg_Light.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Bkg_Light.stopped')
                # update status
                Bkg_Light.status = FINISHED
                Bkg_Light.setAutoDraw(False)
        
        # *EndTxtEN* updates
        
        # if EndTxtEN is starting this frame...
        if EndTxtEN.status == NOT_STARTED and expInfo['Language'] == 'EN':
            # keep track of start time/frame for later
            EndTxtEN.frameNStart = frameN  # exact frame index
            EndTxtEN.tStart = t  # local t and not account for scr refresh
            EndTxtEN.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(EndTxtEN, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'EndTxtEN.started')
            # update status
            EndTxtEN.status = STARTED
            EndTxtEN.setAutoDraw(True)
        
        # if EndTxtEN is active this frame...
        if EndTxtEN.status == STARTED:
            # update params
            pass
        
        # if EndTxtEN is stopping this frame...
        if EndTxtEN.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > EndTxtEN.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                EndTxtEN.tStop = t  # not accounting for scr refresh
                EndTxtEN.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'EndTxtEN.stopped')
                # update status
                EndTxtEN.status = FINISHED
                EndTxtEN.setAutoDraw(False)
        
        # *EndTxtCN* updates
        
        # if EndTxtCN is starting this frame...
        if EndTxtCN.status == NOT_STARTED and expInfo['Language'] == 'CN':
            # keep track of start time/frame for later
            EndTxtCN.frameNStart = frameN  # exact frame index
            EndTxtCN.tStart = t  # local t and not account for scr refresh
            EndTxtCN.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(EndTxtCN, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'EndTxtCN.started')
            # update status
            EndTxtCN.status = STARTED
            EndTxtCN.setAutoDraw(True)
        
        # if EndTxtCN is active this frame...
        if EndTxtCN.status == STARTED:
            # update params
            pass
        
        # if EndTxtCN is stopping this frame...
        if EndTxtCN.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > EndTxtCN.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                EndTxtCN.tStop = t  # not accounting for scr refresh
                EndTxtCN.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'EndTxtCN.stopped')
                # update status
                EndTxtCN.status = FINISHED
                EndTxtCN.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in EndBlockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "EndBlock" ---
    for thisComponent in EndBlockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "EndBlock" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1.0 repeats of 'EndText'


# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
