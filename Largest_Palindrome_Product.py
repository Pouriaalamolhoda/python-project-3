pali = []
for i in range(100,1000):
    
    for j in range(100,1000):
        
        num = str(i * j)
        if len(num) == 6 :
            if num[0] == num[len(num) - 1]:
                if num[1] == num[len(num)-2] :
                    if num[2] == num[len(num) - 3] :
                        # print('{} * {} = {}'.format(i, j, num))
                        pali.append(num)
                        
max_val = pali[0]
for k in pali :
    if k > max_val:
        max_val = k

        
print('result = {}'.format(max_val))

    
# problem : find i * j for 906609
# problem2 : use dictionary in this
# not enough comments
