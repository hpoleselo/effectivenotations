
class Notes(object):
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

        
def main():
    test = Notes()
    test.trying_excepting()
    test.handling_exception()

if __name__ == "__main__":
    main()
