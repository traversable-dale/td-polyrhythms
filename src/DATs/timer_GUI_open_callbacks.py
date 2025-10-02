def onInitialize(timerOp, callCount):
	return 0

def onReady(timerOp):
	return
	
def onStart(timerOp):
	print(f"CONFIG | STARTING: {me.name}")
	return
	
def onTimerPulse(timerOp, segment):
	return

def whileTimerActive(timerOp, segment, cycle, fraction):
	return

def onSegmentEnter(timerOp, segment, interrupt):
	return
	
def onSegmentExit(timerOp, segment, interrupt):
	return

def onCycleStart(timerOp, segment, cycle):
	return

def onCycleEndAlert(timerOp, segment, cycle, alertSegment, alertDone, interrupt):
	return
	
def onCycle(timerOp, segment, cycle):
	return

def onDone(timerOp, segment, interrupt):
	print(f"CONFIG | DONE: {me.name}")
	return

def onSubrangeStart(timerOp):
	return

	