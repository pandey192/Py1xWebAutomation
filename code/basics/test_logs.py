#Loging means -  Capture the details, which are usefull while debuging

#and show the user details about execution of program

#warning to the users
#Information to the users
#Error ,criticals error user, Info

import logging

def test_print_logs():
    LOGGER = logging.getLogger(__name__)

    #Intentional logging to user

    LOGGER.info("This is the information logs")
    LOGGER.warning("This is the warning logs")
    LOGGER.error("This is Error Logs")
    LOGGER.critical("This is the Critical logs")
