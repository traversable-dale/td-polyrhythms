def onInitialize(timerOp, callCount):
	return 0

def onReady(timerOp):
	return
	
def onStart(timerOp):
	print(f"CONFIG | STARTING: {me.name}")
	op.splash.par.display = 1
	op.splash.par.opacity = 1
	op.splash.op('splash_ctrl')['opacity','val'] = 0
	op.splash.op('filter_opacity').par.width = 0
	

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
	op.splash.op('filter_opacity').par.width = 1
	op.splash.op('splash_ctrl')['opacity','val'] = 1
	op.config.op('timer_splash_wait').par.start.pulse()
	return

def onSubrangeStart(timerOp):
	return

	