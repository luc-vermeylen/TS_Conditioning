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
import numpy as np
import pandas as pd
from datetime import datetime
from randomization import randomize
from quest import questionnaire
from instruction_text import introduction, cued_prac_instructions, free_prac_instructions, cued_instructions, free_instructions, review_instructions

#%% Variables

# this will speed up trial presentation and show trial information on screen (ps. skip blocks by pressing 'backspace' on target)
debugging = False

# Dialogue box
info = {'ID': '999', 'Leeftijd': '', 'Geslacht': ['V','M','X'], 'Handvoorkeur': ['Rechts','Geen','Links']}
dlg = gui.DlgFromDict(dictionary = info, title = 'Experiment Setup', order = ['ID', 'Leeftijd', 'Geslacht', 'Handvoorkeur'])
if not dlg.OK: core.quit();
if info['ID'] == '': core.quit();

# Stimulus list and randomization
data, free_keys, CB = randomize(int(info['ID']), info['Leeftijd'],info['Geslacht'],info['Handvoorkeur'])

# Initialize data file
filename = "data/cTSdata_" + info['ID'].zfill(3) + "_{}.csv".format(datetime.now().strftime("%Y%m%d-%H%M%S"))
header = pd.DataFrame([data.columns])
header.to_csv(filename, mode = 'a', header = False, index = False)

# Global keys and clock
#event.globalKeys.clear()
#event.globalKeys.add(key='escape', func=core.quit, name='shutdown')
globalClock = core.Clock(); globalClock.reset()

# Timing
if debugging:
    FIX = 0; CUE = 0; STIM = 10; BLANK = 0; FB = .2; ITI = 0; BLOCKFB = 20
else:
    FIX = .5; CUE = 1; STIM = 5; BLANK = .5; FB = .5; ITI = 1; BLOCKFB = 120

# Initialize stimuli
win = visual.Window(fullscr = True, units="norm")
instr = visual.TextStim(win = win, text = '', height = .05, wrapWidth = 1.75, font = 'monospace')
ufix = visual.TextStim(win = win, text = '+', pos = [0, .05]) # upper fixation (5% o/t distance center - top)
lfix = visual.TextStim(win = win, text = '+', pos = [0, -.05]) # lower fixation (5% o/t distance center - bottom)
cue = visual.TextStim(win = win, pos = [0, .05])
target = visual.TextStim(win = win, pos = [0, -.05])
blank = visual.TextStim(win = win, text = '')
fb = visual.TextStim(win = win, text = '')
block_fb = visual.TextStim(win = win, text = '', height = .05, wrapWidth = 1.75, font = 'monospace')
debug_prevTrial = visual.TextStim(win = win, text = '', pos = [-.7,0], height = .05, wrapWidth = 1.75, font = 'monospace')
debug_thisTrial = visual.TextStim(win = win, text = '', pos = [.7,0], height = .05, wrapWidth = 1.75, font = 'monospace')
debug_respMap = visual.TextStim(win = win, text = 'Free phase response keys:\n' + str(free_keys),pos = [0,.7], height = .05, wrapWidth = 1.75, font = 'monospace')
debug_instr = visual.TextStim(win = win, text = 'Press "backspace" to skip a block, press "esc" to quit.',pos = [0,-.7], height = .05, wrapWidth = 1.75, font = 'monospace')

#%% Instructions
    
if CB['cue_size'] == 'vowel':
    size = 'klinker'
    animacy = 'medeklinker'
elif CB['cue_size'] == 'consonant':
    size = 'medeklinker'
    animacy = 'klinker'
    
introduction(win,size,animacy,free_keys)
    
#%% Experimental Trials

