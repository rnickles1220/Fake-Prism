#Basic GUI for a user to add graph parameters to#

import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

#Creates tkinter window and returns a dictionary with selected values#

def createParameterWindow():
    userParameters = {
    'numReps' : "0",
    'numBindingPartners' : "0",
    'mainTitle' : "",
    'yaxisTitle' : "",
    'color' : "",
    'experimental_conditions' : []
    }

    # Create the main window
    root = tk.Tk()
    root.title("Fake Prism")
    root.geometry("1050x500")

    twomainframes = tk.Frame(master=root, width=1000, height=600)
    twomainframes.pack(pady=10, fill=tk.BOTH, expand=True)

    #will hold the preview graph off to the right
    previewframe = tk.Frame(master=twomainframes, width=500, height=400)
    previewframe.grid(row=0, column=1)

    containerframe = tk.Frame(master=twomainframes, width=500, height=400)
    containerframe.grid(row=0, column=0)

    # Title Label
    label = tk.Label(master=containerframe, text="Data Parameters")
    label.grid(row=0, column=0)

    #holds all user parameter input boxes and descriptions
    parameterframe = tk.Frame(master=containerframe, width=100, height=100)
    parameterframe.grid(row=1, column=0)

    descriptionframe = tk.Frame(master=parameterframe, width=100, height=100)
    descriptionframe.grid(row=0, column=0)

    entryframe = tk.Frame(master=parameterframe, width=100, height=100)
    entryframe.grid(row=0, column=1)

    entry_widgets = {}

    i=0
    for key in userParameters:
        # Create a label widget
        label = tk.Label(descriptionframe, text=key)
        label.grid(row=i, column=0, pady=10)

        # Create an Entry widget
        entry = tk.Entry(entryframe, width=30)
        #add default text
        if key in ["numReps", "numBindingPartners"]:
            entry.insert(0, int("1"))
        elif key in ["mainTitle", "yaxisTitle"]:
            entry.insert(0, "title")
        elif key == "color":
            entry.insert(0, "blue")
        elif key == "experimental_conditions":
            entry.insert(0, "condition 1, condtion 2")
        else:
            entry.insert(0, "default text")

        entry.grid(row=i, column=1, pady=10, padx = 50)

        entry_widgets[key] = entry
        i+=1

    # Function to get the input text
    def collectParameters():
        
        for key in userParameters:
            input_text = entry_widgets[key].get()
            if key == "experimental_conditions":
                userParameters[key] = [item.strip() for item in input_text.split(',')]
            else:
                userParameters[key] = input_text
        print("Input:", input_text)

        exit_application()

    def updatePreview():
                
        for key in userParameters:
            input_text = entry_widgets[key].get()
            if key == "experimental_conditions":
                userParameters[key] = [item.strip() for item in input_text.split(',')]
            else:
                userParameters[key] = input_text
        print("Input:", input_text)

        exit_application()

    def exit_application():
        root.destroy()

    def plot():
        # Create a simple example dataset (you can replace this with your actual data)
        x = [1, 2, 3, 4, 5]
        y = [10, 8, 12, 6, 9]

        # Create a Matplotlib figure
        fig = Figure(figsize=(6, 4), dpi=100)
        plot1 = fig.add_subplot(111)
        plot1.plot(x, y, marker='o', linestyle='-', color='b')
        plot1.set_xlabel('X-axis')
        plot1.set_ylabel('Y-axis')
        plot1.set_title('Preview Plot')

        # Create a Tkinter canvas containing the Matplotlib figure
        canvas = FigureCanvasTkAgg(fig, master=previewframe)
        canvas.draw()
        canvas.get_tk_widget().pack()

        # Add the Matplotlib toolbar (optional)
        toolbar = NavigationToolbar2Tk(canvas, previewframe)
        toolbar.update()
        canvas.get_tk_widget().pack()

    #initialize the right panel of the GUI with an example plot
    plot()

    # Create a "Preview" button
    preview_button = tk.Button(master=containerframe, text="Preview", command=plot)
    preview_button.grid(row=2, column=0)

    # Create a button to gupdate preview graph
    button = tk.Button(master=containerframe, text="Update Preview", command=updatePreview)
    button.grid(row=3, column=0)

    # Create a button to get the input text
    button = tk.Button(master=containerframe, text="Submit Parameters", command=collectParameters)
    button.grid(row=4, column=0)

    # Run the application
    root.mainloop()

    return (userParameters)