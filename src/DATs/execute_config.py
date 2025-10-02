def onStart():
	print(f"CONFIG | onStart: {me.name}")
	op.App.par.performance.pulse()
	op.GUI.Startup()
	op.audio.StopAudio()
	op.config.op('project_res')['project_resX','val'] = 400
	op.config.op('project_res')['project_resY','val'] = 200
	return

def onCreate():
	return

def onExit():
	return

def onFrameStart(frame):
	return

def onFrameEnd(frame):
	return

def onPlayStateChange(state):
	return

def onDeviceChange():
	return

def onProjectPreSave():
	return

def onProjectPostSave():
	return

	