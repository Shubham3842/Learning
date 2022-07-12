from ArrayStack import ArrayStack

def ismatchedhtml(raw):
    S = ArrayStack()
    j = raw.find('<')
    #print(j)
    while j != -1:
        k = raw.find('>',j+1)
        #print(k)
        if k == -1:
            return False
        tag = raw[j+1:k]
        #print(tag)

        if not tag.startswith('/'):
            S.push(tag)
        else:
            if S.is_empty():
                return False
            if tag[1:] != S.pop():
                return False
        j = raw.find('<',k+1)
    return S.is_empty()    

html = "<body><center><h1>The Little Boat</h1></center></body>"

b = ismatchedhtml(html)
print(b)