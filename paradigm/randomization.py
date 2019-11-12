# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 15:33:50 2019

@author: luc
"""

#%% Import Libraries

import numpy as np
import pandas as pd
import itertools
from stimuli.stimuli_dictionary import cued_stim, free_stim, cued_stim_prac, free_stim_prac

def randomize(ID, Age, Gender, Handedness):
    '''
    
    Create a randomized and counterbalanced stimulus list for the current participant
    
    Parameters
    ----------
    ID : INT
        The subject ID. Based on the subject ID the correct counterbalancing is determined


    Returns
    -------
    design : Pandas DataFame
        The dataframe containing the complete stimulus list (including practice trials)
    keys: Dictionary
        the response keys for the free phase
    counterbalancing: Dictionary
        the complete counterbalancing dictionary for the current participant
    '''

    #%% Variables
    
    # experiment variables
    nBlocks = 6
    Phases = ['prac_cued', 'prac_free', 'cued', 'free']
    nstim = 60 # sample 60 stim from each target_type
    
    # randomize word targets to avoid relationship reward - stimulus
    for idx, name in enumerate(['lism','lila','nosm','nola']):
        cued_stim[name] = np.random.choice(cued_stim[name], size = nstim, replace = False) # sample from main stimulus set without replacement
    wide_cued = pd.DataFrame(cued_stim); wide_free = pd.DataFrame(free_stim)
    wide_cued_prac = pd.DataFrame(cued_stim_prac); wide_free_prac = pd.DataFrame(free_stim_prac)
    
    #%% Counterbalancing
    
    # counterbalancing factors
    cue_size = ['vowel','consonant']  # for cued trials only
    reward_group = ['repeat','switch'] # in cued trials
    rhand_parity = ['left','right'] # response hand: for free trials only
    
    keys = ['cue_size', 'reward_group', 'rhand_parity'] # dictionary keys
    
    # cartesian product of factors, then, index by taking modulus of subj ID by N combinations
    counterbalancing = [dict(zip(keys,combination)) for combination in itertools.product(cue_size,reward_group,rhand_parity)]
    counterbalancing = counterbalancing[ID%8] 
    
    # dictionary to retrieve the mapping from the current counterbalancing later on
    if counterbalancing['cue_size'] == 'vowel':
        cues = {'size': ['A','E','I','O','U'], 'animacy': ['V','F','L','Q','C']}
    else:
        cues = {'size': ['V','F','L','Q','C'], 'animacy': ['A','E','I','O','U']}
        
    if counterbalancing['rhand_parity'] == 'left':
        keys = {'parity': {'left': 's', 'right': 'd'}, 'nsize': {'left': 'k', 'right': 'l'}}
    else:
        keys = {'parity': {'left': 'k', 'right': 'l'}, 'nsize': {'left': 's', 'right': 'd'}}
    
    #%% Generate the main stimulus list 
    
    # (!!! half the current stimulus list controlling for word length and freq)
    
    # main loop across all blocks, phases and trials
    D = pd.DataFrame() # initiatlize final dataframe
    for block_i in np.arange(1,nBlocks+1): # block loop
        for phase_i, phase in enumerate(Phases): # phase loop
            
            if phase == 'prac_cued' or phase == 'prac_free': # practice only before first block
                if block_i > 1: continue
            
            # add the target stimuli
            if phase == 'cued':
                temp = wide_cued.iloc[(block_i*10)-10:block_i*10,:] # subset
                temp = pd.melt(temp, var_name = 'target_type', value_name = 'target') # wide -> long format
            elif phase == 'free':
                temp = wide_free.iloc[(block_i*10)-10:block_i*10,:] # subset
                temp = pd.melt(temp, var_name = 'target_type', value_name = 'target') # wide -> long format
            elif phase == 'prac_cued':
                temp = wide_cued_prac
                temp = pd.melt(temp, var_name = 'target_type', value_name = 'target')
            elif phase == 'prac_free':
                temp = wide_free_prac
                temp = pd.melt(temp, var_name = 'target_type', value_name = 'target')
                
            # set some general columns
            temp['subID'] = ID; temp['Age'] = Age; temp['Gender'] = Gender; temp['Handedness'] = Handedness;
            temp['Q1'] = None; temp['Q2'] = None;
            temp['group'] = counterbalancing['reward_group']
            temp['block'] = block_i
            temp['phase'] = phase
            temp['resp'] = None
            temp['rt'] = None
            temp['correct'] = None
            temp['time_elapsed'] = None
            temp['points'] = None
            
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
            
    # chance column order
    design = D[['subID','Age','Gender','Handedness','group','block','phase','trial','target_type',\
                'target','task','cue','transition','reward','cresp','resp','rt','correct','points','time_elapsed', 'Q1','Q2']]
    design.to_csv('data/current_stimulus_list.csv', index= False)
    
    return design, keys, counterbalancing