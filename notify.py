import subprocess


def sendmessage(Title,Message):
	subprocess.Popen(['notify-send',Title,Message])
	return
