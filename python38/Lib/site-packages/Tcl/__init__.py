def window():
	nohup = open('nohup.tcl', 'x')
	
	nohup.write("")
	nohup.close()

def Lb(text):
	rb = open('nohup.tcl', 'w')

	rb.write('ttk::label .lbl -text "' + text + '" \n')
	rb.close()

def Bn(text):
	rn = open('nohup.tcl', 'w')

	rn.write('grid [ttk::button .mybutton -text ' + text + '] \n')
	rn.close()

def Tl(text):
	rl = open('nohup.tcl', 'w')

	rl.write('wm title .window "' + text + '" \n')
	rl.close()

def size(text):
	re = open('nohup.tcl', 'w')

	re.write('wm geometry .window ' + text + ' \n')

def Mx(text):
	rx = open('nohup.tcl', 'w')

	rx.write('tk_messageBox -message "' + text + '" \n')
	rx.close()

def mainloop():
	import os
	os.system('wish nohup.tcl \n')