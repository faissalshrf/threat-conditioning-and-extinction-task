#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on Tue Apr  4 16:10:46 2023
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
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



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.4'
expName = 'TCET'  # from the Builder filename that created this script
expInfo = {
    'Participant_ID': 'P00',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s/%s-%s' %(expInfo['Participant_ID'], expInfo['Participant_ID'], expInfo['date']) 

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/faissal/Library/CloudStorage/OneDrive-Nexus365/2023 – NAP Study/TCET_Task/V3_3Faces/TCET_V3_lastrun.py',
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
    monitor='', color=[0,0,0], colorSpace='rgb',
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

# --- Initialize components for Routine "Init" ---
# Run 'Begin Experiment' code from Properties
import random
parallelTrigger = False

isChinese = False

if parallelTrigger == True:
    from psychopy import parallel
    port = parallel.ParallelPort(address=0x0378)
    port.setData(0)

random.seed()
SetNums = [1,2,3]
Sess = 0

# --- Initialize components for Routine "PreCondInst" ---
InstrBkg = visual.Rect(
    win=win, name='InstrBkg',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=1, depth=0.0, interpolate=True)
PreCondImage = visual.ImageStim(
    win=win,
    name='PreCondImage', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0.05], size=[0.45,0.9],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
PreCondInstEN = visual.TextStim(win=win, name='PreCondInstEN',
    text='',
    font='Helvetica',
    pos=[0,0.7], height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
PreCondInstCN = visual.TextStim(win=win, name='PreCondInstCN',
    text='',
    font='PingFang SC',
    pos=(-0.2,0.7), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
InstrKeyResp = keyboard.Keyboard()
PreCondMouse = event.Mouse(win=win)
x, y = [None, None]
PreCondMouse.mouseClock = core.Clock()
PreCondSubmit = visual.ButtonStim(win, 
    text='CONTINUE', font='Helvetica',
    pos=[0.7, -0.8],
    letterHeight=0.06,
    size=[0.3, 0.1], borderWidth=0.0,
    fillColor=[0.8824, 0.6392, 0.4432], borderColor=None,
    color='black', colorSpace='rgb',
    opacity=1.0,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='PreCondSubmit'
)
PreCondSubmit.buttonClock = core.Clock()

# --- Initialize components for Routine "trialPreCond" ---
precondBkg = visual.Rect(
    win=win, name='precondBkg',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=1.0, depth=0.0, interpolate=True)
imagePreCond = visual.ImageStim(
    win=win,
    name='imagePreCond', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=[0, 0], size=[2, 2],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
PreCond_Mouse = event.Mouse(win=win)
x, y = [None, None]
PreCond_Mouse.mouseClock = core.Clock()

# --- Initialize components for Routine "ITI" ---
BlankBkg = visual.Rect(
    win=win, name='BlankBkg',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=1, depth=0.0, interpolate=True)

# --- Initialize components for Routine "Rating" ---
Bkg = visual.Rect(
    win=win, name='Bkg',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=1.0, depth=0.0, interpolate=True)
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0.1], size=[0.45,0.9],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
RatingInstEN = visual.TextStim(win=win, name='RatingInstEN',
    text='',
    font='Helvetica',
    pos=[0,0.7], height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
RatingInstCN = visual.TextStim(win=win, name='RatingInstCN',
    text='',
    font='PingFang SC',
    pos=[0,0.7], height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
Scale = visual.Slider(win=win, name='Scale',
    startValue=None, size=(1.2, 0.05), pos=(0, -0.5), units=None,
    labels=['– Negative', 'Positive +',], ticks=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='beige', lineColor='White', colorSpace='rgb',
    font='Helvetiva', labelHeight=0.07,
    flip=False, ori=0.0, depth=-4, readOnly=False)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
Submit = visual.ButtonStim(win, 
    text='SUBMIT', font='Helvetica',
    pos=[0.7, -0.8],
    letterHeight=0.06,
    size=[0.3, 0.1], borderWidth=0.0,
    fillColor=[0.8824, 0.6392, 0.4432], borderColor=None,
    color='black', colorSpace='rgb',
    opacity=1.0,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='Submit'
)
Submit.buttonClock = core.Clock()

# --- Initialize components for Routine "CondInst" ---
InstrBkg2 = visual.Rect(
    win=win, name='InstrBkg2',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=1.0, depth=0.0, interpolate=True)
CondImage = visual.ImageStim(
    win=win,
    name='CondImage', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0.05], size=[0.45,0.9],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
CondInstEN = visual.TextStim(win=win, name='CondInstEN',
    text='',
    font='Helvetica',
    pos=[0,0.7], height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
CondInstCN = visual.TextStim(win=win, name='CondInstCN',
    text='',
    font='PingFang SC',
    pos=[-0.2,0.7], height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
key_resp = keyboard.Keyboard()
CondMouse = event.Mouse(win=win)
x, y = [None, None]
CondMouse.mouseClock = core.Clock()
CondSubmit = visual.ButtonStim(win, 
    text='CONTINUE', font='Helvetica',
    pos=[0.7, -0.8],
    letterHeight=0.06,
    size=[0.3, 0.1], borderWidth=0.0,
    fillColor=[0.8824, 0.6392, 0.4432], borderColor=None,
    color='black', colorSpace='rgb',
    opacity=1.0,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='CondSubmit'
)
CondSubmit.buttonClock = core.Clock()

# --- Initialize components for Routine "trialCond" ---
CSBkg = visual.Rect(
    win=win, name='CSBkg',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=1.0, depth=0.0, interpolate=True)
CS_image = visual.ImageStim(
    win=win,
    name='CS_image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Cond_Mouse = event.Mouse(win=win)
x, y = [None, None]
Cond_Mouse.mouseClock = core.Clock()

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
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
sound_1 = sound.Sound('A', secs=1, stereo=True, hamming=True,
    name='sound_1')
sound_1.setVolume(0.3)

# --- Initialize components for Routine "ITI" ---
BlankBkg = visual.Rect(
    win=win, name='BlankBkg',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=1, depth=0.0, interpolate=True)

# --- Initialize components for Routine "Rating" ---
Bkg = visual.Rect(
    win=win, name='Bkg',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=1.0, depth=0.0, interpolate=True)
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0.1], size=[0.45,0.9],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
RatingInstEN = visual.TextStim(win=win, name='RatingInstEN',
    text='',
    font='Helvetica',
    pos=[0,0.7], height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
RatingInstCN = visual.TextStim(win=win, name='RatingInstCN',
    text='',
    font='PingFang SC',
    pos=[0,0.7], height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
Scale = visual.Slider(win=win, name='Scale',
    startValue=None, size=(1.2, 0.05), pos=(0, -0.5), units=None,
    labels=['– Negative', 'Positive +',], ticks=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='beige', lineColor='White', colorSpace='rgb',
    font='Helvetiva', labelHeight=0.07,
    flip=False, ori=0.0, depth=-4, readOnly=False)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
Submit = visual.ButtonStim(win, 
    text='SUBMIT', font='Helvetica',
    pos=[0.7, -0.8],
    letterHeight=0.06,
    size=[0.3, 0.1], borderWidth=0.0,
    fillColor=[0.8824, 0.6392, 0.4432], borderColor=None,
    color='black', colorSpace='rgb',
    opacity=1.0,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='Submit'
)
Submit.buttonClock = core.Clock()

# --- Initialize components for Routine "ExtInst" ---
InstrBkg3 = visual.Rect(
    win=win, name='InstrBkg3',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=1.0, depth=0.0, interpolate=True)
ExtImage = visual.ImageStim(
    win=win,
    name='ExtImage', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0.05], size=[0.45,0.9],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
ExtInstEN = visual.TextStim(win=win, name='ExtInstEN',
    text='',
    font='Helvetica',
    pos=[0,0.7], height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
ExtInstCN = visual.TextStim(win=win, name='ExtInstCN',
    text='',
    font='PingFang SC',
    pos=[-0.2,0.7], height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
ExtMouse = event.Mouse(win=win)
x, y = [None, None]
ExtMouse.mouseClock = core.Clock()
ExtSubmit = visual.ButtonStim(win, 
    text='CONTINUE', font='Helvetica',
    pos=[0.7, -0.8],
    letterHeight=0.06,
    size=[0.3, 0.1], borderWidth=0.0,
    fillColor=[0.8824, 0.6392, 0.4432], borderColor=None,
    color='black', colorSpace='rgb',
    opacity=1.0,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='ExtSubmit'
)
ExtSubmit.buttonClock = core.Clock()

# --- Initialize components for Routine "trialExt" ---
ExtBkg = visual.Rect(
    win=win, name='ExtBkg',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=1.0, depth=0.0, interpolate=True)
Ext_image = visual.ImageStim(
    win=win,
    name='Ext_image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
PreCond_Mouse_2 = event.Mouse(win=win)
x, y = [None, None]
PreCond_Mouse_2.mouseClock = core.Clock()
# Run 'Begin Experiment' code from EachTrial_3
if parallelTrigger == True:
   ParaleData = 50
   #ParaleData = int((TrgCol+0.6)*40+20)
   port.setData(ParaleData)
   core.wait(0.02)
   port.setData(0)

# --- Initialize components for Routine "ITI" ---
BlankBkg = visual.Rect(
    win=win, name='BlankBkg',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=1, depth=0.0, interpolate=True)

# --- Initialize components for Routine "Rating" ---
Bkg = visual.Rect(
    win=win, name='Bkg',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=1.0, depth=0.0, interpolate=True)
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0.1], size=[0.45,0.9],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
RatingInstEN = visual.TextStim(win=win, name='RatingInstEN',
    text='',
    font='Helvetica',
    pos=[0,0.7], height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
RatingInstCN = visual.TextStim(win=win, name='RatingInstCN',
    text='',
    font='PingFang SC',
    pos=[0,0.7], height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
Scale = visual.Slider(win=win, name='Scale',
    startValue=None, size=(1.2, 0.05), pos=(0, -0.5), units=None,
    labels=['– Negative', 'Positive +',], ticks=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='beige', lineColor='White', colorSpace='rgb',
    font='Helvetiva', labelHeight=0.07,
    flip=False, ori=0.0, depth=-4, readOnly=False)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
Submit = visual.ButtonStim(win, 
    text='SUBMIT', font='Helvetica',
    pos=[0.7, -0.8],
    letterHeight=0.06,
    size=[0.3, 0.1], borderWidth=0.0,
    fillColor=[0.8824, 0.6392, 0.4432], borderColor=None,
    color='black', colorSpace='rgb',
    opacity=1.0,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='Submit'
)
Submit.buttonClock = core.Clock()

# --- Initialize components for Routine "EndBlock" ---
Bkg_Light = visual.Rect(
    win=win, name='Bkg_Light',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor=[0.8824, 0.6392, 0.4432],
    opacity=1.0, depth=0.0, interpolate=True)
EndTxtEN = visual.TextStim(win=win, name='EndTxtEN',
    text='',
    font='Helvetica',
    pos=[0, 0], height=0.2, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
EndTxtCN = visual.TextStim(win=win, name='EndTxtCN',
    text='',
    font='PingFang SC',
    pos=[-0.1, 0], height=0.2, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "Init" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
InitComponents = []
for thisComponent in InitComponents:
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

# --- Run Routine "Init" ---
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
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InitComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Init" ---
for thisComponent in InitComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Init" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
PreCondInstText = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('0_Instructions.xlsx'),
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
    routineForceEnded = False
    # update component parameters for each repeat
    PreCondImage.setImage(PreCondInstTextImage)
    PreCondInstEN.setText(PreCondInstTextEN)
    PreCondInstCN.setText(PreCondInstTextCN)
    InstrKeyResp.keys = []
    InstrKeyResp.rt = []
    _InstrKeyResp_allKeys = []
    # setup some python lists for storing info about the PreCondMouse
    PreCondMouse.x = []
    PreCondMouse.y = []
    PreCondMouse.leftButton = []
    PreCondMouse.midButton = []
    PreCondMouse.rightButton = []
    PreCondMouse.time = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    PreCondInstComponents = [InstrBkg, PreCondImage, PreCondInstEN, PreCondInstCN, InstrKeyResp, PreCondMouse, PreCondSubmit]
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
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *InstrBkg* updates
        if InstrBkg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            InstrBkg.frameNStart = frameN  # exact frame index
            InstrBkg.tStart = t  # local t and not account for scr refresh
            InstrBkg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(InstrBkg, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'InstrBkg.started')
            InstrBkg.setAutoDraw(True)
        
        # *PreCondImage* updates
        if PreCondImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            PreCondImage.frameNStart = frameN  # exact frame index
            PreCondImage.tStart = t  # local t and not account for scr refresh
            PreCondImage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PreCondImage, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'PreCondImage.started')
            PreCondImage.setAutoDraw(True)
        
        # *PreCondInstEN* updates
        if PreCondInstEN.status == NOT_STARTED and isChinese==False:
            # keep track of start time/frame for later
            PreCondInstEN.frameNStart = frameN  # exact frame index
            PreCondInstEN.tStart = t  # local t and not account for scr refresh
            PreCondInstEN.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PreCondInstEN, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'PreCondInstEN.started')
            PreCondInstEN.setAutoDraw(True)
        
        # *PreCondInstCN* updates
        if PreCondInstCN.status == NOT_STARTED and isChinese==True:
            # keep track of start time/frame for later
            PreCondInstCN.frameNStart = frameN  # exact frame index
            PreCondInstCN.tStart = t  # local t and not account for scr refresh
            PreCondInstCN.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PreCondInstCN, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'PreCondInstCN.started')
            PreCondInstCN.setAutoDraw(True)
        
        # *InstrKeyResp* updates
        waitOnFlip = False
        if InstrKeyResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            InstrKeyResp.frameNStart = frameN  # exact frame index
            InstrKeyResp.tStart = t  # local t and not account for scr refresh
            InstrKeyResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(InstrKeyResp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'InstrKeyResp.started')
            InstrKeyResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(InstrKeyResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(InstrKeyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if InstrKeyResp.status == STARTED and not waitOnFlip:
            theseKeys = InstrKeyResp.getKeys(keyList=['space'], waitRelease=False)
            _InstrKeyResp_allKeys.extend(theseKeys)
            if len(_InstrKeyResp_allKeys):
                InstrKeyResp.keys = _InstrKeyResp_allKeys[-1].name  # just the last key pressed
                InstrKeyResp.rt = _InstrKeyResp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        # *PreCondMouse* updates
        if PreCondMouse.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            PreCondMouse.frameNStart = frameN  # exact frame index
            PreCondMouse.tStart = t  # local t and not account for scr refresh
            PreCondMouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PreCondMouse, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('PreCondMouse.started', t)
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
        
        # *PreCondSubmit* updates
        if PreCondSubmit.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            PreCondSubmit.frameNStart = frameN  # exact frame index
            PreCondSubmit.tStart = t  # local t and not account for scr refresh
            PreCondSubmit.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PreCondSubmit, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'PreCondSubmit.started')
            PreCondSubmit.setAutoDraw(True)
        if PreCondSubmit.status == STARTED:
            # check whether PreCondSubmit has been pressed
            if PreCondSubmit.isClicked:
                if not PreCondSubmit.wasClicked:
                    PreCondSubmit.timesOn.append(PreCondSubmit.buttonClock.getTime()) # store time of first click
                    PreCondSubmit.timesOff.append(PreCondSubmit.buttonClock.getTime()) # store time clicked until
                else:
                    PreCondSubmit.timesOff[-1] = PreCondSubmit.buttonClock.getTime() # update time clicked until
                if not PreCondSubmit.wasClicked:
                    continueRoutine = False  # end routine when PreCondSubmit is clicked
                    None
                PreCondSubmit.wasClicked = True  # if PreCondSubmit is still clicked next frame, it is not a new click
            else:
                PreCondSubmit.wasClicked = False  # if PreCondSubmit is clicked next frame, it is a new click
        else:
            PreCondSubmit.wasClicked = False  # if PreCondSubmit is clicked next frame, it is a new click
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
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
    if InstrKeyResp.keys in ['', [], None]:  # No response was made
        InstrKeyResp.keys = None
    PreCondInstText.addData('InstrKeyResp.keys',InstrKeyResp.keys)
    if InstrKeyResp.keys != None:  # we had a response
        PreCondInstText.addData('InstrKeyResp.rt', InstrKeyResp.rt)
    # store data for PreCondInstText (TrialHandler)
    PreCondInstText.addData('PreCondMouse.x', PreCondMouse.x)
    PreCondInstText.addData('PreCondMouse.y', PreCondMouse.y)
    PreCondInstText.addData('PreCondMouse.leftButton', PreCondMouse.leftButton)
    PreCondInstText.addData('PreCondMouse.midButton', PreCondMouse.midButton)
    PreCondInstText.addData('PreCondMouse.rightButton', PreCondMouse.rightButton)
    PreCondInstText.addData('PreCondMouse.time', PreCondMouse.time)
    PreCondInstText.addData('PreCondSubmit.numClicks', PreCondSubmit.numClicks)
    if PreCondSubmit.numClicks:
       PreCondInstText.addData('PreCondSubmit.timesOn', PreCondSubmit.timesOn)
       PreCondInstText.addData('PreCondSubmit.timesOff', PreCondSubmit.timesOff)
    else:
       PreCondInstText.addData('PreCondSubmit.timesOn', "")
       PreCondInstText.addData('PreCondSubmit.timesOff', "")
    # the Routine "PreCondInst" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1.0 repeats of 'PreCondInstText'


# set up handler to look after randomisation of conditions etc
PreCond = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('1_PreCondition.xlsx'),
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
    routineForceEnded = False
    # update component parameters for each repeat
    imagePreCond.setImage(PreCondName)
    # setup some python lists for storing info about the PreCond_Mouse
    PreCond_Mouse.x = []
    PreCond_Mouse.y = []
    PreCond_Mouse.leftButton = []
    PreCond_Mouse.midButton = []
    PreCond_Mouse.rightButton = []
    PreCond_Mouse.time = []
    gotValidClick = False  # until a click is received
    PreCond_Mouse.mouseClock.reset()
    # Run 'Begin Routine' code from EachTrial
    if parallelTrigger == True:
       ParaleData = 50  #Faissal
       #ParaleData = int((TrgCol+0.6)*40+20) #Faissal
       port.setData(ParaleData) #Faissal
       core.wait(0.02)
       port.setData(0) #Faissal
    # keep track of which components have finished
    trialPreCondComponents = [precondBkg, imagePreCond, PreCond_Mouse]
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
    while continueRoutine and routineTimer.getTime() < 6.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *precondBkg* updates
        if precondBkg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            precondBkg.frameNStart = frameN  # exact frame index
            precondBkg.tStart = t  # local t and not account for scr refresh
            precondBkg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(precondBkg, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'precondBkg.started')
            precondBkg.setAutoDraw(True)
        if precondBkg.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > precondBkg.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                precondBkg.tStop = t  # not accounting for scr refresh
                precondBkg.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'precondBkg.stopped')
                precondBkg.setAutoDraw(False)
        
        # *imagePreCond* updates
        if imagePreCond.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            imagePreCond.frameNStart = frameN  # exact frame index
            imagePreCond.tStart = t  # local t and not account for scr refresh
            imagePreCond.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imagePreCond, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imagePreCond.started')
            imagePreCond.setAutoDraw(True)
        if imagePreCond.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 6-frameTolerance:
                # keep track of stop time/frame for later
                imagePreCond.tStop = t  # not accounting for scr refresh
                imagePreCond.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imagePreCond.stopped')
                imagePreCond.setAutoDraw(False)
        # *PreCond_Mouse* updates
        if PreCond_Mouse.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            PreCond_Mouse.frameNStart = frameN  # exact frame index
            PreCond_Mouse.tStart = t  # local t and not account for scr refresh
            PreCond_Mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PreCond_Mouse, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'PreCond_Mouse.started')
            PreCond_Mouse.status = STARTED
            prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
        if PreCond_Mouse.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 6-frameTolerance:
                # keep track of stop time/frame for later
                PreCond_Mouse.tStop = t  # not accounting for scr refresh
                PreCond_Mouse.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'PreCond_Mouse.stopped')
                PreCond_Mouse.status = FINISHED
        if PreCond_Mouse.status == STARTED:  # only update if started and not finished!
            buttons = PreCond_Mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    x, y = PreCond_Mouse.getPos()
                    PreCond_Mouse.x.append(x)
                    PreCond_Mouse.y.append(y)
                    buttons = PreCond_Mouse.getPressed()
                    PreCond_Mouse.leftButton.append(buttons[0])
                    PreCond_Mouse.midButton.append(buttons[1])
                    PreCond_Mouse.rightButton.append(buttons[2])
                    PreCond_Mouse.time.append(PreCond_Mouse.mouseClock.getTime())
                    
                    continueRoutine = False  # abort routine on response
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
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
    PreCond.addData('PreCond_Mouse.x', PreCond_Mouse.x)
    PreCond.addData('PreCond_Mouse.y', PreCond_Mouse.y)
    PreCond.addData('PreCond_Mouse.leftButton', PreCond_Mouse.leftButton)
    PreCond.addData('PreCond_Mouse.midButton', PreCond_Mouse.midButton)
    PreCond.addData('PreCond_Mouse.rightButton', PreCond_Mouse.rightButton)
    PreCond.addData('PreCond_Mouse.time', PreCond_Mouse.time)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-6.000000)
    
    # --- Prepare to start Routine "ITI" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    ITIComponents = [BlankBkg]
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
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *BlankBkg* updates
        if BlankBkg.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            BlankBkg.frameNStart = frameN  # exact frame index
            BlankBkg.tStart = t  # local t and not account for scr refresh
            BlankBkg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(BlankBkg, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'BlankBkg.started')
            BlankBkg.setAutoDraw(True)
        if BlankBkg.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > BlankBkg.tStartRefresh + random.uniform(0, 2)+6-frameTolerance:
                # keep track of stop time/frame for later
                BlankBkg.tStop = t  # not accounting for scr refresh
                BlankBkg.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'BlankBkg.stopped')
                BlankBkg.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
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
    routineForceEnded = False
    # update component parameters for each repeat
    image.setImage(CondName)
    RatingInstEN.setText(FearRatingInstTextEN)
    RatingInstCN.setText(FearRatingInstTextCN)
    Scale.reset()
    # setup some python lists for storing info about the mouse
    mouse.x = []
    mouse.y = []
    mouse.leftButton = []
    mouse.midButton = []
    mouse.rightButton = []
    mouse.time = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    RatingComponents = [Bkg, image, RatingInstEN, RatingInstCN, Scale, mouse, Submit]
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
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Bkg* updates
        if Bkg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Bkg.frameNStart = frameN  # exact frame index
            Bkg.tStart = t  # local t and not account for scr refresh
            Bkg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Bkg, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Bkg.started')
            Bkg.setAutoDraw(True)
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image.started')
            image.setAutoDraw(True)
        
        # *RatingInstEN* updates
        if RatingInstEN.status == NOT_STARTED and isChinese==False:
            # keep track of start time/frame for later
            RatingInstEN.frameNStart = frameN  # exact frame index
            RatingInstEN.tStart = t  # local t and not account for scr refresh
            RatingInstEN.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RatingInstEN, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'RatingInstEN.started')
            RatingInstEN.setAutoDraw(True)
        
        # *RatingInstCN* updates
        if RatingInstCN.status == NOT_STARTED and isChinese==True:
            # keep track of start time/frame for later
            RatingInstCN.frameNStart = frameN  # exact frame index
            RatingInstCN.tStart = t  # local t and not account for scr refresh
            RatingInstCN.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RatingInstCN, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'RatingInstCN.started')
            RatingInstCN.setAutoDraw(True)
        
        # *Scale* updates
        if Scale.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Scale.frameNStart = frameN  # exact frame index
            Scale.tStart = t  # local t and not account for scr refresh
            Scale.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Scale, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Scale.started')
            Scale.setAutoDraw(True)
        # *mouse* updates
        if mouse.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse.started', t)
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
        
        # *Submit* updates
        if Submit.status == NOT_STARTED and Scale.rating:
            # keep track of start time/frame for later
            Submit.frameNStart = frameN  # exact frame index
            Submit.tStart = t  # local t and not account for scr refresh
            Submit.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Submit, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Submit.started')
            Submit.setAutoDraw(True)
        if Submit.status == STARTED:
            # check whether Submit has been pressed
            if Submit.isClicked:
                if not Submit.wasClicked:
                    Submit.timesOn.append(Submit.buttonClock.getTime()) # store time of first click
                    Submit.timesOff.append(Submit.buttonClock.getTime()) # store time clicked until
                else:
                    Submit.timesOff[-1] = Submit.buttonClock.getTime() # update time clicked until
                if not Submit.wasClicked:
                    continueRoutine = False  # end routine when Submit is clicked
                    None
                Submit.wasClicked = True  # if Submit is still clicked next frame, it is not a new click
            else:
                Submit.wasClicked = False  # if Submit is clicked next frame, it is a new click
        else:
            Submit.wasClicked = False  # if Submit is clicked next frame, it is a new click
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
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
    # store data for RatingPreCond (TrialHandler)
    RatingPreCond.addData('mouse.x', mouse.x)
    RatingPreCond.addData('mouse.y', mouse.y)
    RatingPreCond.addData('mouse.leftButton', mouse.leftButton)
    RatingPreCond.addData('mouse.midButton', mouse.midButton)
    RatingPreCond.addData('mouse.rightButton', mouse.rightButton)
    RatingPreCond.addData('mouse.time', mouse.time)
    RatingPreCond.addData('Submit.numClicks', Submit.numClicks)
    if Submit.numClicks:
       RatingPreCond.addData('Submit.timesOn', Submit.timesOn)
       RatingPreCond.addData('Submit.timesOff', Submit.timesOff)
    else:
       RatingPreCond.addData('Submit.timesOn', "")
       RatingPreCond.addData('Submit.timesOff', "")
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
    trialList=data.importConditions('0_Instructions.xlsx'),
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
    routineForceEnded = False
    # update component parameters for each repeat
    CondImage.setImage(CondInstTextImage)
    CondInstEN.setText(CondInstTextEN)
    CondInstCN.setText(CondInstTextCN)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # setup some python lists for storing info about the CondMouse
    CondMouse.x = []
    CondMouse.y = []
    CondMouse.leftButton = []
    CondMouse.midButton = []
    CondMouse.rightButton = []
    CondMouse.time = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    CondInstComponents = [InstrBkg2, CondImage, CondInstEN, CondInstCN, key_resp, CondMouse, CondSubmit]
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
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *InstrBkg2* updates
        if InstrBkg2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            InstrBkg2.frameNStart = frameN  # exact frame index
            InstrBkg2.tStart = t  # local t and not account for scr refresh
            InstrBkg2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(InstrBkg2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'InstrBkg2.started')
            InstrBkg2.setAutoDraw(True)
        
        # *CondImage* updates
        if CondImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            CondImage.frameNStart = frameN  # exact frame index
            CondImage.tStart = t  # local t and not account for scr refresh
            CondImage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CondImage, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'CondImage.started')
            CondImage.setAutoDraw(True)
        
        # *CondInstEN* updates
        if CondInstEN.status == NOT_STARTED and isChinese==False:
            # keep track of start time/frame for later
            CondInstEN.frameNStart = frameN  # exact frame index
            CondInstEN.tStart = t  # local t and not account for scr refresh
            CondInstEN.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CondInstEN, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'CondInstEN.started')
            CondInstEN.setAutoDraw(True)
        
        # *CondInstCN* updates
        if CondInstCN.status == NOT_STARTED and isChinese==True:
            # keep track of start time/frame for later
            CondInstCN.frameNStart = frameN  # exact frame index
            CondInstCN.tStart = t  # local t and not account for scr refresh
            CondInstCN.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CondInstCN, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'CondInstCN.started')
            CondInstCN.setAutoDraw(True)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp.started')
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        # *CondMouse* updates
        if CondMouse.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            CondMouse.frameNStart = frameN  # exact frame index
            CondMouse.tStart = t  # local t and not account for scr refresh
            CondMouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CondMouse, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('CondMouse.started', t)
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
        
        # *CondSubmit* updates
        if CondSubmit.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            CondSubmit.frameNStart = frameN  # exact frame index
            CondSubmit.tStart = t  # local t and not account for scr refresh
            CondSubmit.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CondSubmit, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'CondSubmit.started')
            CondSubmit.setAutoDraw(True)
        if CondSubmit.status == STARTED:
            # check whether CondSubmit has been pressed
            if CondSubmit.isClicked:
                if not CondSubmit.wasClicked:
                    CondSubmit.timesOn.append(CondSubmit.buttonClock.getTime()) # store time of first click
                    CondSubmit.timesOff.append(CondSubmit.buttonClock.getTime()) # store time clicked until
                else:
                    CondSubmit.timesOff[-1] = CondSubmit.buttonClock.getTime() # update time clicked until
                if not CondSubmit.wasClicked:
                    continueRoutine = False  # end routine when CondSubmit is clicked
                    None
                CondSubmit.wasClicked = True  # if CondSubmit is still clicked next frame, it is not a new click
            else:
                CondSubmit.wasClicked = False  # if CondSubmit is clicked next frame, it is a new click
        else:
            CondSubmit.wasClicked = False  # if CondSubmit is clicked next frame, it is a new click
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
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
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    CondInstText.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        CondInstText.addData('key_resp.rt', key_resp.rt)
    # store data for CondInstText (TrialHandler)
    CondInstText.addData('CondMouse.x', CondMouse.x)
    CondInstText.addData('CondMouse.y', CondMouse.y)
    CondInstText.addData('CondMouse.leftButton', CondMouse.leftButton)
    CondInstText.addData('CondMouse.midButton', CondMouse.midButton)
    CondInstText.addData('CondMouse.rightButton', CondMouse.rightButton)
    CondInstText.addData('CondMouse.time', CondMouse.time)
    CondInstText.addData('CondSubmit.numClicks', CondSubmit.numClicks)
    if CondSubmit.numClicks:
       CondInstText.addData('CondSubmit.timesOn', CondSubmit.timesOn)
       CondInstText.addData('CondSubmit.timesOff', CondSubmit.timesOff)
    else:
       CondInstText.addData('CondSubmit.timesOn', "")
       CondInstText.addData('CondSubmit.timesOff', "")
    # the Routine "CondInst" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1.0 repeats of 'CondInstText'


# set up handler to look after randomisation of conditions etc
Cond = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('2_Condition.xlsx'),
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
    routineForceEnded = False
    # update component parameters for each repeat
    CS_image.setImage(CSName)
    # setup some python lists for storing info about the Cond_Mouse
    Cond_Mouse.x = []
    Cond_Mouse.y = []
    Cond_Mouse.leftButton = []
    Cond_Mouse.midButton = []
    Cond_Mouse.rightButton = []
    Cond_Mouse.time = []
    gotValidClick = False  # until a click is received
    Cond_Mouse.mouseClock.reset()
    # Run 'Begin Routine' code from EachTrial_2
    if parallelTrigger == True:
       ParaleData = 50
       #ParaleData = int((TrgCol+0.6)*40+20)
       port.setData(ParaleData)
       core.wait(0.02)
       port.setData(0)
    # keep track of which components have finished
    trialCondComponents = [CSBkg, CS_image, Cond_Mouse]
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
    while continueRoutine and routineTimer.getTime() < 6.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *CSBkg* updates
        if CSBkg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            CSBkg.frameNStart = frameN  # exact frame index
            CSBkg.tStart = t  # local t and not account for scr refresh
            CSBkg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CSBkg, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'CSBkg.started')
            CSBkg.setAutoDraw(True)
        if CSBkg.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > CSBkg.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                CSBkg.tStop = t  # not accounting for scr refresh
                CSBkg.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'CSBkg.stopped')
                CSBkg.setAutoDraw(False)
        
        # *CS_image* updates
        if CS_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            CS_image.frameNStart = frameN  # exact frame index
            CS_image.tStart = t  # local t and not account for scr refresh
            CS_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CS_image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'CS_image.started')
            CS_image.setAutoDraw(True)
        if CS_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > CS_image.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                CS_image.tStop = t  # not accounting for scr refresh
                CS_image.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'CS_image.stopped')
                CS_image.setAutoDraw(False)
        # *Cond_Mouse* updates
        if Cond_Mouse.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Cond_Mouse.frameNStart = frameN  # exact frame index
            Cond_Mouse.tStart = t  # local t and not account for scr refresh
            Cond_Mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Cond_Mouse, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Cond_Mouse.started')
            Cond_Mouse.status = STARTED
            prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
        if Cond_Mouse.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 6-frameTolerance:
                # keep track of stop time/frame for later
                Cond_Mouse.tStop = t  # not accounting for scr refresh
                Cond_Mouse.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Cond_Mouse.stopped')
                Cond_Mouse.status = FINISHED
        if Cond_Mouse.status == STARTED:  # only update if started and not finished!
            buttons = Cond_Mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    x, y = Cond_Mouse.getPos()
                    Cond_Mouse.x.append(x)
                    Cond_Mouse.y.append(y)
                    buttons = Cond_Mouse.getPressed()
                    Cond_Mouse.leftButton.append(buttons[0])
                    Cond_Mouse.midButton.append(buttons[1])
                    Cond_Mouse.rightButton.append(buttons[2])
                    Cond_Mouse.time.append(Cond_Mouse.mouseClock.getTime())
                    
                    continueRoutine = False  # abort routine on response
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
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
    Cond.addData('Cond_Mouse.x', Cond_Mouse.x)
    Cond.addData('Cond_Mouse.y', Cond_Mouse.y)
    Cond.addData('Cond_Mouse.leftButton', Cond_Mouse.leftButton)
    Cond.addData('Cond_Mouse.midButton', Cond_Mouse.midButton)
    Cond.addData('Cond_Mouse.rightButton', Cond_Mouse.rightButton)
    Cond.addData('Cond_Mouse.time', Cond_Mouse.time)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-6.000000)
    
    # --- Prepare to start Routine "UCS" ---
    continueRoutine = True
    routineForceEnded = False
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
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *UCSBkg* updates
        if UCSBkg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            UCSBkg.frameNStart = frameN  # exact frame index
            UCSBkg.tStart = t  # local t and not account for scr refresh
            UCSBkg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(UCSBkg, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'UCSBkg.started')
            UCSBkg.setAutoDraw(True)
        if UCSBkg.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > UCSBkg.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                UCSBkg.tStop = t  # not accounting for scr refresh
                UCSBkg.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'UCSBkg.stopped')
                UCSBkg.setAutoDraw(False)
        
        # *UCS_image* updates
        if UCS_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            UCS_image.frameNStart = frameN  # exact frame index
            UCS_image.tStart = t  # local t and not account for scr refresh
            UCS_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(UCS_image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'UCS_image.started')
            UCS_image.setAutoDraw(True)
        if UCS_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > UCS_image.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                UCS_image.tStop = t  # not accounting for scr refresh
                UCS_image.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'UCS_image.stopped')
                UCS_image.setAutoDraw(False)
        # start/stop sound_1
        if sound_1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            sound_1.frameNStart = frameN  # exact frame index
            sound_1.tStart = t  # local t and not account for scr refresh
            sound_1.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('sound_1.started', tThisFlipGlobal)
            sound_1.play(when=win)  # sync with win flip
        if sound_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_1.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                sound_1.tStop = t  # not accounting for scr refresh
                sound_1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sound_1.stopped')
                sound_1.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
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
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    ITIComponents = [BlankBkg]
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
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *BlankBkg* updates
        if BlankBkg.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            BlankBkg.frameNStart = frameN  # exact frame index
            BlankBkg.tStart = t  # local t and not account for scr refresh
            BlankBkg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(BlankBkg, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'BlankBkg.started')
            BlankBkg.setAutoDraw(True)
        if BlankBkg.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > BlankBkg.tStartRefresh + random.uniform(0, 2)+6-frameTolerance:
                # keep track of stop time/frame for later
                BlankBkg.tStop = t  # not accounting for scr refresh
                BlankBkg.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'BlankBkg.stopped')
                BlankBkg.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
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
    routineForceEnded = False
    # update component parameters for each repeat
    image.setImage(CondName)
    RatingInstEN.setText(FearRatingInstTextEN)
    RatingInstCN.setText(FearRatingInstTextCN)
    Scale.reset()
    # setup some python lists for storing info about the mouse
    mouse.x = []
    mouse.y = []
    mouse.leftButton = []
    mouse.midButton = []
    mouse.rightButton = []
    mouse.time = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    RatingComponents = [Bkg, image, RatingInstEN, RatingInstCN, Scale, mouse, Submit]
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
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Bkg* updates
        if Bkg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Bkg.frameNStart = frameN  # exact frame index
            Bkg.tStart = t  # local t and not account for scr refresh
            Bkg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Bkg, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Bkg.started')
            Bkg.setAutoDraw(True)
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image.started')
            image.setAutoDraw(True)
        
        # *RatingInstEN* updates
        if RatingInstEN.status == NOT_STARTED and isChinese==False:
            # keep track of start time/frame for later
            RatingInstEN.frameNStart = frameN  # exact frame index
            RatingInstEN.tStart = t  # local t and not account for scr refresh
            RatingInstEN.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RatingInstEN, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'RatingInstEN.started')
            RatingInstEN.setAutoDraw(True)
        
        # *RatingInstCN* updates
        if RatingInstCN.status == NOT_STARTED and isChinese==True:
            # keep track of start time/frame for later
            RatingInstCN.frameNStart = frameN  # exact frame index
            RatingInstCN.tStart = t  # local t and not account for scr refresh
            RatingInstCN.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RatingInstCN, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'RatingInstCN.started')
            RatingInstCN.setAutoDraw(True)
        
        # *Scale* updates
        if Scale.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Scale.frameNStart = frameN  # exact frame index
            Scale.tStart = t  # local t and not account for scr refresh
            Scale.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Scale, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Scale.started')
            Scale.setAutoDraw(True)
        # *mouse* updates
        if mouse.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse.started', t)
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
        
        # *Submit* updates
        if Submit.status == NOT_STARTED and Scale.rating:
            # keep track of start time/frame for later
            Submit.frameNStart = frameN  # exact frame index
            Submit.tStart = t  # local t and not account for scr refresh
            Submit.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Submit, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Submit.started')
            Submit.setAutoDraw(True)
        if Submit.status == STARTED:
            # check whether Submit has been pressed
            if Submit.isClicked:
                if not Submit.wasClicked:
                    Submit.timesOn.append(Submit.buttonClock.getTime()) # store time of first click
                    Submit.timesOff.append(Submit.buttonClock.getTime()) # store time clicked until
                else:
                    Submit.timesOff[-1] = Submit.buttonClock.getTime() # update time clicked until
                if not Submit.wasClicked:
                    continueRoutine = False  # end routine when Submit is clicked
                    None
                Submit.wasClicked = True  # if Submit is still clicked next frame, it is not a new click
            else:
                Submit.wasClicked = False  # if Submit is clicked next frame, it is a new click
        else:
            Submit.wasClicked = False  # if Submit is clicked next frame, it is a new click
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
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
    # store data for RatingCond (TrialHandler)
    RatingCond.addData('mouse.x', mouse.x)
    RatingCond.addData('mouse.y', mouse.y)
    RatingCond.addData('mouse.leftButton', mouse.leftButton)
    RatingCond.addData('mouse.midButton', mouse.midButton)
    RatingCond.addData('mouse.rightButton', mouse.rightButton)
    RatingCond.addData('mouse.time', mouse.time)
    RatingCond.addData('Submit.numClicks', Submit.numClicks)
    if Submit.numClicks:
       RatingCond.addData('Submit.timesOn', Submit.timesOn)
       RatingCond.addData('Submit.timesOff', Submit.timesOff)
    else:
       RatingCond.addData('Submit.timesOn', "")
       RatingCond.addData('Submit.timesOff', "")
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
    trialList=data.importConditions('0_Instructions.xlsx'),
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
    routineForceEnded = False
    # update component parameters for each repeat
    ExtImage.setImage(ExtInstTextImage)
    ExtInstEN.setText(ExtInstTextEN)
    ExtInstCN.setText(ExtInstTextCN)
    # setup some python lists for storing info about the ExtMouse
    ExtMouse.x = []
    ExtMouse.y = []
    ExtMouse.leftButton = []
    ExtMouse.midButton = []
    ExtMouse.rightButton = []
    ExtMouse.time = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    ExtInstComponents = [InstrBkg3, ExtImage, ExtInstEN, ExtInstCN, ExtMouse, ExtSubmit]
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
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *InstrBkg3* updates
        if InstrBkg3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            InstrBkg3.frameNStart = frameN  # exact frame index
            InstrBkg3.tStart = t  # local t and not account for scr refresh
            InstrBkg3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(InstrBkg3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'InstrBkg3.started')
            InstrBkg3.setAutoDraw(True)
        
        # *ExtImage* updates
        if ExtImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ExtImage.frameNStart = frameN  # exact frame index
            ExtImage.tStart = t  # local t and not account for scr refresh
            ExtImage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ExtImage, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ExtImage.started')
            ExtImage.setAutoDraw(True)
        
        # *ExtInstEN* updates
        if ExtInstEN.status == NOT_STARTED and isChinese==False:
            # keep track of start time/frame for later
            ExtInstEN.frameNStart = frameN  # exact frame index
            ExtInstEN.tStart = t  # local t and not account for scr refresh
            ExtInstEN.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ExtInstEN, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ExtInstEN.started')
            ExtInstEN.setAutoDraw(True)
        
        # *ExtInstCN* updates
        if ExtInstCN.status == NOT_STARTED and isChinese==True:
            # keep track of start time/frame for later
            ExtInstCN.frameNStart = frameN  # exact frame index
            ExtInstCN.tStart = t  # local t and not account for scr refresh
            ExtInstCN.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ExtInstCN, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ExtInstCN.started')
            ExtInstCN.setAutoDraw(True)
        # *ExtMouse* updates
        if ExtMouse.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            ExtMouse.frameNStart = frameN  # exact frame index
            ExtMouse.tStart = t  # local t and not account for scr refresh
            ExtMouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ExtMouse, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('ExtMouse.started', t)
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
        
        # *ExtSubmit* updates
        if ExtSubmit.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            ExtSubmit.frameNStart = frameN  # exact frame index
            ExtSubmit.tStart = t  # local t and not account for scr refresh
            ExtSubmit.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ExtSubmit, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ExtSubmit.started')
            ExtSubmit.setAutoDraw(True)
        if ExtSubmit.status == STARTED:
            # check whether ExtSubmit has been pressed
            if ExtSubmit.isClicked:
                if not ExtSubmit.wasClicked:
                    ExtSubmit.timesOn.append(ExtSubmit.buttonClock.getTime()) # store time of first click
                    ExtSubmit.timesOff.append(ExtSubmit.buttonClock.getTime()) # store time clicked until
                else:
                    ExtSubmit.timesOff[-1] = ExtSubmit.buttonClock.getTime() # update time clicked until
                if not ExtSubmit.wasClicked:
                    continueRoutine = False  # end routine when ExtSubmit is clicked
                    None
                ExtSubmit.wasClicked = True  # if ExtSubmit is still clicked next frame, it is not a new click
            else:
                ExtSubmit.wasClicked = False  # if ExtSubmit is clicked next frame, it is a new click
        else:
            ExtSubmit.wasClicked = False  # if ExtSubmit is clicked next frame, it is a new click
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
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
    # store data for ExtInstText (TrialHandler)
    ExtInstText.addData('ExtMouse.x', ExtMouse.x)
    ExtInstText.addData('ExtMouse.y', ExtMouse.y)
    ExtInstText.addData('ExtMouse.leftButton', ExtMouse.leftButton)
    ExtInstText.addData('ExtMouse.midButton', ExtMouse.midButton)
    ExtInstText.addData('ExtMouse.rightButton', ExtMouse.rightButton)
    ExtInstText.addData('ExtMouse.time', ExtMouse.time)
    ExtInstText.addData('ExtSubmit.numClicks', ExtSubmit.numClicks)
    if ExtSubmit.numClicks:
       ExtInstText.addData('ExtSubmit.timesOn', ExtSubmit.timesOn)
       ExtInstText.addData('ExtSubmit.timesOff', ExtSubmit.timesOff)
    else:
       ExtInstText.addData('ExtSubmit.timesOn', "")
       ExtInstText.addData('ExtSubmit.timesOff', "")
    # the Routine "ExtInst" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1.0 repeats of 'ExtInstText'