for block in np.arange(1,7):
    for phase_i, phase in enumerate(['prac_cued', 'prac_free', 'cued', 'free']):
        if block > 1:
            if phase == 'prac_cued' or phase == 'prac_free': continue
        if phase == 'prac_cued' or phase == 'prac_free':
            ntrials = 16
        else:
            ntrials = 40
        for trial in np.arange(1,ntrials+1):
            
            # instructions
            if trial == 1 and phase == 'prac_cued':
                cued_prac_instructions(win,size,animacy,free_keys)
            elif trial == 1 and phase == 'prac_free':
                free_prac_instructions(win,size,animacy,free_keys)
            elif trial == 1 and phase == 'cued':
                if block == 1:
                    review_instructions(win,size,animacy,free_keys)
                    cued_instructions(win,size,animacy,free_keys)
                else:
                    cued_instructions(win,size,animacy,free_keys)
            elif trial == 1 and phase == 'free':
                free_instructions(win,size,animacy,free_keys)
            
            # set correct index
            i = data[(data['block'] == block) & (data['phase'] == phase) & (data['trial'] == trial)].index.tolist()[0]
            
            # Fixation
            ufix.draw(); lfix.draw(); win.flip(); core.wait(FIX)
            
            # Cue
            cue.text = data['cue'][i]
            cue.draw(); lfix.draw(); win.flip(); core.wait(CUE)
            
            # Target
            if debugging: 
                debug_respMap.draw(); debug_instr.draw()
                debug_thisTrial.text = 'CURRENT TRIAL:\n\n' + data.loc[i].to_string()
                debug_thisTrial.draw()
                if i > 0: debug_prevTrial.text = 'PREVIOUS TRIAL:\n\n' + data.loc[i-1].to_string(); debug_prevTrial.draw()
            target.text = data['target'][i] 
            cue.draw(); target.draw(); win.flip()
            
            # Collect Response
            C = core.Clock(); C.reset()
            keys = ['g', 'h', 'backspace', 'escape'] if data.loc[i,'phase'] == 'cued' or data.loc[i,'phase'] == 'prac_cued' else ['s','d','k','l','backspace','escape']
            resp = event.waitKeys(maxWait = STIM, keyList = keys, timeStamped=C);
            
            # Determine correct response
            if resp:
                resp_key = resp[0][0]; resp_rt = resp[0][1]
                if resp_key == 'backspace': break
                if resp_key == 'escape': win.close(); core.quit()
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
            data.loc[i,'time_elapsed'] = globalClock.getTime()
                
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
            if data.loc[i,'phase'] == 'prac_cued' or data.loc[i,'phase'] == 'prac_free':
                fb_text = 'FOUT!' if correct == 0 else ''
            elif data.loc[i,'phase'] == 'cued':
                if correct: 
                    fb_text = '+01' if data['reward'][i] == 'low' else '+10'
                    data.loc[i,'points'] = 1 if data['reward'][i] == 'low' else 10
                else:
                    fb_text = ''
            elif data.loc[i,'phase'] == 'free': 
                fb_text = ''
            fb.text = fb_text
            fb.draw(); win.flip(); core.wait(FB)
            
            # ITI
            blank.draw(); win.flip(); core.wait(ITI)
            
            # Append data to file
            data.loc[[i]].to_csv(filename, mode = 'a', header = False, index = False)
            
        # Block Feedback (per phase/block combination and thus outside trial loop)
        fb_data = data[(data['block'] == block) & (data['phase'] == phase) & (data['trial'] < trial)]
        nTrials = len(fb_data['correct'])
        nPoints = fb_data['points'].sum() 
        nCorrect = fb_data['correct'].sum()
        nErrors = nTrials - nCorrect
        if phase == 'cued':
            block_fb.text = '''Nu kan je even pauzeren.\n
Je hebt in het verlopen blok {} fout(en) gemaakt.\n
Je hebt in het verlopen blok {} punten verdiend.\n
Duw op spatie om naar het volgende blok te gaan.
'''.format(str(nErrors),str(nPoints))             
        else: 
            block_fb.text = '''Nu kan je even pauzeren.\n
Je hebt in het verlopen blok {} fout(en) gemaakt.\n
Duw op spatie om naar het volgende blok te gaan.
'''.format(str(nErrors))  
        block_fb.draw(); win.flip();
        event.waitKeys(maxWait = BLOCKFB, keyList = ['space'])
        
#%% Questionnaires     

q1, q2 = questionnaire(win, testing = False)
data.loc[i+1,'Q1'] = q1; data.loc[i+1,'Q2'] = q2
data.loc[[i+1]].to_csv(filename, mode = 'a', header = False, index = False)

#%% End Message

end = visual.TextStim(win = win, text = '', pos = [0,0], height = .075, wrapWidth = 1.5, font = 'monospace')
end.text = 'Bedankt voor je deelname!\n\nDit is het einde van het experiment.\nNeem contact op met de proefleider.'
end.draw(); win.flip()
event.waitKeys()
        
#%% Close

win.close()
core.quit()