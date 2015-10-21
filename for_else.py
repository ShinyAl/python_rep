vegies = ['onion', 'potato', 'pumpkin']
for v in vegies:
    if v == 'tomato':
        print "You can cook a soup"
        break
else:
    print "You forgot to add a tomato in soup"
    vegies.append('tomato')
    print vegies