leaving_time = (6 * 60 + 52) * 60  # leaving time in seconds
easy_pace = (8 * 60 + 15) * 2  # duration of easy pace in seconds * miles ran
tempo = (7 * 60 + 12) * 3  # duration of tempo pace in seconds * miles ran
finish_hour = (leaving_time + easy_pace + tempo) / (60 * 60)  # finishing time in seconds / seconds in an hour
finish_floored = (leaving_time + easy_pace + tempo) // (60 * 60)  # same as previous however only return the hour
finish_minute = (finish_hour - finish_floored) * 60  # finished time - finished hour * minutes in hour
print('Finish time was %d:%d' % (finish_hour, finish_minute))  # format time
