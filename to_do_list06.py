# To do-list  
list_work=["learning","excercise","coding","meditation","reading","running"]
#list of working to do list.	
work=input("Enter work: ").lower().strip()
if work=="learning":
   print("good do this.")
elif work=="excercise":
   print("Great")
elif work=="coding":
   print("Addon")
elif work=="meditation":
   print("good mental excercise")
elif work=="reading":
   print("mentality")
elif work=="running":
   print("physical exercise")
else:
   print("Work is not in list")
status=input("Enter status of work: ").lower().strip()
if status =="done":
	print("good you are progressing")
elif status =="still working":
	print("Go to work complete")
elif status == "thinking":
	print("time waste only ")
else:
	print("invalid")