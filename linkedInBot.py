from tkinter import *
from tkinter import ttk
import tkinter as tk
import os, sys, time
from urllib.parse import urlparse
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

sys.setrecursionlimit(3000)

#Title of the app
root = Tk()
root.title("LinkedIn Bot")
root.geometry("800x800")

#Notebook for tabs
my_notebook = ttk.Notebook(root)
my_notebook.pack()

#Adding tabs
tab_one = Frame(my_notebook, width=800, height=800)
tab_two = Frame(my_notebook, width=800, height=800)
tab_three = Frame(my_notebook, width=800, height=800)

tab_one.pack(fill="both", expand=1)
tab_two.pack(fill="both", expand=1)
tab_three.pack(fill="both", expand=1)

my_notebook.add(tab_one, text="Login")
my_notebook.add(tab_two, text="Select Filters")
my_notebook.add(tab_three, text="Send Message")

#Username text and input
empty_label = Label(tab_one, text="", justify=LEFT, anchor="w", font="Raleway", pady=5)
empty_label.grid(sticky = W, row=0, column=0)

""" entry_username = Label(tab_one, text="Username", justify=LEFT, anchor="w", font="Raleway", pady=5)
entry_username.grid(sticky = W, row=1, column=0, padx=10)
username_input = Entry(tab_one, width=35)
username_input.grid(sticky = W, row=2, column=0, columnspan=2, padx=10, pady=5)

#Password text and input
entry_password = Label(tab_one, text="Password", justify=LEFT, anchor="w", pady=5, font="Raleway")
entry_password.grid(sticky = W, row=3, column=0, padx=10)
password_input = Entry(tab_one, width=35, show="*")
password_input.grid(row=4, column=0, columnspan=2, padx=10, pady=5) """

#Delete login items
def delete_login():
    my_notebook.hide(0)

#Call two functions on Login 
def login_final():
    resource_path(".\\selenium\\webdriver")
    login()
    delete_login()

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

#Open driver and login
def login():
    username = 'leoplazavzla@gmail.com'
    password = 'Caracter$$456'
    global driver
    driver = webdriver.Chrome(executable_path = resource_path('./driver/chromedriver.exe'))
    global scrollPauseTime 
    scrollPauseTime = 2
    driver.get('https://www.linkedin.com/login')
    time.sleep(scrollPauseTime)
    elementID = driver.find_element(By.ID, 'username')
    time.sleep(scrollPauseTime-1)
    elementID.send_keys(username)
    elementID = driver.find_element(By.ID, 'password')
    time.sleep(scrollPauseTime-1)
    elementID.send_keys(password)
    time.sleep(scrollPauseTime)
    elementID.submit()
    time.sleep(1)


#Button for login
open_driver = Button(tab_one, text="Login", command=login_final, justify=LEFT, anchor="w", font="Raleway", pady=5, padx= 20)
open_driver.grid(row=5, column=0, columnspan=2, padx=20, pady=20)

#Empty spaces
empty_label2 = Label(tab_two, text="", justify=LEFT, anchor="w", font="Raleway", pady=5)
empty_label2.grid(sticky = W, row=0, column=0)

empty_label3 = Label(tab_two, text="", justify=LEFT, anchor="w", font="Raleway", pady=5)
empty_label3.grid(sticky = W, row=2, column=0)

empty_label4 = Label(tab_two, text="", justify=LEFT, anchor="w", font="Raleway", pady=5)
empty_label4.grid(sticky = W, row=5, column=0)

empty_label5 = Label(tab_three, text="", justify=LEFT, anchor="w", font="Raleway", pady=5)
empty_label5.grid(sticky = W, row=0, column=0)

#start_page
start_page = Label(tab_three, text="Start page", justify=LEFT, anchor="w", font="Raleway", pady=5)
start_page.grid(sticky = W, row=3, column=0)
start_page_input = Entry(tab_three, width=5)
start_page_input.grid(sticky = W, row=3, column=1, padx=5, pady=5)

