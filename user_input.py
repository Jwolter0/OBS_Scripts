# Simple user input example. Based loosely on [nibalizer/weasley.py] (https://gist.github.com/nibalizer/a6649abee758da3f8d08ef5e164b524c)

from datetime import datetime
import obspython as obs

# I'm not too sure what these assignment statements do, except perhaps create
# the global variables corresponding to the script settings.
# The values in here don't seem to matter because they get overwritten by
# script_defaults (q.v.)
year = 2020
month = 12
day = 31

class ServiceTools():
    '''
    This class contains the routines at the heart of the user's scripting. If 
    it's not part of the user interface, it probably goes here. In this simple
    example, I just format the date elements and write them to the console.
    '''

    def print_date(self):
        global year
        global month
        global day
        date = f"{str(year).zfill(4)}-{str(month).zfill(2)}-{str(day).zfill(2)}"
        print(f"print_date: {date}")


st = ServiceTools()

def print_pressed(props, prop):
    '''
    Action to take when the button is pressed
    '''
    st.print_date()


def script_description():
    '''
    Sets the header for the user interface on the right side of
    the Scripts dialog
    '''
    return "Example of a very simple user interface"


def script_defaults(settings):
    '''
    Sets default values for the settings in the user interface
    '''
    today = datetime.today()
    obs.obs_data_set_default_int(settings, "year", today.year)
    obs.obs_data_set_default_int(settings, "month", today.month)
    obs.obs_data_set_default_int(settings, "day", today.day)


def script_properties():
    '''
    Creates the user interface on the right side of the Scripts dialog
    '''
    props = obs.obs_properties_create()
    obs.obs_properties_add_int(props,"year","Year:",1980,2100,1)
    obs.obs_properties_add_int(props,"month","Month:",1,12,1)
    obs.obs_properties_add_int(props,"day","Day:",1,31,1)

    obs.obs_properties_add_button(props, "button", "Print Date", print_pressed)
    return props


def script_update(settings):
    '''
    Called when the script settings are changed by the user.
    Copies the settings into global variables so they can be used elsewhere
    '''
    global year
    global month
    global day

    year  = obs.obs_data_get_int(settings, "year")
    month = obs.obs_data_get_int(settings, "month")
    day   = obs.obs_data_get_int(settings, "day")
    # Diagnostics
    date = f"{str(year).zfill(4)}-{str(month).zfill(2)}-{str(day).zfill(2)}"
    print(f"script_update: {date}")

