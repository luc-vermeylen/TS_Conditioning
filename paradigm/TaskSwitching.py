# -*- coding: utf-8 -*-
"""
Conditioning Task Switching Paradigm

Build to work with:
Python 3.6
Psychopy 3.2.3

@author: Luc Vermeylen, Department of Experimental Psychology, Ghent University
"""

#%% Import Libraries

from psychopy import visual, core, event, gui
import pandas as pd
from datetime import datetime
from randomization import randomize

#%% Variables

# Dialogue box
info = {'ID': '999'} # add age/gender questions after experiment!
dlg = gui.DlgFromDict(dictionary = info, title = 'Experiment', order = ['ID'], show = True)
if not dlg.OK: core.quit();
if info['ID'] == '': core.quit();

# Stimulus list and randomization
data = randomize(int(info['ID']))[0]
free_keys = randomize(int(info['ID']))[1]

# Initialize data file
filename = "data/cTSdata_" + info['ID'].zfill(3) + "_{}.csv".format(datetime.now().strftime("%Y%m%d-%H%M%S"))
header = pd.DataFrame([data.columns])
header.to_csv(filename, mode = 'a', header = False, index = False)

# Global keys
event.globalKeys.clear()
event.globalKeys.add(key='escape', func=core.quit, name='shutdown')

# Timing
FIX = .5
CUE = 1
STIM = 5
BLANK = .5
FB = .5
ITI = 1

# Initialize stimuli
win = visual.Window([1200,800], units="norm", gammaErrorPolicy='ignore')
instr = visual.TextStim(win = win, text = '', height = .05, wrapWidth = 1.75, font = 'monospace')
ufix = visual.TextStim(win = win, text = '+', pos = [0, .05]) # upper fixation (5% o/t distance center - top)
lfix = visual.TextStim(win = win, text = '+', pos = [0, -.05]) # lower fixation (5% o/t distance center - bottom)
cue = visual.TextStim(win = win, pos = [0, .05])
target = visual.TextStim(win = win, pos = [0, -.05])
blank = visual.TextStim(win = win, text = '')
fb = visual.TextStim(win = win)

#%% Experimental Trialss

for i in range(data.shape[0]):  
    
    # Fixation
    ufix.draw(); lfix.draw(); win.flip(); core.wait(FIX)
    resp = event.waitKeys(maxWait = FIX, keyList = ['p'], clearEvents = True);
    fix_key = resp[0][0] if resp else None
    if fix_key == 'p': 
        i = i + 16
        continue
    
    # Cue
    cue.text = data['cue'][i]
    cue.draw(); lfix.draw(); win.flip(); core.wait(CUE)
    
    # Target
    target.text = data['target'][i] 
    cue.draw(); target.draw(); win.flip()
    
    # Collect Response
    C = core.Clock(); C.reset()
    keys = ['g', 'h'] if data.loc[i,'phase'] == 'cued' or data.loc[i,'phase'] == 'prac_cued' else ['s','d','k','l']
    resp = event.waitKeys(maxWait = STIM, keyList = keys, timeStamped=C, clearEvents = True);
    
    # Determine correct response
    if resp:
        resp_key = resp[0][0]; resp_rt = resp[0][1]
        if data.loc[i,'phase'] == 'cued' or data.loc[i,'phase'] == 'prac_cued':
            correct = 1 if resp_key == data.loc[i,'cresp'] else 0
        elif data.loc[i,'phase'] == 'free' or data.loc[i,'phase'] == 'prac_free':
            if resp_key == free_keys['parity']['left'] or resp_key == free_keys['parity']['right']:
                data.loc[i,'task'] = 'parity'
                if data.loc[i,'target_type'] == 'smod' or data.loc[i,'target_type'] == 'laod':
                    data.loc[i,'cresp'] = free_keys['parity']['left']
                else:
                    data.loc[i,'cresp'] = free_keys['parity']['right'] 
            elif resp_key == free_keys['nsize']['left'] or resp_key == free_keys['nsize']['right']:
                data.loc[i,'task'] = 'nsize'
                if data.loc[i,'target_type'] == 'smod' or data.loc[i,'target_type'] == 'smev':
                    data.loc[i,'cresp'] = free_keys['nsize']['left']
                else:
                    data.loc[i,'cresp'] = free_keys['nsize']['right'] 
            correct = 1 if resp_key == data.loc[i,'cresp'] else 0
    else:
        resp_key = None; resp_rt = None; correct = 0
    data.loc[i,'resp'] = resp_key; data.loc[i,'rt'] = resp_rt; data.loc[i,'correct'] = correct;
        
    # Determine transition if free phase
    if data.loc[i,'phase'] == 'free' or data.loc[i,'phase'] == 'prac_free':
        if data.loc[i,'trial'] == 1:
            data.loc[i,'transition'] = None
        else:
            if data.loc[i,'task'] == data.loc[i-1,'task']:
                data.loc[i,'transition'] = 'repetition'
            elif data.loc[i, 'task'] != data.loc[i-1, 'task']:
                data.loc[i,'transition'] = 'switch'
            elif data.loc[i-1,'task'] == None:
                data.loc[i,'transition']= None
    
    # Blank 
    blank.draw(); win.flip(); core.wait(BLANK)
    
    # Feedback (if correct or training)
    fb_text = '+01' if data['reward'][i] == 'low' else '+10'
    fb.text = fb_text if correct == 1 else ''
    fb.draw(); win.flip(); core.wait(FB)
    
    # ITI
    blank.draw(); win.flip(); core.wait(ITI)
    
    # Block Feedback
    
    
    # Append data to file
    data.loc[[i]].to_csv(filename, mode = 'a', header = False, index = False)
    
#%% Close

win.close()
core.quit()