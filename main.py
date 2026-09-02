import os
import json

# Directory that the synchronisation utility is monitoring
MONITORED_DIR = "./data"

# File used to store the previous state of monitored files
# This is a simplified mock version of the SQLite database proposed in the design
STATE_FILE = "mock_sqlite_state.json"


# Load the previous file state so the current scan can be compared against it
if os.path.exists(STATE_FILE):
    with open(STATE_FILE, "r") as file:
        previous_state = json.load(file)
else:
    # If there is no previous state, this is the first scan
    previous_state = {}


# Store the state detected during the current scan
current_state = {}
print("Checking files...\n")


# Check each file in the monitored directory
for filename in os.listdir(MONITORED_DIR):
    path = os.path.join(MONITORED_DIR, filename)

    # Ignore directories and only process files
    if os.path.isfile(path):

        # Get basic file metadata that can be used to detect changes
        modified_time = os.path.getmtime(path)
        file_size = os.path.getsize(path)

        # Save the current file state so it can be used during the next scan
        current_state[filename] = {
            "modified_time": modified_time,
            "file_size": file_size
        }


        # If the file was not in the previous state, it is a new file
        if filename not in previous_state:
            print(f"[NEW] {filename}")
            print("  - New file detected")


        else:
            # Get the previous size and modification time for comparison
            old_size = previous_state[filename]["file_size"]
            old_modified = previous_state[filename]["modified_time"]


            # Check whether either the file size or modification time has changed
            if modified_time != old_modified or file_size != old_size:
                print(f"[CHANGED] {filename}")

                # Show if the file size has changed
                if file_size != old_size:
                    print(
                        f"  - File size changed: "
                        f"{old_size} -> {file_size} bytes"
                    )

                # Show if the modification time has changed
                if modified_time != old_modified:
                    print("  - Modified time changed")


            else:
                # Neither the size nor modification time has changed
                print(f"[UNCHANGED] {filename}")
                print("  - No changes detected")


# Save the current state so it can be used as the previous state
# the next time the program runs
with open(STATE_FILE, "w") as file:
    json.dump(current_state, file)