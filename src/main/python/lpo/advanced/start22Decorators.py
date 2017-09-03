
def repeater(old_function):
    def new_function(*args, **kwds): #See learnpython.org/page/Multiple%20Function%20Arguments for how *args and **kwds works
        old_function(*args, **kwds) #we run the old function
        old_function(*args, **kwds) #we do it twice
    return new_function #we have to return the new_function, or it wouldn't reassign it to the value


@repeater
def functions(arg):
    return "Return"

def Double_Out(old_function):
    def new_function(*args, **kwds):
        return 2 * old_function(*args, **kwds) #modify the return value
    return new_function

def Double_In(old_function):
    def new_function(arg): #only works if the old function has one argument
        return old_function(arg*2) #modify the argument passed
    return new_function

def Check(old_function):
    def new_function(arg):
        if arg<0:
            raise ValueError("Negative Argument") #This causes an error, which is better than it doing the wrong thing
        old_function(arg)
    return new_function

def Multiply(multiplier):
    def Multiply_Generator(old_function):
        def new_function(*args, **kwds):
            return multiplier*old_function(*args, **kwds)
        return new_function
    return Multiply_Generator #it returns the new generator

@Multiply(3) #Multiply is not a generator, but Multiply(3) is
def Num(num):
    return num

print(Num(4))

@repeater
def Multiply(num1, num2):
    return num1*num2

print(Multiply(2, 3))



def Double_Out(old_function):
    def new_function(*args, **kwds):
        return 2 * old_function(*args, **kwds) #modify the return value
    return new_function



def type_check(correct_type):
    def decorator(old_function):
        def new_function(arg):
            if type(arg) is correct_type:   # or use : isinstance(object, type_of_object)
                return old_function(arg)  # modify the return value
            else:
                print("Bad Type")
        return new_function

    return decorator

@type_check(int)
def times2(num):
    return num*2

print(times2(2))
times2('Not A Number')

@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
first_letter(['Not', 'A', 'String'])