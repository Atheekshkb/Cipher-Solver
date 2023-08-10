def open_file(filename, mode) :

            try:

                      f = open(filename, mode)

            except IOError:

                      print ( f "File {filename} cannot be opened.")

            else:

                      print ( f "File {filename} is opened successfully.")

                      return f

f1 = open_file("mynew.txt", "r")

if f1: 
    f1.close()