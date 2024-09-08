def all_variants(text):
    for i in range(len(text)):
        for j in range(len(text)-i):
            slice=text[j:j + i + 1]
            yield slice


a = all_variants("abc")
for i in a:
    print(i)