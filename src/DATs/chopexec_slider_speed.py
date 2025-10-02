def onValueChange(channel, sampleIndex, val, prev):
	user_val = op.slider_speed.op('out1')['v1']
	op.colors.op('colors_ctrl')['hue_offset','val'] = user_val
	print(val)
	return
	