import operator
def calculate(rever_pol):
	operations = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
	stack = []
	for e in rever_pol:
		if isinstance( e, int ):
			stack.append(e)
		else: 
			stack.append(operations[e](stack.pop(-2),stack.pop(-1)))
	return stack[0]

# print(calculate([8,2,5,'*','+',1,3,2,'*','+',4,'-','/']))
