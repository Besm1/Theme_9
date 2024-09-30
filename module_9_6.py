def all_variants(text: str):
    ln = 1
    while ln <= len(text):
        i = 0
        while i <= len(text)-ln:
            yield text[i: i + ln ]
            i += 1
        ln += 1

v = all_variants('abcd')


for v_ in v:
    print(v_)

