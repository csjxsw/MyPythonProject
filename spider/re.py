import re
some_text = 'alpha , beta ,,,gamma delta '
res = re.split('[,]+', some_text)
print res

pat = '[a-zA-Z]+'
text = '"Hm...err -- are you sure?" he said, sounding insecure.'
res = re.findall(pat, text)
print res

pat = '{name}'
text = 'Dear {name}...'
res = re.sub(pat, 'Mr. Gumby',text)
print res

m = re.match(r'www\.(.*)\..{3}', 'www.python.org')
res = m.group()
print res

