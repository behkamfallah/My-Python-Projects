import customtkinter as ctk
import File_Sorter


class FileExplorer:
    def __init__(self):
        # Initialize our window
        self.path: str = ''
        self.window = ctk.CTk()
        self.window.title('File Sorter')
        self.window.geometry('900x200')
        self.window.resizable(False, False)

        # Widget padding
        self.padding: dict = {'padx': 75, 'pady': 20}

        # Explore button
        self.explore_button = ctk.CTkButton(self.window, text='Explore', command=self.getting_path)
        self.explore_button.grid(row=0, column=1, **self.padding)

        #  Selected Path label
        self.path_label = ctk.CTkLabel(self.window, text='Selected path:')
        self.path_label.grid(row=1, column=0, **self.padding)
        self.path_entry = ctk.CTkEntry(self.window, width=550)
        self.path_entry.insert(0, '-')
        self.path_entry.grid(row=1, column=1, **self.padding)

        # Sort button
        self.sort_button = ctk.CTkButton(self.window, text='Sort', command=self.sorting)
        self.sort_button.grid(row=2, column=1, **self.padding)

    def update_field(self, text: str):
        """Updates the result of the path field."""
        self.path_entry.delete(0, ctk.END)
        self.path_entry.insert(0, text)
        self.path_entry.configure(state='disabled')

    def sorting(self):
        if self.path == '':
            pass
        else:
            File_Sorter.sort_files(self.path)

    # Opening Windows explorer with this function.
    def getting_path(self):
        self.path: str = ctk.filedialog.askdirectory()
        print(self.path)
        self.update_field(self.path)

    def run(self):
        """Runs the Explorer window."""
        self.window.mainloop()


class ToplevelWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.geometry("200x100")
        self.resizable(False, False)
        self.title('Message')
        self.label = ctk.CTkLabel(self, text="Sorted Successfully!!!")
        self.label.pack(padx=20, pady=20)
