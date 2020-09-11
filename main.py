import tkinter as tk 
import covidstats


def update_data_env():
    """
    Envelope function for updating the data.
    """
    try:
        covidstats.update_data_table()
        status_label['text'] = "Update Succeeded"
    except:
        status_label['text'] = "Update Failed"


def plot_city_data_env(input, canvas_1, canvas_2, canvas_3, root):
    """
    Envelope function for ploting the data.
    """
    try:
        covidstats.plot_city_data(input, canvas_1, canvas_2, canvas_3, root)
        status_label['text'] = "Graph Succeeded"
    except:
        status_label['text'] = "Graph Failed"



root = tk.Tk()

# size & title & background color
root.title("COVID-19")
root.configure(bg='grey')
root.geometry('800x800')
frame_color = '#DC7963'

# top frame for the user's input
top_frame = tk.Frame(root, bg=frame_color)
top_frame.place(relwidth=0.9, relheight=0.1, relx=0.05, rely=0.05)

# bottom frame for the system output
bottom_frame = tk.Frame(root, bg=frame_color)
bottom_frame.place(relwidth=0.9, relheight=0.7, relx=0.05, rely=0.2)

# 'City Name' label
label = tk.Label(top_frame, bg=frame_color, text='City Name:')
label.place(relx=0.05, rely=0.25, relheight=0.5,  relwidth=0.12)

# 'City Name' entry
entry = tk.Entry(top_frame)
entry.place(relx=0.2, rely=0.25, relheight=0.5, relwidth=0.5)

# 'GIVE ME GRAPHS' button
button = tk.Button(top_frame, text='GIVE ME GRAPHS', \
                    command= lambda: plot_city_data_env(entry.get(), canvas_1, canvas_2, canvas_3, root))
button.place(relx=0.75, rely=0.25, relheight=0.5, relwidth=0.21)

# Graph 1 cavas
canvas_1 = tk.Canvas(bottom_frame, bg=frame_color, bd=0, highlightthickness=0)
canvas_1.place(relx=0, rely=0, relheight=0.5,  relwidth=0.5)

# Graph 2 cavas
canvas_2 = tk.Canvas(bottom_frame, bg=frame_color, bd=0, highlightthickness=0)
canvas_2.place(relx=0.5, rely=0, relheight=0.5,  relwidth=0.5)

# Graph 3 canvas
canvas_3 = tk.Canvas(bottom_frame, bg=frame_color, bd=0, highlightthickness=0)
canvas_3.place(relx=0.2, rely=0.5, relheight=0.5,  relwidth=0.6)

# 'Update Data' button
button2 = tk.Button(root, text='Update Data', command= lambda: update_data_env())
button2.place(relx=0.75, rely=0.925, relheight=0.05, relwidth=0.2)

# Status label
status_label = tk.Label(root, bg='grey', text='')
status_label.place(relx=0.05, rely=0.925, relheight=0.05,  relwidth=0.2)



root.mainloop()