# set up handler to look after randomisation of conditions etc
Extinction = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('3_Extinction.xlsx'),
    seed=None, name='Extinction')
thisExp.addLoop(Extinction)  # add the loop to the experiment
thisExtinction = Extinction.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisExtinction.rgb)
if thisExtinction != None:
    for paramName in thisExtinction:
        exec('{} = thisExtinction[paramName]'.format(paramName))

for thisExtinction in Extinction:
    currentLoop = Extinction
    # abbreviate parameter names if possible (e.g. rgb = thisExtinction.rgb)
    if thisExtinction != None:
        for paramName in thisExtinction:
            exec('{} = thisExtinction[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "trialExt" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    Ext_image.setImage(ExtName)
    # setup some python lists for storing info about the PreCond_Mouse_2
    PreCond_Mouse_2.x = []
    PreCond_Mouse_2.y = []
    PreCond_Mouse_2.leftButton = []
    PreCond_Mouse_2.midButton = []
    PreCond_Mouse_2.rightButton = []
    PreCond_Mouse_2.time = []
    gotValidClick = False  # until a click is received
    PreCond_Mouse_2.mouseClock.reset()
    # keep track of which components have finished
    trialExtComponents = [ExtBkg, Ext_image, PreCond_Mouse_2]
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
    while continueRoutine and routineTimer.getTime() < 6.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ExtBkg* updates
        if ExtBkg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ExtBkg.frameNStart = frameN  # exact frame index
            ExtBkg.tStart = t  # local t and not account for scr refresh
            ExtBkg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ExtBkg, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ExtBkg.started')
            ExtBkg.setAutoDraw(True)
        if ExtBkg.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ExtBkg.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                ExtBkg.tStop = t  # not accounting for scr refresh
                ExtBkg.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ExtBkg.stopped')
                ExtBkg.setAutoDraw(False)
        
        # *Ext_image* updates
        if Ext_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Ext_image.frameNStart = frameN  # exact frame index
            Ext_image.tStart = t  # local t and not account for scr refresh
            Ext_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Ext_image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Ext_image.started')
            Ext_image.setAutoDraw(True)
        if Ext_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Ext_image.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                Ext_image.tStop = t  # not accounting for scr refresh
                Ext_image.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Ext_image.stopped')
                Ext_image.setAutoDraw(False)
        # *PreCond_Mouse_2* updates
        if PreCond_Mouse_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            PreCond_Mouse_2.frameNStart = frameN  # exact frame index
            PreCond_Mouse_2.tStart = t  # local t and not account for scr refresh
            PreCond_Mouse_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PreCond_Mouse_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'PreCond_Mouse_2.started')
            PreCond_Mouse_2.status = STARTED
            prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
        if PreCond_Mouse_2.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 6-frameTolerance:
                # keep track of stop time/frame for later
                PreCond_Mouse_2.tStop = t  # not accounting for scr refresh
                PreCond_Mouse_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'PreCond_Mouse_2.stopped')
                PreCond_Mouse_2.status = FINISHED
        if PreCond_Mouse_2.status == STARTED:  # only update if started and not finished!
            buttons = PreCond_Mouse_2.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    x, y = PreCond_Mouse_2.getPos()
                    PreCond_Mouse_2.x.append(x)
                    PreCond_Mouse_2.y.append(y)
                    buttons = PreCond_Mouse_2.getPressed()
                    PreCond_Mouse_2.leftButton.append(buttons[0])
                    PreCond_Mouse_2.midButton.append(buttons[1])
                    PreCond_Mouse_2.rightButton.append(buttons[2])
                    PreCond_Mouse_2.time.append(PreCond_Mouse_2.mouseClock.getTime())
                    
                    continueRoutine = False  # abort routine on response
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
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
    # store data for Extinction (TrialHandler)
    Extinction.addData('PreCond_Mouse_2.x', PreCond_Mouse_2.x)
    Extinction.addData('PreCond_Mouse_2.y', PreCond_Mouse_2.y)
    Extinction.addData('PreCond_Mouse_2.leftButton', PreCond_Mouse_2.leftButton)
    Extinction.addData('PreCond_Mouse_2.midButton', PreCond_Mouse_2.midButton)
    Extinction.addData('PreCond_Mouse_2.rightButton', PreCond_Mouse_2.rightButton)
    Extinction.addData('PreCond_Mouse_2.time', PreCond_Mouse_2.time)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-6.000000)
    
    # --- Prepare to start Routine "ITI" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    ITIComponents = [BlankBkg]
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
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *BlankBkg* updates
        if BlankBkg.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            BlankBkg.frameNStart = frameN  # exact frame index
            BlankBkg.tStart = t  # local t and not account for scr refresh
            BlankBkg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(BlankBkg, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'BlankBkg.started')
            BlankBkg.setAutoDraw(True)
        if BlankBkg.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > BlankBkg.tStartRefresh + random.uniform(0, 2)+6-frameTolerance:
                # keep track of stop time/frame for later
                BlankBkg.tStop = t  # not accounting for scr refresh
                BlankBkg.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'BlankBkg.stopped')
                BlankBkg.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
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
    