#end_page
end_page = Label(tab_three, text="End page", justify=LEFT, anchor="w", font="Raleway", pady=5)
end_page.grid(sticky = W, row=4, column=0)
end_page_input = Entry(tab_three, width=5)
end_page_input.grid(sticky = W, row=4, column=1, padx=5, pady=5)

countries = [
    "Albania",
    "Algeria",
    "Andorra",
    "Angola",
    "Antigua and Barbuda",
    "Argentina",
    "Armenia",
    "Australia",
    "Austria",
    "Azerbaijan",
    "Bahamas",
    "Bahrain",
    "Bangladesh",
    "Barbados",
    "Belarus",
    "Belgium",
    "Belize",
    "Benin",
    "Bhutan",
    "Bolivia",
    "Bosnia and Herzegovina",
    "Botswana",
    "Brazil",
    "Brunei",
    "Bulgaria",
    "Burkina Faso",
    "Burundi",
    "Côte d Ivoire",
    "Cabo Verde",
    "Cambodia",
    "Cameroon",
    "Canada",
    "Central African Republic",
    "Chad",
    "Chile",
    "China",
    "Colombia",
    "Comoros",
    "Congo",
    "Costa Rica",
    "Croatia",
    "Cuba",
    "Cyprus",
    "Czechia",
    "Democratic Republic of the Congo",
    "Denmark",
    "Djibouti",
    "Dominica",
    "Dominican Republic",
    "Ecuador",
    "Egypt",
    "El Salvador",
    "Equatorial Guinea",
    "Eritrea",
    "Estonia",
    "Eswatini",
    "Ethiopia",
    "Fiji",
    "Finland",
    "France",
    "Gabon",
    "Gambia",
    "Georgia",
    "Germany",
    "Ghana",
    "Greece",
    "Grenada",
    "Guatemala",
    "Guinea",
    "Guinea-Bissau",
    "Guyana",
    "Haiti",
    "Holy See",
    "Honduras",
    "Hungary",
    "Iceland",
    "India",
    "Indonesia",
    "Iran",
    "Iraq",
    "Ireland",
    "Israel",
    "Italy",
    "Jamaica",
    "Japan",
    "Jordan",
    "Kazakhstan",
    "Kenya",
    "Kiribati",
    "Kuwait",
    "Kyrgyzstan",
    "Laos",
    "Latvia",
    "Lebanon",
    "Lesotho",
    "Liberia",
    "Libya",
    "Liechtenstein",
    "Lithuania",
    "Luxembourg",
    "Madagascar",
    "Malawi",
    "Malaysia",
    "Maldives",
    "Mali",
    "Malta",
    "Marshall Islands",
    "Mauritania",
    "Mauritius",
    "Mexico",
    "Micronesia",
    "Moldova",
    "Monaco",
    "Mongolia",
    "Montenegro",
    "Morocco",
    "Mozambique",
    "Myanmar",
    "Namibia",
    "Nauru",
    "Nepal",
    "Netherlands",
    "New Zealand",
    "Nicaragua",
    "Niger",
    "Nigeria",
    "North Korea",
    "North Macedonia",
    "Norway",
    "Oman",
    "Pakistan",
    "Palau",
    "Palestine State",
    "Panama",
    "Papua New Guinea",
    "Paraguay",
    "Peru",
    "Philippines",
    "Poland",
    "Portugal",
    "Qatar",
    "Romania",
    "Russia",
    "Rwanda",
    "Saint Kitts and Nevis",
    "Saint Lucia",
    "Saint Vincent and the Grenadines",
    "Samoa",
    "San Marino",
    "Sao Tome and Principe",
    "Saudi Arabia",
    "Senegal",
    "Serbia",
    "Seychelles",
    "Sierra Leone",
    "Singapore",
    "Slovakia",
    "Slovenia",
    "Solomon Islands",
    "Somalia",
    "South Africa",
    "South Korea",
    "South Sudan",
    "Spain",
    "Sri Lanka",
    "Sudan",
    "Suriname",
    "Sweden",
    "Switzerland",
    "Syria",
    "Tajikistan",
    "Tanzania",
    "Thailand",
    "Timor-Leste",
    "Togo",
    "Tonga",
    "Trinidad and Tobago",
    "Tunisia",
    "Turkey",
    "Turkmenistan",
    "Tuvalu",
    "Uganda",
    "Ukraine",
    "United Arab Emirates",
    "United Kingdom",
    "United States of America",
    "Uruguay",
    "Uzbekistan",
    "Vanuatu",
    "Venezuela",
    "Vietnam",
    "Yemen",
    "Zambia",
    "Zimbabwe",
]
countries_clicked = StringVar()
countries_clicked.set(countries[0])
trans = OptionMenu(tab_two, countries_clicked, *countries)
trans.grid(sticky = W, row=1, column=0, columnspan=2, padx=10)

