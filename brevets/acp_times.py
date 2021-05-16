"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow

MIN_SPEED = [(200, 15), (400, 15), (600, 15), (1000, 11.428), (1300, 13.333)]
MAX_SPEED = [(200, 34), (400, 32), (600, 30), (1000, 28), (1300, 26)]
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
    return arrow.now()


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
    hour_shift = 0
    minute_shift = 0

    if (control_dist_km <= 60):
        hour_shift += 1
        brev_adder = control_dist_km / BEFORE_60_SPEED
        hour_shift += int(brev_adder)
        minute_shift += (brev_adder - int(brev_adder)) * FRACTIONAL_MULT
        return_brev_time = brevet_start_time.shift(hours=+hour_shift)
        return return_brev_time.shift(minutes=+minute_shift)
    else:
        return arrow.now()
