# Change-detection
## How to Test

### 1. Set up the project

Make sure Python is installed, then open a terminal in the project directory.

The project should contain:

```text
project/
├── main.py
├── data/
│   ├── file1.txt
│   └── file2.txt
└── mock_sqlite_state.json
```

The `mock_sqlite_state.json` mock SQLite state file does not need to be created manually. Script will create it after the first run.

### 2. Run the program for the first time

Run:

```bash
python main.py
```

The files in the `data` directory should be reported as:

```text
[NEW] file1.txt
  - New file detected

[NEW] file2.txt
  - New file detected
```

The program will then save the current file state.

### 3. Test an unchanged file

Run the program again without changing anything:

```bash
python main.py
```

The files should now be reported as:

```text
[UNCHANGED] file1.txt
  - No changes detected
```

This demonstrates that previously synchronised files can be identified when their metadata has not changed.

### 4. Test a modified file

Open `file1.txt` and add some text, then save the file.

Run:

```bash
python main.py
```

The program should report:

```text
[CHANGED] file1.txt
  - File size changed: ...
  - Modified time changed
```

This demonstrates that the utility can detect when an existing file has been modified.

### 5. Test a new file

Create a new file inside the `data` directory, for example:

```text
file3.txt
```

Run:

```bash
python main.py
```

The program should report:

```text
[NEW] file3.txt
  - New file detected
```

### 6. Reset the test

To start the test again from the beginning, delete:

```text
mock_sqlite_state.json
```

Then run:

```bash
python main.py
```

The files will be treated as new files again.
