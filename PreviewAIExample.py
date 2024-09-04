import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

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
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()

    # Add the Matplotlib toolbar (optional)
    toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.update()
    canvas.get_tk_widget().pack()

# Create the main Tkinter window
window = tk.Tk()
window.title('Matplotlib Preview in Tkinter')
window.geometry("600x400")

# Create a "Preview" button
preview_button = tk.Button(master=window, text="Preview", command=plot)
preview_button.pack()

# Run the Tkinter event loop
window.mainloop()