insert_message_label = Label(tab_three, text="Insert message", justify=LEFT, anchor="w", font="Raleway", pady=5)
insert_message_label.grid(sticky = W, row=7, column=0, columnspan=2, padx=10)

text_message = Text(tab_three, width=30 )
text_message.grid(sticky= W, row= 8, column=0, columnspan=2, padx=10, pady=2)

verify = True #Global Flag

def look_connections():
    driver.get('https://www.linkedin.com/mynetwork/invite-connect/connections/')
    time.sleep(3)
    filter_button = driver.find_element(By.CLASS_NAME, 'mn-connections__search-with-filters')
    filter_button.click()
    time.sleep(3)
    locations_button = driver.find_element(By.XPATH, '//button[text()="Locations"]')
    locations_button.click()
    time.sleep(3)
    add_location = driver.find_element(By.XPATH, '//input[@placeholder="Add a location"]')
    add_location.click()
    time.sleep(2)
    add_location.send_keys(countries_clicked.get(), Keys.ARROW_DOWN, Keys.ENTER)
    time.sleep(1)
    add_location.send_keys(Keys.ARROW_DOWN)
    time.sleep(1)
    add_location.send_keys(Keys.ENTER)
    show_results = driver.find_element(By.CLASS_NAME, "scaffold-layout-toolbar")
    show_results.click()
    time.sleep(4)

def find_contacts():
    contacts = driver.find_element(By.CLASS_NAME, 'reusable-search__entity-result-list')
    contact_li = contacts.find_elements(By.TAG_NAME, 'li')
    return contact_li


