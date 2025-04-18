# OrderedDict
# It remembers the order of insertion

from collections import OrderedDict, defaultdict

#Normal Dict order is not maintained - the list is small so its not visible
#d ={"address" : "DE", "name" : "Alex", "age" : "78", "id" : "123"}
d = dict()
d["age"] = 78
d["name"] = "Alex"
d["age"] = 67
d["address"] = "DE"
d["id"] = "123"
print(d)

#OrderedDict maintains order
od = OrderedDict()
od['apple'] = 2
od['orange'] = 1
od['kiwi'] = 3
print(od)

#defaultdict
dd=defaultdict(int)
print(dd)