# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 11:58:20 2019

@author: luc
"""

#%% Import Libraries

from psychopy import visual, core, event
import numpy as np
import pandas as pd
from stimuli.stimuli_dictionary import stimuli

#%% Randomization
d = stimuli

# test on local pc


# randomize the order of the stimuli
for idx, name in enumerate(['lism','lila','nosm','nola']):
    d[name] = np.random.choice(d[name], size = len(d[name]), replace = False)

df = pd.DataFrame(d)

block1 = df.iloc[0:10,:]
block1 = pd.melt(block1, var_name = 'target_type', value_name = 'target_word')
transition = (['repetition']*5+['switch']*5)*4
reward = (['low']*4 + ['high']*1 + ['high']*4 + ['low']*1)*4
block1['transition'] = transition
block1['reward'] = reward
block1 = block1.sample(frac=1).reset_index(drop=True)


for idx, r in block1.iterrows():
    if idx == 0:
        block1.loc[idx,'task'] = np.random.choice(['animacy','size'], size = 1)[0]
    else:
        if block1.loc[idx,'transition'] == 'repetition':
            block1.loc[idx,'task'] = block1.loc[idx-1,'task']
        else:
            if block1.loc[idx-1,'task'] == 'animacy':
                block1.loc[idx,'task'] = 'size'
            else:
                block1.loc[idx,'task'] = 'animacy'
block1['task'][block1['task'] == 'size'].count()


# add non repeating cues (a cue cannot be repeated until N-3)
cues = (['A','E','I','O','U'] + ['V','F','L','Q','C'] )*4

# remove repetitions in cues !!! + you could do this step in the previous one
for idx, r in block1.iterrows():
    if block1.loc[idx,'task'] == 'size':
        random_cue = np.random.choice(['A','E','I','O','U'], size = 1)[0]
        block1.loc[idx,'cue'] = np.random.choice(['A','E','I','O','U'], size = 1)[0]
        if idx > 0:
            while block1.loc[idx-1,'cue'] == random_cue:
                random_cue = np.random.choice(['A','E','I','O','U'], size = 1)[0]
                block1.loc[idx,'cue'] = np.random.choice(['A','E','I','O','U'], size = 1)[0]
    else:
        random_cue = np.random.choice(['V','F','L','Q','C'], size = 1)[0]
        block1.loc[idx,'cue'] = np.random.choice(['V','F','L','Q','C'], size = 1)[0]
        if idx > 0: 
            while block1.loc[idx-1,'cue'] == random_cue:
                random_cue = np.random.choice(['V','F','L','Q','C'], size = 1)[0]
                block1.loc[idx,'cue'] = np.random.choice(['V','F','L','Q','C'], size = 1)[0]
        
    



#%% Initiate Stimuli

win = visual.Window([800,800], gammaErrorPolicy='warn')
message = visual.TextStim(win, pos = ([1,0]))
message.autoDraw = True

#%% Helper Functions

#%% Block Loop

#%% Trial Loop

data = block1
for i in range(0,5):
    message.text = '+'
    win.flip()
    core.wait(.5)
    message.text = block1['target_word'][i] 
    win.flip()
    C = core.Clock()
    C.reset()
    resp = event.waitKeys(maxWait = 10, keyList = ['left','right'], timeStamped=C, clearEvents = True);
    data.loc[i,'response'] = resp[0][0]
    data.loc[i,'rt'] = resp[0][1]
    data.loc[[i]].to_csv('data/test.csv', mode = 'a', header = False)
    
#%% Exectute

#%% Close

win.close()
core.quit()