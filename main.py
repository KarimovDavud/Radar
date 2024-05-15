import tkinter as tk
import webbrowser

from faker import Faker
from radar import Radar
from random import randint
from protocol import Protocol
from datetime import datetime
from PIL import Image, ImageTk


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Results of the protocol")
        self.root.configure(bg='white')  

        
        self.background_image = Image.open("dyp.jpg")
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.background_label = tk.Label(root, image=self.background_photo, bg='white')
        self.background_label.place(x=1, y=1, relwidth=0.5, relheight=0.5)

        
        self.radar_options = [
            ("Cemsid naxcivanski", 60, 70),
            ("Lokbatan dairesi", 80, 90),
            ("Heyder aliyev prospekti", 70, 80)
        ]

        self.radar_selection = tk.StringVar()
        self.radar_selection.set(self.radar_options[0][0])

        self.radar_menu = tk.OptionMenu(self.root, self.radar_selection, *self.get_radar_names())
        self.radar_menu.config(bg='white', fg='black')  
        self.radar_menu.pack()

        self.write_protocol_button = tk.Button(self.root, text="|>-Show Protocol-<|", command=self.write_protocol, bg='white', fg='blue')
        self.write_protocol_button.pack()

        self.protocol_number_label = tk.Label(self.root, text="Enter Protocol Number:", bg='white', fg='green')
        self.protocol_number_label.pack()

        self.protocol_number_entry = tk.Entry(self.root)
        self.protocol_number_entry.pack()

        self.search_protocol_button = tk.Button(self.root, text="Search Protocol", command=self.search_protocol, bg='white', fg='blue')
        self.search_protocol_button.pack()

        self.text = tk.Text(self.root, height=19, width=65)
        self.text.pack()

        self.pay_button = tk.Button(self.root, text="Pay", command=self.open_payment_url)
        self.pay_button.pack()


    def get_radar_names(self):
        return [option[0] for option in self.radar_options]

    def write_protocol(self):
        faker = Faker()
        fake_datetime = faker.date_time_this_decade()
        fake_date_without_seconds = fake_datetime.strftime("%Y-%m-%d %H:%M")
        protocol_number = randint(1000, 1100)
        fake_num_police = faker.first_name_female()
        fake_num_driver = faker.first_name()  
        road_name = self.radar_selection.get()
        car_number = f"{randint(10, 99)}-{''.join([chr(randint(65, 90)) for _ in range(2)])}-{randint(100, 999)}"
        
        if "AA" in car_number or "PM" in car_number:
            protocol_text = "    Azerbaycan Respublikasi DIN Bas Devlet Yol Polisi Idaresi\n"
            protocol_text = " \nCars with AA and PM numbers cannot be fined. These numbers are filtered"
        else:
            radar_instance = Radar(road_name, 0, 0)  
            speed_result = radar_instance.check_speed() 
            belt_result = radar_instance.check_seat_belt()  
            protocol_text = Protocol.write_protocol(protocol_number, fake_num_driver, fake_num_police, road_name, car_number, speed_result, belt_result, fake_date_without_seconds)
        
        self.text.delete("1.0", tk.END)
        self.text.insert(tk.END, protocol_text)
        
        if not ("AA" in car_number or "PM" in car_number):
            Protocol.add_protocol_to_database(protocol_number, fake_num_driver, fake_num_police, road_name, car_number, speed_result, belt_result, fake_date_without_seconds)

    def search_protocol(self):
        protocol_number = self.protocol_number_entry.get()
        protocol = Protocol.search_protocol_by_number(protocol_number)
        if protocol:
            protocol_number, fake_num_driver, fake_num_police,  road_name, car_number, speed_result, belt_result, fake_date_without_seconds = protocol[1:]
            protocol_text = Protocol.write_protocol(protocol_number, fake_num_driver, fake_num_police, road_name, car_number, speed_result, belt_result, fake_date_without_seconds)
            self.text.delete("1.0", tk.END)
            self.text.insert(tk.END, protocol_text)
        else:
            self.text.delete("1.0", tk.END)
            self.text.insert(tk.END, "Protocol not found.")

    def open_payment_url(self):
        webbrowser.open("https://www.million.az/services/governmentalpayments/DYP")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()