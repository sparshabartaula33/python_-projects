def find():
    word = "twinkle"
    with open("poem.txt","r") as f:
        data = f.read()
        if(data.find(word)!= -1 ):
            print("found")
        else:
            print("not found")
find()