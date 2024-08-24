#Basic GUI for a user to add graph parameters to#

import tkinter as tk

#Creates tkinter window and returns a dictionary with selected values#

def createParameterWindow():
    userParameters = {
    'numReps' : 0,
    'numBindingPartners' : 0,
    'xaxisTitle' : "",
    'yaxisTitle' : "",
    'color' : ""
    }

    # Create the main window
    root = tk.Tk()
    root.title("Fake Prism")

    # Title Label
    label = tk.Label(root, text="Data Parameters")
    label.pack(pady=10)

    entry_widgets = {}

    for key in userParameters:
        # Create a label widget
        label = tk.Label(root, text=key)
        label.pack(pady=10)

        # Create an Entry widget
        entry = tk.Entry(root, width=30)
        entry.pack(pady=10, padx = 50)

        entry_widgets[key] = entry

    # Function to get the input text
    def collectParameters():
        
        for key in userParameters:
            entryID = "Entry" + key
            input_text = entry_widgets[key].get()
            userParameters[key] = input_text
        print("Input:", input_text)
        """userParameters['numReps'] = 0
        userParameters['numBindingPartners'] = 0 
        userParameters['xaxisTitle'] = ""
        userParameters['yaxisTitle'] = "" 
        userParameters['color'] = """

        exit_application()

    def exit_application():
        root.destroy()
        

    # Create a button to get the input text
    button = tk.Button(root, text="Submit Parameters", command=collectParameters)
    button.pack(pady=10)

    # Run the application
    root.mainloop()

    return (userParameters)