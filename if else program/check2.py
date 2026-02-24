n=int(input("enter number"))
if n<=9:
	print("number is single digit")
elif n>9 and n<1000:
	print("number is double digit")
elif n>=100 and n<1000:
    print("number is triple digit")
else:
    print("other number")
	