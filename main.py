import tkinter as tk 
import covidstats


def update_data_env():
    try:
        covidstats.update_data_table()
        status_label['text'] = "Update Succeeded"
    except:
        status_label['text'] = "Update Failed"


def plot_city_data_env(input):
    try:
        covidstats.plot_city_data(input)
        status_label['text'] = "Graph Succeeded"
    except:
        status_label['text'] = "Graph Failed"



root = tk.Tk()

# size & title & background color
root.title("COVID-19")
root.configure(bg='grey')
root.geometry('600x600')

# top frame for the user's input
top_frame = tk.Frame(root, bg='#DC7963')
top_frame.place(relwidth=0.9, relheight=0.1, relx=0.05, rely=0.05)

# 'City Name' label
label = tk.Label(top_frame, bg='#DC7963', text='City Name:')
label.place(relx=0.05, rely=0.25, relheight=0.5,  relwidth=0.12)

# 'City Name' entry
entry = tk.Entry(top_frame)
entry.place(relx=0.2, rely=0.25, relheight=0.5, relwidth=0.5)

# 'GIVE ME GRAPHS' button
button = tk.Button(top_frame, text='GIVE ME GRAPHS', command= lambda: plot_city_data_env(entry.get()))
button.place(relx=0.75, rely=0.25, relheight=0.5, relwidth=0.21)

# 'Update Data' button
button2 = tk.Button(root, text='Update Data', command= lambda: update_data_env())
button2.place(relx=0.75, rely=0.925, relheight=0.05, relwidth=0.2)

# bottom frame for the system output
bottom_frame = tk.Frame(root, bg='#DC7963')
bottom_frame.place(relwidth=0.9, relheight=0.7, relx=0.05, rely=0.2)

# Status label
status_label = tk.Label(root, bg='grey', text='')
status_label.place(relx=0.05, rely=0.925, relheight=0.05,  relwidth=0.2)



root.mainloop()