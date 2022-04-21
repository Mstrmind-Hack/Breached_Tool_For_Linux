import os,time
os.system('clear')
filenames = ["Banner2.txt","Banner3.txt"]
frames = [] #empty dictionary

for name in filenames:
    with open(name,"r",encoding="utf8") as f:
        frames.append(f.readlines())
for i in range(4): #number of times it circulates
    for frame in frames:
        print("".join(frame))
        time.sleep(0.35) #seconds
        os.system('clear')
            
