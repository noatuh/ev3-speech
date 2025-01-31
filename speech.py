import sys
from ev3dev2.sound import Sound

# Initialize speaker
sound = Sound()

# Instructions
print("Press Enter to enter text input mode. Type 'exit' to quit.")

try:
    while True:
        text = input("Enter your message and press Enter to send: ")
        
        if text.lower() == "exit":
            print("Exiting...")
            break
        
        sound.speak(text)
        print("Sent to EV3: " + text)

except KeyboardInterrupt:
    print("\nManual exit (Ctrl+C). Exiting...")
