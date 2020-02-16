def updatePosts(filename, picname, updated):
    f = open(filename, "r")
    content = f.readlines()
    n=0

    compname = nofiletype(picname)

    if compname in updated:
        return False
    updated.append(compname)
    # print(updated)
    # Finding where to add import statement
    for i in range(0,len(content),1):
        if content[i][0]=="\n":
            n = i
            break

    # Finding picture number
    a=3
    picnumber=""
    while isInt(picname[a]):
        picnumber+=str(picname[a])
        a+=1

    insertline = "import " + compname + " from '../Image/" + picname + "';"
    content.insert(n, insertline)
    content.insert(n+1, "\n")
    endinsert = ["  {\n", "    src: " + compname + ",\n", "    width: 4,\n", "    height: 3\n", "  },\n"]
    content.insert(len(content)-1, endinsert[0])
    content.insert(len(content)-1, endinsert[1])
    content.insert(len(content)-1, endinsert[2])
    content.insert(len(content)-1, endinsert[3])
    content.insert(len(content)-1, endinsert[4])

    # for i in range(0, len(content), 1):
    #     print(content[i])
    
    f.close()

    writefile(filename, content)
    return True


def isInt(a):
    if a in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        return True
    else:
        return False


def nofiletype(a):
    # elliminates the .jpg in a file name
    n = 0
    for i in range(0, len(a), 1):
        if a[i]==".":
            n = i
            break
    return a[0:n]


def writefile(filename, content):
    f = open(filename, "w")
    for i in range(0, len(content), 1):
        f.write(content[i])


def restart(filename):
    f = open(filename, "r")
    content = f.readlines()
    
    write = content[0:3]

    # Find import statement ending position
    n = 0
    for i in range(0, len(content), 1):
        if content[i][0]=="\n":
            n = i
            break
    for i in range(n, len(content), 1):
        if content[i][0]!="e":
            write = write + [content[i]]
        else:
            n = i
            break

    write = write + content[n:n+13] + [content[len(content)-1]]
    f.close()

    writefile(filename, write)

    return True
