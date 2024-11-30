#read width,height,names from cmd line
import sys

if len(sys.argv)<5:
    print("Usage: ",sys.argv[0]," <width> <height> <name of the rectngle>")
    exit(1)
else:
    print("You got it ok, let me get to calculations")
width=int(sys.argv[1])
height=int(sys.argv[2])
short_name_1 = sys.argv[3][-5:]
short_name_2 = sys.argv[4][-5:]
short_name = short_name_1+"-"+short_name_2
print("area of rectangle",short_name," is ",width*height)
