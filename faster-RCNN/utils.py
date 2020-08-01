def load_class_names(namesfile):
    
    # Create an empty list to hold the object classes
    class_names = []
    
    # Open the file containing the COCO object classes in read-only mode
    with open(namesfile, 'r') as fp:
        
        # The coco.names file contains only one object class per line.
        # Read the file line by line and save all the lines in a list.
        lines = fp.readlines()
    
    # Get the object class names
    for line in lines:
        
        # Make a copy of each line with any trailing whitespace removed
        line = line.rstrip()
        
        # Save the object class name into class_names
        class_names.append(line)
        
    return class_names