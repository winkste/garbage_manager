""" Garbage Manager is the processing of multiple garbage calendars.

The garbage manager is loading the data from a prettyprint file and is
initializing the garbage calendards. With the garbage calendars it is
checking on each execution if one of the garbages will be collected the
next days. This is notified to the MQTT broker

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""
__modname__     = "Garbage Manager"
__author__      = "Stephan Wink"
__authors__     = ["Stephan Wink"]
__contact__     = "winkste01@gmail.com"
__copyright__   = "Copyright 2023, WShield"
__date__        = "2023/01/19"
__deprecated__  = False
__license__     = "MIT"
__maintainer__  = "Stephan Wink"
__status__      = "Production"
__version__     = "0.0.1"

################################################################################
# Imports
import logging
import pprint
import datetime

import mqtt_ctrl
import cal_data
import garbcal
logging.basicConfig(level=logging.DEBUG,
    format="%(asctime)s - %(filename)s/%(funcName)s(%(lineno)d) - %(levelname)s - %(message)s")
#logging.disable(logging.DEBUG)

################################################################################
# Variables

################################################################################
# Functions
def main():
    """This function starts the main processing.
    """
    garbage_cal_objects:garbcal.GarbageCalendar = []

    # generate garbage calendars
    resi = garbcal.GarbageCalendar("rest", cal_data.rest_cal)
    pap = garbcal.GarbageCalendar("paper", cal_data.paper_cal)
    plas = garbcal.GarbageCalendar("plastic", cal_data.plastic_cal)
    orga = garbcal.GarbageCalendar("organic", cal_data.organic_cal)
    garbage_cal_objects.append(resi)
    garbage_cal_objects.append(pap)
    garbage_cal_objects.append(plas)
    garbage_cal_objects.append(orga)

    # get the actual date and generate time window for checking
    date_before = datetime.datetime.now() - datetime.timedelta(days=2)
    date_after = datetime.datetime.now() + datetime.timedelta(days=3)
    logging.info("Date Range %s -> %s", date_before, date_after)

    # check if next garbage collection is within time window for all garbages
    for garbage_entry in garbage_cal_objects:
        next_date_for_garbage = garbage_entry.get_date_in_range(date_before, date_after)
        garbage_name = garbage_entry.get_garbage_name()
        if next_date_for_garbage is not None:
            logging.info("Next date for %s is at: %s!", garbage_name, next_date_for_garbage)
            mqtt_data = "ON"
        else:
            logging.info("No date in range for %s!", garbage_name)
            mqtt_data = "OFF"
        # populate the retrieved states
        mqtt_ctrl.publish_data(f"std/dev301/s/garbage/{garbage_name}", mqtt_data)


def load_data_from_file():
    """This function loads the data from data file."""


def store_data_to_file():
    """This function stores the data to the data file."""

    rest_cal = ["16.01.23", "30.01.23", "13.02.23", "27.02.23", "13.03.23", "27.03.23",
                "11.04.23", "24.04.23", "08.05.23", "22.05.23", "05.06.23", "19.06.23",
                "03.07.23", "17.07.23", "31.07.23", "14.08.23", "28.08.23", "11.09.23",
                "25.09.23", "09.10.23", "23.10.23", "06.11.23", "20.11.23", "04.12.23",
                "18.12.23"]

    paper_cal = ["23.01.23", "20.02.23", "20.03.23", "17.04.23", "15.05.23", "12.06.23",
                "10.07.23", "07.08.23", "04.09.23", "02.10.23", "30.10.23", "27.11.23",
                "27.12.23"]

    plastic_cal = ["16.01.23", "30.01.23", "13.02.23", "27.02.23", "13.03.23", "27.03.23",
                "11.04.23", "24.04.23", "08.05.23", "22.05.23", "05.06.23", "19.06.23",
                "03.07.23", "17.07.23", "31.07.23", "14.08.23", "28.08.23", "11.09.23",
                "25.09.23", "09.10.23", "23.10.23", "06.11.23", "20.11.23", "04.12.23",
                "18.12.23"]

    organic_cal = ["09.01.23", "23.01.23", "06.02.23", "20.02.23", "06.03.23", "20.03.23",
                "03.04.23", "17.04.23", "02.05.23", "15.05.23", "30.05.23", "12.06.23",
                "26.06.23", "10.07.23", "24.07.23", "07.08.23", "21.08.23", "04.09.23",
                "18.09.23", "02.10.23", "16.10.23", "30.10.23", "13.11.23", "27.11.23",
                "11.12.23", "27.12.23"]

    # open the new file
    with open("test.py", 'w', encoding="utf8") as file_hdl:
        # write the data to the python file using pprint pformat function
        file_hdl.write("rest_cal = " + pprint.pformat(rest_cal) + '\n')
        file_hdl.write("paper_cal = " + pprint.pformat(paper_cal) + '\n')
        file_hdl.write("plastic_cal = " + pprint.pformat(plastic_cal) + '\n')
        file_hdl.write("organic_cal = " + pprint.pformat(organic_cal) + '\n')



def logger_example():
    """Example logging function
    """
    logging.info("This is an info message")
    logging.debug("This is an debug message")
    logging.warning("This is a warning message")
    logging.error("This is a error message")
    logging.critical("This is a critical message")

def print_module_info(info_type:int):
    """Function to print program information at start
    """
    if info_type == 0: #print full information
        print(f"Program Name: {__modname__}")
        print(f"Author of the program: {__author__}")
        print(f"Date: {__date__}")
        print(f"Copyright information: {__copyright__}")
        print(f"License information: {__license__}")
        print(f"Status of program: {__status__}, in Version: {__version__}")

################################################################################
# Classes

################################################################################
# Scripts
if __name__ == "__main__":
    # execute only if run as a script
    print_module_info(0)
    main()
