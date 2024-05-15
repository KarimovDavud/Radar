
import os
import sqlite3

from faker import Faker
from random import randint


faker = Faker()
class Protocol:
    @staticmethod
    def write_protocol(protocol_number, fake_num_driver, fake_num_police,  road_name, car_number, protocol_amount, belt_check, fake_date_without_seconds):
        os.system("clear")      
        protocol_text = f"      Azerbaycan Respublikasi DIN Bas Devlet Yol Polisi Idaresi\n\n"
        protocol_text += f"                             PRATAKOL N {protocol_number}\n"
        protocol_text += "|--------------------------------------------------------------|\n"
        protocol_text += f" Road Name: {road_name}\n"
        protocol_text += "|--------------------------------------------------------------|\n"
        protocol_text += f" Car Number: {car_number}\n"
        protocol_text += "|--------------------------------------------------------------|\n"
        protocol_text += f" Speed: {protocol_amount}\n"
        protocol_text += "|--------------------------------------------------------------|\n"
        protocol_text += f" Belt: {belt_check}\n"
        protocol_text += "|--------------------------------------------------------------|\n"
        protocol_text += f" Name Police: {fake_num_police}\n"
        protocol_text += "|--------------------------------------------------------------|\n"
        protocol_text += f" Name Driver: {fake_num_driver}\n"
        protocol_text += "|--------------------------------------------------------------|\n"
        protocol_text += f" Date: {fake_date_without_seconds}\n"
        protocol_text += "|--------------------------------------------------------------|\n"
        return protocol_text

    @staticmethod
    def add_protocol_to_database(protocol_number, fake_num_driver, fake_num_police,  road_name, car_number, speed_result, belt_result, fake_date_without_seconds):
        conn = sqlite3.connect('protocol_database.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS protocols
                          (id INTEGER PRIMARY KEY AUTOINCREMENT,
                           protocol_number INTEGER,
                           fake_num_driver TEXT,
                           fake_num_police TEXT,
                           road_name TEXT,
                           car_number TEXT,
                           speed TEXT,
                           belt TEXT,
                           fake_date_without_seconds TEXT)''')
        conn.commit()

        cursor.execute('''INSERT INTO protocols (protocol_number, fake_num_driver, fake_num_police, road_name, car_number, speed, belt, fake_date_without_seconds) VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                       (protocol_number, fake_num_driver, fake_num_police,  road_name, car_number, speed_result, belt_result, fake_date_without_seconds))
        conn.commit()
        conn.close()

    @staticmethod
    def search_protocol_by_number(protocol_number):
        conn = sqlite3.connect('protocol_database.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM protocols WHERE protocol_number = ?''', (protocol_number,))
        result = cursor.fetchone()
        conn.close()
        return result