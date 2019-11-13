# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 12:37:54 2019

@author: luc
"""

from psychopy import core, visual, event

def introduction(win, size, animacy, free_keys):

    def show_text(text, win):
        instr = visual.TextStim(win = win, text = '', height = .05, wrapWidth = 1.5, font = 'monospace')
        instr.text = text;
        instr.draw(); win.flip();
        text_resp = event.waitKeys()
        return text_resp
    
    start = """Welkom en alvast bedankt voor je deelname aan dit experiment! 
Alvorens je begint willen we je eerst even aan twee belangrijke 
regels van uw experimentdeelname herinneren: \n\n
Deze experimentsafname gebeurt in groep. Probeer hier rekening mee te houden: 
Indien u eventuele vragen, onzekerheden of opmerkingen hebt over het experiment, vraag dit 
dan eerst aan de proefleider en indien mogelijk zonder de andere deelnemers te storen. \n\n
Dit experiment is een reactietijden-experiment. 
In reactietijden-experimenten is het steeds de bedoeling zo snel en accuraat mogelijk te  
reageren! Om genoeg data te kunnen verzamelen bieden we daarbij veel opeenvolgende 
beurten aan. Dit kan soms repetitief en eentonig overkomen, dus vragen wij er uw aandacht "
zo goed mogelijk bij te houden.\n\n 
Druk op spatie om verder te gaan..."""
    
    
    prac_instr = """Dit is het experiment, let op, de procedure is een beetje complex, dus lees aandachtig: 
Je zal straks steeds een letter en een woord zien verschijnen. Bijvoorbeeld: \n\n
 A\n
koe\n\n
Jouw taak bestaat er uit om eerst te bepalen of de letter een klinker of een 
medeklinker is, en vervolgens de taak uit te voeren afhankelijk van het type letter. \n\n
Namelijk, als de letter een {} is, moet je in deze taak: \n
op de letter G drukken wanneer het woord kleiner is, en de letter H het woord groter is dan een basketbal.\n\n
Echter, wanneer de letter een {} is, moet je in deze taak: \n
op de letter G drukken wanneer het woord niet levend is, en de letter H wanneer wel levend. 
Met levend bedoelen we hier elk soort levend organisme: dier, boom, plant, fruit, of groente. \n\n
Druk op spatie om verder te gaan...""".format(size,animacy)
    
    prac_instr2 = """Je zal soms ook meerdere beurten na elkaar het # tekentje en een cijfer zien verschijnen in plaats van een letter en een woord. 
Jouw taak bestaat er uit om ofwel te beoordelen of het cijfer even of oneven is,
ofwel te beoordelen of het cijfer kleiner of groter dan 5 is.\n\n
Op deze beurten mag je zelf kiezen welke taak je uitvoert. Echter, probeer dit zo willekeurig 
mogelijk te doen! Alsof een dobbelsteen de keuze zou bepalen van welke taak je uitvoert!\n\n
Let op! De toetsen die je moet gebruiken hangen nu af van je keuze.\n\n
Namelijk, als de je de cijfers wilt beoordelen als kleiner/groter dan 5 moet je \n
op de letter {} drukken wanneer het cijfer kleiner is, 
en de letter {} het cijfer groter is dan 5.\n\n
Echter, wanneer je de cijfers wilt beoordelen als even/oneven moet je \n
op de letter {} drukken wanneer het cijfer oneven is, 
en de letter {} wanneer het cijfer even is.\n\n
Druk op spatie om verder te gaan...""".format(free_keys['nsize']['left'].upper(),free_keys['nsize']['right'].upper(),free_keys['parity']['left'].upper(),free_keys['parity']['right'].upper())
    
    prac_instr3 = """!!Je kan met dit experiment ook een FNAC-BON van 50 euro winnen!!\n\n
Op elke beurt kan je punten winnen als je correct antwoord. Soms is dit maar 1 punt, maar soms 
kunnen dit ook 10 punten zijn. Dit is volledig willekeurig bepaald.\n\n
Je weet dus niet op voorhand hoeveel punten te verdienen zijn voor elke beurt: 
Probeer daarom op elke beurt correct en snel genoeg te antwoorden!\n\n
Enkel op de beurten waar je vrij kan kiezen welke taak je doet kan je geen punten verdienen. 
Echter, deelnemers die daar te veel fouten maken of niet willekeurig taken kiezen 
tijdens deze fase, worden uitgesloten voor de competitie om de FNAC bon.\n\n
Druk op spatie om nog een keer de instructies te zien..."""
    
    show_text(start, win)
    show_text(prac_instr, win)
    show_text(prac_instr2, win)
    show_text(prac_instr3, win)

#%%

def cued_prac_instructions(win, size, animacy, free_keys):

    def show_text(text, win):
        instr = visual.TextStim(win = win, text = '', height = .05, wrapWidth = 1.5, font = 'monospace')
        instr.text = text;
        instr.draw(); win.flip();
        text_resp = event.waitKeys()
        return text_resp

    prac_instr4 = """Jouw taak bestaat er uit om eerst te bepalen of de letter een klinker of een 
