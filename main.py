import customtkinter
from customtkinter import *
import customtkinter as ctk
import random
import string # для генерации пароля
import pyperclip # для копирования в буфер обмена
from PIL import Image

customtkinter.set_appearance_mode('dark')
class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Генератор пароля и логина')
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        window_width = 600
        window_height = 300

        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)

        self.geometry(f'{window_width}x{window_height}+{x}+{y}')
        self.resizable(False, False)
        self.attributes('-alpha', 0.9)  # 90% непрозрачности

        self.tab = ctk.CTkTabview(self, width=450)
        self.tab.pack(pady=10)
        self.tab.add('Пароль')
        self.tab.add('Логин')


        self.img = Image.open('duplicate_96659.png')


        self.main_frame = ctk.CTkFrame(self.tab.tab('Пароль'), width=450, height=400,
                                       border_width=2, border_color='#696969')
        self.main_frame.pack(pady=5)
        self.main_frame.pack_propagate(False)

        title_label = ctk.CTkLabel(self.main_frame, text='Генерация пароля', text_color='#9acd32',
                                   font=('Montserrat', 28))
        title_label.pack(pady=35)

        self.entry_password = ctk.CTkEntry(self.main_frame, text_color='#9acd32',
                                           width=320, border_width=1, border_color='#696969',
                                           height=30, placeholder_text='Ваш пароль',
                                           font=('Montserrat', 15))
        self.entry_password.place(x=50, y=90)

        copy_btn = ctk.CTkButton(self.main_frame, image=CTkImage(dark_image=self.img),
                                 text='', fg_color='transparent', border_width=1,
                                 border_color='#696969', width=17, hover_color='#393939',
                                 command=self.copy_password)
        copy_btn.place(x=390, y=90)

        btn_generate = ctk.CTkButton(self.main_frame, text='Создать',
                                     text_color='#fafafa', font=('Montserrat', 15),
                                     fg_color='transparent', hover_color='#9acd32',
                                     border_width=1, border_color='#fafafa', height=35,
                                     width=150, command=self.generate_passsword)
        btn_generate.pack(pady=30)




        self.main_frame_login = ctk.CTkFrame(self.tab.tab('Логин'), width=450, height=400,
                                       border_width=2, border_color='#696969')
        self.main_frame_login.pack(pady=5)
        self.main_frame_login.pack_propagate(False)

        title_label_login = ctk.CTkLabel(self.main_frame_login, text='Генерация логина',
                                         text_color='#a638f7',
                                   font=('Montserrat', 28))
        title_label_login.pack(pady=35)

        self.entry_login = ctk.CTkEntry(self.main_frame_login, text_color='#a638f7',
                                           width=320, border_width=1, border_color='#696969',
                                           height=30, placeholder_text='Ваш пароль',
                                           font=('Montserrat', 15))
        self.entry_login.place(x=50, y=90)

        copy_btn_login = ctk.CTkButton(self.main_frame_login, image=CTkImage(dark_image=self.img),
                                 text='', fg_color='transparent', border_width=1,
                                 border_color='#696969', width=17, hover_color='#393939',
                                 command=self.copy_login)
        copy_btn_login.place(x=390, y=90)

        btn_generate = ctk.CTkButton(self.main_frame_login, text='Создать',
                                     text_color='#fafafa', font=('Montserrat', 15),
                                     fg_color='transparent', hover_color='#a638f7',
                                     border_width=1, border_color='#fafafa', height=35,
                                     width=150, command=self.generate_login)
        btn_generate.pack(pady=30)

    def generate_login(self):
        characters = string.ascii_letters + string.digits
        login_length = 8
        login = ''.join(random.choice(characters) for _ in range(login_length))
        self.entry_login.delete(0, ctk.END)
        self.entry_login.insert(0, login)


    def generate_passsword(self):
        characters = string.ascii_letters + string.digits + string.punctuation
        password_length = 12
        password = ''.join(random.choice(characters) for _ in range(password_length))
        self.entry_password.delete(0, ctk.END)
        self.entry_password.insert(0, password)

    def copy_password(self):
        password = self.entry_password.get()
        pyperclip.copy(password)

    def copy_login(self):
        password = self.entry_login.get()
        pyperclip.copy(password)



if __name__ == '__main__':
    app = MainApp()
    app.mainloop()