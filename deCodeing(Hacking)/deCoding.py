message = input("please enter your message: ").upper();
letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
file = open("A:\project & example python\project\deCodeing(Hacking)\words.txt","r");
readFile = file.readlines();
newFile = [];
for i in readFile:
    i=i.upper();
    newFile.append(i);
maxp = 0;
for key in range(len(letter)):
 deCode = ""
 for i in message : 
    if i in letter:
        num = letter.find(i);
        num-=key;
        if num <0:
            num+=len(letter);
        deCode+=letter[num];
    else:
        deCode+=i;
 deCodeList=deCode.split();
 counter = 0;
 for j in deCodeList:
    if j+"\n" in newFile:
        counter+=1;
 p = (counter/len(deCodeList))*100;
 if p > maxp:
    maxp = p;
    keyResult = key;
    deCodeResult = deCode;
print(f"key is {keyResult} and deCode is {deCodeResult} ")
        