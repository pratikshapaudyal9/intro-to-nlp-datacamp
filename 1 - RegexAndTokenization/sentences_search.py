import re

# Write a regular expression to search for anything in square brackets: pattern1
pattern1 = r"\[.*\]"

for i, line in enumerate(open("scene_one.txt")):
    for match in re.finditer(pattern1, line):
        print("Found on line {}: {}".format(i + 1, re.search))

# Use re.search to find the first text in square brackets
# print(re.search(pattern1, scene_one))

sentences = [
    "SCENE 1: [wind] [clop clop clop] \nKING ARTHUR: Whoa there!",
    "[clop clop clop] \nSOLDIER #1: Halt!",
    "Who goes there?",
    "ARTHUR: It is I, Arthur, son of Uther Pendragon, from the castle of Camelot.",
    "King of the Britons, defeator of the Saxons, sovereign of all England!",
    "SOLDIER #1: Pull the other one!",
    "ARTHUR: I am, ...  and this is my trusty servant Patsy.",
    "We have ridden the length and breadth of the land in search of knights who will join me in my court at Camelot.",
    "I must speak with your lord and master.",
    "SOLDIER #1: What?",
    "Ridden on a horse?",
    "ARTHUR: Yes!",
    "SOLDIER #1: You're using coconuts!",
    "ARTHUR: What?",
    "SOLDIER #1: You've got two empty halves of coconut and you're bangin' 'em together.",
    "ARTHUR: So?",
    "We have ridden since the snows of winter covered this land, through the kingdom of Mercea, through--\nSOLDIER #1: Where'd you get the coconuts?",
    "ARTHUR: We found them.",
    "SOLDIER #1: Found them?",
    "In Mercea?",
    "The coconut's tropical!",
    "ARTHUR: What do you mean?",
    "SOLDIER #1: Well, this is a temperate zone.",
    "ARTHUR: The swallow may fly south with the sun or the house martin or the plover may seek warmer climes in winter, yet these are not strangers to our land?",
    "SOLDIER #1: Are you suggesting coconuts migrate?",
    "ARTHUR: Not at all.",
    "They could be carried.",
    "SOLDIER #1: What?",
    "A swallow carrying a coconut?",
    "ARTHUR: It could grip it by the husk!",
    "SOLDIER #1: It's not a question of where he grips it!",
    "It's a simple question of weight ratios!",
    "A five ounce bird could not carry a one pound coconut.",
    "ARTHUR: Well, it doesn't matter.",
    "Will you go and tell your master that Arthur from the Court of Camelot is here.",
    "SOLDIER #1: Listen.",
    "In order to maintain air-speed velocity, a swallow needs to beat its wings forty-three times every second, right?",
    "ARTHUR: Please!",
    "SOLDIER #1: Am I right?",
    "ARTHUR: I'm not interested!",
    "SOLDIER #2: It could be carried by an African swallow!",
    "SOLDIER #1: Oh, yeah, an African swallow maybe, but not a European swallow.",
    "That's my point.",
    "SOLDIER #2: Oh, yeah, I agree with that.",
    "ARTHUR: Will you ask your master if he wants to join my court at Camelot?!",
    "SOLDIER #1: But then of course a-- African swallows are non-migratory.",
    "SOLDIER #2: Oh, yeah...",
    "SOLDIER #1: So they couldn't bring a coconut back anyway...  [clop clop clop] \nSOLDIER #2: Wait a minute!",
    "Supposing two swallows carried it together?",
    "SOLDIER #1: No, they'd have to have it on a line.",
    "SOLDIER #2: Well, simple!",
    "They'd just use a strand of creeper!",
    "SOLDIER #1: What, held under the dorsal guiding feathers?",
    "SOLDIER #2: Well, why not?",
]
# Find the script notation at the beginning of the fourth sentence and print it
pattern2 = r"[\w]+:"
print("Sentence: {}".format(re.match(pattern2, sentences[3])))

# for i, line in enumerate(open("sentences.txt")):
#     for match in re.finditer(pattern2, line):
#         print("Found on line {0}: {1}".format(i + 1, match.group()))
