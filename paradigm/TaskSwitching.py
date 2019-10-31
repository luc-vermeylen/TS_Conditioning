# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 11:58:20 2019

@author: luc
"""

#%% Import Libraries

from psychopy import visual, core, event
import numpy as np
import pandas as pd

#%% Randomization

d = {
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

x = 3

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


cues = (['A','E','I','O','U'] + ['V','F','L','Q','C'] )*4

# remove repetitions in cues !!!
for idx, r in block1.iterrows():
    if block1.loc[idx,'task'] == 'size':
        block1.loc[idx,'cue'] = np.random.choice(['A','E','I','O','U'], size = 1)[0]
    else:
        block1.loc[idx,'cue'] = np.random.choice(['V','F','L','Q','C'], size = 1)[0]
    
data = np.column_stack((trial,words,color))
df = pd.DataFrame(data, columns = ['trial','word','color'])


#%% Initiate Stimuli

win = visual.Window([400,400], gammaErrorPolicy='warn')
message = visual.TextStim(win, pos = ([0,0]))
message.autoDraw = True


#%% Helper Functions

#%% Block Loop

#%% Trial Loop
for i in range(0,4):
    print(words[i])
    message.text = words[i]
    message.color = color[i]
    win.flip()
    C = core.Clock()
    C.reset()
    resp = event.waitKeys(maxWait = 3, keyList = ['left','right'], timeStamped=C, clearEvents = True);
    print(resp)
    
#%% Exectute


#%% Close

win.close()
core.quit()