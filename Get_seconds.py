def get_seconds(hours):
	minutes = hours * 60
	seconds = minutes * 60
	return seconds

def get_seiru(sec):
    return sec/50.5

h = float (input("Enter a numbre of hours: "))
s = get_seconds(h)
print("There are", s, "seconds in", h, "hour(s)")

print(h,"hour(s) are",
      get_seiru(get_seconds(h)), "seiru")
