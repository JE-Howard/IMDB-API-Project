#import sys
#!{sys.executable} -m pip install --upgrade pip 
#!{sys.executable} -m pip install omdb
import omdb
import pandas as pd
api_key = '10f7377d'
omdb.set_default('apikey', api_key)

class Movie:
    name = ""
    data = {}
    def __init__(self,movie):
        for x in movie: 
            if "Title" in x: 
                self.name = x[6:]
        for y in movie: 
            splitted = []
            splitted = y.split(";")
            if len(splitted) == 2:
                 self.data[splitted[0].strip()] = splitted[1].strip()

class Movie:
    name = ""
    data = {}
    def __init__(self,movie):
        for x in movie: 
            if "Title" in x: 
                self.name = x[6:]
        for y in movie: 
            splitted = []
            splitted = y.split(";")
            if len(splitted) == 2:
                 self.data[splitted[0].strip()] = splitted[1].strip()

def check_movie_existence(user_continue):
    count = 0
    history_list = []
    history_list.clear()

    try:
        history_textfile = open("Search History.txt", "r")
        for z in history_textfile:
            if ("Here is the History:" in z) or (len(z)<1):
                annoying = ""
            else:
                history_list.append(z.rstrip())
        history_textfile.close()


    except:
        print("History list could not be found")

        history_textfile = open("Search History.txt", "w")
        history_textfile.write("Here is the History:")
        history_textfile.close()

        history_textfile = open("Search History.txt", "r")
        for z in history_textfile:
            if ("Here is the History:" in z) or (len(z)<1):
                annoying = ""
            else:
                history_list.append(z.rstrip())

    if user_continue.lower() == "continue":
        try:
            title_chosen = str(input("Enter the title of the movie or series you would like to lookup:\n"))         
            option = int(input("Is this a movie or a series?:\n Please slect the numberthat corresponds with your choice.\n1.Movie\n2.Series\n"))

            if option == 1:
                
                search = omdb.search_movie(title_chosen)
                search = omdb.search_movie(title_chosen, timeout=5)
                if len(search)== 0: 
                    return "Not Found"
                count_2 = 0
                search_list = []
                print("Please select the correct number that corresponds with the name of the title you are looking for from the list below:")

                for p in search:
                    count_2 += 1
                    print(f"{count_2}." + p["title"])
                    search_list.append(str(p["title"]))

                final_choice = int(input(""))

                if final_choice - 1 > len(search_list):
                    print(
                        "You have enetred a value that does not correspond with any of the options given please retart the program and enter in a new option")

                else:
                    movie_or_series = str(search_list[final_choice - 1])
               

            elif option == 2:
                search = omdb.search_series(title_chosen)
                search = omdb.search_series(title_chosen, timeout=5)
                count_2 = 0
                search_list = []
                print("Please select the correct name of the title you are looking for from the list below:")

                for p in search:
                    count_2 += 1
                    print(f"{count_2}." + p["title"])
                    search_list.append(str(p["title"]))

                final_choice = int(input(""))

                if final_choice - 1 > len(search_list):
                    print(
                        "You have enetred a value that does not correspond with any of the options given please restart the program and enter in a new option")
                else:
                    movie_or_series = str(search_list[final_choice - 1])

            result = omdb.get(title=movie_or_series, fullplot=True, tomatoes=True)
            movie_or_series = movie_or_series.replace(":", "-")
            
            add_to = open("Search History.txt", "a")
            duplicate = ""
            for u in history_list:
                if movie_or_series == u:
                    print("The movie entreated has already been searched and will thus not be added to the recent "
                          "search list again")
                    duplicate = True
                else:
                    duplicate =False
            
            if duplicate == False: 
                history_list.append(movie_or_series)
                add_to.write(f"\n{movie_or_series.capitalize()}\n")
            add_to.close()
            
            try:
                history_file = open(movie_or_series + ".txt", "w")
                for p in result:
                    history_file.write(f"{p};{result[p]}\n")

                history_file.close()

           

                history_file = open(f"{movie_or_series.capitalize()}.txt", "r")

                return history_file
            except:
                print("This movie has already been searched for and will thus not have a textfile assigned to it ")

        except:

            print(
                f"We are so sorry to tell you that the title could not be found on our database."
                f"\nWould you mind please entering in a new title.")

            return "Not Found"

    elif user_continue.lower() == "history":

        print("Here are your previous searches:")

        for x in history_list:
            
            if ("Here is the History:" in x) or (len(x)<1):
                annoying =""
            
            else:
                count+=1
                print(f"{count}.{x}")

        choice = int(input(
            "Which previous search would you like to review ? Please enter the number that corresponds with your "
            "choice:\n"))
        if choice-1 > len(history_list):
            print(
                f"The previous search connected with {choice} could not be found. Please choose a valid option within "
                f"range")
        else:
            try:
                history_file = open(history_list[choice].rstrip() + ".txt", "r")

                return history_file

            except:
                print( "This file could not be open please contact your administrator")

