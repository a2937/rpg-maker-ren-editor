import json
import tkinter as tk
from tkinter import messagebox

class EventPage:
    def __init__(self, jsonData):
        self.conditions = jsonData["conditions"]
        self.image = Image(jsonData["image"])
        self.moveFrequency = jsonData["moveFrequency"]
        self.moveRoute = []

class Image:
    def __init__(self, jsonData):
        self.characterName = jsonData["characterName"]
        self.direction = jsonData["direction"]
        self.pattern = jsonData["pattern"]
        self.characterIndex = jsonData["characterIndex"]

def parse_json(jsonData):
    event_page = EventPage(jsonData)
    return event_page

# Example usage
jsonData = '{"conditions":{"actorId":1,"actorValid":false,"itemId":1,"itemValid":false,"selfSwitchCh":"A","selfSwitchValid":false,"switch1Id":1,"switch1Valid":false,"switch2Id":1,"switch2Valid":false,"variableId":1,"variableValid":false,"variableValue":0},"directionFix":false,"image":{"tileId":0,"characterName":"","direction":2,"pattern":0,"characterIndex":0},"moveFrequency":3,"moveRoute":{"list":[{"code":0,"indent":null,"parameters":[]}],"repeat":true,"skippable":false,"wait":false},"moveSpeed":3,"moveType":0,"priorityType":1,"stepAnime":false,"through":false,"trigger":1,"walkAnime":true,"list":[{"code":201,"indent":0,"parameters":[0,3,8,11,8,0]},{"code":0,"indent":0,"parameters":[]}]}' 

# Create the GUI window
root = tk.Tk()
root.title("Event Page Parser")

# Create a text box to display the parsed event page data
text_box = tk.Text(root)
text_box.pack()

def show_event_data(event_page):
    # Initialize the output string
    output = ""

    # Iterate through the conditions property
    if event_page["conditions"]:
        output += "Conditions:\n"
        for key, value in event_page["conditions"].items():
            output += f"  {key}: {value}\n"

    # Iterate through the image property
    if event_page["image"]:
        output += "\nImage:\n"
        for key, value in event_page["image"].items():
            output += f"  {key}: {value}\n"

    # Iterate through the move route list
    if event_page["moveRoute"]["list"]:
        output += "\nMove Route:\n"
        for step in event_page["moveRoute"]["list"]:
            output += "  Code: {}\n".format(step["code"])
            if step.get("indent"):
                output += f"  Indent: {step['indent']}\n"
            if step.get("parameters"):
                output += "  Parameters:\n"
                for param in step["parameters"]:
                    output += f"    {param}\n"

    # Add any other relevant information
    output += "\nTrigger: {}\n".format(event_page["trigger"])
    output += "Priority Type: {}\n".format(event_page["priorityType"])

    return output

def show_parsed_data(event_page):
    text_box.delete(1.0, "end")
    text_box.insert("1.0",(show_event_data(event_page)))

# Create a button to parse the JSON data and display the result
button = tk.Button(root, text="Parse JSON", command=lambda: show_parsed_data(json.loads(jsonData)))
button.pack()

root.mainloop()