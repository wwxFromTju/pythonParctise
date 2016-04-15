#!/usr/bin/env python

def tranformHour2Mins(hour) : 
    hour,mins = hour.split(":")
    hour,mins = int(hour), int(mins)
    if hour > 24 or hour < 0:
        return "your enter is wrong"
    return hour * 60 + mins

if __name__ == "__main__" : 
    print tranformHour2Mins("1:20")
    print tranformHour2Mins("0:20")
    print tranformHour2Mins("23:20")