def option_1 (result):
    
    opt1_dict = {
        "title" :"",
        "type": "",
        "year": "",
        "season": "",
        "episode": "",
        "plot": "",
        "genre":"",
        "actors":"",
       "director":"",
        "rated":"",
        "writer":""
                }
    
    for x in opt1_dict:
        for y in result:
            if x == y.lower():
                opt1_dict.update({x:result[y]})
            
    print("Here is the full overview of the movie you have searched for:")
    for z in opt1_dict:
        if not (opt1_dict[z]==""):
            print(f"\n{z.capitalize()}:{opt1_dict[z]}")
            
def option_2 (result):
    import webbrowser
    import urllib.request 
    import re
    import time
    from IPython.display import clear_output
    
    opt2_dict = {
                "title" :"",
                "runtime": "",
                "genre": "",
                "director": "",
                "writer": "",
                "plot": ""
                }
    
    for x in opt2_dict:
        for y in result:
            if x == y.lower():
                opt2_dict.update({x:result[y]})
            
    title_list=opt2_dict["title"].split()
    count = 0
    url_title = ""
    for new_title in title_list: 
        count+=1
        if len(title_list)==count: 
            url_title = url_title+new_title+"+"+"trailer"
        else:
            url_title = url_title+ new_title + '+'
    
                
    print("Here are the technical details for: "+search)
    for z in opt2_dict:
         print(f"\n{z.capitalize()}:{opt2_dict[z]}")
    

    html = urllib.request.urlopen('https://www.youtube.com/results?search_query='+ url_title)
    url_id= html.read().decode()

    url = re.findall(r"watch\?v=(\S{11})",url_id)
   
    permission = input("A new tab will be opened on your web browser.\nAre you sure you would like to view this trailer in a new tab? Yes or No\n")
    if permission.lower() == "yes" :
        count = 5
        
        while not (count == 0):
            clear_output(wait=True)
            print(f"The trailer will play in {count} seconds")
            time.sleep(1)
            count-=1
        webbrowser.open("https://www.youtube.com/watch?v="+url[0]) 

def option_3(result):
    import webbrowser
    import urllib.request 
    import re
    import time
    from IPython.display import clear_output
    
    opt3_dict ={
                 "poster":"",
                 "title":""
               }
 
    for x in opt3_dict:
        for y in result:
            if x == y.lower():
                opt3_dict.update({x:result[y]})
        
  
    name= opt3_dict["title"]
    url = opt3_dict["poster"]
    
   

    print(f"This is the poster for the title '{name}\nYou can download it via this link: "+url)
    permission = input("A new tab will be opened on your web browser.\nAre you sure you would like to view this poster in a new tab? Yes or No\n")
   
    if permission.lower() == "yes" :
        count = 5
        
        while not (count == 0):
            clear_output(wait=True)
            print(f"The  poster will show in {count} seconds")
            time.sleep(1)
            count-=1
        webbrowser.open(url) 
    
def option_4 (result):

    opt4_dict = {
        "imdb_votes":"", 
        "awards":""
            }

    for x in opt4_dict:
        for y in result:
            if x == y.lower():
                opt4_dict.update({x:result[y]})
                
    print("Here is the full overview of the movie you have searched for:")
    #for z in opt4_dict:
            #print(f"\n{z.capitalize()}:{opt4_dict[z]}")
    df4=pd.dataframe(opt4_dict)
            
    search = omdb.get(title=result["title"], fullplot=True, tomatoes=True)
    ratings_list=[]
    for w in search: # For loop through dictionary from txt  
        if w == "ratings": # Find ratings item 
            for i in search[w]:# For loop through the ratings item with the 'ratings' key [This is a list]
                for t in i:    # Forl loop through the dictionaries in the list  
                    if isinstance(i[t],int):
                        ratings_list.append(i[t])
                    else: 
                        ratings_list.append(i[t].capitalize())
    for m in range(0,len(ratings_list),2):
        print(f"\n{ratings_list[m]}:{ratings_list[m+1]}")

