import codecs
import sys
import requests
import random
import json
import time
import names


def First_Last_Name():

    Output = open("Generated\First_Last Name List.csv", 'w', newline='')
    print("Do you want to generate First Name ? (1)")
    print("Do you want to generate Last Name ? (2)")
    print('Do you want to generate Full Name (First + Last Name (3)')
    choice = int(input())
    print("How many do you want to generate ?")
    number = int(input())
    print('Do you want to generate male (M) or female (F) or Random (R) first names ? (sorry for all non binary <3)')
    print("Press enter if you have selected Last Name only")
    genre_choice = input()
    for i in range(0,number):

        if choice == 1:

            if genre_choice == "M" or genre_choice =='m':
                Output.write(names.get_first_name(gender='male')+ '\n')
            if genre_choice == "F" or genre_choice == 'f':
                Output.write(names.get_first_name(gender='female')+ '\n')
            if genre_choice == 'R' or genre_choice =='r':
                Output.write(names.get_first_name(gender='male')+ '\n')
                Output.write(names.get_first_name(gender='female')+ '\n')
                i + 1

        if choice == 2:
            Output.write(names.get_last_name())


    if choice ==3:
        Output.write('First Name, Last Name \n')
        for i in range (0,number):
            if genre_choice == "M" or genre_choice =='m':
                Output.write(names.get_first_name(gender='male') +',' + names.get_last_name() + '\n')
            if genre_choice == "F" or genre_choice == 'f':
                Output.write(names.get_first_name(gender='female' ',' + names.get_last_name())+ '\n')
            if genre_choice == 'R' or genre_choice =='r':
                Output.write(names.get_first_name(gender='male') + ',' + names.get_last_name()+ '\n')
                Output.write(names.get_first_name(gender='female') + ',' + names.get_last_name()+ '\n')
                i + 1




def Telephone_number_generator():
    print("It will be written in telephone number.csv")
    print("What's the 'country code' of your country (enter the thing that will stay fix)")
    country_code = input()
    print("How many number in total should the telephone number have")
    length_number = int(input())
    print("How many telephone number do you want to create ?")
    number = int(input())
    output_file = open("Generated\Telephone number.csv", 'w', newline='')  # Dossier de sortie
    output_file.write("Telephone number" + "\n")
    for i in range(0, number):
        output_file.write(country_code)
        for i in range(0, length_number - len(country_code)):
            randomnumber = random.randint(0, 9)
            output_file.write(str(randomnumber))

        output_file.write("\n")


def Dob_generator():
    print("It will be written in Dob.csv")
    print("All date of birth will be above 18 years old")
    output_file = open("Generated\Dob.csv", 'w', newline='')  # Dossier de sortie
    output_file.write("DOB \n")

    print("How many date of birth do you want to generate ?")
    number = int(input())
    print("Choose your format")
    print("Month-Day-Year (1)")
    print("Month/Day/Year (2)")
    print("Day-Month-Year (3)")
    print("Day/Month/Year (4)")
    choice = int(input())

    for i in range(0, number):
        month = str(random.randint(1, 12))
        if int(month) < 10:
            month = '0' + month
        day = str(random.randint(1, 28))
        if int(day) < 10:
            day = '0' + day
        year = str(random.randint(1980, 2001))

        if choice == 1:
            output_file.write(month + "-" + day + "-" + year + "\n")

        if choice == 2:
            output_file.write(month + "/" + day + "/" + year + "\n")

        if choice == 3:
            output_file.write(day + "-" + month + "-" + year + "\n")

        if choice == 4:
            output_file.write(day + "/" + month + "/" + year + "\n")




