answer = 2**5
print(answer * 100)

###############################################################################
# TODO: 1.
#   Read the 2 lines of code ABOVE this _TODO_.
#   When the Python INTERPRETER runs, that is, when this program runs,
#   it does the following with that code:
#  _
#     1. It runs line 1, that is, it:
#          a. Evaluates (aka runs, computes) 2 raised to the 5th power,
#             yielding the object that is the integer 32.
#          b. Makes the name   answer   refer to that object.
#  _
#        We say that "the name  answer  is ASSIGNED the value 32."
#        Names used in assignment statements are commonly called VARIABLES
#        (because their value can "vary" as the program runs).
#  _
#        Note that the RIGHT-hand-side of an assignment statement
#        is evaluated BEFORE the NAME on the LEFT-hand-side
#        gets ASSIGNED the result.
#  _
#     2. It runs line 2, that is, it:
#          a. Looks up the object to which the name   answer  refers
#               (i.e., the object 32).
#          b. Multiplies that object (32) by 100
#               (hence computing the object that is the integer 3,200).
#          c. Prints (that is, displays on the Run/Console window)
#             the newly-computed object.  (It prints WITHOUT the comma.)
#  _
#   Make sure that you understand that those two lines accomplish the above,
#     ** ASKING QUESTIONS AS NEEDED. **
#   Once you completely understand the above, run this module,
#   confirming that it prints 3200.  Then change the above _TODO_ to DONE.
###############################################################################

###############################################################################
# TODO: 2.
#   Some things, like addition (+) and subtraction (-), are built into
#   Python.  Others are defined in modules (aka libraries) that must be
#   IMPORTED into your program for you to use them.  The trigonometric functions
#   (e.g. cos, sin) are defined in the MATH module, so to use them, you must
#   IMPORT the math module by putting the following statement into your code:
#      import math
#   Such statements are traditionally put at the TOP of a module.
#   Go ahead and put an   import math   statement at the top of this module.
#  _
#   To access things defined in an imported module, we use the DOT notation,
#   like this:
#       math.sin
#   to refer to the sine function defined in the imported  math  module.
#  _
#   After putting your  import math  statement at the beginning of this module,
#   and keeping in mind how we use the DOT notation to refer to things defined
#   inside an imported module:
#      Immediately below this _TODO_, write code that:
#        a. Computes 77 plus the cosine of 2.75.
#               When you type   math.co   pause after typing the  "o"
#               and notice what pops up.  It will show you that
#               the name of the cosine function is NOT "cosine"; rather,
#               it is "cos".  Hence, you will type   math.cos(2.75)
#               or (better) press the TAB key to auto-complete the code.
#        b. Stores that computed value using a name of your own choosing.
#        c. Prints the square root of that computed value.
#               You will have to guess what function in the  math  module
#               is used for square roots.  Try typing:
#                   math.s
#               and pause after typing the "s" to see what pops up.
#               Do you see what function to use for square roots?
#               (If not, ask for help.)
#      The answer should be about 8.722.
#   Run your code (fix errors as needed), then change the above _TODO_ to DONE.
###############################################################################

###############################################################################
# TODO: 3.
#   Immediately below this _TODO_, write code that computes and prints:
#      the square root of ((41 * 88) + (5 * the cosine of 2))
#   The answer should be about 60.05.
#   Use as few or as many intermediate names as you feel appropriate.
#   Run your code (fix errors as needed), then change the above _TODO_ to DONE.
###############################################################################

###############################################################################
# TODO: 4.
#   Immediately below this _TODO_,
#   write code that computes the square root of 2 in two ways:
#     1. By using the   math.sqrt   function.
#     2. By raising 2 to the 0.5 power (using   **   for exponentiation).
#   Print both of the expressions that you write.
#   Run your code (fix errors as needed), then change the above _TODO_ to DONE.
###############################################################################

###############################################################################
# TODO: 5.
#   Immediately below this _TODO_,
#   write code that computes and prints:
#     1. the base-10 logarithm of 1,000,000    (which is 6, as you know)
#     2. the base-2 logarithm of 1,000,000     (which is a bit less than 20)
#     3. the base-3 logarithm of 1,000,000     (which is between 6 and 20)
#   For all three, use the relevant functions in the  math  module,
#   and discover the name of those functions by typing:
#      math.l   (pausing after the "l" and noting what pops up)
#   Run your code (fix errors as needed), then change the above _TODO_ to DONE.
###############################################################################

###############################################################################
# TODO: 6.
#   Ensure that no blue bars on the scrollbar-thing to the right remain.
#   Run one more time to be sure that all is still OK.
#  _
#   Then COMMIT-and-PUSH your work as before:
#     1. Select    Git     from the menu bar (above).
#          Or, right-click on the project in the Project window
#          and select   Git  from the pull-down menu that appears.
#     2. Choose   Commit...   from the pull-down menu that appears.
#     3. In the   "Commit and Push"   sub-window that pops up
#        (the one in which you can type),
#        press the   "Commit and Push..."   button.
#            Note: If it asks you to "Specify commit message", do so
#                  using   Done   or something like that for the message.
#  _
#   You can COMMIT-and-PUSH as often as you like.
#   *** DO IT FREQUENTLY - AT LEAST once per module (i.e., file). ***
###############################################################################
