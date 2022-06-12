
class AlarmClock:
    def __init__(self):
        self.clock_time = ()
        self.alarm_time = ()
        self.alarm_set = ()
        self.change_clock_time()
    
    def change_clock_time(self):
        self.clock_time = input(f"Set clock time to: ")
        self.display_clock_time()

    def display_clock_time(self):
        print(f"The clock is currently set to " {self.clock_time})


    def change_alarm_time(self):
        self.alarm_time = input(f"Set alarm time to: ")
        self.display_alarm_time()


    def display_alarm_time(self):
        print(f"The alarm time is set to " {self.alarm_time})


    def turn_alarm_on(self):
        self.alarm_set = False
        if input(f"Turn on alarm? y/n ") == "y":
            self.alarm_set = True
            print(f"Alarm is currently on.")
        else:
            self.alarm_set = False
            print(f"Alarm is currently off.")



# method to set (or change) the current time & print to console current time
# method to toggle the alarm on or off
# method to set the current alarm time & print to console the current alarm time