def reverse_geocoding(key):

    print("How many adresses do you need ?")
    number = int(input())
    print("Where do you want to generate addresses, type for example : 107 avenue Richardson Paul London")
    addy = input().split(' ')
    url_geocoding = 'https://maps.googleapis.com/maps/api/geocode/json?address='
    for i in range (0,len(addy)):
        url_geocoding = url_geocoding + addy[i] + '+'
    url_geocoding = url_geocoding[:-1] + ',+CA&key=' + API_KEY
    print(url_geocoding)
    response = requests.get(url_geocoding)
    data_geocoding = response.text
    data_geocoding = json.loads(data_geocoding)
    latitude = data_geocoding['results'][0]['geometry']['location']['lat']
    longitude = data_geocoding['results'][0]['geometry']['location']['lng']
    print("How far do you want the farest address ?")
    print("1km (1), 3km(3), 5km(5)")
    distance = int(input())
    print('Do you want a special postcode ?')
    print('Random (R) or type the postcode you want')
    postcode_answer = str(input())
    output_file = open("Generated\Random Adress.csv", 'w', newline='',encoding='utf-8')  # Dossier de sortie
    url_reverse_geocoding = "https://maps.googleapis.com/maps/api/geocode/json?latlng=" + str(latitude) + "," + str(longitude)+"&key="+key
    response = requests.get(url_reverse_geocoding)
    Data_test = response.text
    Data_test = json.loads(Data_test)
    list =[]
    i = 0
    unique_adress_list=[]

    #Load the list to know how many headers we have, and to use it after

    while i<10:
        try:
            list.append(str(Data_test["results"][0]['address_components'][i]['types']).replace(',',''))
            output_file.write(list[i] +',')
            i +=1
        except IndexError:
            break


    compteur = 0
    output_file.write('\n')
    lenlistsecond = len(list) -1

    while compteur < number:

        if distance == 1:
            randomlat = random.uniform(latitude - 0.0086, latitude + 0.0086)
            randomlong = random.uniform(longitude - 0.0086, longitude + 0.0086)
        if distance == 3:
            randomlat = random.uniform(latitude - 0.0258, latitude + 0.0258)
            randomlong = random.uniform(longitude - 0.0258, longitude + 0.0258)
        if distance == 5:
            randomlat = random.uniform(latitude - 0.043, latitude + 0.043)
            randomlong = random.uniform(longitude - 0.043, longitude + 0.043)

        url_reverse_geocoding = "https://maps.googleapis.com/maps/api/geocode/json?latlng=" + str(randomlat) + "," + str(randomlong) + "&key=" + key
        response = requests.get(url_reverse_geocoding)
        data = response.text
        data = json.loads(data)
        verifheaders = True
        street_adress_verif = False
        verif_unique = True

        #Unique addresses verification

        for i in range(0,len(unique_adress_list)):
            if unique_adress_list[i] == str(data["results"][0]['address_components'][0]['long_name'] + ' ' +
                                      data["results"][0]['address_components'][1]['long_name']):
                verif_unique = False
                break

        unique_adress_list.append(str(data["results"][0]['address_components'][0]['long_name'] + ' ' +
                                      data["results"][0]['address_components'][1]['long_name']))


        #Verification that Headers are the same for all responses, if not it skips the adress

        for i in range(0, len(list)):
            if str(Data_test["results"][0]['address_components'][i]['types']).replace(',', '') != str(data["results"][0]['address_components'][i]['types']).replace(',', ''):
                verifheaders = False
                break

        if str(data["results"][0]['types']) == "['street_address']":
            street_adress_verif = True

        #Start writing addresses

        if verifheaders and street_adress_verif and verif_unique:
            if postcode_answer == 'R' or postcode_answer == 'r':
                try:
                    for i in range(0,len(list)):
                        output_file.write(str(data['results'][0]['address_components'][i]['long_name']) + ',')

                    output_file.write(str(data["results"][0]['address_components'][0]['long_name'] +' ' +  data["results"][0]['address_components'][1]['long_name']))
                    compteur += 1
                    output_file.write("\n")
                    print('Adress ' + str(compteur) +' Done')
                    time.sleep(1)
                except IndexError:
                    print("Key error, make sure it's valid")
                    break

            else:
            #Only taking addresses with same postcode
                if postcode_answer in str(data["results"][0]['address_components'][lenlistsecond]['long_name']):
                    try:
                        for i in range(0, len(list)):
                            output_file.write(str(data['results'][0]['address_components'][i]['long_name']) + ',')
                        output_file.write((str(data["results"][0]['address_components'][0]['long_name']) +' ' + data["results"][0]['address_components'][1]['long_name']))
                        compteur += 1
                        output_file.write("\n")
                        print('Adress ' + str(compteur) + ' Done')
                        time.sleep(1)
                    except IndexError:
                        print("Key error, make sure it's valid")
                        break




#Main


print('Made by MVoltaj#6005 \n \n')
API_KEY = ''
print("Hi, What do you want to do ?")
print("Telephone number generator (1)")
print("Dob Generator(2)")
print("Getting addresses around you (3)")
print("First / Last Name Generator (4)")
print("Exit (5)")

choice = int(input())

if choice == 1:
    Telephone_number_generator()

if choice == 2:
    Dob_generator()

if choice == 3:
    reverse_geocoding(API_KEY)

if choice == 4:
    First_Last_Name()


