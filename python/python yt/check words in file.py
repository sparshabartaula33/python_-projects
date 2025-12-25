def check():
        word="learning"
        with open("practice.txt","r") as f:
         
         data = f.read()
        if (data.find(word) != -1):
            print("The word is present in the file")    
        else:
            print("there is no such word in the file")
check()

def check_line():
    word="java"
    data = True
    lineno =1
    with open("practice.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(lineno)
            lineno+=1
    return -1

check_line()    
        