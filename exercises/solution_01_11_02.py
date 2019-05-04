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
} 


monthByDays = {
    "28": ["February"], # why `28` can't be used as a key?
    "30": ["April", "June", "September", "November"],
    "31": ["January", "March", "May", "July", "August", "October", "December"]
}

def sameDay(monthA, monthB):
    return daysByMonth[monthA] == daysByMonth[monthB]

def otherMonths(inputMonth):
    # fill the function, too
    numberOfDays = daysByMonth[month]
    sameDayMonths = monthByDays[numberOfDays]
    for month in sameDayMonths:
        if month != inputMonth:
            print(month)