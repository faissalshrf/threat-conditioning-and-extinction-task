﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.1),
    on May 28, 2023, at 00:04
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



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2023.1.1'
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
    originPath='C:\\Users\\Faiss\\OneDrive - Nexus365\\2023 – NAP Study\\TCET_Task\\TCET_Sharif\\TCET_Sharif.py',
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
    size=[1382, 864], fullscr=True, screen=0, 
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

# --- Initialize components for Routine "Init" ---
# Run 'Begin Experiment' code from Properties
import random
parallelTrigger = False

isChinese = False #sets task lang to Chinese
skipPhases = False #Shows only instructions and ratings    

if parallelTrigger == True:
    from psychopy import parallel
    port = parallel.ParallelPort(address=0x0378)
    port.setData(0)
    if lfpTrigger == True:
        lfpCtrlPort = parallel.ParallelPort(address=0x037A)
        lfpCtrlPort.setData(0)

random.seed()
SetNums = [1,2,3]
Sess = 0

# --- Initialize components for Routine "PreCondInst" ---
PreCondImage = visual.ImageStim(
    win=win,
    name='PreCondImage', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0.05], size=[0.45,0.9],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
PreCondInstEN = visual.TextStim(win=win, name='PreCondInstEN',
    text='',
    font='Arial',
    pos=[0,0.7], height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
PreCondInstCN = visual.TextStim(win=win, name='PreCondInstCN',
    text='',
    font='PingFang SC',
    pos=(-0.2,0.7), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
PreCondMouse = event.Mouse(win=win)
x, y = [None, None]
PreCondMouse.mouseClock = core.Clock()
PreCondSubmit = visual.ButtonStim(win, 
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
    name='PreCondSubmit',
    depth=-4
)
PreCondSubmit.buttonClock = core.Clock()

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
    pos=[0,0.7], height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
Scale = visual.Slider(win=win, name='Scale',
    startValue=None, size=(1.2, 0.05), pos=(0, -0.5), units=win.units,
    labels=['– Negative', 'Positive +',], ticks=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='beige', lineColor='White', colorSpace='rgb',
    font='Arial', labelHeight=0.07,
    flip=False, ori=0.0, depth=-3, readOnly=False)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
Submit = visual.ButtonStim(win, 
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
    name='Submit',
    depth=-5
)
Submit.buttonClock = core.Clock()

# --- Initialize components for Routine "CondInst" ---
CondImage = visual.ImageStim(
    win=win,
    name='CondImage', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0.05], size=[0.45,0.9],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
CondInstEN = visual.TextStim(win=win, name='CondInstEN',
    text='',
    font='Arial',
    pos=[0,0.7], height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
CondInstCN = visual.TextStim(win=win, name='CondInstCN',
    text='',
    font='PingFang SC',
    pos=[-0.2,0.7], height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
CondMouse = event.Mouse(win=win)
x, y = [None, None]
CondMouse.mouseClock = core.Clock()
CondSubmit = visual.ButtonStim(win, 
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
    name='CondSubmit',
    depth=-4
)
CondSubmit.buttonClock = core.Clock()

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
    pos=[0,0.7], height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
Scale = visual.Slider(win=win, name='Scale',
    startValue=None, size=(1.2, 0.05), pos=(0, -0.5), units=win.units,
    labels=['– Negative', 'Positive +',], ticks=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='beige', lineColor='White', colorSpace='rgb',
    font='Arial', labelHeight=0.07,
    flip=False, ori=0.0, depth=-3, readOnly=False)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
Submit = visual.ButtonStim(win, 
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
    name='Submit',
    depth=-5
)
Submit.buttonClock = core.Clock()

# --- Initialize components for Routine "ExtInst" ---
ExtImage = visual.ImageStim(
    win=win,
    name='ExtImage', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0.05], size=[0.45,0.9],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
ExtInstEN = visual.TextStim(win=win, name='ExtInstEN',
    text='',
    font='Arial',
    pos=[0,0.7], height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
ExtInstCN = visual.TextStim(win=win, name='ExtInstCN',
    text='',
    font='PingFang SC',
    pos=[-0.2,0.7], height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
ExtMouse = event.Mouse(win=win)
x, y = [None, None]
ExtMouse.mouseClock = core.Clock()
ExtSubmit = visual.ButtonStim(win, 
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
    name='ExtSubmit',
    depth=-4
)
ExtSubmit.buttonClock = core.Clock()

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
    pos=[0,0.7], height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
Scale = visual.Slider(win=win, name='Scale',
    startValue=None, size=(1.2, 0.05), pos=(0, -0.5), units=win.units,
    labels=['– Negative', 'Positive +',], ticks=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='beige', lineColor='White', colorSpace='rgb',
    font='Arial', labelHeight=0.07,
    flip=False, ori=0.0, depth=-3, readOnly=False)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
Submit = visual.ButtonStim(win, 
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
    name='Submit',
    depth=-5
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
    font='Arial',
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
    trialList=data.importConditions('0_Instructions.xlsx', selection='0:4'),
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
    PreCondInstEN.setText(PreCondInstTextEN)
    PreCondInstCN.setText(PreCondInstTextCN)
    # setup some python lists for storing info about the PreCondMouse
    PreCondMouse.x = []
    PreCondMouse.y = []
    PreCondMouse.leftButton = []
    PreCondMouse.midButton = []
    PreCondMouse.rightButton = []
    PreCondMouse.time = []
    gotValidClick = False  # until a click is received
    # reset PreCondSubmit to account for continued clicks & clear times on/off
    PreCondSubmit.reset()
    # keep track of which components have finished
    PreCondInstComponents = [PreCondImage, PreCondInstEN, PreCondInstCN, PreCondMouse, PreCondSubmit]
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
        if PreCondImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
        
        # *PreCondInstEN* updates
        
        # if PreCondInstEN is starting this frame...
        if PreCondInstEN.status == NOT_STARTED and isChinese==False:
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
        if PreCondInstCN.status == NOT_STARTED and isChinese==True:
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
        # *PreCondSubmit* updates
        
        # if PreCondSubmit is starting this frame...
        if PreCondSubmit.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            PreCondSubmit.frameNStart = frameN  # exact frame index
            PreCondSubmit.tStart = t  # local t and not account for scr refresh
            PreCondSubmit.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PreCondSubmit, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'PreCondSubmit.started')
            # update status
            PreCondSubmit.status = STARTED
            PreCondSubmit.setAutoDraw(True)
        
        # if PreCondSubmit is active this frame...
        if PreCondSubmit.status == STARTED:
            # update params
            pass
            # check whether PreCondSubmit has been pressed
            if PreCondSubmit.isClicked:
                if not PreCondSubmit.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    PreCondSubmit.timesOn.append(PreCondSubmit.buttonClock.getTime())
                    PreCondSubmit.timesOff.append(PreCondSubmit.buttonClock.getTime())
                elif len(PreCondSubmit.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    PreCondSubmit.timesOff[-1] = PreCondSubmit.buttonClock.getTime()
                if not PreCondSubmit.wasClicked:
                    # end routine when PreCondSubmit is clicked
                    continueRoutine = False
                if not PreCondSubmit.wasClicked:
                    # run callback code when PreCondSubmit is clicked
                    pass
        # take note of whether PreCondSubmit was clicked, so that next frame we know if clicks are new
        PreCondSubmit.wasClicked = PreCondSubmit.isClicked and PreCondSubmit.status == STARTED
        
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
    # update component parameters for each repeat
    imagePreCond.setImage(PreCondName)
    # Run 'Begin Routine' code from EachTrial
    if skipPhases == True:
        continueRoutine = False #end the routine
        PreCond.finished = True #break the loop
    
    if parallelTrigger == True:
       ParaleData = 50  #Faissal
       #ParaleData = int((TrgCol+0.6)*40+20) #Faissal
       port.setData(ParaleData) #Faissal
       if lfpTrigger == True:
            lfpCtrlPort.setData(1)
       core.wait(0.02)
       port.setData(0) #Faissal
       if lfpTrigger == True:
            lfpCtrlPort.setData(0)
    # setup some python lists for storing info about the PreCondTriggMouse
    PreCondTriggMouse.x = []
    PreCondTriggMouse.y = []
    PreCondTriggMouse.leftButton = []
    PreCondTriggMouse.midButton = []
    PreCondTriggMouse.rightButton = []
    PreCondTriggMouse.time = []
    gotValidClick = False  # until a click is received
    PreCondTriggMouse.mouseClock.reset()
    # keep track of which components have finished
    trialPreCondComponents = [imagePreCond, PreCondTriggMouse]
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
    # setup some python lists for storing info about the mouse
    mouse.x = []
    mouse.y = []
    mouse.leftButton = []
    mouse.midButton = []
    mouse.rightButton = []
    mouse.time = []
    gotValidClick = False  # until a click is received
    # reset Submit to account for continued clicks & clear times on/off
    Submit.reset()
    # keep track of which components have finished
    RatingComponents = [image, RatingInstEN, RatingInstCN, Scale, mouse, Submit]
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
        if RatingInstEN.status == NOT_STARTED and isChinese==False:
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
        if RatingInstCN.status == NOT_STARTED and isChinese==True:
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
        # *Submit* updates
        
        # if Submit is starting this frame...
        if Submit.status == NOT_STARTED and Scale.rating:
            # keep track of start time/frame for later
            Submit.frameNStart = frameN  # exact frame index
            Submit.tStart = t  # local t and not account for scr refresh
            Submit.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Submit, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Submit.started')
            # update status
            Submit.status = STARTED
            Submit.setAutoDraw(True)
        
        # if Submit is active this frame...
        if Submit.status == STARTED:
            # update params
            pass
            # check whether Submit has been pressed
            if Submit.isClicked:
                if not Submit.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    Submit.timesOn.append(Submit.buttonClock.getTime())
                    Submit.timesOff.append(Submit.buttonClock.getTime())
                elif len(Submit.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    Submit.timesOff[-1] = Submit.buttonClock.getTime()
                if not Submit.wasClicked:
                    # end routine when Submit is clicked
                    continueRoutine = False
                if not Submit.wasClicked:
                    # run callback code when Submit is clicked
                    pass
        # take note of whether Submit was clicked, so that next frame we know if clicks are new
        Submit.wasClicked = Submit.isClicked and Submit.status == STARTED
        
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
    trialList=data.importConditions('0_Instructions.xlsx', selection='0:4'),
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
    CondInstEN.setText(CondInstTextEN)
    CondInstCN.setText(CondInstTextCN)
    # setup some python lists for storing info about the CondMouse
    CondMouse.x = []
    CondMouse.y = []
    CondMouse.leftButton = []
    CondMouse.midButton = []
    CondMouse.rightButton = []
    CondMouse.time = []
    gotValidClick = False  # until a click is received
    # reset CondSubmit to account for continued clicks & clear times on/off
    CondSubmit.reset()
    # keep track of which components have finished
    CondInstComponents = [CondImage, CondInstEN, CondInstCN, CondMouse, CondSubmit]
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
        if CondImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
        
        # *CondInstEN* updates
        
        # if CondInstEN is starting this frame...
        if CondInstEN.status == NOT_STARTED and isChinese==False:
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
        if CondInstCN.status == NOT_STARTED and isChinese==True:
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
        # *CondSubmit* updates
        
        # if CondSubmit is starting this frame...
        if CondSubmit.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            CondSubmit.frameNStart = frameN  # exact frame index
            CondSubmit.tStart = t  # local t and not account for scr refresh
            CondSubmit.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CondSubmit, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'CondSubmit.started')
            # update status
            CondSubmit.status = STARTED
            CondSubmit.setAutoDraw(True)
        
        # if CondSubmit is active this frame...
        if CondSubmit.status == STARTED:
            # update params
            pass
            # check whether CondSubmit has been pressed
            if CondSubmit.isClicked:
                if not CondSubmit.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    CondSubmit.timesOn.append(CondSubmit.buttonClock.getTime())
                    CondSubmit.timesOff.append(CondSubmit.buttonClock.getTime())
                elif len(CondSubmit.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    CondSubmit.timesOff[-1] = CondSubmit.buttonClock.getTime()
                if not CondSubmit.wasClicked:
                    # end routine when CondSubmit is clicked
                    continueRoutine = False
                if not CondSubmit.wasClicked:
                    # run callback code when CondSubmit is clicked
                    pass
        # take note of whether CondSubmit was clicked, so that next frame we know if clicks are new
        CondSubmit.wasClicked = CondSubmit.isClicked and CondSubmit.status == STARTED
        
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
    # update component parameters for each repeat
    CS_image.setImage(CSName)
    # Run 'Begin Routine' code from EachTrial_2
    if skipPhases == True:
        continueRoutine = False #end the routine
        Cond.finished = True #break the loop
    
    if parallelTrigger == True:
       ParaleData = 50  #Faissal
       #ParaleData = int((TrgCol+0.6)*40+20) #Faissal
       port.setData(ParaleData) #Faissal
       if lfpTrigger == True:
            lfpCtrlPort.setData(1)
       core.wait(0.02)
       port.setData(0) #Faissal
       if lfpTrigger == True:
            lfpCtrlPort.setData(0)
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
    while continueRoutine:
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
        if CondTriggMouse.status == NOT_STARTED and PreCondName=="Stimuli/Trig.BMP":
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
        if CondTriggKey.status == NOT_STARTED and PreCondName=="Stimuli/Trig.BMP":
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
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > CondTriggKey.tStartRefresh + 6-frameTolerance:
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
    # the Routine "trialCond" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
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
    # setup some python lists for storing info about the mouse
    mouse.x = []
    mouse.y = []
    mouse.leftButton = []
    mouse.midButton = []
    mouse.rightButton = []
    mouse.time = []
    gotValidClick = False  # until a click is received
    # reset Submit to account for continued clicks & clear times on/off
    Submit.reset()
    # keep track of which components have finished
    RatingComponents = [image, RatingInstEN, RatingInstCN, Scale, mouse, Submit]
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
        if RatingInstEN.status == NOT_STARTED and isChinese==False:
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
        if RatingInstCN.status == NOT_STARTED and isChinese==True:
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
        # *Submit* updates
        
        # if Submit is starting this frame...
        if Submit.status == NOT_STARTED and Scale.rating:
            # keep track of start time/frame for later
            Submit.frameNStart = frameN  # exact frame index
            Submit.tStart = t  # local t and not account for scr refresh
            Submit.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Submit, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Submit.started')
            # update status
            Submit.status = STARTED
            Submit.setAutoDraw(True)
        
        # if Submit is active this frame...
        if Submit.status == STARTED:
            # update params
            pass
            # check whether Submit has been pressed
            if Submit.isClicked:
                if not Submit.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    Submit.timesOn.append(Submit.buttonClock.getTime())
                    Submit.timesOff.append(Submit.buttonClock.getTime())
                elif len(Submit.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    Submit.timesOff[-1] = Submit.buttonClock.getTime()
                if not Submit.wasClicked:
                    # end routine when Submit is clicked
                    continueRoutine = False
                if not Submit.wasClicked:
                    # run callback code when Submit is clicked
                    pass
        # take note of whether Submit was clicked, so that next frame we know if clicks are new
        Submit.wasClicked = Submit.isClicked and Submit.status == STARTED
        
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
    # reset ExtSubmit to account for continued clicks & clear times on/off
    ExtSubmit.reset()
    # keep track of which components have finished
    ExtInstComponents = [ExtImage, ExtInstEN, ExtInstCN, ExtMouse, ExtSubmit]
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
        if ExtImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
        
        # *ExtInstEN* updates
        
        # if ExtInstEN is starting this frame...
        if ExtInstEN.status == NOT_STARTED and isChinese==False:
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
        if ExtInstCN.status == NOT_STARTED and isChinese==True:
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
        # *ExtSubmit* updates
        
        # if ExtSubmit is starting this frame...
        if ExtSubmit.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            ExtSubmit.frameNStart = frameN  # exact frame index
            ExtSubmit.tStart = t  # local t and not account for scr refresh
            ExtSubmit.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ExtSubmit, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ExtSubmit.started')
            # update status
            ExtSubmit.status = STARTED
            ExtSubmit.setAutoDraw(True)
        
        # if ExtSubmit is active this frame...
        if ExtSubmit.status == STARTED:
            # update params
            pass
            # check whether ExtSubmit has been pressed
            if ExtSubmit.isClicked:
                if not ExtSubmit.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    ExtSubmit.timesOn.append(ExtSubmit.buttonClock.getTime())
                    ExtSubmit.timesOff.append(ExtSubmit.buttonClock.getTime())
                elif len(ExtSubmit.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    ExtSubmit.timesOff[-1] = ExtSubmit.buttonClock.getTime()
                if not ExtSubmit.wasClicked:
                    # end routine when ExtSubmit is clicked
                    continueRoutine = False
                if not ExtSubmit.wasClicked:
                    # run callback code when ExtSubmit is clicked
                    pass
        # take note of whether ExtSubmit was clicked, so that next frame we know if clicks are new
        ExtSubmit.wasClicked = ExtSubmit.isClicked and ExtSubmit.status == STARTED
        
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
Ext = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('3_Extinction.xlsx'),
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
    if skipPhases == True:
        continueRoutine = False #end the routine
        Ext.finished = True #break the loop
    
    if parallelTrigger == True:
       ParaleData = 50  #Faissal
       #ParaleData = int((TrgCol+0.6)*40+20) #Faissal
       port.setData(ParaleData) #Faissal
       if lfpTrigger == True:
            lfpCtrlPort.setData(1)
       core.wait(0.02)
       port.setData(0) #Faissal
       if lfpTrigger == True:
            lfpCtrlPort.setData(0)
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
    while continueRoutine:
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
        if ExtTriggMouse.status == NOT_STARTED and PreCondName=="Stimuli/Trig.BMP":
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
        if ExtTriggKey.status == NOT_STARTED and PreCondName=="Stimuli/Trig.BMP":
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
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ExtTriggKey.tStartRefresh + 6-frameTolerance:
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
    # the Routine "trialExt" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
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
    # setup some python lists for storing info about the mouse
    mouse.x = []
    mouse.y = []
    mouse.leftButton = []
    mouse.midButton = []
    mouse.rightButton = []
    mouse.time = []
    gotValidClick = False  # until a click is received
    # reset Submit to account for continued clicks & clear times on/off
    Submit.reset()
    # keep track of which components have finished
    RatingComponents = [image, RatingInstEN, RatingInstCN, Scale, mouse, Submit]
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
        if RatingInstEN.status == NOT_STARTED and isChinese==False:
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
        if RatingInstCN.status == NOT_STARTED and isChinese==True:
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
        # *Submit* updates
        
        # if Submit is starting this frame...
        if Submit.status == NOT_STARTED and Scale.rating:
            # keep track of start time/frame for later
            Submit.frameNStart = frameN  # exact frame index
            Submit.tStart = t  # local t and not account for scr refresh
            Submit.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Submit, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Submit.started')
            # update status
            Submit.status = STARTED
            Submit.setAutoDraw(True)
        
        # if Submit is active this frame...
        if Submit.status == STARTED:
            # update params
            pass
            # check whether Submit has been pressed
            if Submit.isClicked:
                if not Submit.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    Submit.timesOn.append(Submit.buttonClock.getTime())
                    Submit.timesOff.append(Submit.buttonClock.getTime())
                elif len(Submit.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    Submit.timesOff[-1] = Submit.buttonClock.getTime()
                if not Submit.wasClicked:
                    # end routine when Submit is clicked
                    continueRoutine = False
                if not Submit.wasClicked:
                    # run callback code when Submit is clicked
                    pass
        # take note of whether Submit was clicked, so that next frame we know if clicks are new
        Submit.wasClicked = Submit.isClicked and Submit.status == STARTED
        
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
        if EndTxtEN.status == NOT_STARTED and isChinese==False:
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
        if EndTxtCN.status == NOT_STARTED and isChinese==True:
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
