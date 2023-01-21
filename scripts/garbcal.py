""" This module handle the garbage calendar for one type of garbage.

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

__author__ = "Stephan Wink"
__contact__ = "winkste01@gmail.com"
__copyright__ = "Copyright $2023, $WShield"
__date__ = "2023/01/18"
__deprecated__ = False
__license__ = "MIT"
__maintainer__ = "Stephan Wink"
__status__ = "Development"
__version__ = "0.0.1"

################################################################################
# Imports
import datetime
import logging

logging.basicConfig(level=logging.DEBUG,
    format="%(asctime)s - %(filename)s/%(funcName)s(%(lineno)d) - %(levelname)s - %(message)s")
#logging.disable(logging.DEBUG)

################################################################################
# Variables

################################################################################
# Functions

################################################################################
# Classes
class GarbageCalendar:
    """
    A class to represent a garbage calendar including type and
    the list of dates where garbage is collected

    ...

    Attributes
    ----------
    garbage_name : str
        a formatted string of the garbage name
    garbage_calendar : List
        a list of all dates of the garbage collection


    Methods
    -------
    get_garbage_name()
        Returns the name of the garbage calendar

    print_dates()
        Print all dates stored in the garbage calendar

    get_date_in_range(date_before, date_after)
        Returns the first date that is in range of date_before and date_after.
        Returns None if there is no date in range.
    """

    ############################################################################
    # Member Functions

    def __init__(self, name:str, cal_strings:list):
        """ This is the object initialization method. """
        self.garbage_name = name
        self.garbage_calendar = []
        self._generate_calendar(cal_strings)

    def get_garbage_name(self) -> str:
        """Returns the object name

        Return
        ------
        str : Name of the object
        """
        return self.garbage_name

    def print_dates(self):
        """Prints the dates stored in the garbage calendar
        """
        for date_item in self.garbage_calendar:
            print(date_item.strftime("%d.%m.%Y"))

    def get_date_in_range(self, before_date, after_date):
        """Returns first date if date is within range, else None
        """
        for date_item in self.garbage_calendar:
            # check if the date iteration is within the given range
            if date_item > before_date and date_item < after_date:
                return date_item

    def _generate_calendar(self, cal_string:list):
        """generates a python list from comma separated dates

        Parameters
        ----------
        calendar : list
            List of garbage collection dates comma separated:
            DD.MM.YY, DD.MM.YY
        """
        for date_item in cal_string:
            self.garbage_calendar.append(datetime.datetime.strptime(date_item, "%d.%m.%y"))


################################################################################
# Scripts
if __name__ == "__main__":
    # execute only if run as a main script
    print("--- test the garbage_manager module ---")
    GARBAGE_NAME = "Rest"
    cal = ["16.01.23", "30.01.23", "13.02.23",
                "27.02.23", "13.03.23", "27.03.23",
                "11.04.23", "24.04.23", "08.05.23",
                "22.05.23", "05.06.23", "19.06.23",
                "03.07.23", "17.07.23", "31.07.23",
                "14.08.23", "28.08.23", "11.09.23",
                "25.09.23", "09.10.23", "23.10.23",
                "06.11.23", "20.11.23", "04.12.23",
                "18.12.23"]

    garb_mgr = GarbageCalendar(GARBAGE_NAME, cal)

    print(f"Garbage Calendar name: {garb_mgr.get_garbage_name()}")
    garb_mgr.print_dates()
    date = datetime.datetime.strptime("05.06.24", "%d.%m.%y")
    date_before = date - datetime.timedelta(days=3)
    date_after = date + datetime.timedelta(days=5)
    print(garb_mgr.get_date_in_range(date_before, date_after))
