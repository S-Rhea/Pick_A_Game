from tkinter import *
import random
import sys

class myGui:
    def __init__(self, master):
        self.master = master
        master.title("Option Selector App")
        self.main_frame = Frame(self.master)
        self.pick_frame = Frame(self.master)
        self.add_frame = Frame(self.master)
        self.redo_add_frame = Frame(self.master)
        self.remove_frame = Frame(self.master)
        self.view_frame = Frame(self.master)
        self.exit_frame = Frame(self.master)
        for frame in (self.main_frame, self.pick_frame, self.add_frame, self.redo_add_frame, self.remove_frame, self.view_frame, self.exit_frame):
            frame.grid(row=0, column=0, sticky='news')
        self.set_frames()
        self.option_list = []
        self.load_list()

    def raise_frame(self, frame):
        frame.tkraise()

    def load_list(self):
        self.option_list = []
        list_file = open("list_file.txt", mode='r')
        for x in list_file:
            x_stripped = x.strip()
            self.option_list.append(x_stripped)
        list_file.close()

    def option_pick(self, pf_label):
        self.raise_frame(self.pick_frame)
        if len(self.option_list) > 0:
            rand_num = random.randint(1, len(self.option_list))
            pf_label.config(text="Selected Option is: " + self.option_list[rand_num-1])
        else:
            pf_label.config(text="No options to choose from...")

    def option_add(self, af_entry, af_label):
        new_option = af_entry.get()
        if not new_option == '':
            self.option_list.append(new_option)
            af_entry.delete(0, END)
            self.save_file()
            self.raise_frame(self.redo_add_frame)
        else:
            af_label.config(text='Please enter an option then press the enter button')
            af_entry.delete(0, END)

    def rf_generate_list(self, remove_frame, rf_label):
        new_text = 'Enter number of option to remove. Only remove one at a time.\n\n'
        for x in range(0, len(self.option_list)):
            new_text += str(x+1) + '. ' + self.option_list[x] + '\n'
        rf_label.config(text=new_text)
        self.raise_frame(remove_frame)

    def option_remove(self, rf_entry, rf_label):
        remove_option = rf_entry.get()
        if not remove_option == '':
            self.option_list.pop(int(remove_option)-1)
        self.rf_generate_list(self.remove_frame, rf_label)
        self.save_file()
        rf_entry.delete(0, END)

    def option_view(self, view_frame, vf_label):
        self.raise_frame(view_frame)
        new_text = 'Current Option Selection\n\n'
        for x in self.option_list:
            new_text += x + '\n'
        vf_label.config(text=new_text)

    def save_file(self):
        file = open('list_file.txt', mode='w')
        for x in self.option_list:
            file.write(x + '\n')
        file.close()

    def program_exit(self, master):
        self.raise_frame(self.exit_frame)
        self.save_file()
        master.destroy()
        sys.exit(0)

    def set_frames(self):
        pf_label = Label(self.pick_frame, text='Selected Option is: ')
        pf_label.pack()
        pf_button1 = Button(self.pick_frame, text='Choose Again', command=lambda: self.option_pick(pf_label))
        pf_button1.pack()
        pf_button2 = Button(self.pick_frame, text='Back', command=lambda: self.raise_frame(self.main_frame))
        pf_button2.pack()

        af_label = Label(self.add_frame, text='Please enter new Option')
        af_label.pack()
        af_entry = Entry(self.add_frame)
        af_entry.pack()
        af_button1 = Button(self.add_frame, text='Enter', command=lambda: self.option_add(af_entry, af_label))
        af_button1.pack()
        af_button2 = Button(self.add_frame, text='Back', command=lambda: self.raise_frame(self.main_frame))
        af_button2.pack()

        arf_label = Label(self.redo_add_frame, text='Option Added!')
        arf_label.pack()
        arf_button1 = Button(self.redo_add_frame, text='Add Another Option', command=lambda: self.raise_frame(self.add_frame))
        arf_button1.pack()
        arf_button2 = Button(self.redo_add_frame, text='Return to Menu', command=lambda: self.raise_frame(self.main_frame))
        arf_button2.pack()

        rf_label = Label(self.remove_frame, text='Select options to remove')
        rf_label.pack()
        rf_entry = Entry(self.remove_frame)
        rf_entry.pack()
        rf_button1 = Button(self.remove_frame, text='Remove', command=lambda: self.option_remove(rf_entry, rf_label))
        rf_button1.pack()
        rf_button2 = Button(self.remove_frame, text='Back', command=lambda: self.raise_frame(self.main_frame))
        rf_button2.pack()

        vf_label = Label(self.view_frame, text='Current option Selection')
        vf_label.pack()
        vf_button1 = Button(self.view_frame, text='Back', command=lambda: self.raise_frame(self.main_frame))
        vf_button1.pack()

        ef_label = Label(self.exit_frame, text='Exiting Program...')
        ef_label.pack()

        Label(self.main_frame, text='Welcome!').pack()
        main_button1 = Button(self.main_frame, text='Random Select', command=lambda: self.option_pick(pf_label))
        main_button1.pack()
        main_button2 = Button(self.main_frame, text='Add Option', command=lambda: self.raise_frame(self.add_frame))
        main_button2.pack()
        main_button3 = Button(self.main_frame, text='Remove Option', command=lambda: self.rf_generate_list(self.remove_frame, rf_label))
        main_button3.pack()
        main_button4 = Button(self.main_frame, text='View Option List', command=lambda: self.option_view(self.view_frame, vf_label))
        main_button4.pack()
        main_button5 = Button(self.main_frame, text='Exit', command=lambda: self.program_exit(self.master))
        main_button5.pack()
