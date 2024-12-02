"""
Do this module WITH (or as directed by) YOUR INSTRUCTOR.
It helps you set up your PyCharm to auto-format your code to meet
the so-called "PEP 8" coding standards, by using the BLACK formatter.

Authors: David Mutchler, Rachel Krohn, Dave Fisher, Shawn Bohner, Sriram Mohan,
         Amanda Stouder, Vibha Alangar, Mark Hays, Dave Henthorn, Matt Boutell,
         Scott McClellan, Yiji Zhang, Mohammed Noureddine, Steve Chenoweth,
         Claude Anderson, Michael Wollowski, Chandan Rupakheti,
         Derek Whitley, Curt Clifton, Valerie Galluzzi, their colleagues and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

"""
Academic Integrity: I got help on this module from:
         PUT_HERE_THE_NAMES_OF_PEOPLE_WHO_HELPED_YOU_ON_THIS_MODULE_(IF_ANY).
"""  # TODO: If you got help from anyone on this module, list their names here.

###############################################################################
# TODO: 2.
#  WITH YOUR INSTRUCTOR'S HELP, enable the BLACK formatter, as follows:
#     1. File ~ Settings
#     2. Click on the   Project   item in the leftmost window,
#          then select   Project Interpreter  in the window to the right.
#     3. Click the little  +  sign to bring up a window to add Packages.
#     4. Type
#            Black
#          in the place to specify the package to add,
#          then press the   Install Package   button.
#          (Leave the "Install to User's ..." checkbox UN-checked
#          unless permission-problems force you to check it.)
#     5. Also install the following if you have not already installed them:
#            pygame
#            pillow
#            paho-mqtt
#     5. Close the window when the installs are done.
#     6. Click on the   Tools   item in the leftmost window,
#          then select   Black   in the window to the right.
#     7. Check the   "On save"   box.
#  _
#  Read the code below briefly, and make some obvious formatting error,
#  e.g. adding extra blank lines.  Then test that Black works by
#  running this file and confirming that it autoformats.
#  Make a few more obvious formatting errors and run again to be sure all is OK.
################################################################################




def ugly():
    print("This has errors that violate"+ " the PEP 8 coding standards")
    print("The BLACK formatter will fix them when you run the code."
          )
    print(    "It will also adjust line breaks in sensible ways.")
    print("One", "Two", "Three", "This is a long line.....................................")

    print(1+3*    5)




ugly()




###############################################################################
# TODO: 3.  Commit-and-push in the usual way.
###############################################################################

