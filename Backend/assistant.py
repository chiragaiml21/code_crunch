# from asr import asr
# from tts2 import tts
import time
from functions import response, search_on_google, play_on_youtube


# -----------------------------Main Function----------------------------
def main():
    try:
        while True:
        #   user_input = asr()
          user_input = input("User : ")
          print("User : ", user_input)

          if "stop" in user_input.lower() or "exit" in user_input.lower():
              break
          elif "search" in user_input.lower():
              search_on_google(user_input)
          elif "play" in user_input.lower() or "youtube" in user_input.lower():
              play_on_youtube(user_input)
              break
          else:
              response(user_input)
              time.sleep(2)

    except KeyboardInterrupt:
        print("Bye Bye....")

    except Exception as e:
        if e:
            print(e)
        else:
            # tts("Sorry I couldn't understand what you said.")
            print("Sorry I couldn't understand what you said.")
        

if __name__ == "__main__":
    main()