def option_6 (result):
    import time
    from IPython.display import clear_output
    movie_2 = str(input("Please enter in the title that you would like to compare:\n"))
    
    search = omdb.search_movie(movie_2)
    search = omdb.search_movie(movie_2, timeout=5)
    count_2 = 0
    search_list = []
    print("Please select the correct name of the title you are looking for from the list below:")

    for p in search:
        count_2 += 1
        print(f"{count_2}." + p["title"])
        search_list.append(str(p["title"]))

    final_choice = int(input(""))
    clear_output(wait=True)

    if final_choice - 1 > len(search_list):
        print("You have enetred a value that does not correspond with any of the options given please retart the program and enter in a new option")
    else:
        movie_2 = str(search_list[final_choice - 1])
     
    result_2 = omdb.get(title=movie_2, tomatoes=True)

    opt6_dict_1 = {
        "box_office":"",
        "awards":"",
        "imdb_votes":"",
        "metascore":""
            }
    
    opt6_dict_2 = {
        "box_office":"",
        "awards":"",
        "imdb_votes":"",
        "metascore":""
        
            }
    
    
    for x in opt6_dict_1:
        for y in result:
            if x == y.lower():
                opt6_dict_1.update({x:result[y]})
                
    for x in opt6_dict_2:
        for y in result_2:
            if x == y.lower():
                opt6_dict_2.update({x:result_2[y]})
                
    name_1 = result["title"] 
    
    
    print(f"\nHere is the full overview of the movie you have searched for your first title:{name_1}")
    for z in opt6_dict_1:
        print(f"\n{z.capitalize()}:{opt6_dict_1[z]}")
       
            
    print(f"\nHere is the full overview of the movie you have searched for your second title: {movie_2}")
    for z in opt6_dict_2:
            print(f"\n{z.capitalize()}:{opt6_dict_2[z]}")
import time
from IPython.display import clear_output

search="Error"
shutdown = "Go"
check ="Not Found"
while search == "Error":
    time.sleep(2)
    clear_output(wait=True)
    search = welcome_screen()
while check == "Not Found":
    clear_output(wait=True)
    check = check_movie_existence(search)
    switch = "On"
    if check == "Not Found":
        print("Please try entering a diffrent movie title, we could not find the title you entered on our database:")
    else: 
        film = Movie(check.readlines())
        title = film.name
        title_dict = film.data
        options = {"1.Full overview":option_1,"2.View ratings":option_4,"3.View and download poster":option_3,"4.View trailer":option_2, "5.Compare two titles":option_6}
        exit_opt = {"1. Return To Main Menu":"", "2.Exit":"off"}

        while not (switch == "off"):
           
            option_num=0
            clear_output(wait=True)
  
            print(f"Here are the options that we offer for the title: {title}:")
            for x in options:
                print(x)
            try:
                option_num = int (input("Which option would you like?:\n"))
                if option_num > len(options):
                    print("You have entered in a number that is out of range")
            except: 
                print("You have made an invaild entry. Please try again, remember to enter in a numeric value.")
      
   
            for y in options:
                if str(option_num) in y:
                    clear_output(wait=True)
                    options[y](title_dict)
            try:
                exit_options = int(input("would you like to:\n1.Return To Main Menu\n2.Exit\nPlease select the number that corresponds with the option you choose\n"))
                if exit_options > len(exit_opt):
                    print("You have entered in a number that is out of range")
            except: 
                print("You have made an invaild entry. Please try again, remember to enter in a numeric value.")
            
            for z in exit_opt:
                if exit_options == int(z[0]):
                    switch = exit_opt[z]
                    
    if switch == "off":
        clear_output(wait=True)
        print("Thank you for making use of our services.\nPlease click 'run' to restart the program")
        time.sleep(5)
        break   
        
      