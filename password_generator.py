import tkinter
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
import customtkinter
from PIL import Image
import password


# доделать:
# 1. Синхронизацию ползунка и цифры
# 2. Отсутствие возможности менять сгенерированный пароль, а только возможность его копировать


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("460x370")
        self.title("Password generator")
        self.resizable(False, False)

        self.logo = customtkinter.CTkImage(dark_image=Image.open("D:/1_dev/Part_2_python/projects/test/2023.06_June/password_generator/assets/img/img.png"), 
                                           size=(440, 150))
        self.logo_label = customtkinter.CTkLabel(master=self, text="", image=self.logo)
        self.logo_label.grid(row=0, column=0, pady=(10, 10))

        self.password_frame = customtkinter.CTkFrame(master=self, fg_color="transparent")
        self.password_frame.grid(row=1, column=0, padx=(20, 20), sticky="nsew")

        self.entry_password = customtkinter.CTkEntry(master=self.password_frame, width=300)
        self.entry_password.grid(row=0, column=0, padx=(0, 20))

        self.button_generate = customtkinter.CTkButton(master=self.password_frame, text="Generate", 
                                                       width=100, command=self.set_password)
        self.button_generate.grid(row=0, column=1)

        self.settings_frame = customtkinter.CTkFrame(master=self)
        self.settings_frame.grid(row=2, column=0, padx=(20, 20), pady=(20, 0), sticky="nsew")

        self.password_length_slider = customtkinter.CTkSlider(master=self.settings_frame, from_=0, to=100, 
                                                              number_of_steps=100, command=self.slider_event)
        self.password_length_slider.grid(row=1, column=0, columnspan=3, pady=(20, 20), sticky="ew")

        self.password_length_entry = customtkinter.CTkEntry(master=self.settings_frame, width=50)
        self.password_length_entry.grid(row=1, column=3, padx=(20, 10), sticky="we")

        self.cb_digits_var = tkinter.StringVar()
        self.cb_digits = customtkinter.CTkCheckBox(master=self.settings_frame, text="0-9", variable=self.cb_digits_var, onvalue=digits, 
                                                   offvalue="")
        self.cb_digits.grid(row=2, column=0, padx=10)
        
        self.cb_lower_var = tkinter.StringVar()
        self.cb_lower = customtkinter.CTkCheckBox(master=self.settings_frame, text="a-z", variable=self.cb_lower_var, 
                                                      onvalue=ascii_lowercase, offvalue="")
        self.cb_lower.grid(row=2, column=1)

        self.cb_upper_var = tkinter.StringVar()
        self.cb_upper = customtkinter.CTkCheckBox(master=self.settings_frame, text="A-Z", variable=self.cb_upper_var,
                                                  onvalue=ascii_uppercase, offvalue="")
        self.cb_upper.grid(row=2, column=2)

        self.cb_symbol_var = tkinter.StringVar()
        self.cb_symbol = customtkinter.CTkCheckBox(master=self.settings_frame, text="@#$%", variable=self.cb_symbol_var,
                                                   onvalue=punctuation, offvalue="")
        self.cb_symbol.grid(row=2, column=3)

        self.appearance_mode_option_menu = customtkinter.CTkOptionMenu(master=self.settings_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_option_menu.grid(row=3, column=0, columnspan=4, pady=(10, 10))

        self.password_length_slider.set(12)
        self.password_length_entry.insert(0, 12)

        self.appearance_mode_option_menu.set("System")
        

    def get_chatacters(self):
        chars = "".join(self.cb_digits_var.get() + self.cb_lower_var.get() + self.cb_upper_var.get() + self.cb_symbol_var.get())
        return chars

    def set_password(self):
        self.entry_password.delete(0, "end")
        self.entry_password.insert(0, password.create_new(length=int(self.password_length_slider.get()), 
                                   characters=self.get_chatacters()))

    def slider_event(self, value):
        self.password_length_entry.delete(0, "end")
        self.password_length_entry.insert(0, int(value))

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    app = App()
    app.mainloop()