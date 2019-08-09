#create a log file
#open the log file
#read each line in log file
#check if the line contains warnings ( find warnings )
#count if warning is present:  or go to next line
#stop at end of file. ( 0 bytes )

fd=open("jerulog.txt","r+")  # opens the text file.
count1=0
for line in fd.readlines():  # reads the file line by line 
    length=len(line)
    print(line) #prints the lines
    if line.find("warning") != -1: #check if line contains warning word
        count1=count1+1
    elif(length<=0):
        break
print(count1)
print("No.of.warnings in log file1:",count1)
        
fd.close()

fd1=open("jerulog2.txt","r+")  # opens the text file.
count2=0
for line in fd1.readlines():  # reads the file line by line 
    
    print(line) #prints the lines
    if line.find("warning") != -1: #check if line contains warning word
        count2=count2+1
    elif(length<=0):
        break

print(count2)
print("No.of.warnings in log file1:",count2)

        
fd1.close()

#comparing the no.of.warnings in two log files
if(count2<count1):
    print("Promoted")
else:
    print("Not Promoted")
