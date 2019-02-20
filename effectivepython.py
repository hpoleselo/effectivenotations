import collections
import argparse


print(" ")
print("-------- Book Notes from Effective Python --------")
print(" ")
print("Chapter 2: Methods and Functions, give number 2 as input.")
print("Chapter 3: Classes, give number 3 as input.")
print(" ")
chapter = input("Which chapter do you want to run? ")


if chapter == 2:
    print(" ")
    class NotesChapter2(object):
        def __init__(self):
            self.ten = 10
            self.three = 3
            self.nine = 9
            self.list = [20, 30, 40, 70]
        
        def generator(self):
            """ What is really a generator """
            pass

        def trying_excepting(self):
            """ except gives us the possibility to cleanup our code regardless what happens on the try block! """
            print (" ")
            print ("---- Trying Excepting Finally ---- ")
            try:
                print "Always gonna be executed"
                print self.three > self.nine
                print 4/0
            except:
                print "Only will be called when an exception error is raised. In this case ValueError!"
            else:
                print "Come on... Another error?"
            finally:
                print "Will ALWAYS be executed as well!"

        def handling_exception(self):
            print (" ")
            print "---- Handling Exception ----"
            def divide(a, b):
                try:
                    a/b
                except ZeroDivisionError as e:
                    raise ValueError("Division not possible, invalid inputs")
            x,y = 5,0
            divide(x,y)

        def closure():
            ''' Closure allows us to a function access variables from other function, like in our case we can call
            the helper function and iterate over the values from the main function.
            The flag Found is in Python 2 poorly implemented because we don't have the nonlocal keyword, hence we
            Found as list (mutable). '''
            print (" ")
            print "---- Closure ----"
            def sorting_w_prio(values, group):
                Found = [False]
                def helper(x):
                    # Uncomment the line below if you are using Python 3
                    #nonlocal Found
                    if x in group:
                        Found[0] = True
                        print Found[0]
                        return 0, x
                    return 1, x
                values.sort(key=helper)
            values = [10, 32, 40, 100, 5, 9]
            group = {5, 7, 40, 32}
            sorting_w_prio(values, group)
            print values

        def generator():
            ''' When we iterate over a list and then for every iteration we do, for instance, a squaring operation,
            then we have to store it to a variable... We can use instead generator expression so it iterates but does'nt
            necessarily stores the value (this makes a difference for huge iterations and saves memory. REMINDER:
            We could use a chain of generator expressions, which is quite fast as well. The output of one generator could feed
            the input of another! '''
            print (" ")
            print "---- Generator Expression ----"
            # We store every squared value in the new list called sqd_value
            list = [1, 2, 3, 4, 5, 10 , 20]
            sqd_value = [x**2 for x in list]

            # Here we don't consume so much memory as above
            # But keep in mind that we end up actually using a stateful method, meaning it's only safe to use it once on our code
            gen = (x**2 for x in list)
            print next(gen)
            print next(gen)
            print next(gen)
            print gen
            print type(gen)

        def variable_positional_argument(self, x, y=1, *z):
            ''' Usually we have a function that takes for instance 2 values as arguments, let's say that this function actua-
            lly doesn't need the two values EVERY time it's called. And we want to pass just one argument... So we can use the
            so famous variable position argument VPA. In this function we use x,y,z as inputs for this func. But z is a VPA.
            Note that when printing the read value from z is contained in a tuple.
            Instead of using VPA for some variable that we don't always need to use we could use the keyword and setting it
            to a value that doesn't change the function! Only when set differently, so we set it to a fixed value like z=1.
            IMPORTANT: we use None as pre-defined value on a position argument that is mutable. '''
            print (" ")
            print ("---- Variable Positional Argument ----")
            w = x + 10
            print ("Value of x + 10 = "), w
            print ("Value of y:"), y
            if y != 1:
                print ("The user has given a different value for y: "), y
            print ("Value of z:"), z

        def keywordarguments_are_important(self, **kwargs):
            """ In this case our function doesn't require ANYTHING. But if we want to provide any value,
            we have then to use the keyword assign to the function, otherwise it will complain about it. """
            print (" ")
            print ("---- Testing kwarg ----")
            print ("Printing the keyword arguments given by the user: \n"), kwargs


        def named_tuple(self):
            """ If we want to create a small container, instead of creating a Class we can use the function
            namedtuple(). """
            Point = collections.namedtuple("Point", ["x","y"], verbose=True)

        
        def defaultdict(self):
            """ Works like a mini github where we can differentiate what has been changed! Super. """
            default_list = [10, 20, 30, 40]

        def test_assert(self):
            """ assert is just for testing a condition in Python, if it's not satisfied (returns False)
            and then it raises an AssertError. A short way to validate if something is True or Not!"""
            print (" ")
            print ("---- Testing assert ----")
            print ("Will raise an AssertError!")
            x = 10
            y = 20
            assert x == y
        
        



    def main():
        nc2 = NotesChapter2()
        nc2.trying_excepting()
        #test.handling_exception()
        nc2.variable_positional_argument(5,5,5)
        # Now we wish to give only ONE variable for it and even though the function doesn't complain about it.
        nc2.variable_positional_argument(3)
        nc2.keywordarguments_are_important(test1="Hello", test2=10)
        nc2.test_assert()
        

    main()


if chapter == 3:
    print (" ")
    class NotesChapter3(object):

        class EasyClassCall(object):
            """ Using the __call__ function inside a Class makes easier to call the Class like a function! """
            print ("---- __call__ function within a Class ----")
            def __call__(self, a, b):
                print (" The inner method of the class was easily called like calling a function!")
                print ("Values passed: "), a, b

    

    def main ():
        nc3 = NotesChapter3()
        ecc = nc3.EasyClassCall()
        # Realize how easy it is to actually pass the variables to the class and call the function.
        ecc(2,3)
    main()


    def parser():
        # In order to run this function we have to execute the python file as:
        # python effectivepython.py -d alvar
        # Because -d is an optional argument and by not giving it to the program the parser parses nothing.
        class Parser(object):
            def __init__(self):
                parser = argparse.ArgumentParser(description="Aruco or Alvar")
                parser.add_argument("-d", "--detection", help="String to choose between Aruco or Alvar detection.")
                self.args = parser.parse_args()
                super(Parser, self).__init__()


        class TypeOfDetection(Parser):
            def __init__(self):
                print ("")
                print ("---- Parser Example with Class Inheritance ----")
                Parser.__init__(self)
                detection = self.args.detection
                if detection == "aruco":
                    print ("Will run aruco")
                if detection == "alvar":
                    print ("Will run alvar")
        TypeOfDetection()
    parser()


    def mult_class_inheritance():
        print ("")
        print ("---- Inheritance between Classes ----")
        class A(object):
            def __init__(self):
                # Will be printed after B
                print ("This is A")
                self.x = 10
                super(A, self).__init__()

        class B(A):
            def __init__(self):
                # Will be printed before A because we call the Class B, and B calls then A.
                print("This is B")
                A.__init__(self)
                # Inheriting variable from A
                print self.x
        # Calling B
        B()

    mult_class_inheritance()




else:
    print("Not a valid option... Exiting the program.")
    quit()
