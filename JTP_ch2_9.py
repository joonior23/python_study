a = dict()
a['name'] = 'python'
print(a)
a[('a',)] = 'python'    #'Tuple' type can be the 'key'
print(a)
a[[1]] = 'python'   #'List' type can't be the 'key'
print(a)
a[250] = 'python'
print(a)