try:
	inp = raw_input("Enter Hours:")
	Hours = float(inp)
	inp = raw_input("Enter Rate:")
	Rate = float(inp)
	
except:
	print "Error, Please enter numeric input"
	quit()
	
print Rate, Hours
if Hours <= 40:
	pay = Rate * Hours
else:
	pay = Rate *40 + (Rate * 1.5 * (Hours - 40))
print pay
	