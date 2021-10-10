N = int(input())
table = []

for i in range(N):
    tower = {}
    tower['i'] = i+1
    arr = list(map(int, input().split()))
    tower['k'] = arr[0]
    tower['a'] = arr[1:] #### ???? ####
    print(tower['a']) #### ???? ####
    tower['s'] = tower['k']
    for j in tower['a']: #######################
        tower['s'] = pow(tower['s'], j) #######################
        #print(tower['s']) #######################
    table.append(tower)

for i in range(N):
    for j in range(i+1, N):
        if table[i]['s'] > table[j]['s']:
            table[j], table[i] = table[i], table[j]

string = ''
for i in table:
    string += (str(i['i']) + ' ')

print(string)
