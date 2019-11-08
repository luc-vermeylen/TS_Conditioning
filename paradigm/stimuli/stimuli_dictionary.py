# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 18:25:42 2019

@author: luc
"""
import numpy as np

cued_stim = {
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


free_stim = {
    'smev': np.array([2, 4]*40), # smaller even
    'smod': np.array([1, 3]*40),
    'laev': np.array([6, 8]*40),
    'laod': np.array([7, 9]*40)
}


# practice stimuli
cued_stim_prac = {
    'lism': np.array(['ui']*4),
    'lila': np.array(['koe']*4),
    'nosm': np.array(['krijt']*4),
    'nola': np.array(['auto']*4)
}

free_stim_prac = {
    'smev': np.array([2, 4]*2), # smaller even
    'smod': np.array([1, 3]*2),
    'laev': np.array([6, 8]*2),
    'laod': np.array([7, 9]*2)
}
