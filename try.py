try:
    file=open('eeee','r+')
except Exception as e:
    print('there is no file named as eeee')
    try:
        response=input('do you want to create a new file')
        if response=='y':
            file=open('eeee','w')
        else:
            print('please do something')
    except Exception as a:
        print('a')
        
else:
    file.write('assa')
try:
    file.close()
except Exception as c:
        print(c)
