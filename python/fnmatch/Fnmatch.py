import fnmatch

print fnmatch.fnmatch('*py', '*.py')
print fnmatch.fnmatch('title.py', '*.py')

names = ['dlsf','ewro.txt','te.py','youe.py']
#/////
print fnmatch.filter(names,'*.py')

print fnmatch.filter(names,'[de]')

print fnmatch.filter(names,'[de]*')
#/////
print fnmatch.fnmatchcase('readme','R*')

print fnmatch.fnmatchcase('Readme','R*')
#/////
print fnmatch.translate('*.py')