def send_message():
    global verify
    verify = True
    #tab_two.update()
    #tab_two.after(5000, realcallback)
    message = text_message.get("1.0", END)
    print(message)

    #scroll window
    height = driver.execute_script("return document.documentElement.scrollHeight")
    scrollPauseTime = 2
    driver.execute_script("window.scrollTo(0, " + str(height/2) + ");")
    time.sleep(scrollPauseTime-1)
    driver.execute_script("window.scrollTo(0, " + str(height) + ");")
    time.sleep(scrollPauseTime)

    # find contact pages
    try:
        page_numbers = driver.find_elements(By.CLASS_NAME, 'artdeco-pagination__indicator')
        try:
            real_page_numbers = int(page_numbers[9].text)
        except:
            real_page_numbers = int(page_numbers[-1].text)
        time.sleep(2)
        page_numbers[int(start_page_input.get()) -1].click()
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, 0); ")
        time.sleep(scrollPauseTime)
    except:
        page_numbers = 1
        time.sleep(1)
    
    #running through every contact page
    driver.execute_script("window.scrollTo(0, 0); ")
    time.sleep(2)

    if page_numbers == 1:
        contact_li = find_contacts()
        time.sleep(1)
        for contact in contact_li:
            #print(contact)
            contact_link = contact.find_element(By.TAG_NAME, 'a').get_attribute('href')
            print(contact_link)
            time.sleep(1)
            user_name_container = contact.find_element(By.CLASS_NAME, 'entity-result__title-text').text
            space_index = user_name_container.find(" ")
            if space_index != -1:
                user_name = user_name_container[:space_index]
                print(user_name_container[:space_index])
            else:
                # If no space was found, print the entire string
                print(user_name)
                user_name = ''
            message_button = contact.find_element(By.TAG_NAME, 'button')
            #df.loc[contact, 'linkedinId'] = contact_link.get_attribute('href')
            #df.to_excel(dataLocation, index=False)
            time.sleep(2)
            message_button.click()
            time.sleep(2)
            message_box_container = driver.find_element(By.CLASS_NAME, 'msg-form__contenteditable')
            message_box_container.click()
            time.sleep(2) 
            message_box_container.send_keys(f'Hello {user_name} \n\n {message}')
            time.sleep(2)
            send_button = driver.find_element(By.XPATH, '//button[text()="Send"]')
            send_button.click()
            time.sleep(3)
    else:
        for contact_page in range (int(start_page_input.get()), int(end_page_input.get())):
            time.sleep(1)
            
            # find contacts
            contacts = driver.find_element(By.CLASS_NAME, 'reusable-search__entity-result-list')
            contact_li = contacts.find_elements(By.TAG_NAME, 'li')
            print(len(contact_li))

            # going through all contacts in every page
            for contact in contact_li:
                #print(contact)
                contact_link = contact.find_element(By.TAG_NAME, 'a').get_attribute('href')
                print(contact_link)
                time.sleep(1)
                user_name_container = contact.find_element(By.CLASS_NAME, 'entity-result__title-text').text
                space_index = user_name_container.find(" ")
                if space_index != -1:
                    user_name = user_name_container[:space_index]
                    print(user_name_container[:space_index])
                else:
                    # If no space was found, print the entire string
                    print(user_name)
                    user_name = ''
                message_button = contact.find_element(By.TAG_NAME, 'button')
                time.sleep(2)
                message_button.click()
                time.sleep(2)
                message_box_container = driver.find_element(By.CLASS_NAME, 'msg-form__contenteditable')
                message_box_container.click()
                time.sleep(2) 
                message_box_container.send_keys(f'Hello {user_name} \n\n {message}')
                time.sleep(2)
                send_button = driver.find_element(By.XPATH, '//button[text()="Send"]')
                send_button.click()
                time.sleep(3)

            #move to next page
            driver.execute_script("window.scrollTo(0, " + str(height) + ");")
            time.sleep(2)
            next_button = driver.find_element(By.XPATH, '//button[@aria-label="Next"]')
            next_button.click()
            time.sleep(2) 

