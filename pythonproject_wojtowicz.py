# Nicholas Wojtowicz

import winsound

pickups = {
  "Seymour Duncan Invader": 200,
  "EMG 81": 200,
  "Bareknuckle Cobra T": 270,
  "DiMarzio Area T": 180,
  "Seymour Duncan SH-2": 180,
  "Seymour Duncan SNS": 260,
  "Benedetto S-6": 155,
  "EMG 85": 200
}

body = {
  "Mahogany": 220,
  "Maple": 250,
  "Ash": 300
}

neck = {
  "Alder": 180,
  "Maple": 200,
  "Rosewood": 170
}

balance = 0

def metalguitar():
    pickupselectm = input('Select pickups; Seymour Duncan Invader: $200, EMG 81: $200, or Bareknuckle Cobra T: $270? ')
    mbalance = balance + pickups[pickupselectm]
    print('The cost of the guitar is now: $', mbalance)
    neckm = input('Select type of wood for neck and fretboard; Alder: $180, Maple: $200, or Rosewood: $170? ')
    mmbalance = mbalance + neck[neckm]
    print('The cost of the guitar is now: $', mmbalance)
    bodym = input('Select type of wood for the body; Mahogany: $220, Maple: $250, or Ash: $300? ')
    mmmbalance = mmbalance + body[bodym]
    print('The total cost of the guitar is: $', mmmbalance)


def rockguitar():
    pickupselectr = input('Select pickups; DiMarzio Area T: $180, Bareknuckle Cobra T: $270, or Seymour Duncan Invader: $200?')
    rbalance = balance + pickups[pickupselectr]
    print('The cost of the guitar is now: $', rbalance)
    neckr = input('Select type of wood for neck and fretboard; Alder: $180, Maple: $200, or Rosewood: $170? ')
    rrbalance = rbalance + neck[neckr]
    print('The cost of the guitar is now: $', rrbalance)
    bodyr = input('Select type of wood for the body; Mahogany: $220, Maple: $250, or Ash: $300? ')
    rrrbalance = rrbalance + body[bodyr]
    print('The total cost of the guitar is: $', rrrbalance)

def jazzguitar():
    pickupselectj = input('Select Pickups: Seymour Duncan SH-2: $180, Seymour Duncan SNS: $260, or Benedetto S-6: $155?')
    jbalance = balance + pickups[pickupselectj]
    print('The cost of the guitar is now: $', balance)
    neckj = input('Select type of wood for neck and fretboard; Alder: $180, Maple: $200, or Rosewood: $170? ')
    jjbalance = jbalance + neck[neckj]
    print('The cost of the guitar is now: $', jjbalance)
    bodyj = input('Select type of wood for the body; Mahogany: $220, Maple: $250, or Ash: $300? ')
    jjjbalance = jjbalance + body[bodyj]
    print('The total cost of the guitar is: $', jjjbalance)

def altguitar():
    pickupselecta = input('Bareknuckle Cobra T: $270, DiMarzio Area T: $180, or EMG 85: $200?')
    abalance = balance + pickups[pickupselecta]


genreselect = input('Select genre of music. Metal, Rock, Jazz, Alternative? ')

if genreselect == 'Metal':
    winsound.PlaySound("metalpython1.wav", winsound.SND_ASYNC)
    metalguitar()
elif genreselect == 'Rock':
    rockguitar()
elif genreselect == 'Jazz':
    jazzguitar()
else:
    altguitar()
