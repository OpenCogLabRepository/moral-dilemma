#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.78.01), Wed 25 Sep 2013 03:59:24 PM EDT
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys

LUMINA = 1
LUMINA_TRIGGER = 4

## initialize communication with the lumina

if LUMINA == 1:
    import pyxid # to interact with the Lumina box
    import sys

    ## initialize communication with the lumina
    devices=pyxid.get_xid_devices()

    if devices:
        lumina_dev=devices[0]
    else:
        print "Could not find Lumina device"
        sys.exit(1)

    print lumina_dev
    if lumina_dev.is_response_device():
        lumina_dev.reset_base_timer()
        lumina_dev.reset_rt_timer()
    else:
        print "Error: Lumina device is not a response device??"
        log.write("Error: Lumina device is not a response device??")
        sys.exit(1)



# Store info about the experiment session
expName = 'moral_dilemma'  # from the Builder filename that created this script
expInfo = {'participant':'', 'session':'001', 'volume':'1.0'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

try:
    audioVolume = float(expInfo['volume'])
except:
    print "Invalid volume setting %s"%(expInfo['volume'])
    sys.exit(1)

if audioVolume < 0.0 or audioVolume > 1.0:
    print "Audio volume (%f) out of range. Should be in the range (0.0, 1.0) inclusive."%(audioVolume)
    sys.exit(1)

# Setup files for saving
if not os.path.isdir('data'):
    os.makedirs('data')  # if this fails (e.g. permissions) we will get error
filename = 'data' + os.path.sep + '%s_%s' %(expInfo['participant'], expInfo['date'])
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)

