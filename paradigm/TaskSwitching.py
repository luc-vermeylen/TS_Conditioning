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

# counterbalancing

# randomize the order of the stimuli
for idx, name in enumerate(['lism','lila','nosm','nola']):
    d[name] = np.random.choice(d[name], size = len(d[name]), replace = False)
df = pd.DataFrame(d)

D = pd.DataFrame() # initiatlize final dataframe
for block_i in np.arange(1,5): # block loop
    for phase_i, phase in enumerate(['cued','free']): # phase loop
        # the main design (change the indexing to take different targets each phase/block)
        B = pd.melt(df.iloc[(block_i*10)-10:block_i*10,:], var_name = 'target_type', value_name = 'target_word') # subset + wide -> long
        B['block'] = [block_i]*40
        B['phase'] = [phase]*40
        B['transition'] = (['repetition']*5+['switch']*5)*4  # balanced amount of transitions per target_type
        B['reward'] = (['low']*4 + ['high']*1 + ['high']*4 + ['low']*1)*4 # counterbalance
        B = B.sample(frac=1).reset_index(drop=True) # shuffle the order
        B['trial'] = np.arange(1,41)
        
        size_cues = ['A','E','I','O','U']
        animacy_cues = ['V','F','L','Q','C']
        
        # add the task (animacy or size) based on shuffled (and balanced) transitions
        for idx, r in B.iterrows():
            if idx == 0:
                B.loc[idx,'task'] = np.random.choice(['animacy','size'], size = 1)[0]
            else:
                if B.loc[idx,'transition'] == 'repetition':
                    B.loc[idx,'task'] = B.loc[idx-1,'task']
                else:
                    if B.loc[idx-1,'task'] == 'animacy':
                        B.loc[idx,'task'] = 'size'
                    else:
                        B.loc[idx,'task'] = 'animacy'
        
        # add task cues: can never reappear within three consecutive trials 
        for idx, r in B.iterrows():
            if B.loc[idx,'task'] == 'size':
                random_cue = np.random.choice(size_cues, size = 1)[0]
                if idx == 0: # simply add random cue on first row
                    B.loc[idx,'cue'] = random_cue
                elif idx == 1: # on second row, avoid repetition with previous row
                    while B.loc[idx-1,'cue'] == random_cue:
                        random_cue = np.random.choice(size_cues, size = 1)[0]
                    B.loc[idx,'cue'] = random_cue
                else: # on all other rows, avoid repetition with previous and n-2 row
                    while B.loc[idx-1,'cue'] == random_cue or B.loc[idx-2,'cue'] == random_cue:
                        random_cue = np.random.choice(size_cues, size = 1)[0]
                    B.loc[idx,'cue'] = random_cue
            elif B.loc[idx,'task'] == 'animacy':
                random_cue = np.random.choice(animacy_cues, size = 1)[0]
                if idx == 0:
                    B.loc[idx,'cue'] = random_cue
                elif idx == 1:           
                    while B.loc[idx-1,'cue'] == random_cue:
                        random_cue = np.random.choice(animacy_cues, size = 1)[0]
                    B.loc[idx,'cue'] = random_cue
                else:
                    while B.loc[idx-1,'cue'] == random_cue or B.loc[idx-2,'cue'] == random_cue:
                        random_cue = np.random.choice(animacy_cues, size = 1)[0]
                    B.loc[idx,'cue'] = random_cue
                    
        # append data to another dataframe
        D = D.append(B, ignore_index = True)


#%% Initiate Stimuli

win = visual.Window([800,800], gammaErrorPolicy='warn')
message = visual.TextStim(win, pos = ([1,0]))
message.autoDraw = True

#%% Helper Functions

#%% Block Loop

#%% Trial Loop

data = B
for i in range(0,5):
    message.text = '+'
    win.flip()
    core.wait(.5)
    message.text = B['target_word'][i] 
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
