# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 11:58:20 2019

@author: luc
"""

#%% Import Libraries

from psychopy import visual, core, event, gui
import numpy as np
import pandas as pd
from datetime import datetime
import itertools

#%% Stimuli

# main stimuli
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

# practice stimuli
Pdict = {
    'lism': np.array(['ui']*3),
    'lila': np.array(['koe']*3),
    'nosm': np.array(['krijt']*3),
    'nola': np.array(['auto']*3)
}


#%% Randomization
d = stimuli
ID = 1

#%% counterbalancing
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

#%% practice randomization

P = pd.DataFrame(Pdict)
Pdf = pd.melt(P, var_name = 'target_type', value_name = 'target_word') # wide -> long format
Pdf['subID'] = [ID]*P.size
Pdf['block'] = ['0']*P.size
Pdf['phase'] = ['practice']*P.size
Pdf['transition'] = (['repetition']*6+['switch']*6)
Pdf['group'] = [counterbalancing['reward_group']]*P.size
Pdf['reward'] = [None]*P.size
Pdf = Pdf.sample(frac=1).reset_index(drop=True) # shuffle the order
Pdf['trial'] = np.arange(1,13)
Pdf.loc[0,'transition'] = None
Pdf['task'] = np.random.choice(['animacy','size'], size = 1)[0]
for idx, r in Pdf.iterrows():
    if idx == 0:
        Pdf.loc[idx,'task'] = np.random.choice(['animacy','size'], size = 1)[0]
    else:
        if Pdf.loc[idx,'transition'] == 'repetition':
            Pdf.loc[idx,'task'] = Pdf.loc[idx-1,'task']
        else:
            if Pdf.loc[idx-1,'task'] == 'animacy':
                Pdf.loc[idx,'task'] = 'size'
            else:
                Pdf.loc[idx,'task'] = 'animacy'
for idx, r in Pdf.iterrows():
    if Pdf.loc[idx,'task'] == 'size':
        Pdf.loc[idx,'cue'] = np.random.choice(size_cues, size = 1)[0]
    else:
        Pdf.loc[idx,'cue'] = np.random.choice(animacy_cues, size = 1)[0]
for idx, r in Pdf.iterrows():
            if Pdf.loc[idx,'task'] == 'size':
                if Pdf.loc[idx,'target_type'] in ['lism','nosm']:
                    Pdf.loc[idx,'cresp'] = keys['size']['left']
                elif Pdf.loc[idx,'target_type'] in ['lila','nola']:
                    Pdf.loc[idx,'cresp'] = keys['size']['right']
            elif Pdf.loc[idx,'task'] == 'animacy':
                if Pdf.loc[idx,'target_type'] in ['nosm','nola']:
                    Pdf.loc[idx,'cresp'] = keys['animacy']['left']
                elif Pdf.loc[idx,'target_type'] in ['lism','lila']:
                    Pdf.loc[idx,'cresp'] = keys['animacy']['right']
        
    

#%% randomize the order of the stimuli
for idx, name in enumerate(['lism','lila','nosm','nola']):
    d[name] = np.random.choice(d[name], size = len(d[name]), replace = False)
df = pd.DataFrame(d)

D = pd.DataFrame() # initiatlize final dataframe
block_counter = 1
for block_i in np.arange(1,5): # block loop
    for phase_i, phase in enumerate(['cued','free']): # phase loop
        # the main design 
        B = df.iloc[(block_counter*10)-10:block_counter*10,:] # subset (to take different targets each phase/block)
        B = pd.melt(B, var_name = 'target_type', value_name = 'target_word') # wide -> long format
        B['subID'] = [ID]*40
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
        B.loc[0,'transition'] = None # first trial doesn't have a task transition
        
        
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
        for idx, r in B.iterrows():
            if B.loc[idx,'task'] == 'size':
                if B.loc[idx,'target_type'] in ['lism','nosm']:
                    B.loc[idx,'cresp'] = keys['size']['left']
                elif B.loc[idx,'target_type'] in ['lila','nola']:
                    B.loc[idx,'cresp'] = keys['size']['right']
            elif B.loc[idx,'task'] == 'animacy':
                if B.loc[idx,'target_type'] in ['nosm','nola']:
                    B.loc[idx,'cresp'] = keys['animacy']['left']
                elif B.loc[idx,'target_type'] in ['lism','lila']:
                    B.loc[idx,'cresp'] = keys['animacy']['right']
                
        # append data to another dataframe
        D = D.append(B, ignore_index = True)
        block_counter += 1

D = Pdf.append(D,ignore_index = True)

# chance column order + inspect if everthing is ok
design = D[['subID','group','block','phase','trial','target_type','target_word','task','cue','transition','reward','cresp']]
design.to_csv('data/design.csv', index= False)

# test if design is correct
#T1 = design.groupby(['block','phase','target_type','transition']).size() # design is balanced
#T2 = design.duplicated(subset = 'target_word'); print(sum(A2)); # target words are unique
#T3 = design.groupby(['block','phase','task','cresp']).size()

#%% Variables

# dialogue box
info = {'ID': '999', 'DebugMode': ''} # add age/gender questions after experiment!
dlg = gui.DlgFromDict(dictionary = info, title = 'Experiment', order = ['ID','DebugMode'], show = True)
if not dlg.OK: core.quit();
if info['ID'] == '': core.quit();

data = D # randomized stimuli list
filename = "data/cTSdata_" + info['ID'].zfill(3) + "_{}.csv".format(datetime.now().strftime("%Y%m%d-%H%M%S"))

event.globalKeys.clear()
event.globalKeys.add(key='escape', func=core.quit, name='shutdown')

FIX = .5
CUE = 1
STIM = 5
BLANK = .5
FB = .5
ITI = 1

win = visual.Window([1000,1000], units="norm", gammaErrorPolicy='ignore')
instr = visual.TextStim(win = win, text = '', height = .05, wrapWidth = 1.75)
ufix = visual.TextStim(win = win, text = '+', pos = [0, .05]) # upper fixation (5% o/t distance center - top)
lfix = visual.TextStim(win = win, text = '+', pos = [0, -.05]) # lower fixation (5% o/t distance center - bottom)
cue = visual.TextStim(win = win, pos = [0, .05])
target = visual.TextStim(win = win, pos = [0, -.05])
blank = visual.TextStim(win = win, text = '')
fb = visual.TextStim(win = win)

#%% Instructions

start = \
"Welkom en alvast bedankt voor je deelname aan dit experiment! " \
"Alvorens je begint willen we je eerst even aan twee belangrijke " \
"regels van uw experimentdeelname herinneren: \n\n" \
"Deze experimentsafname gebeurt in groep. Probeer hier rekening mee te houden: " \
"Indien u eventuele vragen, onzekerheden of opmerkingen hebt over het experiment, vraag dit " \
"dan eerst aan de proefleider en indien mogelijk zonder de andere deelnemers te storen. \n\n" \
"Dit experiment is een reactietijden-experiment. " \
"In reactietijden-experimenten is het steeds de bedoeling zo snel en accuraat mogelijk te " \
"reageren! Om genoeg data te kunnen verzamelen bieden we daarbij veel opeenvolgende " \
"beurten aan. Dit kan soms repetitief en eentonig overkomen, dus vragen wij er uw aandacht " \
"zo goed mogelijk bij te houden.\n\n" \
"Druk op spatie om verder te gaan..."

instr.text = start
instr.draw(); win.flip();
event.waitKeys()

prac_instr = \
"Dit is het experiment, let op, de procedure is een beetje complex, dus lees aandachtig: " \
"Je zal straks steeds een letter en een woord zien verschijnen. Bijvoorbeeld: \n\n" \
"A\n" \
"auto\n\n" \
"Jouw taak bestaat er uit om eerst te bepalen of de letter een klinker of een " \
"medeklinker is, en vervolgens de taak uit te voeren afhankelijk van het type letter. \n\n" \
"Namelijk, als de letter een klinker is, moet je in deze taak: \n" \
"op de letter {} drukken wanneer het woord niet levend is, en de letter {} \
    wanneer wel levend. ".format(keys['size']['left'].upper(), keys['size']['right'].upper()) \
        
"Met levend bedoelen we hier elk soort levend organisme: dier, boom, plant, fruit, of groente. \n\n" \
    
# "Echter, wanneer de letter een medeklinker is, moet je in deze taak: \n" \
# "op de letter S drukken wanneer het woord niet levend is, en de letter D wanneer wel levend. " \
# "Met levend bedoelen we hier elk soort levend organisme: dier, boom, plant, fruit, of groente. \n\n" \
# "Je zal soms ook meerdere beurten na elkaar het # tekentje zien verschijnen in plaats van een letter. " \
# "Op deze beurten mag je zelf kiezen welke taak je uitvoert. Echter, probeer dit zo willekeurig " \
# "mogelijk te doen! Alsof een dobbelsteen de keuze zou bepalen van welke taak je uitvoert!\n\n" \
# "Druk op spatie om verder te gaan..."

instr.text = prac_instr
instr.draw(); win.flip();
event.waitKeys()

#%% Experimental Trials

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
    
    # Block Feedback
    
    # Save/append data
    data.loc[i,'resp'] = resp_key; data.loc[i,'rt'] = resp_rt; data.loc[i,'correct'] = correct;    
    data.loc[[i]].to_csv(filename, mode = 'a', header = (True if i == 0 else False), index = False)
    
    
#%% Questions



#%% Close

win.close()
core.quit()