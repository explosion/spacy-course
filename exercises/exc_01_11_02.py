daysByMonth = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
} # finish this dictionary


monthByDays = {
    "28": ["February"], # why `28` can't be used as a key?
    "30": ["April", "June", "September", "November"],
    "31": ["January", "March", "May", "July", "August", "October", "December"]
} # finish this dictionary

def sameDay(monthA, monthB):
    # fill the function here
    return 

def otherMonths(inputMonth):
    # fill the function, too
    # hint `!=` checks whether two values equal each other
    

print(sameDay("January", "November")) # should be False
print(sameDay("September", "November")) # should be True

otherMonths("January") # should output "March", "May", "July", "August", "October", "December"