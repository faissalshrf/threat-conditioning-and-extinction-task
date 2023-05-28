/******************** 
 * Tcet_Sharif Test *
 ********************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2023.1.1.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'TCET_Sharif';  // from the Builder filename that created this script
let expInfo = {
    'Participant_ID': 'S00',
    'Version': ["Standard", "Short"],
    'Language': ["EN", "CN"],
};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color('black'),
  units: 'height',
  waitBlanking: true
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(SettingsRoutineBegin());
flowScheduler.add(SettingsRoutineEachFrame());
flowScheduler.add(SettingsRoutineEnd());
const PreCondInstTextLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(PreCondInstTextLoopBegin(PreCondInstTextLoopScheduler));
flowScheduler.add(PreCondInstTextLoopScheduler);
flowScheduler.add(PreCondInstTextLoopEnd);
const PreCondLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(PreCondLoopBegin(PreCondLoopScheduler));
flowScheduler.add(PreCondLoopScheduler);
flowScheduler.add(PreCondLoopEnd);
const RatingPreCondLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(RatingPreCondLoopBegin(RatingPreCondLoopScheduler));
flowScheduler.add(RatingPreCondLoopScheduler);
flowScheduler.add(RatingPreCondLoopEnd);
const CondInstTextLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(CondInstTextLoopBegin(CondInstTextLoopScheduler));
flowScheduler.add(CondInstTextLoopScheduler);
flowScheduler.add(CondInstTextLoopEnd);
const CondLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(CondLoopBegin(CondLoopScheduler));
flowScheduler.add(CondLoopScheduler);
flowScheduler.add(CondLoopEnd);
const RatingCondLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(RatingCondLoopBegin(RatingCondLoopScheduler));
flowScheduler.add(RatingCondLoopScheduler);
flowScheduler.add(RatingCondLoopEnd);
const ExtInstTextLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(ExtInstTextLoopBegin(ExtInstTextLoopScheduler));
flowScheduler.add(ExtInstTextLoopScheduler);
flowScheduler.add(ExtInstTextLoopEnd);
const ExtLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(ExtLoopBegin(ExtLoopScheduler));
flowScheduler.add(ExtLoopScheduler);
flowScheduler.add(ExtLoopEnd);
const RatingExtLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(RatingExtLoopBegin(RatingExtLoopScheduler));
flowScheduler.add(RatingExtLoopScheduler);
flowScheduler.add(RatingExtLoopEnd);
const EndTextLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(EndTextLoopBegin(EndTextLoopScheduler));
flowScheduler.add(EndTextLoopScheduler);
flowScheduler.add(EndTextLoopEnd);
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  });

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);

async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2023.1.1';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["Participant_ID"]}/${expInfo["Participant_ID"]}-${expInfo["date"]}`);


  return Scheduler.Event.NEXT;
}

async function experimentInit() {
  // Initialize components for Routine "Settings"
  SettingsClock = new util.Clock();
  // Run 'Begin Experiment' code from Settings
  import * as random from 'random';
  parallelTrigger = false;
  isChinese = false;
  skipPhases = false;
  if ((parallelTrigger === true)) {
      import {parallel} from 'psychopy';
      port = new parallel.ParallelPort({"address": 888});
      port.setData(0);
      if ((lfpTrigger === true)) {
          lfpCtrlPort = new parallel.ParallelPort({"address": 890});
          lfpCtrlPort.setData(0);
      }
  }
  Math.random.seed();
  SetNums = [1, 2, 3];
  Sess = 0;
  
  // Initialize components for Routine "PreCondInst"
  PreCondInstClock = new util.Clock();
  PreCondImage = new visual.ImageStim({
    win : psychoJS.window,
    name : 'PreCondImage', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0.05], size : [0.45, 0.9],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  PreCondImageOverview = new visual.ImageStim({
    win : psychoJS.window,
    name : 'PreCondImageOverview', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0.05], size : [1.5, 0.9],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  PreCondInstEN = new visual.TextStim({
    win: psychoJS.window,
    name: 'PreCondInstEN',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.7], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  PreCondInstCN = new visual.TextStim({
    win: psychoJS.window,
    name: 'PreCondInstCN',
    text: '',
    font: 'PingFang SC',
    units: undefined, 
    pos: [(- 0.3), 0.7], height: 0.08,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  PreCondRespKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  PreCondMouse = new core.Mouse({
    win: psychoJS.window,
  });
  PreCondMouse.mouseClock = new util.Clock();
  PreCondSubmit = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'PreCondSubmit',
    text: 'CONTINUE',
    fillColor: [0.8824, 0.6392, 0.4432],
    borderColor: null,
    color: 'black',
    colorSpace: 'rgb',
    pos: [0.7, (- 0.8)],
    letterHeight: 0.06,
    size: [0.3, 0.1],
    depth: -6
  });
  PreCondSubmit.clock = new util.Clock();
  
  // Initialize components for Routine "trialPreCond"
  trialPreCondClock = new util.Clock();
  imagePreCond = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imagePreCond', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0, pos : [0, 0], size : [2, 2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  PreCondTriggMouse = new core.Mouse({
    win: psychoJS.window,
  });
  PreCondTriggMouse.mouseClock = new util.Clock();
  PreCondTriggKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "ITI"
  ITIClock = new util.Clock();
  FixCross = new visual.ShapeStim ({
    win: psychoJS.window, name: 'FixCross', 
    vertices: 'cross', size:[0.05, 0.07],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('black'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  // Initialize components for Routine "Rating"
  RatingClock = new util.Clock();
  image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0.1], size : [0.45, 0.9],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  RatingInstEN = new visual.TextStim({
    win: psychoJS.window,
    name: 'RatingInstEN',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.7], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  RatingInstCN = new visual.TextStim({
    win: psychoJS.window,
    name: 'RatingInstCN',
    text: '',
    font: 'PingFang SC',
    units: undefined, 
    pos: [0, 0.7], height: 0.08,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  Scale = new visual.Slider({
    win: psychoJS.window, name: 'Scale',
    startValue: undefined,
    size: [1.3, 0.05], pos: [0, (- 0.5)], ori: 0.0, units: psychoJS.window.units,
    labels: ["\u2013 Negative", "Positive +"], fontSize: 0.04, ticks: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    granularity: 1.0, style: ["RATING"],
    color: new util.Color('LightGray'), markerColor: new util.Color('beige'), lineColor: new util.Color('White'), 
    opacity: undefined, fontFamily: 'Arial', bold: true, italic: false, depth: -3, 
    flip: false,
  });
  
  RatingKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  mouse = new core.Mouse({
    win: psychoJS.window,
  });
  mouse.mouseClock = new util.Clock();
  Submit = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'Submit',
    text: 'SUBMIT',
    fillColor: [0.8824, 0.6392, 0.4432],
    borderColor: null,
    color: 'black',
    colorSpace: 'rgb',
    pos: [0.7, (- 0.8)],
    letterHeight: 0.06,
    size: [0.3, 0.1],
    depth: -6
  });
  Submit.clock = new util.Clock();
  
  // Initialize components for Routine "CondInst"
  CondInstClock = new util.Clock();
  CondImage = new visual.ImageStim({
    win : psychoJS.window,
    name : 'CondImage', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0.05], size : [0.45, 0.9],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  CondImageOverview = new visual.ImageStim({
    win : psychoJS.window,
    name : 'CondImageOverview', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0.05], size : [1.5, 0.9],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  CondInstEN = new visual.TextStim({
    win: psychoJS.window,
    name: 'CondInstEN',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.7], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  CondInstCN = new visual.TextStim({
    win: psychoJS.window,
    name: 'CondInstCN',
    text: '',
    font: 'PingFang SC',
    units: undefined, 
    pos: [(- 0.3), 0.7], height: 0.08,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  CondRespKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  CondMouse = new core.Mouse({
    win: psychoJS.window,
  });
  CondMouse.mouseClock = new util.Clock();
  CondSubmit = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'CondSubmit',
    text: 'CONTINUE',
    fillColor: [0.8824, 0.6392, 0.4432],
    borderColor: null,
    color: 'black',
    colorSpace: 'rgb',
    pos: [0.7, (- 0.8)],
    letterHeight: 0.06,
    size: [0.3, 0.1],
    depth: -6
  });
  CondSubmit.clock = new util.Clock();
  
  // Initialize components for Routine "trialCond"
  trialCondClock = new util.Clock();
  CS_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'CS_image', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [2, 2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  CondTriggMouse = new core.Mouse({
    win: psychoJS.window,
  });
  CondTriggMouse.mouseClock = new util.Clock();
  CondTriggKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "UCS"
  UCSClock = new util.Clock();
  UCSBkg = new visual.Rect ({
    win: psychoJS.window, name: 'UCSBkg', 
    width: [2, 2][0], height: [2, 2][1],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('black'),
    fillColor: new util.Color('black'),
    opacity: 1.0, depth: 0, interpolate: true,
  });
  
  UCS_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'UCS_image', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [2, 2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  sound_1 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: 1,
    });
  sound_1.setVolume(0.3);
  // Initialize components for Routine "ExtInst"
  ExtInstClock = new util.Clock();
  ExtImage = new visual.ImageStim({
    win : psychoJS.window,
    name : 'ExtImage', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0.05], size : [0.45, 0.9],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  ExtImageOverview = new visual.ImageStim({
    win : psychoJS.window,
    name : 'ExtImageOverview', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0.05], size : [1.5, 0.9],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  ExtInstEN = new visual.TextStim({
    win: psychoJS.window,
    name: 'ExtInstEN',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.7], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  ExtInstCN = new visual.TextStim({
    win: psychoJS.window,
    name: 'ExtInstCN',
    text: '',
    font: 'PingFang SC',
    units: undefined, 
    pos: [(- 0.3), 0.7], height: 0.08,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  ExtRespKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  ExtMouse = new core.Mouse({
    win: psychoJS.window,
  });
  ExtMouse.mouseClock = new util.Clock();
  ExtSubmit = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'ExtSubmit',
    text: 'CONTINUE',
    fillColor: [0.8824, 0.6392, 0.4432],
    borderColor: null,
    color: 'black',
    colorSpace: 'rgb',
    pos: [0.7, (- 0.8)],
    letterHeight: 0.06,
    size: [0.3, 0.1],
    depth: -6
  });
  ExtSubmit.clock = new util.Clock();
  
  // Initialize components for Routine "trialExt"
  trialExtClock = new util.Clock();
  Ext_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Ext_image', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [2, 2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  ExtTriggMouse = new core.Mouse({
    win: psychoJS.window,
  });
  ExtTriggMouse.mouseClock = new util.Clock();
  ExtTriggKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "EndBlock"
  EndBlockClock = new util.Clock();
  Bkg_Light = new visual.Rect ({
    win: psychoJS.window, name: 'Bkg_Light', 
    width: [2, 2][0], height: [2, 2][1],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('black'),
    fillColor: new util.Color([0.8824, 0.6392, 0.4432]),
    opacity: 1.0, depth: 0, interpolate: true,
  });
  
  EndTxtEN = new visual.TextStim({
    win: psychoJS.window,
    name: 'EndTxtEN',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.2,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  EndTxtCN = new visual.TextStim({
    win: psychoJS.window,
    name: 'EndTxtCN',
    text: '',
    font: 'PingFang SC',
    units: undefined, 
    pos: [(- 0.3), 0], height: 0.2,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

function SettingsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Settings' ---
    t = 0;
    SettingsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    SettingsComponents = [];
    
    for (const thisComponent of SettingsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function SettingsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Settings' ---
    // get current time
    t = SettingsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of SettingsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function SettingsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Settings' ---
    for (const thisComponent of SettingsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "Settings" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function PreCondInstTextLoopBegin(PreCondInstTextLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    PreCondInstText = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, '0_Instructions.xlsx', '0:5'),
      seed: undefined, name: 'PreCondInstText'
    });
    psychoJS.experiment.addLoop(PreCondInstText); // add the loop to the experiment
    currentLoop = PreCondInstText;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisPreCondInstText of PreCondInstText) {
      snapshot = PreCondInstText.getSnapshot();
      PreCondInstTextLoopScheduler.add(importConditions(snapshot));
      PreCondInstTextLoopScheduler.add(PreCondInstRoutineBegin(snapshot));
      PreCondInstTextLoopScheduler.add(PreCondInstRoutineEachFrame());
      PreCondInstTextLoopScheduler.add(PreCondInstRoutineEnd(snapshot));
      PreCondInstTextLoopScheduler.add(PreCondInstTextLoopEndIteration(PreCondInstTextLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

async function PreCondInstTextLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(PreCondInstText);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function PreCondInstTextLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function PreCondLoopBegin(PreCondLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    PreCond = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: schedule_files[0],
      seed: undefined, name: 'PreCond'
    });
    psychoJS.experiment.addLoop(PreCond); // add the loop to the experiment
    currentLoop = PreCond;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisPreCond of PreCond) {
      snapshot = PreCond.getSnapshot();
      PreCondLoopScheduler.add(importConditions(snapshot));
      PreCondLoopScheduler.add(trialPreCondRoutineBegin(snapshot));
      PreCondLoopScheduler.add(trialPreCondRoutineEachFrame());
      PreCondLoopScheduler.add(trialPreCondRoutineEnd(snapshot));
      PreCondLoopScheduler.add(ITIRoutineBegin(snapshot));
      PreCondLoopScheduler.add(ITIRoutineEachFrame());
      PreCondLoopScheduler.add(ITIRoutineEnd(snapshot));
      PreCondLoopScheduler.add(PreCondLoopEndIteration(PreCondLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

async function PreCondLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(PreCond);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function PreCondLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function RatingPreCondLoopBegin(RatingPreCondLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    RatingPreCond = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: '4_Rating.xlsx',
      seed: undefined, name: 'RatingPreCond'
    });
    psychoJS.experiment.addLoop(RatingPreCond); // add the loop to the experiment
    currentLoop = RatingPreCond;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisRatingPreCond of RatingPreCond) {
      snapshot = RatingPreCond.getSnapshot();
      RatingPreCondLoopScheduler.add(importConditions(snapshot));
      RatingPreCondLoopScheduler.add(RatingRoutineBegin(snapshot));
      RatingPreCondLoopScheduler.add(RatingRoutineEachFrame());
      RatingPreCondLoopScheduler.add(RatingRoutineEnd(snapshot));
      RatingPreCondLoopScheduler.add(RatingPreCondLoopEndIteration(RatingPreCondLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

async function RatingPreCondLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(RatingPreCond);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function RatingPreCondLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function CondInstTextLoopBegin(CondInstTextLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    CondInstText = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, '0_Instructions.xlsx', '0:5'),
      seed: undefined, name: 'CondInstText'
    });
    psychoJS.experiment.addLoop(CondInstText); // add the loop to the experiment
    currentLoop = CondInstText;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisCondInstText of CondInstText) {
      snapshot = CondInstText.getSnapshot();
      CondInstTextLoopScheduler.add(importConditions(snapshot));
      CondInstTextLoopScheduler.add(CondInstRoutineBegin(snapshot));
      CondInstTextLoopScheduler.add(CondInstRoutineEachFrame());
      CondInstTextLoopScheduler.add(CondInstRoutineEnd(snapshot));
      CondInstTextLoopScheduler.add(CondInstTextLoopEndIteration(CondInstTextLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

async function CondInstTextLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(CondInstText);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function CondInstTextLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function CondLoopBegin(CondLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    Cond = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: schedule_files[1],
      seed: undefined, name: 'Cond'
    });
    psychoJS.experiment.addLoop(Cond); // add the loop to the experiment
    currentLoop = Cond;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisCond of Cond) {
      snapshot = Cond.getSnapshot();
      CondLoopScheduler.add(importConditions(snapshot));
      CondLoopScheduler.add(trialCondRoutineBegin(snapshot));
      CondLoopScheduler.add(trialCondRoutineEachFrame());
      CondLoopScheduler.add(trialCondRoutineEnd(snapshot));
      CondLoopScheduler.add(UCSRoutineBegin(snapshot));
      CondLoopScheduler.add(UCSRoutineEachFrame());
      CondLoopScheduler.add(UCSRoutineEnd(snapshot));
      CondLoopScheduler.add(ITIRoutineBegin(snapshot));
      CondLoopScheduler.add(ITIRoutineEachFrame());
      CondLoopScheduler.add(ITIRoutineEnd(snapshot));
      CondLoopScheduler.add(CondLoopEndIteration(CondLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

async function CondLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(Cond);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function CondLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function RatingCondLoopBegin(RatingCondLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    RatingCond = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: '4_Rating.xlsx',
      seed: undefined, name: 'RatingCond'
    });
    psychoJS.experiment.addLoop(RatingCond); // add the loop to the experiment
    currentLoop = RatingCond;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisRatingCond of RatingCond) {
      snapshot = RatingCond.getSnapshot();
      RatingCondLoopScheduler.add(importConditions(snapshot));
      RatingCondLoopScheduler.add(RatingRoutineBegin(snapshot));
      RatingCondLoopScheduler.add(RatingRoutineEachFrame());
      RatingCondLoopScheduler.add(RatingRoutineEnd(snapshot));
      RatingCondLoopScheduler.add(RatingCondLoopEndIteration(RatingCondLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

async function RatingCondLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(RatingCond);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function RatingCondLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function ExtInstTextLoopBegin(ExtInstTextLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    ExtInstText = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, '0_Instructions.xlsx', '0:6'),
      seed: undefined, name: 'ExtInstText'
    });
    psychoJS.experiment.addLoop(ExtInstText); // add the loop to the experiment
    currentLoop = ExtInstText;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisExtInstText of ExtInstText) {
      snapshot = ExtInstText.getSnapshot();
      ExtInstTextLoopScheduler.add(importConditions(snapshot));
      ExtInstTextLoopScheduler.add(ExtInstRoutineBegin(snapshot));
      ExtInstTextLoopScheduler.add(ExtInstRoutineEachFrame());
      ExtInstTextLoopScheduler.add(ExtInstRoutineEnd(snapshot));
      ExtInstTextLoopScheduler.add(ExtInstTextLoopEndIteration(ExtInstTextLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

async function ExtInstTextLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(ExtInstText);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function ExtInstTextLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function ExtLoopBegin(ExtLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    Ext = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: schedule_files[2],
      seed: undefined, name: 'Ext'
    });
    psychoJS.experiment.addLoop(Ext); // add the loop to the experiment
    currentLoop = Ext;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisExt of Ext) {
      snapshot = Ext.getSnapshot();
      ExtLoopScheduler.add(importConditions(snapshot));
      ExtLoopScheduler.add(trialExtRoutineBegin(snapshot));
      ExtLoopScheduler.add(trialExtRoutineEachFrame());
      ExtLoopScheduler.add(trialExtRoutineEnd(snapshot));
      ExtLoopScheduler.add(ITIRoutineBegin(snapshot));
      ExtLoopScheduler.add(ITIRoutineEachFrame());
      ExtLoopScheduler.add(ITIRoutineEnd(snapshot));
      ExtLoopScheduler.add(ExtLoopEndIteration(ExtLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

async function ExtLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(Ext);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function ExtLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function RatingExtLoopBegin(RatingExtLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    RatingExt = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: '4_Rating.xlsx',
      seed: undefined, name: 'RatingExt'
    });
    psychoJS.experiment.addLoop(RatingExt); // add the loop to the experiment
    currentLoop = RatingExt;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisRatingExt of RatingExt) {
      snapshot = RatingExt.getSnapshot();
      RatingExtLoopScheduler.add(importConditions(snapshot));
      RatingExtLoopScheduler.add(RatingRoutineBegin(snapshot));
      RatingExtLoopScheduler.add(RatingRoutineEachFrame());
      RatingExtLoopScheduler.add(RatingRoutineEnd(snapshot));
      RatingExtLoopScheduler.add(RatingExtLoopEndIteration(RatingExtLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

async function RatingExtLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(RatingExt);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function RatingExtLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function EndTextLoopBegin(EndTextLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    EndText = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, '0_Instructions.xlsx', '0:1'),
      seed: undefined, name: 'EndText'
    });
    psychoJS.experiment.addLoop(EndText); // add the loop to the experiment
    currentLoop = EndText;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisEndText of EndText) {
      snapshot = EndText.getSnapshot();
      EndTextLoopScheduler.add(importConditions(snapshot));
      EndTextLoopScheduler.add(EndBlockRoutineBegin(snapshot));
      EndTextLoopScheduler.add(EndBlockRoutineEachFrame());
      EndTextLoopScheduler.add(EndBlockRoutineEnd(snapshot));
      EndTextLoopScheduler.add(EndTextLoopEndIteration(EndTextLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

async function EndTextLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(EndText);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function EndTextLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function PreCondInstRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'PreCondInst' ---
    t = 0;
    PreCondInstClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    PreCondImage.setImage(PreCondInstTextImage);
    PreCondImageOverview.setImage(PreCondInstTextImage);
    PreCondInstEN.setText(PreCondInstTextEN);
    PreCondInstCN.setText(PreCondInstTextCN);
    PreCondRespKey.keys = undefined;
    PreCondRespKey.rt = undefined;
    _PreCondRespKey_allKeys = [];
    // setup some python lists for storing info about the PreCondMouse
    // current position of the mouse:
    PreCondMouse.x = [];
    PreCondMouse.y = [];
    PreCondMouse.leftButton = [];
    PreCondMouse.midButton = [];
    PreCondMouse.rightButton = [];
    PreCondMouse.time = [];
    gotValidClick = false; // until a click is received
    // reset PreCondSubmit to account for continued clicks & clear times on/off
    PreCondSubmit.reset()
    // keep track of which components have finished
    PreCondInstComponents = [];
    PreCondInstComponents.push(PreCondImage);
    PreCondInstComponents.push(PreCondImageOverview);
    PreCondInstComponents.push(PreCondInstEN);
    PreCondInstComponents.push(PreCondInstCN);
    PreCondInstComponents.push(PreCondRespKey);
    PreCondInstComponents.push(PreCondMouse);
    PreCondInstComponents.push(PreCondSubmit);
    
    for (const thisComponent of PreCondInstComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function PreCondInstRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'PreCondInst' ---
    // get current time
    t = PreCondInstClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *PreCondImage* updates
    if (((PreCondInstTextImage == 'Stimuli/Raw_Trig.BMP')) && PreCondImage.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      PreCondImage.tStart = t;  // (not accounting for frame time here)
      PreCondImage.frameNStart = frameN;  // exact frame index
      
      PreCondImage.setAutoDraw(true);
    }

    
    // *PreCondImageOverview* updates
    if (((PreCondInstTextImage == 'Stimuli/Raw_3Faces.BMP')) && PreCondImageOverview.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      PreCondImageOverview.tStart = t;  // (not accounting for frame time here)
      PreCondImageOverview.frameNStart = frameN;  // exact frame index
      
      PreCondImageOverview.setAutoDraw(true);
    }

    
    // *PreCondInstEN* updates
    if (((expInfo['Language'] == 'EN')) && PreCondInstEN.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      PreCondInstEN.tStart = t;  // (not accounting for frame time here)
      PreCondInstEN.frameNStart = frameN;  // exact frame index
      
      PreCondInstEN.setAutoDraw(true);
    }

    
    // *PreCondInstCN* updates
    if (((expInfo['Language'] == 'CN')) && PreCondInstCN.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      PreCondInstCN.tStart = t;  // (not accounting for frame time here)
      PreCondInstCN.frameNStart = frameN;  // exact frame index
      
      PreCondInstCN.setAutoDraw(true);
    }

    
    // *PreCondRespKey* updates
    if (t >= 0.0 && PreCondRespKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      PreCondRespKey.tStart = t;  // (not accounting for frame time here)
      PreCondRespKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { PreCondRespKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { PreCondRespKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { PreCondRespKey.clearEvents(); });
    }

    if (PreCondRespKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = PreCondRespKey.getKeys({keyList: ['space'], waitRelease: false});
      _PreCondRespKey_allKeys = _PreCondRespKey_allKeys.concat(theseKeys);
      if (_PreCondRespKey_allKeys.length > 0) {
        PreCondRespKey.keys = _PreCondRespKey_allKeys[_PreCondRespKey_allKeys.length - 1].name;  // just the last key pressed
        PreCondRespKey.rt = _PreCondRespKey_allKeys[_PreCondRespKey_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // *PreCondMouse* updates
    if (t >= 0 && PreCondMouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      PreCondMouse.tStart = t;  // (not accounting for frame time here)
      PreCondMouse.frameNStart = frameN;  // exact frame index
      
      PreCondMouse.status = PsychoJS.Status.STARTED;
      PreCondMouse.mouseClock.reset();
      prevButtonState = PreCondMouse.getPressed();  // if button is down already this ISN'T a new click
      }
    if (PreCondMouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = PreCondMouse.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          _mouseXYs = PreCondMouse.getPos();
          PreCondMouse.x.push(_mouseXYs[0]);
          PreCondMouse.y.push(_mouseXYs[1]);
          PreCondMouse.leftButton.push(_mouseButtons[0]);
          PreCondMouse.midButton.push(_mouseButtons[1]);
          PreCondMouse.rightButton.push(_mouseButtons[2]);
          PreCondMouse.time.push(PreCondMouse.mouseClock.getTime());
        }
      }
    }
    
    // *PreCondSubmit* updates
    if (t >= 0 && PreCondSubmit.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      PreCondSubmit.tStart = t;  // (not accounting for frame time here)
      PreCondSubmit.frameNStart = frameN;  // exact frame index
      
      PreCondSubmit.setAutoDraw(true);
    }

    if (PreCondSubmit.status === PsychoJS.Status.STARTED) {
      // check whether PreCondSubmit has been pressed
      if (PreCondSubmit.isClicked) {
        if (!PreCondSubmit.wasClicked) {
          // store time of first click
          PreCondSubmit.timesOn.push(PreCondSubmit.clock.getTime());
          PreCondSubmit.numClicks += 1;
          // store time clicked until
          PreCondSubmit.timesOff.push(PreCondSubmit.clock.getTime());
        } else {
          // update time clicked until;
          PreCondSubmit.timesOff[PreCondSubmit.timesOff.length - 1] = PreCondSubmit.clock.getTime();
        }
        if (!PreCondSubmit.wasClicked) {
          // end routine when PreCondSubmit is clicked
          continueRoutine = false;
        }
        // if PreCondSubmit is still clicked next frame, it is not a new click
        PreCondSubmit.wasClicked = true;
      } else {
        // if PreCondSubmit is clicked next frame, it is a new click
        PreCondSubmit.wasClicked = false;
      }
    } else {
      // keep clock at 0 if PreCondSubmit hasn't started / has finished
      PreCondSubmit.clock.reset();
      // if PreCondSubmit is clicked next frame, it is a new click
      PreCondSubmit.wasClicked = false;
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of PreCondInstComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function PreCondInstRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'PreCondInst' ---
    for (const thisComponent of PreCondInstComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(PreCondRespKey.corr, level);
    }
    psychoJS.experiment.addData('PreCondRespKey.keys', PreCondRespKey.keys);
    if (typeof PreCondRespKey.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('PreCondRespKey.rt', PreCondRespKey.rt);
        routineTimer.reset();
        }
    
    PreCondRespKey.stop();
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('PreCondMouse.x', PreCondMouse.x);
    psychoJS.experiment.addData('PreCondMouse.y', PreCondMouse.y);
    psychoJS.experiment.addData('PreCondMouse.leftButton', PreCondMouse.leftButton);
    psychoJS.experiment.addData('PreCondMouse.midButton', PreCondMouse.midButton);
    psychoJS.experiment.addData('PreCondMouse.rightButton', PreCondMouse.rightButton);
    psychoJS.experiment.addData('PreCondMouse.time', PreCondMouse.time);
    
    psychoJS.experiment.addData('PreCondSubmit.numClicks', PreCondSubmit.numClicks);
    psychoJS.experiment.addData('PreCondSubmit.timesOn', PreCondSubmit.timesOn);
    psychoJS.experiment.addData('PreCondSubmit.timesOff', PreCondSubmit.timesOff);
    // the Routine "PreCondInst" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function trialPreCondRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'trialPreCond' ---
    t = 0;
    trialPreCondClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(6.000000);
    // update component parameters for each repeat
    imagePreCond.setImage(PreCondName);
    // Run 'Begin Routine' code from EachTrial
    if ((skipPhases === true)) {
        continueRoutine = false;
        PreCond.finished = true;
    }
    if ((parallelTrigger === true)) {
        ParaleData = 50;
        port.setData(ParaleData);
        if ((lfpTrigger === true)) {
            lfpCtrlPort.setData(1);
        }
        core.wait(0.02);
        port.setData(0);
        if ((lfpTrigger === true)) {
            lfpCtrlPort.setData(0);
        }
    }
    
    // setup some python lists for storing info about the PreCondTriggMouse
    // current position of the mouse:
    PreCondTriggMouse.x = [];
    PreCondTriggMouse.y = [];
    PreCondTriggMouse.leftButton = [];
    PreCondTriggMouse.midButton = [];
    PreCondTriggMouse.rightButton = [];
    PreCondTriggMouse.time = [];
    gotValidClick = false; // until a click is received
    PreCondTriggMouse.mouseClock.reset();
    PreCondTriggKey.keys = undefined;
    PreCondTriggKey.rt = undefined;
    _PreCondTriggKey_allKeys = [];
    // keep track of which components have finished
    trialPreCondComponents = [];
    trialPreCondComponents.push(imagePreCond);
    trialPreCondComponents.push(PreCondTriggMouse);
    trialPreCondComponents.push(PreCondTriggKey);
    
    for (const thisComponent of trialPreCondComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function trialPreCondRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trialPreCond' ---
    // get current time
    t = trialPreCondClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *imagePreCond* updates
    if (t >= 0.0 && imagePreCond.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imagePreCond.tStart = t;  // (not accounting for frame time here)
      imagePreCond.frameNStart = frameN;  // exact frame index
      
      imagePreCond.setAutoDraw(true);
    }

    frameRemains = 6  - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((imagePreCond.status === PsychoJS.Status.STARTED || imagePreCond.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      imagePreCond.setAutoDraw(false);
    }
    // *PreCondTriggMouse* updates
    if (((PreCondName == 'Stimuli/Trig.BMP')) && PreCondTriggMouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      PreCondTriggMouse.tStart = t;  // (not accounting for frame time here)
      PreCondTriggMouse.frameNStart = frameN;  // exact frame index
      
      PreCondTriggMouse.status = PsychoJS.Status.STARTED;
      prevButtonState = PreCondTriggMouse.getPressed();  // if button is down already this ISN'T a new click
      }
    frameRemains = 6  - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((PreCondTriggMouse.status === PsychoJS.Status.STARTED || PreCondTriggMouse.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      PreCondTriggMouse.status = PsychoJS.Status.FINISHED;
  }
    if (PreCondTriggMouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = PreCondTriggMouse.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          _mouseXYs = PreCondTriggMouse.getPos();
          PreCondTriggMouse.x.push(_mouseXYs[0]);
          PreCondTriggMouse.y.push(_mouseXYs[1]);
          PreCondTriggMouse.leftButton.push(_mouseButtons[0]);
          PreCondTriggMouse.midButton.push(_mouseButtons[1]);
          PreCondTriggMouse.rightButton.push(_mouseButtons[2]);
          PreCondTriggMouse.time.push(PreCondTriggMouse.mouseClock.getTime());
          // end routine on response
          continueRoutine = false;
        }
      }
    }
    
    // *PreCondTriggKey* updates
    if (((PreCondName == 'Stimuli/Trig.BMP')) && PreCondTriggKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      PreCondTriggKey.tStart = t;  // (not accounting for frame time here)
      PreCondTriggKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { PreCondTriggKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { PreCondTriggKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { PreCondTriggKey.clearEvents(); });
    }

    frameRemains = 6  - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((PreCondTriggKey.status === PsychoJS.Status.STARTED || PreCondTriggKey.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      PreCondTriggKey.status = PsychoJS.Status.FINISHED;
  }

    if (PreCondTriggKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = PreCondTriggKey.getKeys({keyList: ['space'], waitRelease: false});
      _PreCondTriggKey_allKeys = _PreCondTriggKey_allKeys.concat(theseKeys);
      if (_PreCondTriggKey_allKeys.length > 0) {
        PreCondTriggKey.keys = _PreCondTriggKey_allKeys[_PreCondTriggKey_allKeys.length - 1].name;  // just the last key pressed
        PreCondTriggKey.rt = _PreCondTriggKey_allKeys[_PreCondTriggKey_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of trialPreCondComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function trialPreCondRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'trialPreCond' ---
    for (const thisComponent of trialPreCondComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for psychoJS.experiment (ExperimentHandler)
    if (PreCondTriggMouse.x) {  psychoJS.experiment.addData('PreCondTriggMouse.x', PreCondTriggMouse.x[0])};
    if (PreCondTriggMouse.y) {  psychoJS.experiment.addData('PreCondTriggMouse.y', PreCondTriggMouse.y[0])};
    if (PreCondTriggMouse.leftButton) {  psychoJS.experiment.addData('PreCondTriggMouse.leftButton', PreCondTriggMouse.leftButton[0])};
    if (PreCondTriggMouse.midButton) {  psychoJS.experiment.addData('PreCondTriggMouse.midButton', PreCondTriggMouse.midButton[0])};
    if (PreCondTriggMouse.rightButton) {  psychoJS.experiment.addData('PreCondTriggMouse.rightButton', PreCondTriggMouse.rightButton[0])};
    if (PreCondTriggMouse.time) {  psychoJS.experiment.addData('PreCondTriggMouse.time', PreCondTriggMouse.time[0])};
    
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(PreCondTriggKey.corr, level);
    }
    psychoJS.experiment.addData('PreCondTriggKey.keys', PreCondTriggKey.keys);
    if (typeof PreCondTriggKey.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('PreCondTriggKey.rt', PreCondTriggKey.rt);
        routineTimer.reset();
        }
    
    PreCondTriggKey.stop();
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function ITIRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'ITI' ---
    t = 0;
    ITIClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    ITIComponents = [];
    ITIComponents.push(FixCross);
    
    for (const thisComponent of ITIComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function ITIRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'ITI' ---
    // get current time
    t = ITIClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *FixCross* updates
    if (t >= 0.0 && FixCross.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      FixCross.tStart = t;  // (not accounting for frame time here)
      FixCross.frameNStart = frameN;  // exact frame index
      
      FixCross.setAutoDraw(true);
    }

    frameRemains = 0.0 + (Math.random.uniform(0, 2) + 6) - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (FixCross.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      FixCross.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of ITIComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function ITIRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'ITI' ---
    for (const thisComponent of ITIComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function RatingRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Rating' ---
    t = 0;
    RatingClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    image.setImage(CondName);
    RatingInstEN.setText(FearRatingInstTextEN);
    RatingInstCN.setText(FearRatingInstTextCN);
    Scale.reset()
    RatingKey.keys = undefined;
    RatingKey.rt = undefined;
    _RatingKey_allKeys = [];
    // setup some python lists for storing info about the mouse
    // current position of the mouse:
    mouse.x = [];
    mouse.y = [];
    mouse.leftButton = [];
    mouse.midButton = [];
    mouse.rightButton = [];
    mouse.time = [];
    gotValidClick = false; // until a click is received
    // reset Submit to account for continued clicks & clear times on/off
    Submit.reset()
    // keep track of which components have finished
    RatingComponents = [];
    RatingComponents.push(image);
    RatingComponents.push(RatingInstEN);
    RatingComponents.push(RatingInstCN);
    RatingComponents.push(Scale);
    RatingComponents.push(RatingKey);
    RatingComponents.push(mouse);
    RatingComponents.push(Submit);
    
    for (const thisComponent of RatingComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function RatingRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Rating' ---
    // get current time
    t = RatingClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image* updates
    if (t >= 0.0 && image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image.tStart = t;  // (not accounting for frame time here)
      image.frameNStart = frameN;  // exact frame index
      
      image.setAutoDraw(true);
    }

    
    // *RatingInstEN* updates
    if (((expInfo['Language'] == 'EN')) && RatingInstEN.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      RatingInstEN.tStart = t;  // (not accounting for frame time here)
      RatingInstEN.frameNStart = frameN;  // exact frame index
      
      RatingInstEN.setAutoDraw(true);
    }

    
    // *RatingInstCN* updates
    if (((expInfo['Language'] == 'CN')) && RatingInstCN.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      RatingInstCN.tStart = t;  // (not accounting for frame time here)
      RatingInstCN.frameNStart = frameN;  // exact frame index
      
      RatingInstCN.setAutoDraw(true);
    }

    
    // *Scale* updates
    if (t >= 0.0 && Scale.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Scale.tStart = t;  // (not accounting for frame time here)
      Scale.frameNStart = frameN;  // exact frame index
      
      Scale.setAutoDraw(true);
    }

    
    // *RatingKey* updates
    if ((Scale.rating) && RatingKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      RatingKey.tStart = t;  // (not accounting for frame time here)
      RatingKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { RatingKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { RatingKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { RatingKey.clearEvents(); });
    }

    if (RatingKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = RatingKey.getKeys({keyList: ['space'], waitRelease: false});
      _RatingKey_allKeys = _RatingKey_allKeys.concat(theseKeys);
      if (_RatingKey_allKeys.length > 0) {
        RatingKey.keys = _RatingKey_allKeys[_RatingKey_allKeys.length - 1].name;  // just the last key pressed
        RatingKey.rt = _RatingKey_allKeys[_RatingKey_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // *mouse* updates
    if (t >= 0 && mouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse.tStart = t;  // (not accounting for frame time here)
      mouse.frameNStart = frameN;  // exact frame index
      
      mouse.status = PsychoJS.Status.STARTED;
      mouse.mouseClock.reset();
      prevButtonState = mouse.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          _mouseXYs = mouse.getPos();
          mouse.x.push(_mouseXYs[0]);
          mouse.y.push(_mouseXYs[1]);
          mouse.leftButton.push(_mouseButtons[0]);
          mouse.midButton.push(_mouseButtons[1]);
          mouse.rightButton.push(_mouseButtons[2]);
          mouse.time.push(mouse.mouseClock.getTime());
        }
      }
    }
    
    // *Submit* updates
    if ((Scale.rating) && Submit.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Submit.tStart = t;  // (not accounting for frame time here)
      Submit.frameNStart = frameN;  // exact frame index
      
      Submit.setAutoDraw(true);
    }

    if (Submit.status === PsychoJS.Status.STARTED) {
      // check whether Submit has been pressed
      if (Submit.isClicked) {
        if (!Submit.wasClicked) {
          // store time of first click
          Submit.timesOn.push(Submit.clock.getTime());
          Submit.numClicks += 1;
          // store time clicked until
          Submit.timesOff.push(Submit.clock.getTime());
        } else {
          // update time clicked until;
          Submit.timesOff[Submit.timesOff.length - 1] = Submit.clock.getTime();
        }
        if (!Submit.wasClicked) {
          // end routine when Submit is clicked
          continueRoutine = false;
        }
        // if Submit is still clicked next frame, it is not a new click
        Submit.wasClicked = true;
      } else {
        // if Submit is clicked next frame, it is a new click
        Submit.wasClicked = false;
      }
    } else {
      // keep clock at 0 if Submit hasn't started / has finished
      Submit.clock.reset();
      // if Submit is clicked next frame, it is a new click
      Submit.wasClicked = false;
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of RatingComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function RatingRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Rating' ---
    for (const thisComponent of RatingComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Scale.response', Scale.getRating());
    psychoJS.experiment.addData('Scale.rt', Scale.getRT());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(RatingKey.corr, level);
    }
    psychoJS.experiment.addData('RatingKey.keys', RatingKey.keys);
    if (typeof RatingKey.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('RatingKey.rt', RatingKey.rt);
        routineTimer.reset();
        }
    
    RatingKey.stop();
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('mouse.x', mouse.x);
    psychoJS.experiment.addData('mouse.y', mouse.y);
    psychoJS.experiment.addData('mouse.leftButton', mouse.leftButton);
    psychoJS.experiment.addData('mouse.midButton', mouse.midButton);
    psychoJS.experiment.addData('mouse.rightButton', mouse.rightButton);
    psychoJS.experiment.addData('mouse.time', mouse.time);
    
    psychoJS.experiment.addData('Submit.numClicks', Submit.numClicks);
    psychoJS.experiment.addData('Submit.timesOn', Submit.timesOn);
    psychoJS.experiment.addData('Submit.timesOff', Submit.timesOff);
    // the Routine "Rating" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function CondInstRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'CondInst' ---
    t = 0;
    CondInstClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    CondImage.setImage(CondInstTextImage);
    CondImageOverview.setImage(CondInstTextImage);
    CondInstEN.setText(CondInstTextEN);
    CondInstCN.setText(CondInstTextCN);
    CondRespKey.keys = undefined;
    CondRespKey.rt = undefined;
    _CondRespKey_allKeys = [];
    // setup some python lists for storing info about the CondMouse
    // current position of the mouse:
    CondMouse.x = [];
    CondMouse.y = [];
    CondMouse.leftButton = [];
    CondMouse.midButton = [];
    CondMouse.rightButton = [];
    CondMouse.time = [];
    gotValidClick = false; // until a click is received
    // reset CondSubmit to account for continued clicks & clear times on/off
    CondSubmit.reset()
    // keep track of which components have finished
    CondInstComponents = [];
    CondInstComponents.push(CondImage);
    CondInstComponents.push(CondImageOverview);
    CondInstComponents.push(CondInstEN);
    CondInstComponents.push(CondInstCN);
    CondInstComponents.push(CondRespKey);
    CondInstComponents.push(CondMouse);
    CondInstComponents.push(CondSubmit);
    
    for (const thisComponent of CondInstComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function CondInstRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'CondInst' ---
    // get current time
    t = CondInstClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *CondImage* updates
    if (((CondInstTextImage == 'Stimuli/Raw_Trig.BMP')) && CondImage.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      CondImage.tStart = t;  // (not accounting for frame time here)
      CondImage.frameNStart = frameN;  // exact frame index
      
      CondImage.setAutoDraw(true);
    }

    
    // *CondImageOverview* updates
    if (((CondInstTextImage == 'Stimuli/Raw_3Faces.BMP')) && CondImageOverview.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      CondImageOverview.tStart = t;  // (not accounting for frame time here)
      CondImageOverview.frameNStart = frameN;  // exact frame index
      
      CondImageOverview.setAutoDraw(true);
    }

    
    // *CondInstEN* updates
    if (((expInfo['Language'] == 'EN')) && CondInstEN.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      CondInstEN.tStart = t;  // (not accounting for frame time here)
      CondInstEN.frameNStart = frameN;  // exact frame index
      
      CondInstEN.setAutoDraw(true);
    }

    
    // *CondInstCN* updates
    if (((expInfo['Language'] == 'CN')) && CondInstCN.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      CondInstCN.tStart = t;  // (not accounting for frame time here)
      CondInstCN.frameNStart = frameN;  // exact frame index
      
      CondInstCN.setAutoDraw(true);
    }

    
    // *CondRespKey* updates
    if (t >= 0.0 && CondRespKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      CondRespKey.tStart = t;  // (not accounting for frame time here)
      CondRespKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { CondRespKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { CondRespKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { CondRespKey.clearEvents(); });
    }

    if (CondRespKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = CondRespKey.getKeys({keyList: ['space'], waitRelease: false});
      _CondRespKey_allKeys = _CondRespKey_allKeys.concat(theseKeys);
      if (_CondRespKey_allKeys.length > 0) {
        CondRespKey.keys = _CondRespKey_allKeys[_CondRespKey_allKeys.length - 1].name;  // just the last key pressed
        CondRespKey.rt = _CondRespKey_allKeys[_CondRespKey_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // *CondMouse* updates
    if (t >= 0 && CondMouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      CondMouse.tStart = t;  // (not accounting for frame time here)
      CondMouse.frameNStart = frameN;  // exact frame index
      
      CondMouse.status = PsychoJS.Status.STARTED;
      CondMouse.mouseClock.reset();
      prevButtonState = CondMouse.getPressed();  // if button is down already this ISN'T a new click
      }
    if (CondMouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = CondMouse.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          _mouseXYs = CondMouse.getPos();
          CondMouse.x.push(_mouseXYs[0]);
          CondMouse.y.push(_mouseXYs[1]);
          CondMouse.leftButton.push(_mouseButtons[0]);
          CondMouse.midButton.push(_mouseButtons[1]);
          CondMouse.rightButton.push(_mouseButtons[2]);
          CondMouse.time.push(CondMouse.mouseClock.getTime());
        }
      }
    }
    
    // *CondSubmit* updates
    if (t >= 0 && CondSubmit.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      CondSubmit.tStart = t;  // (not accounting for frame time here)
      CondSubmit.frameNStart = frameN;  // exact frame index
      
      CondSubmit.setAutoDraw(true);
    }

    if (CondSubmit.status === PsychoJS.Status.STARTED) {
      // check whether CondSubmit has been pressed
      if (CondSubmit.isClicked) {
        if (!CondSubmit.wasClicked) {
          // store time of first click
          CondSubmit.timesOn.push(CondSubmit.clock.getTime());
          CondSubmit.numClicks += 1;
          // store time clicked until
          CondSubmit.timesOff.push(CondSubmit.clock.getTime());
        } else {
          // update time clicked until;
          CondSubmit.timesOff[CondSubmit.timesOff.length - 1] = CondSubmit.clock.getTime();
        }
        if (!CondSubmit.wasClicked) {
          // end routine when CondSubmit is clicked
          continueRoutine = false;
        }
        // if CondSubmit is still clicked next frame, it is not a new click
        CondSubmit.wasClicked = true;
      } else {
        // if CondSubmit is clicked next frame, it is a new click
        CondSubmit.wasClicked = false;
      }
    } else {
      // keep clock at 0 if CondSubmit hasn't started / has finished
      CondSubmit.clock.reset();
      // if CondSubmit is clicked next frame, it is a new click
      CondSubmit.wasClicked = false;
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of CondInstComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function CondInstRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'CondInst' ---
    for (const thisComponent of CondInstComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(CondRespKey.corr, level);
    }
    psychoJS.experiment.addData('CondRespKey.keys', CondRespKey.keys);
    if (typeof CondRespKey.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('CondRespKey.rt', CondRespKey.rt);
        routineTimer.reset();
        }
    
    CondRespKey.stop();
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('CondMouse.x', CondMouse.x);
    psychoJS.experiment.addData('CondMouse.y', CondMouse.y);
    psychoJS.experiment.addData('CondMouse.leftButton', CondMouse.leftButton);
    psychoJS.experiment.addData('CondMouse.midButton', CondMouse.midButton);
    psychoJS.experiment.addData('CondMouse.rightButton', CondMouse.rightButton);
    psychoJS.experiment.addData('CondMouse.time', CondMouse.time);
    
    psychoJS.experiment.addData('CondSubmit.numClicks', CondSubmit.numClicks);
    psychoJS.experiment.addData('CondSubmit.timesOn', CondSubmit.timesOn);
    psychoJS.experiment.addData('CondSubmit.timesOff', CondSubmit.timesOff);
    // the Routine "CondInst" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function trialCondRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'trialCond' ---
    t = 0;
    trialCondClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(6.000000);
    // update component parameters for each repeat
    CS_image.setImage(CSName);
    // Run 'Begin Routine' code from EachTrial_2
    if ((skipPhases === true)) {
        continueRoutine = false;
        Cond.finished = true;
    }
    if ((parallelTrigger === true)) {
        ParaleData = 50;
        port.setData(ParaleData);
        if ((lfpTrigger === true)) {
            lfpCtrlPort.setData(1);
        }
        core.wait(0.02);
        port.setData(0);
        if ((lfpTrigger === true)) {
            lfpCtrlPort.setData(0);
        }
    }
    
    // setup some python lists for storing info about the CondTriggMouse
    // current position of the mouse:
    CondTriggMouse.x = [];
    CondTriggMouse.y = [];
    CondTriggMouse.leftButton = [];
    CondTriggMouse.midButton = [];
    CondTriggMouse.rightButton = [];
    CondTriggMouse.time = [];
    gotValidClick = false; // until a click is received
    CondTriggMouse.mouseClock.reset();
    CondTriggKey.keys = undefined;
    CondTriggKey.rt = undefined;
    _CondTriggKey_allKeys = [];
    // keep track of which components have finished
    trialCondComponents = [];
    trialCondComponents.push(CS_image);
    trialCondComponents.push(CondTriggMouse);
    trialCondComponents.push(CondTriggKey);
    
    for (const thisComponent of trialCondComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function trialCondRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trialCond' ---
    // get current time
    t = trialCondClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *CS_image* updates
    if (t >= 0.0 && CS_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      CS_image.tStart = t;  // (not accounting for frame time here)
      CS_image.frameNStart = frameN;  // exact frame index
      
      CS_image.setAutoDraw(true);
    }

    frameRemains = 0.0 + 6 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (CS_image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      CS_image.setAutoDraw(false);
    }
    // *CondTriggMouse* updates
    if (((CSName == 'Stimuli/Trig.BMP')) && CondTriggMouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      CondTriggMouse.tStart = t;  // (not accounting for frame time here)
      CondTriggMouse.frameNStart = frameN;  // exact frame index
      
      CondTriggMouse.status = PsychoJS.Status.STARTED;
      prevButtonState = CondTriggMouse.getPressed();  // if button is down already this ISN'T a new click
      }
    frameRemains = 6  - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((CondTriggMouse.status === PsychoJS.Status.STARTED || CondTriggMouse.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      CondTriggMouse.status = PsychoJS.Status.FINISHED;
  }
    if (CondTriggMouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = CondTriggMouse.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          _mouseXYs = CondTriggMouse.getPos();
          CondTriggMouse.x.push(_mouseXYs[0]);
          CondTriggMouse.y.push(_mouseXYs[1]);
          CondTriggMouse.leftButton.push(_mouseButtons[0]);
          CondTriggMouse.midButton.push(_mouseButtons[1]);
          CondTriggMouse.rightButton.push(_mouseButtons[2]);
          CondTriggMouse.time.push(CondTriggMouse.mouseClock.getTime());
          // end routine on response
          continueRoutine = false;
        }
      }
    }
    
    // *CondTriggKey* updates
    if (((CSName == 'Stimuli/Trig.BMP')) && CondTriggKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      CondTriggKey.tStart = t;  // (not accounting for frame time here)
      CondTriggKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { CondTriggKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { CondTriggKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { CondTriggKey.clearEvents(); });
    }

    frameRemains = 6  - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((CondTriggKey.status === PsychoJS.Status.STARTED || CondTriggKey.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      CondTriggKey.status = PsychoJS.Status.FINISHED;
  }

    if (CondTriggKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = CondTriggKey.getKeys({keyList: ['space'], waitRelease: false});
      _CondTriggKey_allKeys = _CondTriggKey_allKeys.concat(theseKeys);
      if (_CondTriggKey_allKeys.length > 0) {
        CondTriggKey.keys = _CondTriggKey_allKeys[_CondTriggKey_allKeys.length - 1].name;  // just the last key pressed
        CondTriggKey.rt = _CondTriggKey_allKeys[_CondTriggKey_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of trialCondComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function trialCondRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'trialCond' ---
    for (const thisComponent of trialCondComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for psychoJS.experiment (ExperimentHandler)
    if (CondTriggMouse.x) {  psychoJS.experiment.addData('CondTriggMouse.x', CondTriggMouse.x[0])};
    if (CondTriggMouse.y) {  psychoJS.experiment.addData('CondTriggMouse.y', CondTriggMouse.y[0])};
    if (CondTriggMouse.leftButton) {  psychoJS.experiment.addData('CondTriggMouse.leftButton', CondTriggMouse.leftButton[0])};
    if (CondTriggMouse.midButton) {  psychoJS.experiment.addData('CondTriggMouse.midButton', CondTriggMouse.midButton[0])};
    if (CondTriggMouse.rightButton) {  psychoJS.experiment.addData('CondTriggMouse.rightButton', CondTriggMouse.rightButton[0])};
    if (CondTriggMouse.time) {  psychoJS.experiment.addData('CondTriggMouse.time', CondTriggMouse.time[0])};
    
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(CondTriggKey.corr, level);
    }
    psychoJS.experiment.addData('CondTriggKey.keys', CondTriggKey.keys);
    if (typeof CondTriggKey.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('CondTriggKey.rt', CondTriggKey.rt);
        routineTimer.reset();
        }
    
    CondTriggKey.stop();
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function UCSRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'UCS' ---
    t = 0;
    UCSClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    UCS_image.setImage(UCSName);
    sound_1.setValue(SoundName);
    sound_1.secs=1;
    sound_1.setVolume(0.3);
    // keep track of which components have finished
    UCSComponents = [];
    UCSComponents.push(UCSBkg);
    UCSComponents.push(UCS_image);
    UCSComponents.push(sound_1);
    
    for (const thisComponent of UCSComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function UCSRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'UCS' ---
    // get current time
    t = UCSClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *UCSBkg* updates
    if (t >= 0.0 && UCSBkg.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      UCSBkg.tStart = t;  // (not accounting for frame time here)
      UCSBkg.frameNStart = frameN;  // exact frame index
      
      UCSBkg.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (UCSBkg.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      UCSBkg.setAutoDraw(false);
    }
    
    // *UCS_image* updates
    if (t >= 0.0 && UCS_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      UCS_image.tStart = t;  // (not accounting for frame time here)
      UCS_image.frameNStart = frameN;  // exact frame index
      
      UCS_image.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (UCS_image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      UCS_image.setAutoDraw(false);
    }
    // start/stop sound_1
    if (t >= 0 && sound_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sound_1.tStart = t;  // (not accounting for frame time here)
      sound_1.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ sound_1.play(); });  // screen flip
      sound_1.status = PsychoJS.Status.STARTED;
    }
    frameRemains = 0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (sound_1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      if (1 > 0.5) {
        sound_1.stop();  // stop the sound (if longer than duration)
      }
      sound_1.status = PsychoJS.Status.FINISHED;
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of UCSComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function UCSRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'UCS' ---
    for (const thisComponent of UCSComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    sound_1.stop();  // ensure sound has stopped at end of routine
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function ExtInstRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'ExtInst' ---
    t = 0;
    ExtInstClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    ExtImage.setImage(ExtInstTextImage);
    ExtImageOverview.setImage(ExtInstTextImage);
    ExtInstEN.setText(ExtInstTextEN);
    ExtInstCN.setText(ExtInstTextCN);
    ExtRespKey.keys = undefined;
    ExtRespKey.rt = undefined;
    _ExtRespKey_allKeys = [];
    // setup some python lists for storing info about the ExtMouse
    // current position of the mouse:
    ExtMouse.x = [];
    ExtMouse.y = [];
    ExtMouse.leftButton = [];
    ExtMouse.midButton = [];
    ExtMouse.rightButton = [];
    ExtMouse.time = [];
    gotValidClick = false; // until a click is received
    // reset ExtSubmit to account for continued clicks & clear times on/off
    ExtSubmit.reset()
    // keep track of which components have finished
    ExtInstComponents = [];
    ExtInstComponents.push(ExtImage);
    ExtInstComponents.push(ExtImageOverview);
    ExtInstComponents.push(ExtInstEN);
    ExtInstComponents.push(ExtInstCN);
    ExtInstComponents.push(ExtRespKey);
    ExtInstComponents.push(ExtMouse);
    ExtInstComponents.push(ExtSubmit);
    
    for (const thisComponent of ExtInstComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function ExtInstRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'ExtInst' ---
    // get current time
    t = ExtInstClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *ExtImage* updates
    if (((ExtInstTextImage == 'Stimuli/Raw_Trig.BMP')) && ExtImage.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ExtImage.tStart = t;  // (not accounting for frame time here)
      ExtImage.frameNStart = frameN;  // exact frame index
      
      ExtImage.setAutoDraw(true);
    }

    
    // *ExtImageOverview* updates
    if (((ExtInstTextImage == 'Stimuli/Raw_3Faces.BMP')) && ExtImageOverview.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ExtImageOverview.tStart = t;  // (not accounting for frame time here)
      ExtImageOverview.frameNStart = frameN;  // exact frame index
      
      ExtImageOverview.setAutoDraw(true);
    }

    
    // *ExtInstEN* updates
    if (((expInfo['Language'] == 'EN')) && ExtInstEN.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ExtInstEN.tStart = t;  // (not accounting for frame time here)
      ExtInstEN.frameNStart = frameN;  // exact frame index
      
      ExtInstEN.setAutoDraw(true);
    }

    
    // *ExtInstCN* updates
    if (((expInfo['Language'] == 'CN')) && ExtInstCN.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ExtInstCN.tStart = t;  // (not accounting for frame time here)
      ExtInstCN.frameNStart = frameN;  // exact frame index
      
      ExtInstCN.setAutoDraw(true);
    }

    
    // *ExtRespKey* updates
    if (t >= 0.0 && ExtRespKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ExtRespKey.tStart = t;  // (not accounting for frame time here)
      ExtRespKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { ExtRespKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { ExtRespKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { ExtRespKey.clearEvents(); });
    }

    if (ExtRespKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = ExtRespKey.getKeys({keyList: ['space'], waitRelease: false});
      _ExtRespKey_allKeys = _ExtRespKey_allKeys.concat(theseKeys);
      if (_ExtRespKey_allKeys.length > 0) {
        ExtRespKey.keys = _ExtRespKey_allKeys[_ExtRespKey_allKeys.length - 1].name;  // just the last key pressed
        ExtRespKey.rt = _ExtRespKey_allKeys[_ExtRespKey_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // *ExtMouse* updates
    if (t >= 0 && ExtMouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ExtMouse.tStart = t;  // (not accounting for frame time here)
      ExtMouse.frameNStart = frameN;  // exact frame index
      
      ExtMouse.status = PsychoJS.Status.STARTED;
      ExtMouse.mouseClock.reset();
      prevButtonState = ExtMouse.getPressed();  // if button is down already this ISN'T a new click
      }
    if (ExtMouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = ExtMouse.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          _mouseXYs = ExtMouse.getPos();
          ExtMouse.x.push(_mouseXYs[0]);
          ExtMouse.y.push(_mouseXYs[1]);
          ExtMouse.leftButton.push(_mouseButtons[0]);
          ExtMouse.midButton.push(_mouseButtons[1]);
          ExtMouse.rightButton.push(_mouseButtons[2]);
          ExtMouse.time.push(ExtMouse.mouseClock.getTime());
        }
      }
    }
    
    // *ExtSubmit* updates
    if (t >= 0 && ExtSubmit.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ExtSubmit.tStart = t;  // (not accounting for frame time here)
      ExtSubmit.frameNStart = frameN;  // exact frame index
      
      ExtSubmit.setAutoDraw(true);
    }

    if (ExtSubmit.status === PsychoJS.Status.STARTED) {
      // check whether ExtSubmit has been pressed
      if (ExtSubmit.isClicked) {
        if (!ExtSubmit.wasClicked) {
          // store time of first click
          ExtSubmit.timesOn.push(ExtSubmit.clock.getTime());
          ExtSubmit.numClicks += 1;
          // store time clicked until
          ExtSubmit.timesOff.push(ExtSubmit.clock.getTime());
        } else {
          // update time clicked until;
          ExtSubmit.timesOff[ExtSubmit.timesOff.length - 1] = ExtSubmit.clock.getTime();
        }
        if (!ExtSubmit.wasClicked) {
          // end routine when ExtSubmit is clicked
          continueRoutine = false;
        }
        // if ExtSubmit is still clicked next frame, it is not a new click
        ExtSubmit.wasClicked = true;
      } else {
        // if ExtSubmit is clicked next frame, it is a new click
        ExtSubmit.wasClicked = false;
      }
    } else {
      // keep clock at 0 if ExtSubmit hasn't started / has finished
      ExtSubmit.clock.reset();
      // if ExtSubmit is clicked next frame, it is a new click
      ExtSubmit.wasClicked = false;
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of ExtInstComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function ExtInstRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'ExtInst' ---
    for (const thisComponent of ExtInstComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(ExtRespKey.corr, level);
    }
    psychoJS.experiment.addData('ExtRespKey.keys', ExtRespKey.keys);
    if (typeof ExtRespKey.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('ExtRespKey.rt', ExtRespKey.rt);
        routineTimer.reset();
        }
    
    ExtRespKey.stop();
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('ExtMouse.x', ExtMouse.x);
    psychoJS.experiment.addData('ExtMouse.y', ExtMouse.y);
    psychoJS.experiment.addData('ExtMouse.leftButton', ExtMouse.leftButton);
    psychoJS.experiment.addData('ExtMouse.midButton', ExtMouse.midButton);
    psychoJS.experiment.addData('ExtMouse.rightButton', ExtMouse.rightButton);
    psychoJS.experiment.addData('ExtMouse.time', ExtMouse.time);
    
    psychoJS.experiment.addData('ExtSubmit.numClicks', ExtSubmit.numClicks);
    psychoJS.experiment.addData('ExtSubmit.timesOn', ExtSubmit.timesOn);
    psychoJS.experiment.addData('ExtSubmit.timesOff', ExtSubmit.timesOff);
    // the Routine "ExtInst" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function trialExtRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'trialExt' ---
    t = 0;
    trialExtClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(6.000000);
    // update component parameters for each repeat
    Ext_image.setImage(ExtName);
    // Run 'Begin Routine' code from EachTrial_3
    if ((skipPhases === true)) {
        continueRoutine = false;
        Ext.finished = true;
    }
    if ((parallelTrigger === true)) {
        ParaleData = 50;
        port.setData(ParaleData);
        if ((lfpTrigger === true)) {
            lfpCtrlPort.setData(1);
        }
        core.wait(0.02);
        port.setData(0);
        if ((lfpTrigger === true)) {
            lfpCtrlPort.setData(0);
        }
    }
    
    // setup some python lists for storing info about the ExtTriggMouse
    // current position of the mouse:
    ExtTriggMouse.x = [];
    ExtTriggMouse.y = [];
    ExtTriggMouse.leftButton = [];
    ExtTriggMouse.midButton = [];
    ExtTriggMouse.rightButton = [];
    ExtTriggMouse.time = [];
    gotValidClick = false; // until a click is received
    ExtTriggMouse.mouseClock.reset();
    ExtTriggKey.keys = undefined;
    ExtTriggKey.rt = undefined;
    _ExtTriggKey_allKeys = [];
    // keep track of which components have finished
    trialExtComponents = [];
    trialExtComponents.push(Ext_image);
    trialExtComponents.push(ExtTriggMouse);
    trialExtComponents.push(ExtTriggKey);
    
    for (const thisComponent of trialExtComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function trialExtRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trialExt' ---
    // get current time
    t = trialExtClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Ext_image* updates
    if (t >= 0.0 && Ext_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Ext_image.tStart = t;  // (not accounting for frame time here)
      Ext_image.frameNStart = frameN;  // exact frame index
      
      Ext_image.setAutoDraw(true);
    }

    frameRemains = 0.0 + 6 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Ext_image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Ext_image.setAutoDraw(false);
    }
    // *ExtTriggMouse* updates
    if (((ExtName == 'Stimuli/Trig.BMP')) && ExtTriggMouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ExtTriggMouse.tStart = t;  // (not accounting for frame time here)
      ExtTriggMouse.frameNStart = frameN;  // exact frame index
      
      ExtTriggMouse.status = PsychoJS.Status.STARTED;
      prevButtonState = ExtTriggMouse.getPressed();  // if button is down already this ISN'T a new click
      }
    frameRemains = 6  - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((ExtTriggMouse.status === PsychoJS.Status.STARTED || ExtTriggMouse.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      ExtTriggMouse.status = PsychoJS.Status.FINISHED;
  }
    if (ExtTriggMouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = ExtTriggMouse.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          _mouseXYs = ExtTriggMouse.getPos();
          ExtTriggMouse.x.push(_mouseXYs[0]);
          ExtTriggMouse.y.push(_mouseXYs[1]);
          ExtTriggMouse.leftButton.push(_mouseButtons[0]);
          ExtTriggMouse.midButton.push(_mouseButtons[1]);
          ExtTriggMouse.rightButton.push(_mouseButtons[2]);
          ExtTriggMouse.time.push(ExtTriggMouse.mouseClock.getTime());
          // end routine on response
          continueRoutine = false;
        }
      }
    }
    
    // *ExtTriggKey* updates
    if (((ExtName == 'Stimuli/Trig.BMP')) && ExtTriggKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ExtTriggKey.tStart = t;  // (not accounting for frame time here)
      ExtTriggKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { ExtTriggKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { ExtTriggKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { ExtTriggKey.clearEvents(); });
    }

    frameRemains = 6  - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((ExtTriggKey.status === PsychoJS.Status.STARTED || ExtTriggKey.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      ExtTriggKey.status = PsychoJS.Status.FINISHED;
  }

    if (ExtTriggKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = ExtTriggKey.getKeys({keyList: ['space'], waitRelease: false});
      _ExtTriggKey_allKeys = _ExtTriggKey_allKeys.concat(theseKeys);
      if (_ExtTriggKey_allKeys.length > 0) {
        ExtTriggKey.keys = _ExtTriggKey_allKeys[_ExtTriggKey_allKeys.length - 1].name;  // just the last key pressed
        ExtTriggKey.rt = _ExtTriggKey_allKeys[_ExtTriggKey_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of trialExtComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function trialExtRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'trialExt' ---
    for (const thisComponent of trialExtComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for psychoJS.experiment (ExperimentHandler)
    if (ExtTriggMouse.x) {  psychoJS.experiment.addData('ExtTriggMouse.x', ExtTriggMouse.x[0])};
    if (ExtTriggMouse.y) {  psychoJS.experiment.addData('ExtTriggMouse.y', ExtTriggMouse.y[0])};
    if (ExtTriggMouse.leftButton) {  psychoJS.experiment.addData('ExtTriggMouse.leftButton', ExtTriggMouse.leftButton[0])};
    if (ExtTriggMouse.midButton) {  psychoJS.experiment.addData('ExtTriggMouse.midButton', ExtTriggMouse.midButton[0])};
    if (ExtTriggMouse.rightButton) {  psychoJS.experiment.addData('ExtTriggMouse.rightButton', ExtTriggMouse.rightButton[0])};
    if (ExtTriggMouse.time) {  psychoJS.experiment.addData('ExtTriggMouse.time', ExtTriggMouse.time[0])};
    
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(ExtTriggKey.corr, level);
    }
    psychoJS.experiment.addData('ExtTriggKey.keys', ExtTriggKey.keys);
    if (typeof ExtTriggKey.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('ExtTriggKey.rt', ExtTriggKey.rt);
        routineTimer.reset();
        }
    
    ExtTriggKey.stop();
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function EndBlockRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'EndBlock' ---
    t = 0;
    EndBlockClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    EndTxtEN.setText(EndTextEN);
    EndTxtCN.setText(EndTextCN);
    // keep track of which components have finished
    EndBlockComponents = [];
    EndBlockComponents.push(Bkg_Light);
    EndBlockComponents.push(EndTxtEN);
    EndBlockComponents.push(EndTxtCN);
    
    for (const thisComponent of EndBlockComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function EndBlockRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'EndBlock' ---
    // get current time
    t = EndBlockClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Bkg_Light* updates
    if (t >= 0.0 && Bkg_Light.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Bkg_Light.tStart = t;  // (not accounting for frame time here)
      Bkg_Light.frameNStart = frameN;  // exact frame index
      
      Bkg_Light.setAutoDraw(true);
    }

    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Bkg_Light.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Bkg_Light.setAutoDraw(false);
    }
    
    // *EndTxtEN* updates
    if (((expInfo['Language'] == 'EN')) && EndTxtEN.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      EndTxtEN.tStart = t;  // (not accounting for frame time here)
      EndTxtEN.frameNStart = frameN;  // exact frame index
      
      EndTxtEN.setAutoDraw(true);
    }

    if (EndTxtEN.status === PsychoJS.Status.STARTED && t >= (EndTxtEN.tStart + 5)) {
      EndTxtEN.setAutoDraw(false);
    }
    
    // *EndTxtCN* updates
    if (((expInfo['Language'] == 'CN')) && EndTxtCN.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      EndTxtCN.tStart = t;  // (not accounting for frame time here)
      EndTxtCN.frameNStart = frameN;  // exact frame index
      
      EndTxtCN.setAutoDraw(true);
    }

    if (EndTxtCN.status === PsychoJS.Status.STARTED && t >= (EndTxtCN.tStart + 5)) {
      EndTxtCN.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of EndBlockComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function EndBlockRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'EndBlock' ---
    for (const thisComponent of EndBlockComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "EndBlock" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}

async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
