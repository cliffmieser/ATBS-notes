def spam():
    global eggs
    eggs = 'spam' #the global

def bacon():
    eggs = 'bacon' #the local

def ham():
    print(eggs) # the global


eggs = 42 # global variable
spam()
print(eggs)