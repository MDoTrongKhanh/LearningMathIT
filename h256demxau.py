s1 = input()
s = input()
dem = 0
for i in range(len(s) - len(s1) + 1):
    if s[i:i+len(s1)] == s1:
        dem += 1
print(dem)