import subprocess
import os

def sendmessage(Title,Message):
	killNotify()
	subprocess.Popen(['notify-send',Title,Message])
	
def killNotify():
	killer = subprocess.Popen(['killall', 'notify-osd'])
	killer.wait()

