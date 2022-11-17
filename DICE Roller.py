import random

# if we are going to create an askii art we have to use the unicodes characters

#print(" \u25CF  \u250C  \u2500  \u2510  \u2502  \u2514  \u2518 ")
#     ●  ┌  ─  ┐  │  └  ┘   these will be used to make some askii arts

dice_arts = {1:("┌─────────┐",
                "│         │",
                "│    ●    │",
                "│         │",
                "└─────────┘"),
             2:("┌─────────┐",
                "│      ●  │",
                "│         │",
                "│  ●      │",
                "└─────────┘"),
             3:("┌─────────┐",
                "│      ●  │",
                "│    ●    │",
                "│  ●      │",
                "└─────────┘"),
             4:("┌─────────┐",
                "│  ●   ●  │",
                "│         │",
                "│  ●   ●  │",
                "└─────────┘"),
             5:("┌─────────┐",
                "│  ●   ●  │",
                "│    ●    │",
                "│  ●   ●  │",
                "└─────────┘"),
             6:("┌─────────┐",
                "│ ●     ● │",
                "│ ●     ● │",
                "│ ●     ● │",
                "└─────────┘")
             }

dice = []
total = 0
num = int(input(" No. of dice : "))

for die in range(num):
    dice.append(random.randint(1,6))
