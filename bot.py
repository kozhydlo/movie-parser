import sqlite3
import telebot
from telebot import types
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

bot = telebot.TeleBot("TOKEN")


options = Options()
options.headless = True

@bot.message_handler(commands=['start'])

def send_welcome(message):
    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = types.KeyboardButton('Пошук по назві')
    itembtn2 = types.KeyboardButton('Пошук по опису')
    itembtn3 = types.KeyboardButton('Рандомний')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.send_message(chat_id, "Що найти?", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == 'Пошук по назві':
        f = open("text.txt", "w")
        f.write("Назва")
        f.close()
        chat_id = message.chat.id
        bot.send_message(chat_id, "Введіть назву:")


    elif message.text == 'Пошук по опису':
        f = open("text.txt", "w")
        f.write("Опис")
        f.close()
        chat_id = message.chat.id
        bot.send_message(chat_id, "Введіть опис:")        

    elif message.text == 'Рандомний':
        f = open("text.txt", "w")
        f.write("Рандомний")
        f.close()
        
        chat_id = message.chat.id
        bot.send_message(chat_id, "Опрацьовую запрос...")

        db = sqlite3.connect('KINO3.db')
        cur = db.cursor()

        for rand in cur.execute('SELECT * FROM KINO3 WHERE ID IN (SELECT ID FROM KINO3 ORDER BY RANDOM() LIMIT 1)'):

            print(rand)       
            name = rand[2]
            quality = rand[3]
            opisanie = rand[4]
            link1 = rand[5]

            driver = webdriver.Firefox(options=options)

            try:
                driver.get(link1)
                time.sleep(2)
            
                driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
                element2 = driver.find_element(By.XPATH, """/html/body/div/pjsdiv/pjsdiv[1]/video""")
            
                            
                print(element2.get_attribute('src'))
            
                itog = str(element2.get_attribute('src'))
            
                a1 = itog.split('/240.mp4') 
                a2 = str(a1[0]) + "/720.mp4"
                print(a2)
            
                link2 = a2
            
            except:
                print("Помилка")
            
                link2 = "Помилка"

            driver.quit()

            q = open("text.txt", "w")
            q.write(str(name))
            q.write('\n')
            q.write(str(quality))
            q.write('\n')
            q.write('\n')
            q.write(str(opisanie))
            q.write('\n')
            q.write('\n')
            q.write(str(link1))
            q.write('\n')
            q.write('\n')
            q.write(str(link2))
            q.close()
            
            msg = open("text.txt", "r")
            msgR = msg.read()
            chat_id = message.chat.id
            bot.send_message(chat_id, msgR)                            




    else:
        chat_id = message.chat.id
        bot.send_message(chat_id, "Опрцьовую запрос...")

        db = sqlite3.connect('KINO3.db')
        cur = db.cursor()

        word = message.text
        r = open("text.txt", "r")
        readR = r.read()

        if readR == "Назва":
            driver = webdriver.Firefox(options=options)
            
            name_list = []
            opisanie_list = []
            quality_list = []
            Link1_list = []
            Link2_list = []

            
            for name in cur.execute('SELECT NAME FROM KINO3 WHERE NAME LIKE ?', ('%'+word+'%',)):
                name_list.append(name[0])

            for opisanie in cur.execute('SELECT OPISANIE FROM KINO3 WHERE NAME LIKE ?', ('%'+word+'%',)):
                opisanie_list.append(opisanie[0]) 

            for quality in cur.execute('SELECT QUALITY FROM KINO3 WHERE NAME LIKE ?', ('%'+word+'%',)):
                quality_list.append(quality[0])     

            for Link1 in cur.execute('SELECT LINK_STR FROM KINO3 WHERE NAME LIKE ?', ('%'+word+'%',)):
                Link1_list.append(Link1[0])  

            for film in Link1_list:
                try:
                    driver.get(film)
                    time.sleep(2)
                    driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
                    element2 = driver.find_element(By.XPATH, """/html/body/div/pjsdiv/pjsdiv[1]/video""")

                    itog = str(element2.get_attribute('src'))
                    a1 = itog.split('/240.mp4')
                    a2 = str(a1[0]) + "/720.mp4"
                    print(a2)                

                    Link2_list.append(a2)

                except:
                    print("Помилка")

                    Link2_list.append("Помилка") 


            driver.quit()

            i = 0
            while i < len(name_list):

                q = open("text.txt", "w")
                q.write(str(name_list[i]))
                q.write('\n')
                q.write(str(quality_list[i]))
                q.write('\n')
                q.write('\n')
                q.write(str(opisanie_list[i]))
                q.write('\n')
                q.write('\n')
                q.write(str(Link1_list[i]))
                q.write('\n')
                q.write('\n')
                q.write(str(Link2_list[i]))
                q.close()

                msg = open("text.txt", "r")
                msgR = msg.read()
                chat_id = message.chat.id
                bot.send_message(chat_id, msgR)
                time.sleep(1)
                i = i + 1

        elif readR == "Опис":

            driver = webdriver.Firefox(options=options)
            z = open('text.txt', 'w')
            z.seek(0)
            z.close()
            name_list = []
            opisanie_list = []
            quality_list = []
            Link1_list = []
            Link2_list = []
            for name in cur.execute('SELECT NAME FROM KINO3 WHERE OPISANIE LIKE ?', ('%'+word+'%',)):
                print(name)
                name_list.append(name[0])

            for opisanie in cur.execute('SELECT OPISANIE FROM KINO3 WHERE OPISANIE LIKE ?', ('%'+word+'%',)):
                print(opisanie)
                opisanie_list.append(opisanie[0])

            for quality_list in cur.execute('SELECT QUALITY FROM KINO3 WHERE OPISANIE LIKE ?', ('%'+word+'%',)):
                print(quality)
                quality_list.append(quality[0])                        

            for Link1 in cur.execute('SELECT LINK_STR FROM KINO3 WHERE OPISANIE LIKE ?', ('%'+word+'%',)):
                print(Link1)
                Link1_list.append(Link1[0])

            for film in Link1_list:
            
                try:
                    driver.get(film)
                    time.sleep(2)

                    driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
                    element2 = driver.find_element(By.XPATH, """/html/body/div/pjsdiv/pjsdiv[1]/video""")

                
                    print(element2.get_attribute('src'))

                    itog = str(element2.get_attribute('src'))

                    a1 = itog.split('/240.mp4') 
                    a2 = str(a1[0]) + "/720.mp4"
                    print(a2)

                    Link2_list.append(a2)

                except:

                    print("Помилка")

                    Link2_list.append("Помилка")
                 
            

            
            i = 0
            driver.quit()             
            while i < len(name_list):
                

                q = open("text.txt", "w")
                q.write(str(name_list[i]))
                q.write('\n')
                q.write(str(quality_list[i]))
                q.write('\n')
                q.write('\n')
                q.write(str(opisanie_list[i]))
                q.write('\n')
                q.write('\n')
                q.write(str(Link1_list[i]))
                q.write('\n')
                q.write('\n')
                q.write(str(Link2_list[i]))
                q.close()

                msg = open("text.txt", "r")
                msgR = msg.read()
                chat_id = message.chat.id
                bot.send_message(chat_id, msgR)
                time.sleep(1)
                i = i + 1 
                

bot.polling()
