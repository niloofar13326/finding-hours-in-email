fh=open('mbox-short.txt')
count=0
dic={}
for line in fh:
    find_line = line.split(' ')

    if 'From' in find_line:

        indx = find_line.index('From')
        if '@' in find_line[indx + 1]:
            dic[find_line[6][:2]]=dic.get(find_line[6][:2],0)+1

tmp=sorted(dic.items())
for k,v in tmp:
    print(k,v)
