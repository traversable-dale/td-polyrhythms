import os

class module_polyrhthm :

	def __init__ (self, ownerComp):
		self.ownerComp = ownerComp
		
	def SyncRhythms(self):
		print(f"POLYRHYTHM | SyncRhythms(): {me.name}")
		table = op('select_lfos')
		for row in table.rows():
			op_name = row[0].val  # value from column 0
			target = op(op_name)  # get the actual operator
			if target and hasattr(target.par, 'play'):
				target.par.resetpulse.pulse()
		return
