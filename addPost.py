def updatePosts(filename, picname):
    f = open(filename, "r")
    content = f.readlines()
    n=0
    for i in range(0,len(content),1):
        if content[i][0]=="\n":
            n=i
            break
    
    insertline = "import " + picname[0:4] + " from '../Image/" + picname + "';"
    content.insert(n, insertline)
    content.insert(n+1, "\n")
    endinsert = ["  {\n", "    src: " + picname[0:4] + ",\n", "    width: 4,\n", "    height: 3\n", "  },\n"]
    content.insert(len(content)-1, endinsert[0])
    content.insert(len(content)-1, endinsert[1])
    content.insert(len(content)-1, endinsert[2])
    content.insert(len(content)-1, endinsert[3])
    content.insert(len(content)-1, endinsert[4])

    # for i in range(0, len(content), 1):
    #     print(content[i])
    
    f.close()
    f = open(filename, "w")
    for i in range(0, len(content), 1):
        f.write(content[i])
    print(content)
    return True
