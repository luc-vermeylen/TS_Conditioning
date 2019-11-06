# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 15:33:50 2019

@author: luc
"""


#%% Import Libraries

import numpy as np
import pandas as pd
import itertools
from stimuli.stimuli_dictionary import stimuli, practice

#%% Set Variables

d = stimuli
d2 = stim2
p = practice
p2 = practice2

ID = 1

nBlocks = 4 
NPhase = 2
nTrials = 40

#%% Custom functions


#%% Counterbalancing

# counterbalancing factors
cue_size = ['vowel','consonant']  # for cued trials only
reward_group = ['repeat','switch'] # in cued trials
rhand_odd = ['left','right'] # response hand: for free trials only

keys = ['cue_size', 'reward_group', 'rhand_odd']

# cartesian product -> take modulus of subj ID divided by N combinations
counterbalancing = [dict(zip(keys,combination)) for combination in itertools.product(cue_size,reward_group,rhand_odd)]
counterbalancing = counterbalancing[ID%8] 

# dictionary to retrieve the mapping from the current counterbalancing later on
if counterbalancing['cue_size'] == 'vowel':
    cues = {'size': ['A','E','I','O','U'], 'animacy': ['V','F','L','Q','C']}
else:
    cues = {'size': ['V','F','L','Q','C'], 'animacy': ['A','E','I','O','U']}
    
if counterbalancing['rhand_odd'] == 'left':
    keys = {'size': {'left': 's', 'right': 'd'}, 'animacy': {'left': 'k', 'right': 'l'}}
else:
    keys = {'size': {'left': 'k', 'right': 'l'}, 'animacy': {'left': 's', 'right': 'd'}}

#%% Generate the main stimulus list 

# (!!! half the current stimulus list controlling for word length and freq)

for idx, name in enumerate(['lism','lila','nosm','nola']):
    d[name] = np.random.choice(d[name], size = len(d[name]), replace = False)
wide_stimList = pd.DataFrame(d)
wide_stim2List = pd.DataFrame(d2)
wide_stim3List = pd.DataFrame(p)
wide_stim4List = pd.DataFrame(p2)

# main loop across all blocks, phases and trials
D = pd.DataFrame() # initiatlize final dataframe
for block_i in np.arange(1,5): # block loop
    for phase_i, phase in enumerate(['prac_cued', 'prac_free', 'cued', 'free']): # phase loop
        
        if phase == 'prac_cued' or phase == 'prac_free': # practice only before first block
            if block_i > 1: continue
        
        # add the target stimuli
        if phase == 'cued':
            temp = wide_stimList.iloc[(block_i*10)-10:block_i*10,:] # subset
            temp = pd.melt(temp, var_name = 'target_type', value_name = 'target') # wide -> long format
        elif phase == 'free':
            temp = wide_stim2List.iloc[(block_i*10)-10:block_i*10,:] # subset
            temp = pd.melt(temp, var_name = 'target_type', value_name = 'target') # wide -> long format
        elif phase == 'prac_cued':
            temp = wide_stim3List
            temp = pd.melt(temp, var_name = 'target_type', value_name = 'target')
        elif phase == 'prac_free':
            temp = wide_stim4List
            temp = pd.melt(temp, var_name = 'target_type', value_name = 'target')
            
        # set some general columns
        temp['subID'] = ID
        temp['group'] = counterbalancing['reward_group']
        temp['block'] = block_i
        temp['phase'] = phase
        
        # determine transitions and rewards
        if phase == 'cued' or phase == 'prac_cued':
            nTransPerType = int(len(temp)/8) 
            temp['transition'] = (['repetition']*nTransPerType+['switch']*nTransPerType)*4  # balanced amount of transitions per target_type
            temp['reward'] = None
            if phase == 'cued':
                if counterbalancing['reward_group'] == 'switch':
                    temp['reward'] = (['low']*4 + ['high']*1 + ['high']*4 + ['low']*1)*4
                else:
                    temp['reward'] = (['high']*4 + ['low']*1 + ['low']*4 + ['high']*1)*4
        else: 
            temp['transition'] = None
            temp['reward'] = None
        
        # now we can randomize the trials
        temp = temp.sample(frac=1).reset_index(drop=True) # shuffle the order
        temp['trial'] = np.arange(1, len(temp)+1)
        
        # determine the task based on the transition (for cued only)
        if phase == 'cued' or phase == 'prac_cued':           
            temp.loc[0,'task'] = np.random.choice(['animacy','size'], size = 1)[0]               
            for idx, row in temp.iloc[1:].iterrows():
                if temp.loc[idx, 'transition'] == 'repetition':
                    if temp.loc[idx-1, 'task'] == 'size':
                        temp.loc[idx, 'task'] = 'size'            
                    elif temp.loc[idx-1, 'task'] == 'animacy':
                        temp.loc[idx, 'task'] = 'animacy'
                elif temp.loc[idx, 'transition'] == 'switch':
                    if temp.loc[idx-1, 'task'] == 'size':
                        temp.loc[idx, 'task'] = 'animacy'
                    elif temp.loc[idx-1, 'task'] == 'animacy':
                        temp.loc[idx, 'task'] = 'size'                                           
        else:
            temp['task'] = None
            
        # determine the cue based on the current task (without n-1 and n-2 repetitions)
        if phase == 'cued' or phase == 'prac_cued':
            for idx, row in temp.iterrows():
                if idx == 0:
                    if temp.loc[idx,'task'] == 'size':
                        temp.loc[0,'cue'] = np.random.choice(cues['size'])
                    else:
                        temp.loc[0,'cue'] = np.random.choice(cues['animacy'])
                elif idx == 1:
                    if temp.loc[idx,'task'] == 'size':
                        cue = np.random.choice(cues['size'])
                        while cue == temp.loc[idx-1,'cue']:
                            cue = np.random.choice(cues['size'])
                        temp.loc[idx,'cue'] = cue
                    else:
                        cue = np.random.choice(cues['animacy'])
                        while cue == temp.loc[idx-1,'cue']:
                            cue = np.random.choice(cues['size'])
                        temp.loc[idx,'cue'] = cue
                else:
                    if temp.loc[idx,'task'] == 'size':
                        cue = np.random.choice(cues['size'])
                        while cue == temp.loc[idx-1,'cue'] or cue == temp.loc[idx-2,'cue']:
                            cue = np.random.choice(cues['size'])
                        temp.loc[idx,'cue'] = cue
                    else:
                        cue = np.random.choice(cues['animacy'])
                        while cue == temp.loc[idx-1,'cue'] or cue == temp.loc[idx-2,'cue']:
                            cue = np.random.choice(cues['size'])
                        temp.loc[idx,'cue'] = cue
        else:
            temp['cue'] = '#'
            
        # determine the response based on the current task (for cued only)
        if phase == 'cued' or phase == 'prac_cued':
            for idx, row in temp.iterrows():
                if temp.loc[idx, 'task'] == 'size':
                    if temp.loc[idx, 'target_type'] == 'lism' or temp.loc[idx, 'target_type'] == 'nosm':
                        temp.loc[idx, 'cresp'] = 'g'
                    else:
                        temp.loc[idx, 'cresp'] = 'h'
                elif temp.loc[idx, 'task'] == 'animacy':
                    if temp.loc[idx, 'target_type'] == 'nosm' or temp.loc[idx, 'target_type'] == 'nola':
                        temp.loc[idx, 'cresp'] = 'g'
                    else:
                        temp.loc[idx, 'cresp'] = 'h'
        else:
            temp['cresp'] = None
        
        
        # append data to the final dataframe
        D = D.append(temp, ignore_index = True)
        
# chance column order + inspect if everthing is ok
design = D[['subID','group','block','phase','trial','target_type','target','task','cue','transition','reward','cresp']]
#design.to_csv('data/design.csv', index= False)

# test if design is correct
#T1 = design.groupby(['block','phase','target_type','transition']).size() # design is balanced
#T2 = design.duplicated(subset = 'target_word'); print(sum(A2)); # target words are unique
#T3 = design.groupby(['block','phase','task','cresp']).size()
