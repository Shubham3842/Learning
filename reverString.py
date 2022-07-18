def reverString(s: str):
    stack = []
    reverse_s = ""

    for i in range(len(s)):
        stack.append(s[i])

    while stack:
        reverse_s+=stack.pop()
    return reverse_s

if __name__=='__main__':
    s = "abcnd"
    print(reverString(s))