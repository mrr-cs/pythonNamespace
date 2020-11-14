def firstFn():
    print('Start firstFn()')
    
    def enclosedFn():
        print('Start enclosedFn()')
        print('End g()')
        return

    enclosedFn() # call
    
    print('End firstFn()')
    return

# driver code
firstFn()