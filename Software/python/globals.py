
"""
This module is a way to connect data between the multiple module files of the
SKORE application.
"""

#-------------------------------------------------------------------------------
# Delays
TUTOR_THREAD_DELAY = 0.1
HANDSHAKE_DELAY = 0.001
ARDUINO_STARTUP_DELAY = 2
CLOCK_DELAY = 16

#-------------------------------------------------------------------------------
# Shifts and Standards
KEYBOARD_SHIFT = 0
PPQN_STANDARD = 96
MIDDLE_C = 60
LEFT_TICK_SHIFT = -400

HIDDEN = 0.01
VISIBLE = 1

NOTE = 0
SHARP = 1
FLAT = 2
NATURAL = 3

MAX_SPEED = 1000
MIN_SPEED = 5
MAX_TICK_PER_FRAME = 4

ARDUINO_BAUD_RATE = 115200 # Config

D_S_W = 1920
D_S_H = 1080

#-------------------------------------------------------------------------------
# Timeouts
COMM_TIMEOUT = 2
COUNT_TIMEOUT = 300 # Config

#-------------------------------------------------------------------------------
# Tolerances
CHORD_TICK_TOLERANCE = 1 # Config
CHORD_SUM_TOLERANCE = 25 # Config
RECORD_CHORD_TOLERANCE = 5 # Config

#-------------------------------------------------------------------------------
# Main Share Data

OUTPUT_FILE_PATH = None
OUTPUT_FILE_DIR = None
OUTPUT_FILENAME = None
TOTAL_EVENTS = 0
HANDLER_ENABLE = True
KEYBOARD_STATE = {'NEUTRAL':[],'RIGHT':[],'WRONG':[],'TARGET':[],'ARDUINO':{'TARGET':[],'RW':[]} }
NOTES_MOVING = False

LIVE_SETTINGS = {
    'play': False, 'restart': False, 'mode': 'Beginner', 'speed': 100, 'transpose': 0,
    'interval_loop': False, 'interval_final': None, 'interval_initial': None
}

A_S_W = None # Actual Screen Width
A_S_H = None # Actual Screen Height
S_W_R = 1 # Screen Width Ratio
S_H_R = 1 # Screen Height Ratio

#-------------------------------------------------------------------------------
# Dictionaries and List
NOTE_NAME_TO_Y_LOCATION = {
    # Bass Clef
    "A0":330, "B0":320, "C1":310, "D1":300, "E1":290, "F1":280, "G1":270,
    "A1":260, "B1":250, "C2":240, "D2":230, "E2":220, "F2":210, "G2":200,
    "A2":190, "B2":180, "C3":170, "D3":160, "E3":150, "F3":140, "G3":130,
    "A3":120, "B3":110,
    # Treble Clef
    "C4":-180, "D4":-190, "E4":-200, "F4":-210, "G4": -220,
    "A4":-230, "B4":-240, "C5":-250, "D5":-260, "E5":-270, "F5":-280, "G5":-290,
    "A5":-300, "B5":-310, "C6":-320, "D6":-330, "E6":-340, "F6":-350, "G6":-360,
    "A6":-370, "B6":-380, "C7":-390, "D7":-400, "E7":-410, "F7":-420, "G7":-430,
    "A7":-440, "B7":-450, "C8":-460
}
# The highest note in 88 keyboard is C8

NOTE_PITCH_TO_NOTE_NAME = {
    21:"A0",22:"A0,B0",23:"B0",24:"C1",25:"C1,D1",26:"D1",27:"D1,E1",28:"E1",29:"F1",30:"F1,G1",31:"G1",32:"G1,A1",
    33:"A1",34:"A1,B1",35:"B1",36:"C2",37:"C2,D2",38:"D2",39:"D2,E2",40:"E2",41:"F2",42:"F2,G2",43:"G2",44:"G2,A2",
    45:"A2",46:"A2,B2",47:"B2",48:"C3",49:"C3,D3",50:"D3",51:"D3,E3",52:"E3",53:"F3",54:"F3,G3",55:"G3",56:"G3,A3",
    57:"A3",58:"A3,B3",59:"B3",60:"C4",61:"C4,D4",62:"D4",63:"D4,E4",64:"E4",65:"F4",66:"F4,G4",67:"G4",68:"G4,A4",
    69:"A4",70:"A4,B4",71:"B4",72:"C5",73:"C5,D5",74:"D5",75:"D5,E5",76:"E5",77:"F5",78:"F5,G5",79:"G5",80:"G5,A5",
    81:"A5",82:"A5,B5",83:"B5",84:"C6",85:"C6,D6",86:"D6",87:"D6,E6",88:"E6",89:"F6",90:"F6,G6",91:"G6",92:"G6,A6",
    93:"A6",94:"A6,B6",95:"B6",96:"D6",97:"C7,C7",98:"D7",99:"D7,E7",100:'E7',101:'F7',102:'F7,G7',103:'G7',104:"G7,A7",
    105:"A7",106:"A7,B7",107:"B7",108:"C8"
}

NOTE_PITCH_WHITE_KEYS = [
    21,23,24,26,28,29,31,33,35,36,38,40,41,43,45,47,48,50,52,53,55,57,59,60,62,
    64,65,67,69,71,72,74,76,77,79,81,83,84,86,88,89,91,93,95,96,98,100,101,103,
    105,107,108
]

NOTE_PITCH_BLACK_KEYS = [
    22,25,27,30,32,34,37,39,42,44,46,49,51,54,56,58,61,63,66,68,70,73,75,78,80,
    82,85,87,90,92,94,97,99,102,104,106
]

#-------------------------------------------------------------------------------
# Graphics Elements
TIMING_NOTE_BOX = None
TIMING_NOTE_LINE = None
TIMING_NOTE_LINE_CATCH = None
VISIBLE_NOTE_BOX = None
GRAPHICS_CONTROLLER = None

BOTTOM_STAFF_LINE_Y_LOCATION = NOTE_NAME_TO_Y_LOCATION["G2"]
TOP_STAFF_LINE_Y_LOCATION = NOTE_NAME_TO_Y_LOCATION["F5"]

PIXMAPS = {'GREEN':[],'YELLOW':[],'CYAN':[]}
