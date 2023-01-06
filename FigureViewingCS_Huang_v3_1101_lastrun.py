#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on Fri Jan  6 02:45:17 2023
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

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.4'
expName = 'FigureTest'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data' + os.sep + '%s_%s' % (expInfo['participant'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/faissal/My Drive/Research/2022 – Oxford Tan Lab/2023 – Study 1/2022_11_TCET_Task/V3_3Faces/FigureViewingCS_Huang_v3_1101_lastrun.py',
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
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
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

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "Ins" ---
# Run 'Begin Experiment' code from code
import random
parallelTrigger = False

isChinese = False

if isChinese == True:
    instructionFolder = 'Instructions_CN'
else:
    instructionFolder = 'Instructions_EN'

#if parallelTrigger == True:
#    from psychopy import parallel
#    port = parallel.ParallelPort(address=0x0378)
#    port.setData(0)

random.seed()
SetNums = [1,2,3]
Sess = 0

# --- Initialize components for Routine "CondSessStart" ---

# --- Initialize components for Routine "PreCondInst" ---
InstrBkg = visual.Rect(
    win=win, name='InstrBkg',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=1, depth=0.0, interpolate=True)
TagFig = visual.ImageStim(
    win=win,
    name='TagFig', 
    image=instructionFolder+'/Slide1.PNG', mask=None, anchor='center',
    ori=0, pos=(0, 0), size=(1.8, 1.8),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
InstrKeyResp = keyboard.Keyboard()

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

# --- Initialize components for Routine "ITI" ---
BlankBkg = visual.Rect(
    win=win, name='BlankBkg',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=1, depth=0.0, interpolate=True)

# --- Initialize components for Routine "FearRating" ---
Bkg = visual.Rect(
    win=win, name='Bkg',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=1.0, depth=-1.0, interpolate=True)
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.8, 1.8),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
Scale = visual.Slider(win=win, name='Scale',
    startValue=None, size=(1.2, 0.05), pos=(0, -0.6), units=None,
    labels=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'], ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-3, readOnly=False)
fearRating = keyboard.Keyboard()

# --- Initialize components for Routine "CondInst" ---
InstrBkg2 = visual.Rect(
    win=win, name='InstrBkg2',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=1.0, depth=0.0, interpolate=True)
TagFig2 = visual.ImageStim(
    win=win,
    name='TagFig2', 
    image=instructionFolder+'/Slide2.PNG', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.8, 1.8),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
key_resp = keyboard.Keyboard()

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

# --- Initialize components for Routine "FearRating" ---
Bkg = visual.Rect(
    win=win, name='Bkg',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=1.0, depth=-1.0, interpolate=True)
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.8, 1.8),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
Scale = visual.Slider(win=win, name='Scale',
    startValue=None, size=(1.2, 0.05), pos=(0, -0.6), units=None,
    labels=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'], ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-3, readOnly=False)
fearRating = keyboard.Keyboard()

# --- Initialize components for Routine "ExtInstruction" ---
InstrBkg3 = visual.Rect(
    win=win, name='InstrBkg3',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=1.0, depth=0.0, interpolate=True)
TagFig3 = visual.ImageStim(
    win=win,
    name='TagFig3', 
    image=instructionFolder+'/Slide3.PNG', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.8, 1.8),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
key_resp_3 = keyboard.Keyboard()
# Run 'Begin Experiment' code from code_3
import random
random.seed()
SetNums2 = [1,2,3]
Sess2 = 0

# --- Initialize components for Routine "ExtSessStart" ---

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
# Run 'Begin Experiment' code from EachTrial_3
if parallelTrigger == True:
#   ParaleData = 50
   ParaleData = int((TrgCol+0.6)*40+20)
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

# --- Initialize components for Routine "FearRating" ---
Bkg = visual.Rect(
    win=win, name='Bkg',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=1.0, depth=-1.0, interpolate=True)
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.8, 1.8),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
Scale = visual.Slider(win=win, name='Scale',
    startValue=None, size=(1.2, 0.05), pos=(0, -0.6), units=None,
    labels=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'], ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-3, readOnly=False)
fearRating = keyboard.Keyboard()

# --- Initialize components for Routine "EndBlock" ---
EndTxt = visual.TextStim(win=win, name='EndTxt',
    text='谢谢您！\nThank you!',
    font='Microsoft YaHei',
    pos=[0, 0], height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "Ins" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
InsComponents = []
for thisComponent in InsComponents:
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

# --- Run Routine "Ins" ---
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
    for thisComponent in InsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Ins" ---
for thisComponent in InsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Ins" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "CondSessStart" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from SessInitCode
iSet = SetNums[Sess]
# Set Condition files here
PreConditionFN = 'PreCondition'+str(iSet)+'.xlsx'
#The ConditionFN sheet includes 30 conditions, of whih 24 (80%) include UCS
ConditionFN = 'Condition'+str(iSet)+'.xlsx'
RatingFN = 'Rating'+str(iSet)+'.xlsx'
Sess = Sess + 1
# keep track of which components have finished
CondSessStartComponents = []
for thisComponent in CondSessStartComponents:
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

# --- Run Routine "CondSessStart" ---
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
    for thisComponent in CondSessStartComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "CondSessStart" ---
for thisComponent in CondSessStartComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "CondSessStart" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "PreCondInst" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
InstrKeyResp.keys = []
InstrKeyResp.rt = []
_InstrKeyResp_allKeys = []
# keep track of which components have finished
PreCondInstComponents = [InstrBkg, TagFig, InstrKeyResp]
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
    
    # *TagFig* updates
    if TagFig.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        TagFig.frameNStart = frameN  # exact frame index
        TagFig.tStart = t  # local t and not account for scr refresh
        TagFig.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(TagFig, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'TagFig.started')
        TagFig.setAutoDraw(True)
    
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
thisExp.addData('InstrKeyResp.keys',InstrKeyResp.keys)
if InstrKeyResp.keys != None:  # we had a response
    thisExp.addData('InstrKeyResp.rt', InstrKeyResp.rt)
thisExp.nextEntry()
# the Routine "PreCondInst" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
PreCond = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(PreConditionFN),
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
    # Run 'Begin Routine' code from EachTrial
    if parallelTrigger == True:
       ParaleData = 50  #Faissal
       #ParaleData = int((TrgCol+0.6)*40+20) #Faissal
       #port.setData(ParaleData) #Faissal
       core.wait(0.02)
       #port.setData(0) #Faissal
    # keep track of which components have finished
    trialPreCondComponents = [precondBkg, imagePreCond]
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
    trialList=data.importConditions(RatingFN),
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
    
    # --- Prepare to start Routine "FearRating" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from setLang
    if isChinese == True:
        ratingName = ratingName_CN
    else:
        ratingName = ratingName_EN
    image.setImage(ratingName)
    Scale.reset()
    fearRating.keys = []
    fearRating.rt = []
    _fearRating_allKeys = []
    # keep track of which components have finished
    FearRatingComponents = [Bkg, image, Scale, fearRating]
    for thisComponent in FearRatingComponents:
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
    
    # --- Run Routine "FearRating" ---
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
        
        # Check Scale for response to end routine
        if Scale.getRating() is not None and Scale.status == STARTED:
            continueRoutine = False
        
        # *fearRating* updates
        waitOnFlip = False
        if fearRating.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fearRating.frameNStart = frameN  # exact frame index
            fearRating.tStart = t  # local t and not account for scr refresh
            fearRating.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fearRating, 'tStartRefresh')  # time at next scr refresh
            fearRating.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(fearRating.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(fearRating.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if fearRating.status == STARTED and not waitOnFlip:
            theseKeys = fearRating.getKeys(keyList=['1','2','3','4','5','6','7','8','9','10'], waitRelease=False)
            _fearRating_allKeys.extend(theseKeys)
            if len(_fearRating_allKeys):
                fearRating.keys = _fearRating_allKeys[-1].name  # just the last key pressed
                fearRating.rt = _fearRating_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FearRatingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "FearRating" ---
    for thisComponent in FearRatingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    RatingPreCond.addData('Scale.response', Scale.getRating())
    RatingPreCond.addData('Scale.rt', Scale.getRT())
    # check responses
    if fearRating.keys in ['', [], None]:  # No response was made
        fearRating.keys = None
    RatingPreCond.addData('fearRating.keys',fearRating.keys)
    if fearRating.keys != None:  # we had a response
        RatingPreCond.addData('fearRating.rt', fearRating.rt)
    # the Routine "FearRating" was not non-slip safe, so reset the non-slip timer
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

# --- Prepare to start Routine "CondInst" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
CondInstComponents = [InstrBkg2, TagFig2, key_resp]
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
    
    # *TagFig2* updates
    if TagFig2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        TagFig2.frameNStart = frameN  # exact frame index
        TagFig2.tStart = t  # local t and not account for scr refresh
        TagFig2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(TagFig2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'TagFig2.started')
        TagFig2.setAutoDraw(True)
    
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
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.nextEntry()
# the Routine "CondInst" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Cond = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(ConditionFN),
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
    # Run 'Begin Routine' code from EachTrial_2
    if parallelTrigger == True:
    #   ParaleData = 50
       ParaleData = int((TrgCol+0.6)*40+20)
       port.setData(ParaleData)
       core.wait(0.02)
       port.setData(0)
    # keep track of which components have finished
    trialCondComponents = [CSBkg, CS_image]
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
    trialList=data.importConditions(RatingFN),
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
    
    # --- Prepare to start Routine "FearRating" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from setLang
    if isChinese == True:
        ratingName = ratingName_CN
    else:
        ratingName = ratingName_EN
    image.setImage(ratingName)
    Scale.reset()
    fearRating.keys = []
    fearRating.rt = []
    _fearRating_allKeys = []
    # keep track of which components have finished
    FearRatingComponents = [Bkg, image, Scale, fearRating]
    for thisComponent in FearRatingComponents:
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
    
    # --- Run Routine "FearRating" ---
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
        
        # Check Scale for response to end routine
        if Scale.getRating() is not None and Scale.status == STARTED:
            continueRoutine = False
        
        # *fearRating* updates
        waitOnFlip = False
        if fearRating.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fearRating.frameNStart = frameN  # exact frame index
            fearRating.tStart = t  # local t and not account for scr refresh
            fearRating.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fearRating, 'tStartRefresh')  # time at next scr refresh
            fearRating.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(fearRating.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(fearRating.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if fearRating.status == STARTED and not waitOnFlip:
            theseKeys = fearRating.getKeys(keyList=['1','2','3','4','5','6','7','8','9','10'], waitRelease=False)
            _fearRating_allKeys.extend(theseKeys)
            if len(_fearRating_allKeys):
                fearRating.keys = _fearRating_allKeys[-1].name  # just the last key pressed
                fearRating.rt = _fearRating_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FearRatingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "FearRating" ---
    for thisComponent in FearRatingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    RatingCond.addData('Scale.response', Scale.getRating())
    RatingCond.addData('Scale.rt', Scale.getRT())
    # check responses
    if fearRating.keys in ['', [], None]:  # No response was made
        fearRating.keys = None
    RatingCond.addData('fearRating.keys',fearRating.keys)
    if fearRating.keys != None:  # we had a response
        RatingCond.addData('fearRating.rt', fearRating.rt)
    # the Routine "FearRating" was not non-slip safe, so reset the non-slip timer
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

# --- Prepare to start Routine "ExtInstruction" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
ExtInstructionComponents = [InstrBkg3, TagFig3, key_resp_3]
for thisComponent in ExtInstructionComponents:
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

# --- Run Routine "ExtInstruction" ---
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
    
    # *TagFig3* updates
    if TagFig3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        TagFig3.frameNStart = frameN  # exact frame index
        TagFig3.tStart = t  # local t and not account for scr refresh
        TagFig3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(TagFig3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'TagFig3.started')
        TagFig3.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_3.started')
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ExtInstructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "ExtInstruction" ---
for thisComponent in ExtInstructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.nextEntry()
# the Routine "ExtInstruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "ExtSessStart" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from code_2
iSet2 = SetNums2[Sess2]
ExtinctionFN = 'Extinction'+str(iSet2)+'.xlsx'
RatingFN = 'Rating'+str(iSet2)+'.xlsx'
Sess2 = Sess2 + 1
# keep track of which components have finished
ExtSessStartComponents = []
for thisComponent in ExtSessStartComponents:
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

# --- Run Routine "ExtSessStart" ---
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
    for thisComponent in ExtSessStartComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "ExtSessStart" ---
for thisComponent in ExtSessStartComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "ExtSessStart" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Extinction = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(ExtinctionFN),
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
    # keep track of which components have finished
    trialExtComponents = [ExtBkg, Ext_image]
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
    trialList=data.importConditions(RatingFN),
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
    
    # --- Prepare to start Routine "FearRating" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from setLang
    if isChinese == True:
        ratingName = ratingName_CN
    else:
        ratingName = ratingName_EN
    image.setImage(ratingName)
    Scale.reset()
    fearRating.keys = []
    fearRating.rt = []
    _fearRating_allKeys = []
    # keep track of which components have finished
    FearRatingComponents = [Bkg, image, Scale, fearRating]
    for thisComponent in FearRatingComponents:
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
    
    # --- Run Routine "FearRating" ---
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
        
        # Check Scale for response to end routine
        if Scale.getRating() is not None and Scale.status == STARTED:
            continueRoutine = False
        
        # *fearRating* updates
        waitOnFlip = False
        if fearRating.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fearRating.frameNStart = frameN  # exact frame index
            fearRating.tStart = t  # local t and not account for scr refresh
            fearRating.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fearRating, 'tStartRefresh')  # time at next scr refresh
            fearRating.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(fearRating.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(fearRating.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if fearRating.status == STARTED and not waitOnFlip:
            theseKeys = fearRating.getKeys(keyList=['1','2','3','4','5','6','7','8','9','10'], waitRelease=False)
            _fearRating_allKeys.extend(theseKeys)
            if len(_fearRating_allKeys):
                fearRating.keys = _fearRating_allKeys[-1].name  # just the last key pressed
                fearRating.rt = _fearRating_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FearRatingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "FearRating" ---
    for thisComponent in FearRatingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    RatingExt.addData('Scale.response', Scale.getRating())
    RatingExt.addData('Scale.rt', Scale.getRT())
    # check responses
    if fearRating.keys in ['', [], None]:  # No response was made
        fearRating.keys = None
    RatingExt.addData('fearRating.keys',fearRating.keys)
    if fearRating.keys != None:  # we had a response
        RatingExt.addData('fearRating.rt', fearRating.rt)
    # the Routine "FearRating" was not non-slip safe, so reset the non-slip timer
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

# --- Prepare to start Routine "EndBlock" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
EndBlockComponents = [EndTxt]
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
while continueRoutine and routineTimer.getTime() < 5.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *EndTxt* updates
    if EndTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        EndTxt.frameNStart = frameN  # exact frame index
        EndTxt.tStart = t  # local t and not account for scr refresh
        EndTxt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EndTxt, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'EndTxt.started')
        EndTxt.setAutoDraw(True)
    if EndTxt.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > EndTxt.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            EndTxt.tStop = t  # not accounting for scr refresh
            EndTxt.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'EndTxt.stopped')
            EndTxt.setAutoDraw(False)
    
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
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-5.000000)

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
