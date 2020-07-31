def walk_once(command,num,loc):
    #check structure
    if command == 'A':
        loc[0] = loc[0] - num
    elif command == 'D':
        loc[0] = loc[0] + num
    elif command == 'W':
        loc[1] = loc[1] + num
    else:
        loc[1] = loc[1] - num
    return
        
        
def walk(s):
    fin_loc = [0,0]
    lens = len(s)
    for i in range(lens):
        bin_s = s[i]
        lens = len(bin_s)
        print(bin_s)
        if lens<=1 or lens>3:
            continue
        elif bin_s[0] not in ['A','D','W','S']:
            continue
        elif bin_s[1] == '0':
            continue
        elif bin_s[1:].isdigit():
            num = int(''.join(bin_s[1:]))
            walk_once(bin_s[0],num,fin_loc)
            print(fin_loc)
    return fin_loc
try:
    while(True):
        s = input()
        while not s:
            break
        s = s.split(';')
        loc = walk(s)
        print('{:d},{:d}'.format(loc[0], loc[1]))
except:
    pass