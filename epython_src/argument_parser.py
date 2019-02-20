import argparse

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
                # 'Instantiating' the parent class, we have not only to declare that this Class inherits from Parser but use the __init__ as well
                Parser.__init__(self)

		# Store the detection
		# Realize that we are inheriting from the attribute 'self.args' of Parser 
                detection = self.args.detection
                if detection == "aruco":
                    print ("Will run aruco")
                if detection == "alvar":
                    print ("Will run alvar")
	
	# Only calls the child class
        TypeOfDetection()
parser()
