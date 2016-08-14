#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.77.00), Thu Jan  2 17:47:47 2014
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""
from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import os  # handy system and path functions

# Store info about the experiment session
expName = 'moralD_training'  # from the Builder filename that created this script
expInfo = {}
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Setup files for saving
if not os.path.isdir('../data'):
    os.makedirs('../data')  # if this fails (e.g. permissions) we will get error
filename = '../data' + os.path.sep + '%s' %(expInfo['date'])
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=False, saveWideText=False,
    dataFileName=filename)

# Setup the Window
win = visual.Window(size=(1024, 768), screen=0, fullscr=True, allowGUI=False, allowStencil=False,
                    monitor='testMonitor', color='black', colorSpace='rgb')
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
inst_text1 = visual.TextStim(win=win, ori=0, name='inst_text1',
    text='A series of short stories will be read to you while',    font='Arial',
    pos=[0, 0.385], height=0.1, wrapWidth=2.5,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
inst_text2 = visual.TextStim(win=win, ori=0, name='inst_text2',
    text='you view corresponding illustrations. Please pay',    font='Arial',
    pos=[0, 0.275], height=0.1, wrapWidth=2.5,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
inst_text3 = visual.TextStim(win=win, ori=0, name='inst_text3',
    text=' close attention to the stories and illustrations - you will',    font='Arial',
    pos=[0, 0.165], height=0.1, wrapWidth=2.5,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)
inst_text4 = visual.TextStim(win=win, ori=0, name='inst_text4',
    text='  be asked questions about them during the MRI scan. ',    font='Arial',
    pos=[0, 0.055], height=0.1, wrapWidth=2.5,
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0)
inst_text5 = visual.TextStim(win=win, ori=0, name='inst_text5',
    text='After a story is completed, press the space bar',    font='Arial',
    pos=[0, -0.155], height=0.1, wrapWidth=2.5,
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0)
inst_text6 = visual.TextStim(win=win, ori=0, name='inst_text6',
    text=' to advance to the next one.',    font='Arial',
    pos=[0, -.265], height=0.1, wrapWidth=2.5,
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0)
inst_text7 = visual.TextStim(win=win, ori=0, name='inst_text7',
    text='Press the space bar to continue.',    font='Arial',
    pos=[0, -.485], height=0.1, wrapWidth=2.0,
    color='white', colorSpace='rgb', opacity=1,
    depth=-6.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
story = sound.Sound('A', secs=60)
story.setVolume(1)
illustration = visual.ImageStim(win=win, name='illustration',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1, 1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "finished"
finishedClock = core.Clock()
text = visual.TextStim(win=win, ori=0, name='text',
    text='Thank you for your participation!',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=1.5,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "instructions"-------
t = 0
instructionsClock.reset()  # clock 
frameN = -1
routineTimer.add(60.000000)
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_2.status = NOT_STARTED
# keep track of which components have finished
instructionsComponents = []
instructionsComponents.append(inst_text1)
instructionsComponents.append(inst_text2)
instructionsComponents.append(inst_text3)
instructionsComponents.append(inst_text4)
instructionsComponents.append(inst_text5)
instructionsComponents.append(inst_text6)
instructionsComponents.append(inst_text7)
instructionsComponents.append(key_resp_2)
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instructions"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = instructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *inst_text1* updates
    if t >= 0.0 and inst_text1.status == NOT_STARTED:
        # keep track of start time/frame for later
        inst_text1.tStart = t  # underestimates by a little under one frame
        inst_text1.frameNStart = frameN  # exact frame index
        inst_text1.setAutoDraw(True)
    elif inst_text1.status == STARTED and t >= (0.0 + 60.0):
        inst_text1.setAutoDraw(False)
    
    # *inst_text2* updates
    if t >= 0.0 and inst_text2.status == NOT_STARTED:
        # keep track of start time/frame for later
        inst_text2.tStart = t  # underestimates by a little under one frame
        inst_text2.frameNStart = frameN  # exact frame index
        inst_text2.setAutoDraw(True)
    elif inst_text2.status == STARTED and t >= (0.0 + 60.0):
        inst_text2.setAutoDraw(False)
    
    # *inst_text3* updates
    if t >= 0.0 and inst_text3.status == NOT_STARTED:
        # keep track of start time/frame for later
        inst_text3.tStart = t  # underestimates by a little under one frame
        inst_text3.frameNStart = frameN  # exact frame index
        inst_text3.setAutoDraw(True)
    elif inst_text3.status == STARTED and t >= (0.0 + 60):
        inst_text3.setAutoDraw(False)
    
    # *inst_text4* updates
    if t >= 0.0 and inst_text4.status == NOT_STARTED:
        # keep track of start time/frame for later
        inst_text4.tStart = t  # underestimates by a little under one frame
        inst_text4.frameNStart = frameN  # exact frame index
        inst_text4.setAutoDraw(True)
    elif inst_text4.status == STARTED and t >= (0.0 + 60.0):
        inst_text4.setAutoDraw(False)
    
    # *inst_text5* updates
    if t >= 0.0 and inst_text5.status == NOT_STARTED:
        # keep track of start time/frame for later
        inst_text5.tStart = t  # underestimates by a little under one frame
        inst_text5.frameNStart = frameN  # exact frame index
        inst_text5.setAutoDraw(True)
    elif inst_text5.status == STARTED and t >= (0.0 + 60):
        inst_text5.setAutoDraw(False)
    
    # *inst_text6* updates
    if t >= 0.0 and inst_text6.status == NOT_STARTED:
        # keep track of start time/frame for later
        inst_text6.tStart = t  # underestimates by a little under one frame
        inst_text6.frameNStart = frameN  # exact frame index
        inst_text6.setAutoDraw(True)
    elif inst_text6.status == STARTED and t >= (0.0 + 60.0):
        inst_text6.setAutoDraw(False)
    
    # *inst_text7* updates
    if t >= 0.0 and inst_text7.status == NOT_STARTED:
        # keep track of start time/frame for later
        inst_text7.tStart = t  # underestimates by a little under one frame
        inst_text7.frameNStart = frameN  # exact frame index
        inst_text7.setAutoDraw(True)
    elif inst_text7.status == STARTED and t >= (0.0 + 60):
        inst_text7.setAutoDraw(False)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t  # underestimates by a little under one frame
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        key_resp_2.clock.reset()  # now t=0
        event.clearEvents()
    elif key_resp_2.status == STARTED and t >= (0.0 + 60.0):
        key_resp_2.status = STOPPED
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_2.keys = theseKeys[-1]  # just the last key pressed
            key_resp_2.rt = key_resp_2.clock.getTime()
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

#-------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='fullRandom', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('training_stim_list.csv'),
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
    
    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    story.setSound(audio)
    illustration.setImage(image)
    press_space_bar = event.BuilderKeyResponse()  # create an object of type KeyResponse
    press_space_bar.status = NOT_STARTED
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(story)
    trialComponents.append(illustration)
    trialComponents.append(press_space_bar)
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop story
        if t >= 0.0 and story.status == NOT_STARTED:
            # keep track of start time/frame for later
            story.tStart = t  # underestimates by a little under one frame
            story.frameNStart = frameN  # exact frame index
            story.play()  # start the sound (it finishes automatically)
        elif story.status == STARTED and t >= (0.0 + 60):
            story.stop()  # stop the sound (if longer than duration)
        
        # *illustration* updates
        if t >= 0.0 and illustration.status == NOT_STARTED:
            # keep track of start time/frame for later
            illustration.tStart = t  # underestimates by a little under one frame
            illustration.frameNStart = frameN  # exact frame index
            illustration.setAutoDraw(True)
        elif illustration.status == STARTED and t >= (0.0 + 60):
            illustration.setAutoDraw(False)
        
        # *press_space_bar* updates
        if t >= float(duration) and press_space_bar.status == NOT_STARTED:
            # keep track of start time/frame for later
            press_space_bar.tStart = t  # underestimates by a little under one frame
            press_space_bar.frameNStart = frameN  # exact frame index
            press_space_bar.status = STARTED
            # keyboard checking is just starting
            press_space_bar.clock.reset()  # now t=0
            event.clearEvents()
        elif press_space_bar.status == STARTED and t >= (float(duration) + 60.0-float(duration)):
            press_space_bar.status = STOPPED
        if press_space_bar.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            if len(theseKeys) > 0:  # at least one key was pressed
                press_space_bar.keys = theseKeys[-1]  # just the last key pressed
                press_space_bar.rt = press_space_bar.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
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
    
    #-------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if len(press_space_bar.keys) == 0:  # No response was made
       press_space_bar.keys=None
    # store data for trials (TrialHandler)
    trials.addData('press_space_bar.keys',press_space_bar.keys)
    if press_space_bar.keys != None:  # we had a response
        trials.addData('press_space_bar.rt', press_space_bar.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


#------Prepare to start Routine "finished"-------
t = 0
finishedClock.reset()  # clock 
frameN = -1
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
finishedComponents = []
finishedComponents.append(text)
for thisComponent in finishedComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "finished"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = finishedClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t  # underestimates by a little under one frame
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    elif text.status == STARTED and t >= (0.0 + 5.0):
        text.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in finishedComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "finished"-------
for thisComponent in finishedComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
win.close()
core.quit()
