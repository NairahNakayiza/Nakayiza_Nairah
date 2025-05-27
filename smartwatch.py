class SmartDevice:
    def notify(self):
        print("Device notification")

class SmartWatch(SmartDevice):
    def notify(self):
        print("Vibration on notification for the smart watch")

class SmartPhone(SmartDevice):
    def notify(self):
        print("Pop-up and sound on notification for a smart phone")

class SmartWatchPhone(SmartWatch, SmartPhone):
    pass

device = SmartWatchPhone()
device.notify()  


