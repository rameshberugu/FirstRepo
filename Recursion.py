
# counting items in list using recursion
def count(ls):
    if not ls:
        return 0
    length = 1 + count(ls[1:])
    return length


l = [1, 2, 3, 4]
print("count ", count(l))

# learning If 0  and If [] returns false
