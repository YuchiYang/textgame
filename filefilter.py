def compare(list,str):
	r=0
	for i in list:
		if(i.find(str)>=0):
			r=i
	return r

# Define a filename.
filename = "Convo1.txt"

# Open the file as f.
# The function readlines() reads the file.
with open(filename) as f:
	content = f.read().splitlines()

# make an array which will allow us to know which answers correspond to which questions for quick access whhen compared to reading the file multiple times
# first col=qnums following cols point to other questions corresponding to answer selected
# third index is relationship points gained

#step 1 find participant names in chat
# stap 2
special=["block","A","min","max"]
participants=[]
convo=[]
i=0
in_block=0
in_ans=0

# Show the file contents line by line.
for line in content:
	if(participants==[]):
		a=line.find("Participants:")
		if (a>=0):
			t=line[line.find(":")+1:]
			participants=t.split()

	sid=line.find("//")
	if(sid>=0):
		temp=line[sid+2:]
		temp=temp[:]

	else:
		convo.append(i)
		i+=1
		convo[i-1].append

	# print(line)

print(participants)
