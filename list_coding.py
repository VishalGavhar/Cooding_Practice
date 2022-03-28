l=[8,6,9,6,5,'Vishal','Ganesh',656,656]

l.sort(key=lambda e:(isinstance(e,str),e))

print(l)