medeklinker is, en vervolgens de taak uit te voeren afhankelijk van het type letter. \n\n
Namelijk, als de letter een {} is, moet je in deze taak: \n
op de letter G drukken wanneer het woord kleiner is, en de letter H het woord groter is dan een basketbal.\n\n
Echter, wanneer de letter een {} is, moet je in deze taak: \n
op de letter G drukken wanneer het woord niet levend is, en de letter H wanneer wel levend. 
Met levend bedoelen we hier elk soort levend organisme: dier, boom, plant, fruit, of groente. \n\n
Druk op spatie om eens enkele oefenbeurten te proberen (nog niet voor punten)...""".format(size,animacy)
    
    show_text(prac_instr4,win)

#%%

def free_prac_instructions(win, size, animacy, free_keys):

    def show_text(text, win):
        instr = visual.TextStim(win = win, text = '', height = .05, wrapWidth = 1.5, font = 'monospace')
        instr.text = text;
        instr.draw(); win.flip();
        text_resp = event.waitKeys()
        return text_resp

    prac_instr5 = """Nu zal je meerdere beurten na elkaar het # tekentje en een cijfer zien verschijnen in plaats van een letter en een woord. 
Jouw taak bestaat er uit om ofwel te beoordelen of het cijfer even of oneven is, 
ofwel te beoordelen of het cijfer kleiner of groter dan 5 is.\n\n
Op deze beurten mag je zelf kiezen welke taak je uitvoert. Echter, probeer dit zo willekeurig 
mogelijk te doen! Alsof een dobbelsteen de keuze zou bepalen van welke taak je uitvoert!\n\n
Let op! De toetsen die je moet gebruiken hangen nu af van je keuze.\n\n
Namelijk, als de je de cijfers wilt beoordelen als kleiner/groter dan 5 moet je \n
op de letter {} drukken wanneer het cijfer kleiner is, 
en de letter {} het cijfer groter is dan 5.\n\n
Echter, wanneer je de cijfers wilt beoordelen als even/oneven moet je \n
op de letter {} drukken wanneer het cijfer oneven is, 
en de letter {} wanneer het cijfer even is.\n\n
Druk op spatie om eens enkele oefenbeurten te proberen ...""".format(free_keys['nsize']['left'].upper(),free_keys['nsize']['right'].upper(),free_keys['parity']['left'].upper(),free_keys['parity']['right'].upper())
    
    show_text(prac_instr5,win)

#%% 

def review_instructions(win, size, animacy, free_keys):
    
    def show_text(text, win):
        instr = visual.TextStim(win = win, text = '', height = .05, wrapWidth = 1.5, font = 'monospace')
        instr.text = text;
        instr.draw(); win.flip();
        text_resp = event.waitKeys()
        return text_resp
    
    prac_instr6 = """Duidelijk? Zoniet, laat zeker nog eens weten aan de proefleider.\n\n
Nu begint het eigenlijke experiment voor punten!\n\n
Veel succes!\n\n
Druk op 'spatie' om aan het eigenlijke experiment te beginnen.\n\n"""
    show_text(prac_instr6,win)[0]

        
#%% 
        
def cued_instructions(win, size, animacy, free_keys):

  def show_text(text, win):
      instr = visual.TextStim(win = win, text = '', height = .05, wrapWidth = 1.5, font = 'monospace')
      instr.text = text;
      instr.draw(); win.flip();
      text_resp = event.waitKeys()
      return text_resp

  prac_instr4 = """In het volgende blok, moet je op basis van de letter het woord beoordelen. \n\n
Namelijk, als de letter een {} is, moet je in deze taak: \n
op de letter G drukken wanneer het woord kleiner is, en de letter H het woord groter is dan een basketbal.\n\n
Echter, wanneer de letter een {} is, moet je in deze taak: \n
op de letter G drukken wanneer het woord niet levend is, en de letter H wanneer wel levend. 
Met levend bedoelen we hier elk soort levend organisme: dier, boom, plant, fruit, of groente. \n\n
Druk op spatie om te starten...""".format(size,animacy)
  
  show_text(prac_instr4,win)


#%%
  
def free_instructions(win, size, animacy, free_keys):

    def show_text(text, win):
        instr = visual.TextStim(win = win, text = '', height = .05, wrapWidth = 1.5, font = 'monospace')
        instr.text = text;
        instr.draw(); win.flip();
        text_resp = event.waitKeys()
        return text_resp

    prac_instr5 = """In het volgende blok kies je zelf hoe je de cijfers zal beoordelen! 
Namelijk, als de je de cijfers wilt beoordelen als kleiner/groter dan 5 moet je \n
op de letter {} drukken wanneer het cijfer kleiner is, 
en de letter {} het cijfer groter is dan 5.\n\n
Echter, wanneer je de cijfers wilt beoordelen als even/oneven moet je \n
op de letter {} drukken wanneer het cijfer oneven is, 
en de letter {} wanneer het cijfer even is.\n\n
Druk op spatie om te starten...""".format(free_keys['nsize']['left'].upper(),free_keys['nsize']['right'].upper(),free_keys['parity']['left'].upper(),free_keys['parity']['right'].upper())
    
