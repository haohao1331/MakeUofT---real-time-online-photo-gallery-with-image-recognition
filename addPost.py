def addImport(filename, picname):
    f = open(filename, "r")
    content = f.readlines()
    for i in range(0,len(content),1):
        if content[i][0]=="\\":
            insertline = "import pic" + picname[3] + " from '../Image/" + picname + "';"
            content.insert(i+1, insertline)
            content.insert(i+2, )
            break
    
    # print(content)