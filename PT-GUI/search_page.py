from tkinter import font as tkfont
from tkinter import messagebox

from nav_bar import *

class SearchPage(tk.Frame):
    """
    Search Result page class.
    """

    def __init__(self, parent, controller):
        """
        Search result page init.
        """
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        # displays navbar at top of app screen
        display_nav_bar(self, controller)
        # sets font for frame
        framefont = tkfont.Font(family='Calibri', size=33, weight="bold")
        # sets font for buttons
        tkfont.Font(family='Calibri', size=13)

        # creates blue bar as canvas below nav bar housing label containing title of page
        title_canvas = tk.Canvas(self, bg='#3A4C5E', highlightthickness=0)
        title_canvas.place(rely=0.08, relheight=0.12, relwidth=1)
        title_label = tk.Label(self, text="Search Results", bg='#3A4C5E', fg='white',
                               anchor="c", font=framefont)
        title_label.place(rely=0.08, relheight=0.12, relwidth=1)

        # extra frame for spacing, pushes all subsquent content below nav bar and title
        # label using the pady field
        frameextra = Label(self, bg='#3A4C5E')
        frameextra.pack(pady=120)

        # new frame for tools list
        container = Frame(self)
        container.pack(fill='both', expand=True)
        # create a canvas on the new frame
        canvas = Canvas(container)

        # create scrollbar on new frame
        # scrollbar y
        scrollbar_y = ttk.Scrollbar(container,
                                orient=VERTICAL,
                                command=canvas.yview)
        scrollbar_y.pack(side=RIGHT, fill=Y)
        scrollbar_y.config(command=canvas.yview)
        # create scrollbar x
        scrollbar_x = ttk.Scrollbar(container,
                                orient=HORIZONTAL,
                                command=canvas.xview)
        scrollbar_x.pack(side=BOTTOM, fill=X)
        scrollbar_x.config(command=canvas.xview)
        # create new canvas that will be scrolled
        scrollable_frame = Frame(canvas)
        # binds scroll canvas to execute function that gets scrollable region of canvas on event e
        scrollable_frame.bind("<Configure>",
                              lambda _: canvas.configure(scrollregion=canvas.bbox("all")))

        # creates new window using scrollable frame as a base
        canvas.create_window((565, 0), window=scrollable_frame, anchor="nw")

        # sets scrollcommand to the existing scrollbar, linking the widgets
        canvas.config(
            xscrollcommand=scrollbar_x.set,
            yscrollcommand=scrollbar_y.set
        )
        canvas.pack(side=LEFT, fill=BOTH, expand=True)
        global info_image
        info_image = tk.PhotoImage(file='resources/Info_button.png')

        # packs passed widget to the left of screen, used for creating a vector entry
        def pack_widget_left(button):
            button.pack(fill='x', padx=10, pady=(1, 1), side=LEFT)

        # same as above but to right of screen
        def pack_widget_right(button):
            button.pack(fill='x', padx=10, pady=(1, 1), side=RIGHT)

        #show search field and button
        global data
        data = ''
        search_text_box = ttk.Entry(scrollable_frame)
        pack_widget_left(search_text_box)
        #search_text_box.grid(row = 0, column = 10)
        search_button = ttk.Button(scrollable_frame, compound=LEFT, text="Search", command=lambda: controller.command(search_function(data)))
        pack_widget_right(search_button)
        #search_button.grid(row = 0, column = 20)

        # search function that runs when the search page starts if the search field is not empty
        def search_function(data):
            # creates a canvas for all the search results/pages
            search_canvas = tk.Canvas(scrollable_frame, height=10)
            data = search_text_box.get()

            if data == '':
                messagebox.showerror('Error:', 'Please Enter Search Parameters.')
            else:
                data_string = "Search parameters are: " + data + ". "
                messagebox.showerror('Success:', data_string)

