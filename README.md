# Raffle-Bot-Tools-for-Botting

Made by MVoltaj#6005

Random Information Generator

Hi, i made this little tool to help people entering in raffles where you need random info.
All csv’s will be generated in the folder Generated.


Telephone number Generator

What’s the country code of your country ?

Write things that will stay fix for all telephone numbers.
Example : +33 for France or +44 for the United Kingdom.

If you want to generate national numbers like 0645984563 in France, just enter 06.

In some country like Uk, number are generated like this :
One of those provider prefix is for example : 7781 
In this case, you need to put as ‘country code’ +447781 
Make sure to check what needs to stay fixed when you want to generate some telephone number from a specific country, or you will be filtered from raffles like Naked. 
Thanks Aj#0069 for help.

How many numbers in total should the telephone number have ?

When you enter this, make sure to count character into the country code(including the ‘+’)
Example : +447700900077. Enter 13






Dob Generator:

No really hard things here, just follow instruction. Also, as mentioned, all date of birth are above 18 years old.

Getting address around you:

Setup :

First, get an API Google key, following this : 
https://developers.google.com/maps/documentation/embed/get-api-key
You must accept billing. Don’t worry, it’s free.
200$ is 40k requests, so don’t abuse too much of the bot.
Then, click on library

Search Geocoding API, click on it, then on enable. (That’s why you guys had trouble with key, thanks Xuan Kickz#5693 who found out this).
Then go in Credentials, and if you set up all right, it show this:

Insert your API Key at the end of the file



After that, you will need to find the coordinates of the place you want address around.
Go to Google Maps
Click on the map where you want to generate addresses around.

     -	Then click on the coordinates

Don’t put coordinates with a letter, it will make the bot crash.
First coordinate is the latitude and the second one is the longitude.

Enter the latitude, then the longitude into the bot

Farest Adress
Bot will take addresses in a square around your house.

Enter 1, 3 or 5 depending if you want far addresses from the coordinates you choose or not.

Do you want a special postcode ?

If you want all your addresses to be in only one postcode, enter the postcode you want. Else, just enter R for random.
Bot also handle ‘including. 
Example : you input ‘SW1’, bot will generate adress with postcode ‘SW1 AZE’, ‘SW1 JKL’, etc…

All your addresses should be generated into random addresses.csv in the Datafile Folder

Error: 
Don’t panic or say that the bot doesn't work if you choose a special postcode to generate an address. I tested it a bit for Uk, and because of one postcode = one road, it will take a while to generate. Approximately about 1 address of 25 requests is with the same postcode.
Sometimes, Google Api reverses postcode and another column on one line, to sort bad formatted addresses, just double click on a header. 
Don’t dm me about bot ‘not generating’ addresses when you try random coordinates, for sure it won't generate if there are no houses around the coordinates. Also, don’t mix latitude and longitude, if you invert it, bot will not generate addresses or generate addresses far away for your coordinates.
if you still have errors, enter this into google, and replace ‘YOUR_API_KEY’by your real API Key, google’s response should answer you what’s wrong.

https://maps.googleapis.com/maps/api/geocode/json?latlng=40.714224,-73.961452&key=YOUR_API_KEY
If the bot is stucked after putting postcode or ‘R’, make sure your coordinates are right please.




First / Last Name Generator

Just follow instructions as given.
File will be generated in First_Last_Name List.csv in the Generated folder.








