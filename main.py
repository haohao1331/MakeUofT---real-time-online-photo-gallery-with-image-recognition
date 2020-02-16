from addPost import *

a=2
b=15

for i in range(a, b, 1):
    updatePosts("./src/components/Posts.tsx", "pic" + str(i) + ".jpg")
