import os

class module_audio :

	def __init__ (self, ownerComp):
		self.ownerComp = ownerComp
		
	def StopAudio(self):
		print(f"AUDIO | StopAudio(): {me.name}")
		table = op('select_audio_files')
		for row in table.rows():
			op_name = row[0].val  # value from column 0
			target = op(op_name)  # get the actual operator
			if target and hasattr(target.par, 'play'):
				target.par.play = 0
		return
	
	def PlayAudio(self):
		print(f"AUDIO | StartAudio(): {me.name}")
		table = op('select_audio_files')
		for row in table.rows():
			op_name = row[0].val  # value from column 0
			target = op(op_name)  # get the actual operator
			if target and hasattr(target.par, 'play'):
				target.par.play = 1
		return
			