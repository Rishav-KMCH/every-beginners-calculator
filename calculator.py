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

############### IMPORTS           ###############
import sys

############### REQUEST FOR INPUT ###############

print("Welcome to the calculator!")
try:
	a = float(input("Enter the first number you prefer > "))
	b = float(input("Enter the second number you prefer > "))
except:
	print("Error: Please input a valid number! (You can also use decimals)")
	sys.exit()
print("Thanks, now choose: × (m)ultiplication, ÷ (d)ivision, + (a)ddition, - (s)ubtraction (case-sensitive)")
c = input("Write the first letter of the preffered operator > ")

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

############### ANSWER            ###############
print("Your answer is:", result)

