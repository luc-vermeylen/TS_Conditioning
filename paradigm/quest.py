# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 16:57:36 2019

@author: luc
"""

def questionnaire(win, testing):

    #%% import library
    
    from psychopy import visual, core, event
    
    #%% Question 1: Initialize variables
    
    # visual components
    t = visual.TextStim(win = win, text = '', height = .05, wrapWidth = 1, font = 'monospace')
    q = visual.TextStim(win = win, text = '', pos = [0,.8], height = .075, wrapWidth = 1.5, font = 'monospace')
    qInstr = visual.TextStim(win = win, text = '', pos = [0,.6], height = .05, wrapWidth = 1.5, font = 'monospace', italic = True)
    continue_button = visual.RatingScale(win, choices=['','Klik hier om verder te gaan als je klaar bent...', ''],
        markerStart=0.5, singleClick=False, scale = None, labels = None, tickHeight = 2, size = 1, stretch = 2.5,
        textSize = .65, showValue = False, acceptPreText = 'Maak een keuze', acceptText = 'Klik om verder te gaan...',
        acceptSize = 2, mouseOnly = True, marker = 'hover')
    
    # question and instructions
    q.text = "Had je het gevoel dat sommige beurten meer beloond werden (meer +10's) \
dan andere of leek dit volkomen willekeurig?"
    
    qInstr.text = "Gebruik het toetsenbord om je antwoord te typen. \
Leestekens kan je niet gebruiken. Gebruik dus best de 'enter' toets om een nieuwe zin te beginnen."
    
    # initialize variables
    inputText = ""
    theseKeys= ""
    shift_flag = False
    
    #%% Question 1: display and collect free text input
    
    while continue_button.noResponse:
        
        theseKeys = event.getKeys()
        
        n = len(theseKeys)
        i = 0
        
        while i < n:
            
            if theseKeys[i] == 'escape':
                # pressing RETURN means time to stop
                continue_button.noResponse = False
                break
            
            elif theseKeys[i] == 'return':
                inputText += '\n'
                i = i + 1
        
            elif theseKeys[i] == 'backspace':
                inputText = inputText[:-1]  # lose the final character
                i = i + 1
        
            elif theseKeys[i] == 'space':
                inputText += ' '
                i = i + 1
        
            elif theseKeys[i] in ['lshift', 'rshift']:
                shift_flag = True
                i = i + 1
        
            else:
                if len(theseKeys[i]) == 1:
                    # we only have 1 char so should be a normal key, 
                    # otherwise it might be 'ctrl' or similar so ignore it
                    if shift_flag:
                        inputText += chr( ord(theseKeys[i]) - ord(' ')) # this maks shift to caps possible
                        shift_flag = False
                    else:
                        inputText += theseKeys[i]
                i = i + 1
        
        t.text = inputText
        t.draw(); q.draw(); qInstr.draw(); continue_button.draw()
        win.flip()
    
    resp_q1 = inputText
    
    #%% Question 2
        
    q2 = visual.TextStim(win = win, text = '', pos = [0,.25], height = .05, wrapWidth = 1.5, font = 'monospace')
    q2.text = "Bij sommige deelnemers werden correcte responsen meer beloond met +10 wanneer de vorige taak dezelfde was als de huidige, \
dan wanneer de vorige taak verschillend was dan de huidige.\n\n\
Bij andere deelnemers kon dit omgekeerd zijn: taak herhalingen werden \
minder beloond dan wanneer taken wisselden.\n\n\
Echter, bij de andere helft deelnemers was dit volkomen willekeurig en werden alle volgordes evenveel met +10 als met +1 beloond.\n\n\
(Er wordt per groep een aparte FNAC bon uitgedeeld aan de beste deelnemer)\n\n\
Tot welke groep denk je dat jij behoorde?"
    
    ratingScale = visual.RatingScale(
        win, choices=['Herhalingen \nmeer beloond', 'Willekeurige \nbeloning', 'Wisselingen \nmeer beloond'],
        markerStart=0.5, singleClick=False, scale = None, labels = None, tickHeight = 2, size = 1, stretch = 2.5,
        textSize = .65, showValue = False, acceptPreText = 'Maak een keuze', acceptText = 'Klik om verder te gaan...',
        acceptSize = 2, mouseOnly = True, marker = 'hover')
    
    while ratingScale.noResponse:
        ratingScale.lineColor = 'white'
        ratingScale.draw(); q2.draw()
        win.flip()
    
    resp_q2 = ratingScale.getRating()

    
    #%% Close
    if testing == True:
        win.close(); core.quit()
    
    return resp_q1, resp_q2

# from psychopy import visual
# win = visual.Window([1200,800], units="norm", gammaErrorPolicy='ignore')
# q1, q2 = questionnaire(win, testing = True)