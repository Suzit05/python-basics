
import time
def monitor_log(file_path):
    with open(file_path, "r") as file:
        file.seek(0,2) # move to end of the line, aage se read krega
        print(f"Watching `{file_path}` for changes..")

        while(True):
          line= file.readline()
          if line:
            print(line.strip()) #strip removes the empty space
            if "ERROR" in line:
                print("Error found")
            else:
                time.sleep(1)  #wait and check again



monitor_log("script.log")

