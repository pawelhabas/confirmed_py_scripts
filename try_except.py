#   Some common try / except modules

#   Basic try
try:
    print(1/0)
except Exception as e:
    if type(e) == ZeroDivisionError:
        print(type(e),'|',e)
        # return (type(e),str(e))
    elif type(e) == TypeError:
        print(type(e),'|',e)
        # return (type(e),str(e))
    elif type(e) == ValueError:
        print(type(e),'|',e)
        # return (type(e),str(e))
    else:
        print(type(e),'|',e)
        # return (type(e),str(e))
else:
    print('No error occured')
finally:
    print('try is done')

#   Rasie an error
try:
    raise NameError('HiThere')
except:
    pass

#   file exceptions modules
try:
    plik = open('temp.py',encoding='abc')
except UnicodeError as e:
    print(type(e),'|',e)
except FileNotFoundError as e:
    print(type(e),'|',e)
except Exception as e:
    print(type(e),'|',e)
