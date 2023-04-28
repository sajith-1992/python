s = input ("do you agree:")

s = s.lower()
if s in ["Y","YES"]:
   print("agreed")
if s in ["no","n"]:
   print("not agreed")