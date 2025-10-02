def onInitialize(timerOp, callCount):
	return 0

def onReady(timerOp):
	return
	
def onStart(timerOp):
	print(f"CONFIG | STARTING: {me.name}")
	op.splash.op('splash_ctrl')['opacity','val'] = 0
	return

def onDone(timerOp, segment, interrupt):
	print(f"CONFIG | DONE: {me.name}")
	op.config.op('project_res')['project_resX','val'] = 400
	op.config.op('project_res')['project_resY','val'] = 400
	op.GUI.OpenProgram()
	op.splash.par.opacity = 0
	op.splash.par.display = 0
	return

def onSubrangeStart(timerOp):
	return

	