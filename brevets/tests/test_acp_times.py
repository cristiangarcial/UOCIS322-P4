"""
Nose tests for vocab.py
"""
import arrow
import acp_times
import nose    # Testing framework
import logging
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)

START_TIME = arrow.get('2021-01-01T01:00', "YYYY-MM-DDTHH:mm")

arrow.get(start_time, "YYYY-MM-DDTHH:mm")
def test_opening():
    correct_open_time_1 = START_TIME
    correct_open_time_2 = START_TIME.shift(hours=+7, minutes=+27)

    output_open_1 = acp_times.open_time(0, 200, START_TIME)
    output_open_2 = acp_times.open_time(250, 200, START_TIME)

    assert correct_open_time_1 == output_open_1
    assert correct_open_time_2 == output_open_2

def test_closing():
    correct_close_time_1 = START_TIME.shift(hour=+1)
    correct_close_time_2 = START_TIME.shift(hours=+16, minutes=+40)

    output_close_1 = acp_times.close_time(0, 200, START_TIME)
    output_close_2 = acp_times.close_time(250, 200, START_TIME)

    assert correct_close_time_1 == output_close_1
    assert correct_close_time_2 == output_close_2

def test_edgecases():
    correct_close_time_1 = START_TIME.shift(hour=+3, minutes=+40)

    output_close_1 = acp_times.open_time(200, 200, START_TIME)

    assert correct_close_time_1 == output_close_1


def test_edgecases_2():
    correct_close_time_1 = START_TIME.shift(hour=+26, minutes=+40)

    output_close_1 = acp_times.open_time(400, 400, START_TIME)

    assert correct_close_time_1 == output_close_1


