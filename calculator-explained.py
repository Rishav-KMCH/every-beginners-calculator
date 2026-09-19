#  Every Beginner's Calculator

#  Copyright (C) 2026 rishav
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 2 of the License, or
#  (at your option) any later version.

#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
  
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

# This is the explained version, for the regular version see calculator.py.
# The script will run just like calculator.py.

############### IMPORTS           ###############
import sys
# The import function imports other third-party or first-party libraries.
# The sys library handles the system.

############### REQUEST FOR INPUT ###############

print("Welcome to the calculator!")
# Uses the print() function to print "Welcome to the calculator!"
# The print() function "prints" text on the screen.

try:
	a = float(input("Enter the first number you prefer > "))
	b = float(input("Enter the second number you prefer > "))
except:
	print("Error: Please input a valid number! (You can also use decimals)")
	sys.exit()
# a and b are variables, that hold data. The function input() prints a prompt
# and then reads what the user types. We wrap input() in float(). If you don't
# use float() Python saves the input as a text string and math operations
# wouldn't work. This section is error-proofed with try and except blocks. If the
# user enters letters, a ValueError is raised and it immediately jumps to the except block.
# The sys.exit() then exits the program gracefully, and prevents a crash of the system.

print("Thanks, now choose: × (m)ultiplication, ÷ (d)ivision, + (a)ddition, - (s)ubtraction (case-sensitive)")
c = input("Write the first letter of the preffered operator > ")
# This uses the print() function to add a layout to choose an operator.
# And it puts the input() function inside c as a variable.
# This input function does not use float as we need a text string.

############### LOGIC             ###############

if c == 'm':
	result = a * b
elif c == 'd':
	if b == 0:
		print("Error: Nothing is divisible by zero!")
		sys.exit()
	else:
		result = a / b
elif c == 'a':
	result = a + b
elif c == 's':
	result = a - b
else:
	print("Error: Use m, d, a, or s, not anything else. Remember, it's case-sensitive!")
	sys.exit()
# This part uses if and elif statements to decide which math operation to use.
# It checks the variable c against the text characters m, d, an or s.
# Characters are always enclosed in single quotes (' ') to let Python know that it is a text string.
# Inside the division block ('d') a nested if-else statement is checking to see if variable b is 0.
# If it is 0, it stops the program from crashing with a ZeroDivisionError.
# The last else catches totally invalid letters and exits cleanly.

############### ANSWER            ###############
print("Your answer is:", result)
# This uses the print() function to print the text "Your answer is:" and then the answer which is stored
# inside the result variable.
