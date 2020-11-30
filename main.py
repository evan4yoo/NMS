import database
import settings
import time

settings_object = settings.SetConfig()
print(settings_object.dbhost)
#time.sleep(5)
#readback = database.read_db('')
#print(readback)
database.setup()



# First time run
def firsttimesetup():
    print("thing will happen")

def promptsetup():
    while setup_choice:
        setup_choice = input("Do you want to run setup now? y/n", default="yes")
        if setup_choice.lower() == "yes" or "y":
            firsttimesetup()
        elif setup_choice.lower() == "no" or "n":
            print("Ok, Shutting down")
            exit(2)
        else:
            print("type yes or no")