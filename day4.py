filename = "input-day4.txt"
# filename = "input-day4-test.txt"
import datetime
import operator

import logging
logging.basicConfig(filename='day4.log',level=logging.DEBUG)
logging.debug('Start of logging')

class Guard:
    def __init__(self, id):
        self.id = id
        self.sleep_minutes = 0
        self.top_minutes = [0] * 60

    def __str__(self):
        return str(self.__dict__)

class Event:
    def __init__(self, day, time, event):
        self.d = datetime.datetime(1518, int(day[:2]), int(day[3:]), int(time[:2]), int(time[3:]))
        self.event = event

    def __str__(self):
        return str(self.__dict__)

def read_guard_behaviour(filename):
    file = open(filename, "r")
    events = []
    for line in file:
        elements = line.split()
        day = elements[0][6:]
        time = elements[1][:-1]
        event = " ".join(elements[2:])

        event = Event(day, time, event)
        events.append(event)

    return events

# alle events van een dag bij elkaar zoeken
def as_the_world_turns():
    events = read_guard_behaviour(filename)
    days = {}

    def date_hack(event):

        # # dit voelt wel een _beetje_ aguilera (c.q. coal chamber)
        # if event.time[:2] == '23':
        #     new_day_int = int(event.day[3:]) + 1
        #     new_day = str(new_day_int) if new_day_int > 9 else '0' + str(new_day_int)
        #     event.day = event.day[:3] + new_day
        #     logging.debug( 'hacked day ' + event.day

        if event.d.hour == 23:
            day = datetime.timedelta(days=1)
            event.d = event.d + day

        return event

    for event in events:
        # logging.debug( event
        event = date_hack(event)
        day = str(event.d.month) + '-' + str(event.d.day)
        # logging.debug( day
        # logging.debug( event
        try:
            days[day].append(event)
        except:
            days[day] = []
            days[day].append(event)
    # logging.debug( days
    return days

def time_is_ticking():
    days = as_the_world_turns()
    guards = []
    # guard id bepalen (eerste event?)
    for day in days.iteritems():
        sleep_starts = []
        sleep_stops = []
        for event in day[1]:
            keyword = event.event[:5] 
            if keyword == 'Guard':
                guard_id = event.event.split()[1][1:]
            elif keyword == 'falls':
                sleep_starts.append(event.d.minute)
            elif keyword == 'wakes':
                sleep_stops.append(event.d.minute)

        def get_guard(guard_id):
            return next((g for g in guards if g.id == guard_id), None)

        # conditioneel aanmaken
        guard = get_guard(guard_id)
        # logging.debug( guard
        if guard:
            pass
        else:
            guard = Guard(guard_id)
            guards.append(guard)
        

        day = str(event.d.month) + '-' + str(event.d.day)
        logging.debug( "dag is: " + day)
        logging.debug( "guard id: " + guard_id)
        logging.debug( "sleep starts " + str(sleep_starts))
        logging.debug( "sleep stops " + str(sleep_stops))

        # minuten optellen
        sleep_starts.sort()
        sleep_stops.sort()

        for idx, start in enumerate(sleep_starts):
            # logging.debug( sleep_stops[idx], start)
            stop, start = int(sleep_stops[idx]), int(start)
            mins = stop - start
            guard.sleep_minutes += mins
            for m in range(mins):
                guard.top_minutes[start + m] += 1
        logging.debug( guard)

    logging.debug( len(guards))

    # vind meest sleepy guard:
    max_min = 0
    most_slept_min_val = 0
    for guard in guards:
        if guard.sleep_minutes > max_min:
            sleepy_king = guard
            max_min = guard.sleep_minutes
        top_min, value = max(enumerate(guard.top_minutes), key=operator.itemgetter(1))
        if value > most_slept_min_val:
            sleepy_ambtenaar = guard
            most_slept_min_val = value    
            most_slept_min = top_min    

    top_min, value = max(enumerate(sleepy_king.top_minutes), key=operator.itemgetter(1))    
        
    # return sleepy_king.id, max_min, top_min, int(sleepy_king.id) * top_min
    return sleepy_ambtenaar.id, most_slept_min, int(sleepy_ambtenaar.id) * most_slept_min

print time_is_ticking()