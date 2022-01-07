def sequence(a, b):
    boolean = True
    c = 0
    if len(a) != len(b):
        print("Size of sequences must be same")
        return False
    else:
        for x in a:
            if a[c] != b[c]:
                boolean = False
            c += 1
        return boolean


a = [1, 2, 'gg', 'wp']
b = [1, 2, 'gg', 'wp']
print(sequence(a, b))





