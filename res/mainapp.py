#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on Thu Mar 13 14:32:31 2025

@author: Wiesinger Franz
'''


# Python 3+
import tkinter as tk
from tkinter import ttk
from . views import ConvertView
from tkinter import messagebox
from . constants import AppFonts as af
from tkhtmlview import HTMLScrolledText as html_st
from tkhtmlview import RenderHTML


class Application(tk.Tk):
    '''Application root window'''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Unixtime Converter')
        self.uxicon_sm = tk.PhotoImage(file='ux_logo_white_16.png')
        self.uxicon_med = tk.PhotoImage(file='ux_logo_white_32.png')
        self.iconphoto(False, self.uxicon_med, self.uxicon_sm)

        # containers:
        container = tk.Frame(self, width=400)

        # set position for the objects:
        container.grid(
            row=0, column=0, padx=10, pady=10, sticky=(
                tk.N + tk.S + tk.W + tk.E
            )
        )

        menbar_main = tk.Menu(self)

        men_file = tk.Menu(menbar_main, tearoff=0)
        men_file.add_command(label='Close', command=self.quit)
        menbar_main.add_cascade(label='File', menu=men_file)

        men_help = tk.Menu(menbar_main, tearoff=0)
        men_help.add_command(
            label='License',
            command=self.show_license
        )
        men_help.add_command(
            label='Help',
            command=self.show_help
        )
        men_help.add_command(
            label='About...', command=self.aboutbox)
        menbar_main.add_cascade(label='Help', menu=men_help)

        tk.Tk.config(self, menu=menbar_main)

        self.mainform = ConvertView(container)
        self.mainform.grid(
            row=0, padx=10, sticky=(tk.N + tk.S + tk.W + tk.E)
        )

    def donothing(self):
        pass

    def aboutbox(self):
        '''shows the box About... on click in menu'''

        about_header = 'Unixtime Converter'

        about_body = (
            ('Free tool for convertig local or utc date and time')
            + (' into unixtime or reverse. \n\n')
            + ('Author: Franz Wiesinger \n\n')
            + ('www.roadrunnerserver.com \n\n')
            + ('Copyright (c) 2025 Franz Wiesinger, roadrunnerserver.com')
        )

        messagebox.showinfo(
            title='About Unixtime Converter', message=about_header,
            detail=about_body
        )

    def show_license(self):

        self.license_dialog = tk.Toplevel(self)
        self.license_dialog.minsize(250, 300)

        container = tk.Frame(self.license_dialog)
        frame_head = tk.Frame(container)
        frame_body = tk.Frame(container)

        lbl_lic_header = tk.Label(
            frame_body, text='Lincense', relief='flat', anchor=(tk.W),
            font=af.fontabout_header
        )
        lbl_lic_body = tk.Label(
            frame_body,
            text='Copyright (c) 2025, Franz Wiesinger (roadrunnerserver.com)',
            relief='flat', anchor=(tk.W),
            font=af.fontdefault
        )

        self.txt_lic_text = html_st(
            frame_body, html=RenderHTML('license.html')
        )

        self.btn_close = ttk.Button(
            frame_body, text='Close', width=15,
            command=self.btn_tl_close
        )

        container.grid(
            row=0, column=0, padx=10, pady=10,
            sticky=(tk.N + tk.S + tk.W + tk.E)
        )
        frame_head.grid(row=0, column=0, pady=15, sticky=(tk.W + tk.E))
        frame_body.grid(
            row=0, column=0, pady=15, sticky=(tk.N + tk.S + tk.W + tk.E)
        )

        lbl_lic_header.grid(row=0, column=0, pady=15, sticky=(tk.W + tk.E))
        lbl_lic_body.grid(row=1, column=0, pady=10, sticky=(tk.W + tk.E))
        self.txt_lic_text.grid(
            row=2, column=0, pady=10, sticky=(tk.N + tk.S + tk.W + tk.E)
        )
        self.btn_close.grid(row=10, column=0, sticky=(tk.W))

    def show_help(self):

        self.help_dlg = tk.Toplevel(self)
        self.help_dlg.minsize(250, 300)

        dlgcontainer = tk.Frame(self.help_dlg)
        dlgframe_head = tk.Frame(dlgcontainer)
        dlgframe_body = tk.Frame(dlgcontainer)

        lbl_dlg_header = tk.Label(
            dlgframe_body, text='Get help...', relief='flat', anchor=(tk.W),
            font=af.fontabout_header
        )
        lbl_dlg_body = tk.Label(
            dlgframe_body,
            text='Copyright (c) 2025, Franz Wiesinger (roadrunnerserver.com)',
            relief='flat', anchor=(tk.W),
            font=af.fontdefault
        )
        self.txt_lic_text = html_st(
            dlgframe_body, html=RenderHTML('res/help.html')
        )

        self.btn_close = ttk.Button(
            dlgframe_body, text='Close', width=15,
            command=self.btn_helpdlg_close
        )

        dlgcontainer.grid(
            row=0, column=0, padx=10, pady=10,
            sticky=(tk.N + tk.S + tk.W + tk.E)
        )
        dlgframe_head.grid(row=0, column=0, pady=15, sticky=(tk.W + tk.E))
        dlgframe_body.grid(
            row=0, column=0, pady=15, sticky=(tk.N + tk.S + tk.W + tk.E)
        )

        lbl_dlg_header.grid(row=0, column=0, pady=15, sticky=(tk.W + tk.E))
        lbl_dlg_body.grid(row=1, column=0, pady=10, sticky=(tk.W + tk.E))
        self.txt_lic_text.grid(
            row=2, column=0, pady=10, sticky=(tk.N + tk.S + tk.W + tk.E)
        )
        self.btn_close.grid(row=10, column=0, sticky=(tk.W))

    def btn_tl_close(self):
        self.license_dialog.destroy()

    def btn_helpdlg_close(self):
        self.help_dlg.destroy()
