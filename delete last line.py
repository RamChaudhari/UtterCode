def del_last():
    
    lines = []
    # read file
    with open("CodeFile.py", 'r') as fp:
        # read an store all lines into list
        lines = fp.readlines()

    # Write file
    with open("CodeFile.py", 'w') as fp:
        # iterate each line
        for number, line in enumerate(lines):
            # delete line 5 and 8. or pass any Nth line you want to remove
            # note list index starts from 0
            p = len(lines)
            if number not in [p-1]:
                fp.write(line)

del_last()