# Setup the Window
win = visual.Window(size=(1600, 900), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb')

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
text_instruct = visual.TextStim(win=win, ori=0, name='text_instruct',
    text="Please respond:\n\n'YES' with your index finger \n\nor\n\n'NO' with your middle finger \n\nfor each vignette.",    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
fixation_txt = visual.TextStim(win=win, ori=0, name='fixation_txt',
    text=u'+',    font=u'Arial',
    pos=[0, 0], height=0.5, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "control"
controlClock = core.Clock()
ctrl_image = visual.ImageStim(win=win, name='ctrl_image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1, 1.3],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=0.0)
sound_1 = sound.Sound('A', secs=5)
sound_1.setVolume(audioVolume)

# Initialize components for Routine "dilemma"
dilemmaClock = core.Clock()
dil_image = visual.ImageStim(win=win, name='dil_image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1,1.3],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=0.0)
sound_2 = sound.Sound('A', secs=5)
sound_2.setVolume(audioVolume)

# Initialize components for Routine "control"
controlClock = core.Clock()
ctrl_image = visual.ImageStim(win=win, name='ctrl_image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1, 1.3],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=0.0)
sound_1 = sound.Sound('A', secs=5)
sound_1.setVolume(audioVolume)

# Initialize components for Routine "dilemma"
dilemmaClock = core.Clock()
dil_image = visual.ImageStim(win=win, name='dil_image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1,1.3],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=0.0)
sound_2 = sound.Sound('A', secs=5)
sound_2.setVolume(audioVolume)

# Initialize components for Routine "control"
controlClock = core.Clock()
ctrl_image = visual.ImageStim(win=win, name='ctrl_image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1, 1.3],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=0.0)
sound_1 = sound.Sound('A', secs=5)
sound_1.setVolume(audioVolume)

# Initialize components for Routine "dilemma"
dilemmaClock = core.Clock()
dil_image = visual.ImageStim(win=win, name='dil_image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1,1.3],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=0.0)
sound_2 = sound.Sound('A', secs=5)
sound_2.setVolume(audioVolume)

# Initialize components for Routine "control"
controlClock = core.Clock()
ctrl_image = visual.ImageStim(win=win, name='ctrl_image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1, 1.3],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=0.0)
sound_1 = sound.Sound('A', secs=5)
sound_1.setVolume(audioVolume)

# Initialize components for Routine "dilemma"
dilemmaClock = core.Clock()
dil_image = visual.ImageStim(win=win, name='dil_image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1,1.3],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=0.0)
sound_2 = sound.Sound('A', secs=5)
sound_2.setVolume(1)

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
fixation_txt = visual.TextStim(win=win, ori=0, name='fixation_txt',
    text=u'+',    font=u'Arial',
    pos=[0, 0], height=0.5, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "thanks"
thanksClock = core.Clock()
text = visual.TextStim(win=win, ori=0, name='text',
    text='Thanks!',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "instructions"-------
t = 0
instructionsClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_5 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_5.status = NOT_STARTED
# keep track of which components have finished
instructionsComponents = []
instructionsComponents.append(text_instruct)
instructionsComponents.append(key_resp_5)
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instructions"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_instruct* updates
    if t >= 0.0 and text_instruct.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_instruct.tStart = t  # underestimates by a little under one frame
        text_instruct.frameNStart = frameN  # exact frame index
        text_instruct.setAutoDraw(True)
    
    # *key_resp_5* updates
    if t >= 0.0 and key_resp_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_5.tStart = t  # underestimates by a little under one frame
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        key_resp_5.clock.reset()  # now t=0
        event.clearEvents()
        theseKeys=[]
        if LUMINA==1:
            lumina_dev.clear_response_queue()
    if key_resp_5.status == STARTED:
        # check for a LUMINA_TRIGGER from the Lumina box
        if LUMINA == 1:
            theseKeys=[]
            lumina_dev.poll_for_response()
            while lumina_dev.response_queue_size() > 0:
                response = lumina_dev.get_next_response() 
                if response["pressed"]:
                    print "Lumina received: %s, %d"%(response["key"],response["key"])
                    if response["key"] == 4: 
                        theseKeys.append(str(response["key"]))
        else:
            theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space'])
        
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_5.keys = theseKeys[-1]  # just the last key pressed
            key_resp_5.rt = key_resp_5.clock.getTime()
            # a response ends the routine
            continueRoutine = False
        
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "fixation"-------
t = 0
fixationClock.reset()  # clock 
frameN = -1
routineTimer.add(20.000000)
# update component parameters for each repeat
# keep track of which components have finished
fixationComponents = []
fixationComponents.append(fixation_txt)
for thisComponent in fixationComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "fixation"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = fixationClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fixation_txt* updates
    if t >= 0.0 and fixation_txt.status == NOT_STARTED:
        # keep track of start time/frame for later
        fixation_txt.tStart = t  # underestimates by a little under one frame
        fixation_txt.frameNStart = frameN  # exact frame index
        fixation_txt.setAutoDraw(True)
    elif fixation_txt.status == STARTED and t >= (0.0 + 20):
        fixation_txt.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "fixation"-------
for thisComponent in fixationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('moral_dilemma_targets_1.csv'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2.keys():
        exec(paramName + '= thisTrial_2.' + paramName)

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2.keys():
            exec(paramName + '= thisTrial_2.' + paramName)
    
    #------Prepare to start Routine "control"-------
    t = 0
    controlClock.reset()  # clock 
    frameN = -1
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    ctrl_image.setImage(control_image)
    sound_1.setSound(control_sound)
    key_resp_3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_3.status = NOT_STARTED
    # keep track of which components have finished
    controlComponents = []
    controlComponents.append(ctrl_image)
    controlComponents.append(sound_1)
    controlComponents.append(key_resp_3)
    for thisComponent in controlComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "control"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = controlClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ctrl_image* updates
        if t >= 0.0 and ctrl_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            ctrl_image.tStart = t  # underestimates by a little under one frame
            ctrl_image.frameNStart = frameN  # exact frame index
            ctrl_image.setAutoDraw(True)
        elif ctrl_image.status == STARTED and t >= (0.0 + 5):
            ctrl_image.setAutoDraw(False)
        # start/stop sound_1
        if t >= 0 and sound_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_1.tStart = t  # underestimates by a little under one frame
            sound_1.frameNStart = frameN  # exact frame index
            sound_1.play()  # start the sound (it finishes automatically)
        elif sound_1.status == STARTED and t >= (0 + 5):
            sound_1.stop()  # stop the sound (if longer than duration)
        
        # *key_resp_3* updates
        if t >= 0 and key_resp_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_3.tStart = t  # underestimates by a little under one frame
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            key_resp_3.clock.reset()  # now t=0
            event.clearEvents()
            theseKeys=[]
            if LUMINA==1:
                lumina_dev.clear_response_queue()
        elif key_resp_3.status == STARTED and t >= (0 + 5):
            key_resp_3.status = STOPPED
        if key_resp_3.status == STARTED:
            # check for a LUMINA_TRIGGER from the Lumina box
            if LUMINA == 1:
                theseKeys=[]
                lumina_dev.poll_for_response()
                while lumina_dev.response_queue_size() > 0:
                    response = lumina_dev.get_next_response() 
                    if response["pressed"]:
                        print "Lumina received: %s, %d"%(response["key"],response["key"])
                        if response["key"] in [0,1,2]: 
                            theseKeys.append(str(response["key"]+1))
            else:
                theseKeys = event.getKeys(keyList=['y', 'n'])

            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_3.keys = theseKeys[-1]  # just the last key pressed
                key_resp_3.rt = key_resp_3.clock.getTime()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in controlComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "control"-------
    for thisComponent in controlComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if len(key_resp_3.keys) == 0:  # No response was made
       key_resp_3.keys=None
    # store data for trials_2 (TrialHandler)
    trials_2.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        trials_2.addData('key_resp_3.rt', key_resp_3.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_2'


# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('moral_dilemma_targets_1.csv'),
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3.keys():
        exec(paramName + '= thisTrial_3.' + paramName)

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3.keys():
            exec(paramName + '= thisTrial_3.' + paramName)
    
    #------Prepare to start Routine "dilemma"-------
    t = 0
    dilemmaClock.reset()  # clock 
    frameN = -1
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    dil_image.setImage(dilemma_image)
    sound_2.setSound(dilemma_sound)
    key_resp_4 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_4.status = NOT_STARTED
    # keep track of which components have finished
    dilemmaComponents = []
    dilemmaComponents.append(dil_image)
    dilemmaComponents.append(sound_2)
    dilemmaComponents.append(key_resp_4)
    for thisComponent in dilemmaComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "dilemma"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = dilemmaClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *dil_image* updates
        if t >= 0.0 and dil_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            dil_image.tStart = t  # underestimates by a little under one frame
            dil_image.frameNStart = frameN  # exact frame index
            dil_image.setAutoDraw(True)
        elif dil_image.status == STARTED and t >= (0.0 + 5):
            dil_image.setAutoDraw(False)
        # start/stop sound_2
        if t >= 0 and sound_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_2.tStart = t  # underestimates by a little under one frame
            sound_2.frameNStart = frameN  # exact frame index
            sound_2.play()  # start the sound (it finishes automatically)
        elif sound_2.status == STARTED and t >= (0 + 5):
            sound_2.stop()  # stop the sound (if longer than duration)
        
        # *key_resp_4* updates
        if t >= 0 and key_resp_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_4.tStart = t  # underestimates by a little under one frame
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            key_resp_4.clock.reset()  # now t=0
            event.clearEvents()
            theseKeys=[]
            if LUMINA==1:
                lumina_dev.clear_response_queue()
        elif key_resp_4.status == STARTED and t >= (0 + 5):
            key_resp_4.status = STOPPED
        if key_resp_4.status == STARTED:
            # check for a LUMINA_TRIGGER from the Lumina box
            if LUMINA == 1:
                theseKeys=[]
                lumina_dev.poll_for_response()
                while lumina_dev.response_queue_size() > 0:
                    response = lumina_dev.get_next_response() 
                    if response["pressed"]:
                        print "Lumina received: %s, %d"%(response["key"],response["key"])
                        if response["key"] in [0,1,2]: 
                            theseKeys.append(str(response["key"]+1))
            else:
                theseKeys = event.getKeys(keyList=['y', 'n'])

            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_4.keys = theseKeys[-1]  # just the last key pressed
                key_resp_4.rt = key_resp_4.clock.getTime()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in dilemmaComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "dilemma"-------
    for thisComponent in dilemmaComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if len(key_resp_4.keys) == 0:  # No response was made
       key_resp_4.keys=None
    # store data for trials_3 (TrialHandler)
    trials_3.addData('key_resp_4.keys',key_resp_4.keys)
    if key_resp_4.keys != None:  # we had a response
        trials_3.addData('key_resp_4.rt', key_resp_4.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_3'


# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('moral_dilemma_targets_2.csv'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    #------Prepare to start Routine "control"-------
    t = 0
    controlClock.reset()  # clock 
    frameN = -1
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    ctrl_image.setImage(control_image)
    sound_1.setSound(control_sound)
    key_resp_3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_3.status = NOT_STARTED
    # keep track of which components have finished
    controlComponents = []
    controlComponents.append(ctrl_image)
    controlComponents.append(sound_1)
    controlComponents.append(key_resp_3)
    for thisComponent in controlComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "control"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = controlClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ctrl_image* updates
        if t >= 0.0 and ctrl_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            ctrl_image.tStart = t  # underestimates by a little under one frame
            ctrl_image.frameNStart = frameN  # exact frame index
            ctrl_image.setAutoDraw(True)
        elif ctrl_image.status == STARTED and t >= (0.0 + 5):
            ctrl_image.setAutoDraw(False)
        # start/stop sound_1
        if t >= 0 and sound_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_1.tStart = t  # underestimates by a little under one frame
            sound_1.frameNStart = frameN  # exact frame index
            sound_1.play()  # start the sound (it finishes automatically)
        elif sound_1.status == STARTED and t >= (0 + 5):
            sound_1.stop()  # stop the sound (if longer than duration)
        
        # *key_resp_3* updates
        if t >= 0 and key_resp_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_3.tStart = t  # underestimates by a little under one frame
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            key_resp_3.clock.reset()  # now t=0
            event.clearEvents()
            theseKeys=[]
            if LUMINA==1:
                lumina_dev.clear_response_queue()
        elif key_resp_3.status == STARTED and t >= (0 + 5):
            key_resp_3.status = STOPPED
        if key_resp_3.status == STARTED:
            # check for a LUMINA_TRIGGER from the Lumina box
            if LUMINA == 1:
                theseKeys=[]
                lumina_dev.poll_for_response()
                while lumina_dev.response_queue_size() > 0:
                    response = lumina_dev.get_next_response() 
                    if response["pressed"]:
                        print "Lumina received: %s, %d"%(response["key"],response["key"])
                        if response["key"] in [0,1,2]: 
                            theseKeys.append(str(response["key"]+1))
            else:
                theseKeys = event.getKeys(keyList=['y', 'n'])
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_3.keys = theseKeys[-1]  # just the last key pressed
                key_resp_3.rt = key_resp_3.clock.getTime()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in controlComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "control"-------
    for thisComponent in controlComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if len(key_resp_3.keys) == 0:  # No response was made
       key_resp_3.keys=None
    # store data for trials (TrialHandler)
    trials.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        trials.addData('key_resp_3.rt', key_resp_3.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# set up handler to look after randomisation of conditions etc
trials_4 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('moral_dilemma_targets_2.csv'),
    seed=None, name='trials_4')
thisExp.addLoop(trials_4)  # add the loop to the experiment
thisTrial_4 = trials_4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial_4.rgb)
if thisTrial_4 != None:
    for paramName in thisTrial_4.keys():
        exec(paramName + '= thisTrial_4.' + paramName)

for thisTrial_4 in trials_4:
    currentLoop = trials_4
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
    if thisTrial_4 != None:
        for paramName in thisTrial_4.keys():
            exec(paramName + '= thisTrial_4.' + paramName)
    
    #------Prepare to start Routine "dilemma"-------
    t = 0
    dilemmaClock.reset()  # clock 
    frameN = -1
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    dil_image.setImage(dilemma_image)
    sound_2.setSound(dilemma_sound)
    key_resp_4 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_4.status = NOT_STARTED
    # keep track of which components have finished
    dilemmaComponents = []
    dilemmaComponents.append(dil_image)
    dilemmaComponents.append(sound_2)
    dilemmaComponents.append(key_resp_4)
    for thisComponent in dilemmaComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "dilemma"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = dilemmaClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *dil_image* updates
        if t >= 0.0 and dil_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            dil_image.tStart = t  # underestimates by a little under one frame
            dil_image.frameNStart = frameN  # exact frame index
            dil_image.setAutoDraw(True)
        elif dil_image.status == STARTED and t >= (0.0 + 5):
            dil_image.setAutoDraw(False)
        # start/stop sound_2
        if t >= 0 and sound_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_2.tStart = t  # underestimates by a little under one frame
            sound_2.frameNStart = frameN  # exact frame index
            sound_2.play()  # start the sound (it finishes automatically)
        elif sound_2.status == STARTED and t >= (0 + 5):
            sound_2.stop()  # stop the sound (if longer than duration)
        
        # *key_resp_4* updates
        if t >= 0 and key_resp_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_4.tStart = t  # underestimates by a little under one frame
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            key_resp_4.clock.reset()  # now t=0
            event.clearEvents()
            theseKeys=[]
            if LUMINA==1:
                lumina_dev.clear_response_queue()
        elif key_resp_4.status == STARTED and t >= (0 + 5):
            key_resp_4.status = STOPPED
        if key_resp_4.status == STARTED:
            # check for a LUMINA_TRIGGER from the Lumina box
            if LUMINA == 1:
                theseKeys=[]
                lumina_dev.poll_for_response()
                while lumina_dev.response_queue_size() > 0:
                    response = lumina_dev.get_next_response() 
                    if response["pressed"]:
                        print "Lumina received: %s, %d"%(response["key"],response["key"])
                        if response["key"] in [0,1,2]: 
                            theseKeys.append(str(response["key"]+1))
            else:
                theseKeys = event.getKeys(keyList=['y', 'n'])

            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_4.keys = theseKeys[-1]  # just the last key pressed
                key_resp_4.rt = key_resp_4.clock.getTime()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in dilemmaComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "dilemma"-------
    for thisComponent in dilemmaComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if len(key_resp_4.keys) == 0:  # No response was made
       key_resp_4.keys=None
    # store data for trials_4 (TrialHandler)
    trials_4.addData('key_resp_4.keys',key_resp_4.keys)
    if key_resp_4.keys != None:  # we had a response
        trials_4.addData('key_resp_4.rt', key_resp_4.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_4'


# set up handler to look after randomisation of conditions etc
trials_5 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('moral_dilemma_targets_3.csv'),
    seed=None, name='trials_5')
thisExp.addLoop(trials_5)  # add the loop to the experiment
thisTrial_5 = trials_5.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial_5.rgb)
if thisTrial_5 != None:
    for paramName in thisTrial_5.keys():
        exec(paramName + '= thisTrial_5.' + paramName)

for thisTrial_5 in trials_5:
    currentLoop = trials_5
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
    if thisTrial_5 != None:
        for paramName in thisTrial_5.keys():
            exec(paramName + '= thisTrial_5.' + paramName)
    
    #------Prepare to start Routine "control"-------
    t = 0
    controlClock.reset()  # clock 
    frameN = -1
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    ctrl_image.setImage(control_image)
    sound_1.setSound(control_sound)
    key_resp_3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_3.status = NOT_STARTED
    # keep track of which components have finished
    controlComponents = []
    controlComponents.append(ctrl_image)
    controlComponents.append(sound_1)
    controlComponents.append(key_resp_3)
    for thisComponent in controlComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "control"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = controlClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ctrl_image* updates
        if t >= 0.0 and ctrl_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            ctrl_image.tStart = t  # underestimates by a little under one frame
            ctrl_image.frameNStart = frameN  # exact frame index
            ctrl_image.setAutoDraw(True)
        elif ctrl_image.status == STARTED and t >= (0.0 + 5):
            ctrl_image.setAutoDraw(False)
        # start/stop sound_1
        if t >= 0 and sound_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_1.tStart = t  # underestimates by a little under one frame
            sound_1.frameNStart = frameN  # exact frame index
            sound_1.play()  # start the sound (it finishes automatically)
        elif sound_1.status == STARTED and t >= (0 + 5):
            sound_1.stop()  # stop the sound (if longer than duration)
        
        # *key_resp_3* updates
        if t >= 0 and key_resp_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_3.tStart = t  # underestimates by a little under one frame
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            key_resp_3.clock.reset()  # now t=0
            event.clearEvents()
            theseKeys=[]
            if LUMINA==1:
                lumina_dev.clear_response_queue()
        elif key_resp_3.status == STARTED and t >= (0 + 5):
            key_resp_3.status = STOPPED
        if key_resp_3.status == STARTED:
            # check for a LUMINA_TRIGGER from the Lumina box
            if LUMINA == 1:
                theseKeys=[]
                lumina_dev.poll_for_response()
                while lumina_dev.response_queue_size() > 0:
                    response = lumina_dev.get_next_response() 
                    if response["pressed"]:
                        print "Lumina received: %s, %d"%(response["key"],response["key"])
                        if response["key"] in [0,1,2]: 
                            theseKeys.append(str(response["key"]+1))
            else:
                theseKeys = event.getKeys(keyList=['y', 'n'])

            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_3.keys = theseKeys[-1]  # just the last key pressed
                key_resp_3.rt = key_resp_3.clock.getTime()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in controlComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "control"-------
    for thisComponent in controlComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if len(key_resp_3.keys) == 0:  # No response was made
       key_resp_3.keys=None
    # store data for trials_5 (TrialHandler)
    trials_5.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        trials_5.addData('key_resp_3.rt', key_resp_3.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_5'


# set up handler to look after randomisation of conditions etc
trials_6 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('moral_dilemma_targets_3.csv'),
    seed=None, name='trials_6')
thisExp.addLoop(trials_6)  # add the loop to the experiment
thisTrial_6 = trials_6.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial_6.rgb)
if thisTrial_6 != None:
    for paramName in thisTrial_6.keys():
        exec(paramName + '= thisTrial_6.' + paramName)

for thisTrial_6 in trials_6:
    currentLoop = trials_6
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_6.rgb)
    if thisTrial_6 != None:
        for paramName in thisTrial_6.keys():
            exec(paramName + '= thisTrial_6.' + paramName)
    
    #------Prepare to start Routine "dilemma"-------
    t = 0
    dilemmaClock.reset()  # clock 
    frameN = -1
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    dil_image.setImage(dilemma_image)
    sound_2.setSound(dilemma_sound)
    key_resp_4 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_4.status = NOT_STARTED
    # keep track of which components have finished
    dilemmaComponents = []
    dilemmaComponents.append(dil_image)
    dilemmaComponents.append(sound_2)
    dilemmaComponents.append(key_resp_4)
    for thisComponent in dilemmaComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "dilemma"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = dilemmaClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *dil_image* updates
        if t >= 0.0 and dil_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            dil_image.tStart = t  # underestimates by a little under one frame
            dil_image.frameNStart = frameN  # exact frame index
            dil_image.setAutoDraw(True)
        elif dil_image.status == STARTED and t >= (0.0 + 5):
            dil_image.setAutoDraw(False)
        # start/stop sound_2
        if t >= 0 and sound_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_2.tStart = t  # underestimates by a little under one frame
            sound_2.frameNStart = frameN  # exact frame index
            sound_2.play()  # start the sound (it finishes automatically)
        elif sound_2.status == STARTED and t >= (0 + 5):
            sound_2.stop()  # stop the sound (if longer than duration)
        
        # *key_resp_4* updates
        if t >= 0 and key_resp_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_4.tStart = t  # underestimates by a little under one frame
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            key_resp_4.clock.reset()  # now t=0
            event.clearEvents()
            theseKeys=[]
            if LUMINA==1:
                lumina_dev.clear_response_queue()
        elif key_resp_4.status == STARTED and t >= (0 + 5):
            key_resp_4.status = STOPPED
        if key_resp_4.status == STARTED:
            # check for a LUMINA_TRIGGER from the Lumina box
            if LUMINA == 1:
                theseKeys=[]
                lumina_dev.poll_for_response()
                while lumina_dev.response_queue_size() > 0:
                    response = lumina_dev.get_next_response() 
                    if response["pressed"]:
                        print "Lumina received: %s, %d"%(response["key"],response["key"])
                        if response["key"] in [0,1,2]: 
                            theseKeys.append(str(response["key"]+1))
            else:
                theseKeys = event.getKeys(keyList=['y', 'n'])

            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_4.keys = theseKeys[-1]  # just the last key pressed
                key_resp_4.rt = key_resp_4.clock.getTime()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in dilemmaComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "dilemma"-------
    for thisComponent in dilemmaComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if len(key_resp_4.keys) == 0:  # No response was made
       key_resp_4.keys=None
    # store data for trials_6 (TrialHandler)
    trials_6.addData('key_resp_4.keys',key_resp_4.keys)
    if key_resp_4.keys != None:  # we had a response
        trials_6.addData('key_resp_4.rt', key_resp_4.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_6'


# set up handler to look after randomisation of conditions etc
trials_7 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('moral_dilemma_targets_4.csv'),
    seed=None, name='trials_7')
thisExp.addLoop(trials_7)  # add the loop to the experiment
thisTrial_7 = trials_7.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial_7.rgb)
if thisTrial_7 != None:
    for paramName in thisTrial_7.keys():
        exec(paramName + '= thisTrial_7.' + paramName)

for thisTrial_7 in trials_7:
    currentLoop = trials_7
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_7.rgb)
    if thisTrial_7 != None:
        for paramName in thisTrial_7.keys():
            exec(paramName + '= thisTrial_7.' + paramName)
    
    #------Prepare to start Routine "control"-------
    t = 0
    controlClock.reset()  # clock 
    frameN = -1
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    ctrl_image.setImage(control_image)
    sound_1.setSound(control_sound)
    key_resp_3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_3.status = NOT_STARTED
    # keep track of which components have finished
    controlComponents = []
    controlComponents.append(ctrl_image)
    controlComponents.append(sound_1)
    controlComponents.append(key_resp_3)
    for thisComponent in controlComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "control"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = controlClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ctrl_image* updates
        if t >= 0.0 and ctrl_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            ctrl_image.tStart = t  # underestimates by a little under one frame
            ctrl_image.frameNStart = frameN  # exact frame index
            ctrl_image.setAutoDraw(True)
        elif ctrl_image.status == STARTED and t >= (0.0 + 5):
            ctrl_image.setAutoDraw(False)
        # start/stop sound_1
        if t >= 0 and sound_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_1.tStart = t  # underestimates by a little under one frame
            sound_1.frameNStart = frameN  # exact frame index
            sound_1.play()  # start the sound (it finishes automatically)
        elif sound_1.status == STARTED and t >= (0 + 5):
            sound_1.stop()  # stop the sound (if longer than duration)
        
        # *key_resp_3* updates
        if t >= 0 and key_resp_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_3.tStart = t  # underestimates by a little under one frame
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            key_resp_3.clock.reset()  # now t=0
            event.clearEvents()
            theseKeys=[]
            if LUMINA==1:
                lumina_dev.clear_response_queue()
        elif key_resp_3.status == STARTED and t >= (0 + 5):
            key_resp_3.status = STOPPED
        if key_resp_3.status == STARTED:
            # check for a LUMINA_TRIGGER from the Lumina box
            if LUMINA == 1:
                theseKeys=[]
                lumina_dev.poll_for_response()
                while lumina_dev.response_queue_size() > 0:
                    response = lumina_dev.get_next_response() 
                    if response["pressed"]:
                        print "Lumina received: %s, %d"%(response["key"],response["key"])
                        if response["key"] in [0,1,2]: 
                            theseKeys.append(str(response["key"]+1))
            else:
                theseKeys = event.getKeys(keyList=['y', 'n'])

            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_3.keys = theseKeys[-1]  # just the last key pressed
                key_resp_3.rt = key_resp_3.clock.getTime()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in controlComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "control"-------
    for thisComponent in controlComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if len(key_resp_3.keys) == 0:  # No response was made
       key_resp_3.keys=None
    # store data for trials_7 (TrialHandler)
    trials_7.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        trials_7.addData('key_resp_3.rt', key_resp_3.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_7'


# set up handler to look after randomisation of conditions etc
trials_8 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('moral_dilemma_targets_4.csv'),
    seed=None, name='trials_8')
thisExp.addLoop(trials_8)  # add the loop to the experiment
thisTrial_8 = trials_8.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial_8.rgb)
if thisTrial_8 != None:
    for paramName in thisTrial_8.keys():
        exec(paramName + '= thisTrial_8.' + paramName)

for thisTrial_8 in trials_8:
    currentLoop = trials_8
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_8.rgb)
    if thisTrial_8 != None:
        for paramName in thisTrial_8.keys():
            exec(paramName + '= thisTrial_8.' + paramName)
    
    #------Prepare to start Routine "dilemma"-------
    t = 0
    dilemmaClock.reset()  # clock 
    frameN = -1
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    dil_image.setImage(dilemma_image)
    sound_2.setSound(dilemma_sound)
    key_resp_4 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_4.status = NOT_STARTED
    # keep track of which components have finished
    dilemmaComponents = []
    dilemmaComponents.append(dil_image)
    dilemmaComponents.append(sound_2)
    dilemmaComponents.append(key_resp_4)
    for thisComponent in dilemmaComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "dilemma"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = dilemmaClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *dil_image* updates
        if t >= 0.0 and dil_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            dil_image.tStart = t  # underestimates by a little under one frame
            dil_image.frameNStart = frameN  # exact frame index
            dil_image.setAutoDraw(True)
        elif dil_image.status == STARTED and t >= (0.0 + 5):
            dil_image.setAutoDraw(False)
        # start/stop sound_2
        if t >= 0 and sound_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_2.tStart = t  # underestimates by a little under one frame
            sound_2.frameNStart = frameN  # exact frame index
            sound_2.play()  # start the sound (it finishes automatically)
        elif sound_2.status == STARTED and t >= (0 + 5):
            sound_2.stop()  # stop the sound (if longer than duration)
        
        # *key_resp_4* updates
        if t >= 0 and key_resp_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_4.tStart = t  # underestimates by a little under one frame
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            key_resp_4.clock.reset()  # now t=0
            event.clearEvents()
            theseKeys=[]
            if LUMINA==1:
                lumina_dev.clear_response_queue()
        elif key_resp_4.status == STARTED and t >= (0 + 5):
            key_resp_4.status = STOPPED
        if key_resp_4.status == STARTED:
            # check for a LUMINA_TRIGGER from the Lumina box
            if LUMINA == 1:
                theseKeys=[]
                lumina_dev.poll_for_response()
                while lumina_dev.response_queue_size() > 0:
                    response = lumina_dev.get_next_response() 
                    if response["pressed"]:
                        print "Lumina received: %s, %d"%(response["key"],response["key"])
                        if response["key"] in [0,1,2]: 
                            theseKeys.append(str(response["key"]+1))
            else:
                theseKeys = event.getKeys(keyList=['y', 'n'])

            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_4.keys = theseKeys[-1]  # just the last key pressed
                key_resp_4.rt = key_resp_4.clock.getTime()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in dilemmaComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "dilemma"-------
    for thisComponent in dilemmaComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if len(key_resp_4.keys) == 0:  # No response was made
       key_resp_4.keys=None
    # store data for trials_8 (TrialHandler)
    trials_8.addData('key_resp_4.keys',key_resp_4.keys)
    if key_resp_4.keys != None:  # we had a response
        trials_8.addData('key_resp_4.rt', key_resp_4.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_8'


#------Prepare to start Routine "fixation"-------
t = 0
fixationClock.reset()  # clock 
frameN = -1
routineTimer.add(20.000000)
# update component parameters for each repeat
# keep track of which components have finished
fixationComponents = []
fixationComponents.append(fixation_txt)
for thisComponent in fixationComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "fixation"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = fixationClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fixation_txt* updates
    if t >= 0.0 and fixation_txt.status == NOT_STARTED:
        # keep track of start time/frame for later
        fixation_txt.tStart = t  # underestimates by a little under one frame
        fixation_txt.frameNStart = frameN  # exact frame index
        fixation_txt.setAutoDraw(True)
    elif fixation_txt.status == STARTED and t >= (0.0 + 20):
        fixation_txt.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "fixation"-------
for thisComponent in fixationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "thanks"-------
t = 0
thanksClock.reset()  # clock 
frameN = -1
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
thanksComponents = []
thanksComponents.append(text)
for thisComponent in thanksComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "thanks"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = thanksClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t  # underestimates by a little under one frame
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    elif text.status == STARTED and t >= (0.0 + 5):
        text.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "thanks"-------
for thisComponent in thanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
win.close()
core.quit()
