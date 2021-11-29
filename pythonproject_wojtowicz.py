# Nicholas Wojtowicz

# use winsound to enable .wav files to be played in program

import winsound

#create dictionary for pickups, body, and neck with prices for each key

pickups = {
  "1": 200,
  "2": 200,
  "3": 270,
  "4": 180,
  "5": 180,
  "6": 260,
  "7": 155,
  "8": 200
}

body = {
  "12": 220,
  "13": 250,
  "14": 300
}

neck = {
  "9": 180,
  "10": 200,
  "11": 170
}

# balance starts at 0 and money is added to balance for each part selected

balance = 0

def metalguitar():
    statementm = print('Please type the number associated with the part you want')
    pickupselectm = input('Select pickups; Seymour Duncan Invader(1): $200, EMG 81(2): $200, or Bareknuckle Cobra T(3): $270? ')
    while True:
        if pickupselectm == '1' or '2' or '3':
            mbalance = balance + pickups[pickupselectm]
            print('The cost of the guitar is now: $', mbalance)
            neckm = input('Select type of wood for neck and fretboard; Alder(9): $180, Maple(10): $200, or Rosewood(11): $170? ')
            if neckm == '9' or '10' or '11':
               mmbalance = mbalance + neck[neckm]
               print('The cost of the guitar is now: $', mmbalance)
               bodym = input('Select type of wood for the body; Mahogany(12): $220, Maple (13): $250, or Ash(14): $300? ')
               if bodym == '12' or '13' or '14':
                   mmmbalance = mmbalance + body[bodym]
                   print('The total cost of the guitar is: $', mmmbalance)
                   break
               else:
                   print('invalid answer. Try again.')
                   bodym = input('Select type of wood for the body; Mahogany(12): $220, Maple (13): $250, or Ash(14): $300? ')
                   break
            else:
                print('invalid answer. Try again.')
                neckm = input('Select type of wood for neck and fretboard; Alder(9): $180, Maple(10): $200, or Rosewood(11): $170? ')
                break
        else:
            print('Invalid answer. Try again.')
            pickupselectm = input('Select pickups; Seymour Duncan Invader(1): $200, EMG 81(2): $200, or Bareknuckle Cobra T(3): $270? ')
            break


def rockguitar():
    statementr = print('Please type the number associated with the part you want')
    pickupselectr = input('Select pickups; DiMarzio Area T(4): $180, Bareknuckle Cobra T(3): $270, or Seymour Duncan Invader(1): $200?')
    while True:
        if pickupselectr == '1' or '3' or '4':
            rbalance = balance + pickups[pickupselectr]
            print('The cost of the guitar is now: $', rbalance)
            neckr = input('Select type of wood for neck and fretboard; Alder(9): $180, Maple(10): $200, or Rosewood(11): $170? ')
            if neckr == '9' or '10' or '11':
                rrbalance = rbalance + neck[neckr]
                print('The cost of the guitar is now: $', rrbalance)
                bodyr = input('Select type of wood for the body; Mahogany (12): $220, Maple (13): $250, or Ash(14): $300? ')
                if bodyr == '12' or '13' or '14':
                    rrrbalance = rrbalance + body[bodyr]
                    print('The total cost of the guitar is: $', rrrbalance)
                    break
                else:
                    print('invalid answer. Try again.')
                    bodyr = input('Select type of wood for the body; Mahogany(12): $220, Maple (13): $250, or Ash(14): $300? ')
                    break
            else:
                print('invalid answer. Try again.')
                neckr = input('Select type of wood for neck and fretboard; Alder(9): $180, Maple(10): $200, or Rosewood(11): $170? ')
                break
        else:
            print('invalid answer. Try again.')
            pickupselectr = input('Select pickups; DiMarzio Area T(4): $180, Bareknuckle Cobra T(3): $270, or Seymour Duncan Invader(1): $200?')
            break

def jazzguitar():
    statementj = print('Please type the number associated with the part you want')
    pickupselectj = input('Select Pickups: Seymour Duncan SH-2(5): $180, Seymour Duncan SNS(6): $260, or Benedetto S-6 (7): $155?')
    while True:
        if pickupselectj == '5' or '6' or '7':
            jbalance = balance + pickups[pickupselectj]
            print('The cost of the guitar is now: $', balance)
            neckj = input('Select type of wood for neck and fretboard; Alder(9): $180, Maple(10): $200, or Rosewood(11): $170? ')
            if neckj == '9' or '10' or '11':
                jjbalance = jbalance + neck[neckj]
                print('The cost of the guitar is now: $', jjbalance)
                bodyj = input('Select type of wood for the body; Mahogany (12): $220, Maple (13): $250, or Ash(14): $300? ')
                if bodyj == '12' or '13' or '14':
                    jjjbalance = jjbalance + body[bodyj]
                    print('The total cost of the guitar is: $', jjjbalance)
                    break
                else:
                    print('invalid answer. Try again.')
                    bodyj = input('Select type of wood for the body; Mahogany(12): $220, Maple (13): $250, or Ash(14): $300? ')
                    break
            else:
                print('invalid answer. Try again.')
                neckj = input('Select type of wood for neck and fretboard; Alder(9): $180, Maple(10): $200, or Rosewood(11): $170? ')
                break
        else:
            print('invalid answer. Try again.')
            input('Select Pickups: Seymour Duncan SH-2(5): $180, Seymour Duncan SNS(6): $260, or Benedetto S-6 (7): $155?')
            break

def altguitar():
    statementj = print('Please type the number associated with the part you want')
    pickupselecta = input('Bareknuckle Cobra T(3): $270, DiMarzio Area T (4): $180, or EMG 85 (8): $200?')
    while True:
        if pickupselectj == '3' or '4' or '8':
            abalance = balance + pickups[pickupselecta]
            print('The cost of the guitar is now: $', balance)
            necka = input('Select type of wood for neck and fretboard; Alder(9): $180, Maple(10): $200, or Rosewood(11): $170? ')
            if necka == '9' or '10' or '11':
                aabalance = abalance + neck[necka]
                print('The cost of the guitar is now: $', aabalance)
                bodya = input('Select type of wood for the body; Mahogany (12): $220, Maple (13): $250, or Ash(14): $300? ')
                if bodya == '12' or '13' or '14':
                    aaabalance = aabalance + body[bodya]
                    print('The total cost of the guitar is: $', aaabalance)
                    break
                else:
                    print('invalid answer. Try again.')
                    bodya = input('Select type of wood for the body; Mahogany(12): $220, Maple (13): $250, or Ash(14): $300? ')
                    break
            else:
                print('invalid answer. Try again.')
                necka = input('Select type of wood for neck and fretboard; Alder(9): $180, Maple(10): $200, or Rosewood(11): $170? ')
                break
        else:
            print('invalid answer. Try again.')
            input('Select Pickups: Seymour Duncan SH-2(5): $180, Seymour Duncan SNS(6): $260, or Benedetto S-6 (7): $155?')
            break

# user is prompted to choose a genre

genreselect = input('Select genre of music. Metal, Rock, Jazz, Alternative? ')

while True:
    if genreselect == 'Metal':
        winsound.PlaySound("metalpython1.wav", winsound.SND_ASYNC)
        metalguitar()
    elif genreselect == 'Rock':
        rockguitar()
    elif genreselect == 'Jazz':
        jazzguitar()
    elif genreselect == 'Alternative':
        altguitar()
    else:
         print("Option not available. Try Again")
         genreselect = input('Select genre of music. Metal, Rock, Jazz, Alternative? ')
         continue


# depending on which genre the user selects, the appropriate function
# will be called
