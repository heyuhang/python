x = dict4ini.DictIni('./ConfigParser/config.ini')
print x['portal']['url']
print x.default.url

x.portal.newvalue = 'value'
x.save()
