def validate_grid(text):        
    if text.isnumeric()==False or int(text) < 11 or int(text) > 99:
        return "Please enter an integer between 11 and 99."
    return "Mars sector created successfully", text
def validate_start(text):        
    if len(text)!=4 or text[2]!= " ":
        return "Please enter a set of coordinates and a direction, eg (12 E)."
    if text[3] not in ["N","W","S","E"]:
        return "Please enter a valid direction, eg N, E, S or W."       
    if text[0].isnumeric==False or text[1].isnumeric==False or int(text[0]+text[1]) > 99 or int(text[0]+text[1]) < 11:
        return "Please enter a set of coordinates between 11 and 99."    
    return "Starting position and direction recieved successfully", text
def validate_command(text):
    for i in text:
        if i not in ["M","R","L"]:
            return f"{i} is not a valid command"
        else:
            return "Command recieved successfully", text

    

