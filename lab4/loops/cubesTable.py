# CPE 101 Lab 4
# Name:

def main():
   table_size = get_table_size()
   while table_size != 0:
      first = get_first()
      increment = get_increment()
      show_table(table_size, first, increment)
      table_size = get_table_size()

# Obtain a valid table size from the user
def get_table_size():
   size = input("Enter number of rows in table (0 to end): ")

   while size < 0:
      print "Size must be non-negative."
      size = input("Enter number of rows in table (0 to end): ")
      
   return size;

# Obtain the first table entry from the user 
def get_first():
   first = input("Enter the value of the first number in the table: ")

   while first < 0:
      print "Size must be non-negative."
      first = input("Enter the value of the first number in the table: ")

   return first;

# Display the table of cubes
def show_table(size, first, increment):
   print "A cube table of size %d will appear here starting with %d." % (size, first)
   print "Number  Cube"
   sum_of_cubes = 0
   for i in range(size):
       print "%-7d %d" %(first, first**3)
       sum_of_cubes = first**3 + sum_of_cubes
       first += increment
   print "\nThe sum of cubes is: ", sum_of_cubes

# Get Increment
def get_increment():
   increment = input("Enter the increment between rows: ")

   while increment < 0:
      print "Size must be non-negative."
      increment = input("Enter the increment between rows: ")
   
   return increment;

if __name__ == "__main__":
   main()
