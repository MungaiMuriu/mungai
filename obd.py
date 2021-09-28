from obd import OBD
from at_commands import *


def setup():
	adapters = scanner.scan("OBD")
	if len( adapters ) == 0:
		print ("[!]\tNo adapters were found that have 'OBD' in their name.\nExiting...")
	else:
		global adapter
		adapter = OBD( type="bluetooth", addr=adapters[0]['addr'], name=adapters[0]['name'], baud=BAUD )
		adapter.bind()
		adapter.connect()
		print(SendOBD("ate0"))
		print(SendOBD("atl0"))
		print(SendOBD("ath0"))

def bluetooth():
    adapters = scanner.scan("OBD")

    if len(adapters) == 0:
        print
        "[!]\tNo adapters were found that have 'OBD' in their name.\nExiting..."

    # Adapters were found.
    else:
        # Grab the first adapter returned.
        # adapter = OBD( adapters[0]['addr'], adapters[0]['name'], BAUD )
        adapter = OBD(type="bluetooth", addr=adapters[0]['addr'], name=adapters[0]['name'], baud=BAUD)
        adapter.bind()
        adapter.connect()

 def run(self):
        print ("\tOBDReader: connecting...")

        #init
        connection = OBD('/dev/ttyUSB1')
        if not connection.is_connected():
            print ("\tOBDReader: Error: could not connecto to vehicle")
            connection = OBD(self.port)
            if not connection.is_connected():
                print("\tOBDReader: Error: could not connect to obdsim")
                return
        self.connected = True

        #print "\treadOBD thread connected. Entering main loop."
        #main loop
        while not self.stopped():
            STATUS = connection.query(commands.STATUS) # MIL: bool, DTC_count int
            MAF = connection.query(commands.MAF) # grams/sec
            SPEED = connection.query(commands.SPEED) # kph
            THROTTLE_POS = connection.query(commands.THROTTLE_POS) # %
            RPM = connection.query(commands.RPM) # rpm
            COOLANT_TEMP = connection.query(commands.COOLANT_TEMP) # deg C
            GET_DTC = connection.query(commands.GET_DTC) # [('code','desc')]
            print "|%s|" % GET_DTC

            SharedData.lock.acquire()
            try:
                SharedData.MIL = STATUS.value.MIL                     if not STATUS.is_null()         else None
                SharedData.DTC_count = STATUS.value.DTC_count         if not STATUS.is_null()         else None
                SharedData.MAF = MAF.value                      if not MAF.is_null()            else None
                SharedData.SPEED = SPEED.value                  if not SPEED.is_null()          else None
                SharedData.THROTTLE_POS = THROTTLE_POS.value    if not THROTTLE_POS.is_null()   else None
                SharedData.RPM = RPM.value                      if not RPM.is_null()            else None
                SharedData.COOLANT_TEMP = COOLANT_TEMP.value    if not COOLANT_TEMP.is_null()   else None
                SharedData.GET_DTC = GET_DTC.value              if not GET_DTC.is_null          else None
            finally:
                SharedData.lock.release()

        connection.close()
        print ("\tOBDReader: disconnected.")


HIREKEN_MAC_ADDR = '00:1D:A5:00:03:43'

adapter = OBD()
adapter.scan()
adapter.connect_specific(HIREKEN_MAC_ADDR)
adapter.connect()

print(adapter.send_obd(DESC_PROTOCOL)
print(adapter.send_obd(ECHO_OFF)
print(adapter.send_obd(DISP_DEV_ID)
print(adapter.send_obd(REPEAT_CMD)
print(adapter.send_obd('010C')
print(adapter.send_obd(WARM_START)
print(adapter.send_obd('010C')

adapter = OBD_User()
adapter.connect()

print (adapter.send_obd(WARM_ATART)