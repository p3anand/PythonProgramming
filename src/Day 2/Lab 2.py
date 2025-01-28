# Learning print function:
# def print(self, *args, sep=' ', end='\n', file=None):  # known special case of print

print ("Hello","This","is","a","trial",123,True,78.9)

#sep
print ("Hello","This","is","a","trial",123,True,78.9,sep='-')
print ("Hello","This","is","a","trial",123,True,78.9,sep='|')

# end="-"
print("Hello",end="=")
print("There")