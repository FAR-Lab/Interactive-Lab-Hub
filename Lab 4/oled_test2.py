import qwiic_oled_display
import sys


def runExample():

    #  These lines of code are all you need to initialize the OLED display and print text on the screen.
  
    print("\nSparkFun Qwiic OLED Display - Hello Example\n")
    myOLED = qwiic_oled_display.QwiicOledDisplay()

    if myOLED.is_connected() == False:
        print("The Qwiic OLED Display isn't connected to the system. Please check your connection", \
            file=sys.stderr)
        return
    
    #  Before you can start using the OLED, call begin() to init all of the pins and configure the OLED.
    myOLED.begin()

    myOLED.clear(myOLED.PAGE)  #  Clear the display's buffer

    myOLED.print("Hello World")  #  Add "Hello World" to buffer

    #  To actually draw anything on the display, you must call the display() function. 
    myOLED.display()

runExample()