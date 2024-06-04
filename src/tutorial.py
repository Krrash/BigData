test={'hello':4, 'world':5, 'kaushal': 7}
test2={}

for key,value in test.copy().items():
    if value==5:
        del test[key]
print(test)



    