def send_message_test():
    global verify
    verify = True
    #tab_two.update()
    #tab_two.after(5000, realcallback)
    message = text_message.get("1.0", END)
    print(message)
    
    #scroll window
    height = driver.execute_script("return document.documentElement.scrollHeight")
    scrollPauseTime = 2
    driver.execute_script("window.scrollTo(0, " + str(height/2) + ");")
    time.sleep(scrollPauseTime-1)
    driver.execute_script("window.scrollTo(0, " + str(height) + ");")
    time.sleep(scrollPauseTime)

    # find contact pages
    try:
        page_numbers = driver.find_elements(By.CLASS_NAME, 'artdeco-pagination__indicator')
        try:
            real_page_numbers = int(page_numbers[9].text)
        except:
            real_page_numbers = int(page_numbers[-1].text)
        time.sleep(2)
        page_numbers[int(start_page_input.get()) -1].click()
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, 0); ")
        time.sleep(scrollPauseTime)
    except:
        page_numbers = 1
        time.sleep(1)
    
    #running through every contact page
    #for contact_page in range(1, real_page_numbers +1)
    driver.execute_script("window.scrollTo(0, 0); ")
    time.sleep(scrollPauseTime)

    if page_numbers == 1:
        contact_li = find_contacts()
        for contact in contact_li:
            #print(contact)
            contact_link = contact.find_element(By.TAG_NAME, 'a').get_attribute('href')
            print(contact_link)
            time.sleep(1)
            user_name_container = contact.find_element(By.CLASS_NAME, 'entity-result__title-text').text
            space_index = user_name_container.find(" ")
            if space_index != -1:
                user_name = user_name_container[:space_index]
                print(user_name_container[:space_index])
            else:
                # If no space was found, print the entire string
                print(user_name)
                user_name = ''
            message_button = contact.find_element(By.TAG_NAME, 'button')
            #df.loc[contact, 'linkedinId'] = contact_link.get_attribute('href')
            #df.to_excel(dataLocation, index=False)
            time.sleep(2)
            message_button.click()
            time.sleep(2)
            message_box_container = driver.find_element(By.CLASS_NAME, 'msg-form__contenteditable')
            message_box_container.click()
            time.sleep(2) 
            message_box_container.send_keys(f'Hello {user_name} \n\n {message}')
            """ time.sleep(2)
            send_button = driver.find_element(By.XPATH, '//button[text()="Send"]')
            send_button.click() """
            time.sleep(3)
            message_box_container.send_keys(Keys.ESCAPE)
            time.sleep(2)
            discard_container = driver.find_elements(By.TAG_NAME, 'button')
            time.sleep(1)
            discard_container[2].click()
    else:
        for contact_page in range (int(start_page_input.get()), int(end_page_input.get())):
            time.sleep(1)
            # find contacts
            contact_li = find_contacts()

            # going through all contacts in every page
            for contact in contact_li:
                #print(contact)
                contact_link = contact.find_element(By.TAG_NAME, 'a').get_attribute('href')
                print(contact_link)
                time.sleep(1)
                user_name_container = contact.find_element(By.CLASS_NAME, 'entity-result__title-text').text
                space_index = user_name_container.find(" ")
                if space_index != -1:
                    user_name = user_name_container[:space_index]
                    print(user_name_container[:space_index])
                else:
                    # If no space was found, print the entire string
                    print(user_name)
                    user_name = ''
                message_button = contact.find_element(By.TAG_NAME, 'button')
                #df.loc[contact, 'linkedinId'] = contact_link.get_attribute('href')
                #df.to_excel(dataLocation, index=False)
                time.sleep(2)
                message_button.click()
                time.sleep(2)
                message_box_container = driver.find_element(By.CLASS_NAME, 'msg-form__contenteditable')
                message_box_container.click()
                time.sleep(2) 
                message_box_container.send_keys(f'Hello {user_name} \n\n {message}')
                """ time.sleep(2)
                send_button = driver.find_element(By.XPATH, '//button[text()="Send"]')
                send_button.click() """
                time.sleep(3)
                message_box_container.send_keys(Keys.ESCAPE)
                time.sleep(3)
                discard_container = driver.find_elements(By.TAG_NAME, 'button')
                time.sleep(1)
                discard_container[2].click()

            #move to next page
            driver.execute_script("window.scrollTo(0, " + str(height) + ");")
            time.sleep(2)
            next_button = driver.find_element(By.XPATH, '//button[@aria-label="Next"]')
            next_button.click()
            time.sleep(2)
        

#Button for look connections with filters
search_with_filters = Button(tab_two, text="Search with filters", command=look_connections, justify=LEFT, anchor="w", font="Raleway", pady=5)
search_with_filters.grid(row=6, column=0, columnspan=2, padx=20, pady=20)
    
#Button for send message
empty_label3 = Label(tab_two, text="", justify=LEFT, anchor="w", font="Raleway", pady=5)
empty_label3.grid(row=5, column=0)

find_trans = Button(tab_three, text="Send Message", command=send_message, justify=LEFT, anchor="w", font="Raleway", pady=5)
find_trans.grid(row=9, column=0, columnspan=1, padx=20, pady=20)

sending_test_message = Button(tab_three, text="Make Test", command=send_message_test, justify=LEFT, anchor="w", font="Raleway", pady=5)
sending_test_message.grid(row=9, column=2, columnspan=1, padx=20, pady=20)

root.mainloop()