# completed 1.0 repeats of 'Extinction'

# get names of stimulus parameters
if Extinction.trialList in ([], [None], None):
    params = []
else:
    params = Extinction.trialList[0].keys()
# save data for this loop
Extinction.saveAsExcel(filename + '.xlsx', sheetName='Extinction',
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
    routineForceEnded = False
    # update component parameters for each repeat
    image.setImage(CondName)
    RatingInstEN.setText(FearRatingInstTextEN)
    RatingInstCN.setText(FearRatingInstTextCN)
    Scale.reset()
    # setup some python lists for storing info about the mouse
    mouse.x = []
    mouse.y = []
    mouse.leftButton = []
    mouse.midButton = []
    mouse.rightButton = []
    mouse.time = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    RatingComponents = [Bkg, image, RatingInstEN, RatingInstCN, Scale, mouse, Submit]
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
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Bkg* updates
        if Bkg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Bkg.frameNStart = frameN  # exact frame index
            Bkg.tStart = t  # local t and not account for scr refresh
            Bkg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Bkg, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Bkg.started')
            Bkg.setAutoDraw(True)
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image.started')
            image.setAutoDraw(True)
        
        # *RatingInstEN* updates
        if RatingInstEN.status == NOT_STARTED and isChinese==False:
            # keep track of start time/frame for later
            RatingInstEN.frameNStart = frameN  # exact frame index
            RatingInstEN.tStart = t  # local t and not account for scr refresh
            RatingInstEN.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RatingInstEN, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'RatingInstEN.started')
            RatingInstEN.setAutoDraw(True)
        
        # *RatingInstCN* updates
        if RatingInstCN.status == NOT_STARTED and isChinese==True:
            # keep track of start time/frame for later
            RatingInstCN.frameNStart = frameN  # exact frame index
            RatingInstCN.tStart = t  # local t and not account for scr refresh
            RatingInstCN.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RatingInstCN, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'RatingInstCN.started')
            RatingInstCN.setAutoDraw(True)
        
        # *Scale* updates
        if Scale.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Scale.frameNStart = frameN  # exact frame index
            Scale.tStart = t  # local t and not account for scr refresh
            Scale.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Scale, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Scale.started')
            Scale.setAutoDraw(True)
        # *mouse* updates
        if mouse.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse.started', t)
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
        
        # *Submit* updates
        if Submit.status == NOT_STARTED and Scale.rating:
            # keep track of start time/frame for later
            Submit.frameNStart = frameN  # exact frame index
            Submit.tStart = t  # local t and not account for scr refresh
            Submit.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Submit, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Submit.started')
            Submit.setAutoDraw(True)
        if Submit.status == STARTED:
            # check whether Submit has been pressed
            if Submit.isClicked:
                if not Submit.wasClicked:
                    Submit.timesOn.append(Submit.buttonClock.getTime()) # store time of first click
                    Submit.timesOff.append(Submit.buttonClock.getTime()) # store time clicked until
                else:
                    Submit.timesOff[-1] = Submit.buttonClock.getTime() # update time clicked until
                if not Submit.wasClicked:
                    continueRoutine = False  # end routine when Submit is clicked
                    None
                Submit.wasClicked = True  # if Submit is still clicked next frame, it is not a new click
            else:
                Submit.wasClicked = False  # if Submit is clicked next frame, it is a new click
        else:
            Submit.wasClicked = False  # if Submit is clicked next frame, it is a new click
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
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
    # store data for RatingExt (TrialHandler)
    RatingExt.addData('mouse.x', mouse.x)
    RatingExt.addData('mouse.y', mouse.y)
    RatingExt.addData('mouse.leftButton', mouse.leftButton)
    RatingExt.addData('mouse.midButton', mouse.midButton)
    RatingExt.addData('mouse.rightButton', mouse.rightButton)
    RatingExt.addData('mouse.time', mouse.time)
    RatingExt.addData('Submit.numClicks', Submit.numClicks)
    if Submit.numClicks:
       RatingExt.addData('Submit.timesOn', Submit.timesOn)
       RatingExt.addData('Submit.timesOff', Submit.timesOff)
    else:
       RatingExt.addData('Submit.timesOn', "")
       RatingExt.addData('Submit.timesOff', "")
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
    trialList=data.importConditions('0_Instructions.xlsx'),
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
    routineForceEnded = False
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
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Bkg_Light* updates
        if Bkg_Light.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Bkg_Light.frameNStart = frameN  # exact frame index
            Bkg_Light.tStart = t  # local t and not account for scr refresh
            Bkg_Light.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Bkg_Light, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Bkg_Light.started')
            Bkg_Light.setAutoDraw(True)
        if Bkg_Light.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Bkg_Light.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                Bkg_Light.tStop = t  # not accounting for scr refresh
                Bkg_Light.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Bkg_Light.stopped')
                Bkg_Light.setAutoDraw(False)
        
        # *EndTxtEN* updates
        if EndTxtEN.status == NOT_STARTED and isChinese==False:
            # keep track of start time/frame for later
            EndTxtEN.frameNStart = frameN  # exact frame index
            EndTxtEN.tStart = t  # local t and not account for scr refresh
            EndTxtEN.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(EndTxtEN, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'EndTxtEN.started')
            EndTxtEN.setAutoDraw(True)
        if EndTxtEN.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > EndTxtEN.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                EndTxtEN.tStop = t  # not accounting for scr refresh
                EndTxtEN.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'EndTxtEN.stopped')
                EndTxtEN.setAutoDraw(False)
        
        # *EndTxtCN* updates
        if EndTxtCN.status == NOT_STARTED and isChinese==True:
            # keep track of start time/frame for later
            EndTxtCN.frameNStart = frameN  # exact frame index
            EndTxtCN.tStart = t  # local t and not account for scr refresh
            EndTxtCN.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(EndTxtCN, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'EndTxtCN.started')
            EndTxtCN.setAutoDraw(True)
        if EndTxtCN.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > EndTxtCN.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                EndTxtCN.tStop = t  # not accounting for scr refresh
                EndTxtCN.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'EndTxtCN.stopped')
                EndTxtCN.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
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
