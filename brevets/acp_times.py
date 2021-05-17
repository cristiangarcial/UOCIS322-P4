"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow

MIN_SPEED = [(200, 15), (400, 15), (600, 15), (1000, 11.428), (1300, 13.333)]
MAX_SPEED = [(200, 34), (400, 32), (600, 30), (1000, 28), (1300, 26)]
MIN_TIME = [800, 1600, 2400, 4500]
MAX_TIME = [352.94, 727.94, 1127.94]
BEFORE_60_SPEED = 20
FRACTIONAL_MULT = 60
#  You MUST provide the following two functions
#  with these signatures. You must keep
#  these signatures even if you don't use all the
#  same arguments.
#


def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
       brevet_dist_km: number, nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  A date object (arrow)
    Returns:
       A date object indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    hour_shift = 0
    minute_shift = 0
    brev_adder = 0

    if control_dist_km > (brevet_dist_km * 1.2):
        print("Error!")
        return -1
    if control_dist_km <= 200:
        brev_adder = control_dist_km / MAX_SPEED[0][1]
        hour_shift = int(brev_adder)
        minute_shift += ((brev_adder - int(brev_adder)) * FRACTIONAL_MULT) + (hour_shift*60)
        return brevet_start_time.shift(minutes=+minute_shift)
    elif control_dist_km <= 400:
        minute_shift = MIN_TIME[0]  
        brev_adder = control_dist_km / MAX_SPEED[1][1]
        hour_shift = int(brev_adder)
        minute_shift += ((brev_adder - int(brev_adder)) * FRACTIONAL_MULT) + (hour_shift*60)
        return brevet_start_time.shift(minutes=+minute_shift)
    elif control_dist_km <= 600:
        minute_shift = MIN_TIME[1]  
        brev_adder = control_dist_km / MAX_SPEED[2][1]
        hour_shift = int(brev_adder)
        minute_shift += ((brev_adder - int(brev_adder)) * FRACTIONAL_MULT) + (hour_shift*60)
        return brevet_start_time.shift(minutes=+minute_shift)
    elif control_dist_km <= 1000:
        minute_shift = MIN_TIME[2]  
        brev_adder = control_dist_km / MAX_SPEED[3][1]
        hour_shift = int(brev_adder)
        minute_shift += ((brev_adder - int(brev_adder)) * FRACTIONAL_MULT) + (hour_shift*60)
        return brevet_start_time.shift(minutes=+minute_shift)
    elif control_dist_km <= 1300:
        minute_shift = MIN_TIME[3]  
        brev_adder = control_dist_km / MAX_SPEED[4][1]
        hour_shift = int(brev_adder)
        minute_shift += ((brev_adder - int(brev_adder)) * FRACTIONAL_MULT) + (hour_shift*60)
        return brevet_start_time.shift(minutes=+minute_shift)

def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
          brevet_dist_km: number, nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  A date object (arrow)
    Returns:
       A date object indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    if control_dist_km > (brevet_dist_km * 1.2):
        print("Error!")
        return -1 
    hour_shift = 0
    minute_shift = 0
    brev_adder = 0
    
    if control_dist_km <= 60:
        minute_shift += 60
        brev_adder = control_dist_km / BEFORE_60_SPEED
        hour_shift = int(brev_adder)
        minute_shift += ((brev_adder - int(brev_adder)) * FRACTIONAL_MULT) + (hour_shift*60)
        return brevet_start_time.shift(minutes=+minute_shift)
    else:
        if control_dist_km <= 200:
            brev_adder = control_dist_km / MIN_SPEED[0][1]
            hour_shift = int(brev_adder)
            minute_shift += ((brev_adder - int(brev_adder)) * FRACTIONAL_MULT) + (hour_shift*60)
            if control_dist_km == 200:
                minute_shift += 10
            return brevet_start_time.shift(minutes=+minute_shift)
        elif control_dist_km <= 400:
            minute_shift = MIN_TIME[0]  
            brev_adder = control_dist_km / MIN_SPEED[1][1]
            hour_shift = int(brev_adder)
            minute_shift += ((brev_adder - int(brev_adder)) * FRACTIONAL_MULT) + (hour_shift*60)
            return brevet_start_time.shift(minutes=+minute_shift)
        elif control_dist_km <= 600:
            minute_shift = MIN_TIME[1]  
            brev_adder = control_dist_km / MIN_SPEED[2][1]
            hour_shift = int(brev_adder)
            minute_shift += ((brev_adder - int(brev_adder)) * FRACTIONAL_MULT) + (hour_shift*60)
            return brevet_start_time.shift(minutes=+minute_shift)
        elif control_dist_km <= 1000:
            minute_shift = MIN_TIME[2]  
            brev_adder = control_dist_km / MIN_SPEED[3][1]
            hour_shift = int(brev_adder)
            minute_shift += ((brev_adder - int(brev_adder)) * FRACTIONAL_MULT) + (hour_shift*60)
            return brevet_start_time.shift(minutes=+minute_shift)
        elif control_dist_km <= 1300:
            minute_shift = MIN_TIME[3]  
            brev_adder = control_dist_km / MIN_SPEED[4][1]
            hour_shift = int(brev_adder)
            minute_shift += ((brev_adder - int(brev_adder)) * FRACTIONAL_MULT) + (hour_shift*60)
            return brevet_start_time.shift(minutes=+minute_shift)
