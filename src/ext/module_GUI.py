import os

class module_GUI :

	def __init__ (self, ownerComp):
		self.ownerComp = ownerComp
		
	def Startup(self):
		#On startup TouchDesigner should open to splash screen
		#After Splash screen there should be a loading screen
		#Program opens fullscreen after that
		print(f"GUI | Startup(): {me.name}")
		op.ctrl_splash.op('splash_ctrl')['opacity','val'] = 0
		op.ctrl_splash.op('filter_opacity').par.width = 0
		op.config.op('timer_splash_startup').par.start.pulse()
		op.splash.par.display = 1

		op.GUI.par.display = 0
		op.vis.par.opacity = 0
		

		op.config.op('timer_splash_startup').par.start.pulse()
		
		pass
	
	def ExitSplash(self):
		op.config.op('timer_splash_exit').par.start()
		return
	
	def OpenProgram(self):
		#open program upon exiting splash screen
		print(f"GUI | OpenProgram(): {me.name}")
		op.GUI.par.display = 1
		op.vis.par.opacity = 1
		op.config.op('timer_GUI_open').par.start.pulse()
		op.ctrl_GUI.op('GUI_ctrl')['opacity','val'] = 1
		op.audio.PlayAudio()
		pass