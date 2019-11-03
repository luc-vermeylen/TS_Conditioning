# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 11:58:20 2019

@author: luc
"""

#%% Import Libraries

from psychopy import visual, core, event
import numpy as np
import pandas as pd
from datetime import datetime
import itertools

#%% Stimuli
stimuli = {
     'lism': np.array(["aardappel", "aardbei", "abrikoos", "appel", "avocado", "bacterie", "banaan", "bes", 
							 "bloemkool", "bloesem", "boon", "bosbes", "boterbloem", "druif", "duif", "duizendpoot", 
							 "eekhoorn", "egel", "erwt", "framboos", "fruit", "garnaal", "goudvis", "grasspriet", 
							 "hart", "honingbij", "kakkerlak", "kanarie", "kers", "kever", "kikker", "kiwi", 
							 "konijn", "kool", "kraai", "krab", "krekel", "kuiken", "larve", "lelie", 
							 "libelle", "limoen", "look", "luis", "mandarijn", "meloen", "mier", "mol", 
							 "mot", "mug", "muis", "mus", "olijf", "virus", "paddestoel", "paprika",  
							 "parkiet", "peer", "perzik", "peterselie", "poes", "pompelmoes", "pruim", "radijs", 
							 "rat", "rups", "salamander", "sardien", "sinaasappel", "slak", "spin", "sprinkhaan", 
							 "teek", "tomaat", "vlieg", "vlinder", "vlo", "wesp", "worm", "wortel"]),
     'lila': np.array(["adelaar", "alligator", "anaconda", "antilope", "baviaan", "beer", "bever", "bizon",
							 "boom", "buffel", "chimpansee", "coyote", "denneboom", "dolfijn", "dromedaris", "eik", 
							 "eland", "esdoorn", "everzwijn", "ezel", "flamingo", "gazelle", "geit", "gier", 
							 "giraffe", "gnoe", "gorilla", "haai", "havik", "hengst", "hert", "hond", 
							 "hyena", "ijsbeer", "jachtluipaard", "kameel", "kangoeroe", "krokodil", "lama", "leeuw", 
							 "luipaard", "lynx", "muildier", "naaldboom", "neushoorn", "nijlpaard", "octopus", "olifant", 
							 "ooievaar", "orka", "os", "panda", "panter", "pauw", "pinguïn", "poema", 
							 "pony", "potvis", "primaat", "ram", "ree", "rendier", "rund", "schaap", 
							 "slang", "spar", "stier", "struik", "struisvogel", "tijger", "vinvis", "vos", 
							 "walrus", "walvis", "wilg", "wolf", "zebra", "zeeleeuw", "zwaan", "zwijn"]),
     'nosm': np.array(["aansteker", "armband", "asbak", "badge", "baksteen", "bankkaart", "beitel", "beker", 
							 "blik", "briefkaart", "bril", "cassette", "coupon", "deurbel", "diamant", "edelsteen", 
							 "gloeilamp", "golfbal", "gom", "hamer", "juweel", "kaars", "kam", "kauwgom", 
							 "kiezelsteen", "knikker", "knoop", "knop", "kompas", "krijt", "kurk", "lepel", 
							 "medaille", "mok", "muntstuk", "naald", "nagel", "paperclip", "parel", "pen", 
							 "pijp", "pil", "pin", "pincet", "plakband", "pleister", "postzegel", "potlood", 
							 "rasp", "ring", "rits", "robijn", "saffier", "sandaal", "scalpel", "schaar", 
							 "scheermes", "schroef", "servet", "shampoo", "sierraad", "sigaar", "sleutel", "sok", 
							 "spatel", "speld", "spijker", "spuit", "stift", "strik", "tang", "tennisbal", 
							 "theelepel", "theepot", "ticket", "vingerhoed", "vork", "wasknijper", "zakmes", "zeep"]),
     'nola': np.array(["anker", "apartement", "balkon", "boomhut", "bus", "caravan", "dijk", "droogkast", 
							 "fiets", "fornuis", "gletsjer", "glijbaan", "grot", "haard", "hangar", "hangmat", 
							 "harp", "hut", "iglo", "ijskar", "jeep", "kachel", "kano", "kanon", 
							 "kapstok", "kar", "kerker", "kist", "kluis", "komeet", "kraan", "kruiwagen", 
							 "lantaarn", "limousine", "locomotief", "etalagepop", "matras", "melkweg", "moto", "orgel", 
							 "oven", "patio", "piano", "pier", "raket", "reclamebord", "reuzenrad", "roeiboot", 
							 "roltrap", "rotsblok", "saxofoon", "schild", "slaapzaal", "slagboom", "slee", "sofa", 
							 "speedboot", "steeg", "stoomboot", "surfboard", "tank", "tent", "ton", "toren", 
							 "tractor", "loopband", "tribune", "valies", "vat", "veerboot", "venster", "vlieger", 
							 "vlot", "vuilbak", "vulkaan", "wagon", "windmolen", "zeppelin", "zetel", "zitbank"])
}

#%% Randomization
d = stimuli
ID = 1

# counterbalancing
cue_size = ['vowel','consonant']
reward_group = ['repeat','switch']
rhand_size = ['left','right']
keys = ['cue_size', 'reward_group', 'rhand_size']
counterbalancing = [dict(zip(keys,combination)) for combination in itertools.product(cue_size,reward_group,rhand_size)]
counterbalancing = counterbalancing[ID%8]

if counterbalancing['cue_size'] == 'vowel':
    size_cues = ['A','E','I','O','U']; animacy_cues = ['V','F','L','Q','C']
else:
    size_cues = ['V','F','L','Q','C']; animacy_cues = ['A','E','I','O','U']
    
if counterbalancing['rhand_size'] == 'left':
    keys = {'size': {'left': 's', 'right': 'd'}, 'animacy': {'left': 'k', 'right': 'l'}}
else:
    keys = {'size': {'left': 'k', 'right': 'l'}, 'animacy': {'left': 's', 'right': 'd'}}

# randomize the order of the stimuli
for idx, name in enumerate(['lism','lila','nosm','nola']):
    d[name] = np.random.choice(d[name], size = len(d[name]), replace = False)
df = pd.DataFrame(d)

D = pd.DataFrame() # initiatlize final dataframe
for block_i in np.arange(1,5): # block loop
    for phase_i, phase in enumerate(['cued','free']): # phase loop
        
        # the main design 
        B = df.iloc[(block_i*10)-10:block_i*10,:] # subset (to take different targets each phase/block)
        B = pd.melt(B, var_name = 'target_type', value_name = 'target_word') # wide -> long format
        B['ID'] = [ID]*40
        B['block'] = [block_i]*40
        B['phase'] = [phase]*40
        B['transition'] = (['repetition']*5+['switch']*5)*4  # balanced amount of transitions per target_type
        if counterbalancing['reward_group'] == 'switch':
            B['group'] = ['switch']*40
            B['reward'] = (['low']*4 + ['high']*1 + ['high']*4 + ['low']*1)*4
        else:
            B['group'] = ['repeat']*40
            B['reward'] = (['high']*4 + ['low']*1 + ['low']*4 + ['high']*1)*4
        B = B.sample(frac=1).reset_index(drop=True) # shuffle the order
        B['trial'] = np.arange(1,41)
        
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
            if B.loc[idx,'phase'] == 'cued':
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
            else:
                B.loc[idx,'cue'] = '#'
                
        # determine the correct response
        B['cresp'] = np.where((B.task == 'size') & (B.target_type.isin(['lism','nosm'])), keys['size']['left'],
                              np.where((B.task == 'size') & (B.target_type.isin(['lila','nola'])), keys['size']['right'],
                              np.where((B.task == 'animacy') & (B.target_type.isin(['nosm','nola'])), keys['animacy']['left'],
                              np.where((B.task == 'animacy') & (B.target_type.isin(['lism','lila'])), keys['animacy']['left'], 'ERROR'))))
                    
        # append data to another dataframe
        D = D.append(B, ignore_index = True)


#%% Variables

data = D # randomized stimuli list
filename = "data/cTSdata_" + str(ID).zfill(3) + "_{}.csv".format(datetime.now().strftime("%Y%m%d-%H%M%S"))

event.globalKeys.add(key='q', func=core.quit, name='shutdown', modifiers=['ctrl'])

FIX = .5
CUE = 1
STIM = 5
BLANK = .5
FB = .5
ITI = 1

win = visual.Window([800,800], units="norm")
ufix = visual.TextStim(win = win, text = '+', pos = [0, .075]) # upper fixation
lfix = visual.TextStim(win = win, text = '+', pos = [0, -.075]) # lower fixation
cue = visual.TextStim(win = win, pos = [0, .075])
target = visual.TextStim(win = win, pos = [0, -.075])
blank = visual.TextStim(win = win, text = '')
fb = visual.TextStim(win = win)

#%% Run

for i in range(D.shape[0]):  
    # Fixation
    ufix.draw(); lfix.draw(); win.flip(); core.wait(FIX)
    
    # Cue
    cue.text = data['cue'][i]
    cue.draw(); lfix.draw(); win.flip(); core.wait(CUE)
    
    # Target
    target.text = data['target_word'][i] 
    cue.draw(); target.draw(); win.flip()
    
    # Response
    C = core.Clock(); C.reset()
    resp = event.waitKeys(maxWait = STIM, keyList = ['s','d','k','l'], timeStamped=C, clearEvents = True);   
    if resp:
        resp_key = resp[0][0]; resp_rt = resp[0][1]
        correct = 1 if resp_key == data.loc[i,'cresp'] else 0
        if resp_key == 'escape': win.close(); core.quit();
    else:
        resp_key = None; resp_rt = None; correct = 0
    
    # Blank 
    blank.draw(); win.flip(); core.wait(BLANK)
    
    # Feedback (if correct or training)
    fb_text = '+01' if data['reward'][i] == 'low' else '+10'
    fb.text = fb_text if correct == 1 else ''
    fb.draw(); win.flip(); core.wait(FB)
    
    # ITI
    blank.draw(); win.flip(); core.wait(ITI)
    
    # Save/append data
    data.loc[i,'resp'] = resp_key; data.loc[i,'rt'] = resp_rt; data.loc[i,'correct'] = correct;    
    data.loc[[i]].to_csv(filename, mode = 'a', header = (True if i == 0 else False), index = False)

#%% Close

win.close()
core.quit()