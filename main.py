import hashlib

choice = input('\u001b[0mAre you\n(1) Signing Up\n(2) Signing In?: ')
pd = input("Password: ")

pd = hashlib.pbkdf2_hmac('sha256', pd.encode('utf-8'), b'salt', 100000) # hashes and salts the password
pd = pd.hex() # converts password from byte to string

if(choice == '1'):
  usrInput = open('save.dat', 'w') # creates/opens save.dat file and sets to write mode
  usrInput.write(pd) # writes password in file
  usrInput.close() # closes save.dat
  print()
  print("\u001b[34mSign Up Complete! \u001b[0m") # prints in color blue and then rests

elif(choice == '2'):
  try:
    with open('save.dat', 'r') as file: # opens save.dat file and sets to read mode
      for line in file: # starts looping through every line in save.dat
        line = line.replace('\n', '') # replaces all '/n' with blank character
        print() 
        if(pd == line):
          print("\u001b[32mCorrect Password \u001b[0m") # prints in green then resets
        else:
          print("\u001b[31mIncorrect Password \u001b[0m") # prints in red then resets
  except:
    print("\u001b[31m Couldn't read file 'save.dat' \u001b[0m") # error prompt in red