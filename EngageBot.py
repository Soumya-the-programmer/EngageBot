from customtkinter import *
from tkinter import *
from tkinter import messagebox as tmsg
import webbrowser
from datetime import *
import datetime
import time
from huggingface_hub import InferenceClient
import json
import requests

# main window
root=CTk() # CTk() class instance
root.title("EngageBot") # title
root.iconbitmap(r"C:\Users\user\Downloads\EngageBot.ico") # icon
root.geometry("1200x980")  # geometry size fixing
root.maxsize(1200,980) # max size fixing
root.minsize(1200,980) # min size fixing
root.configure(fg_color="grey11") # background setting

# function for removing place holder text 
def s_bar_focus_in(event):
    place_hold="Enter Your Message..." # storing the placeholder text to match
    # checking if the text matches with placeholder text or not
    if search_bar.get(1.0,END).strip()==place_hold:
        search_bar.delete(1.0,END) # deleting the placeholder text when clicking
        
# function for inserting place holder text         
def s_bar_focus_out(event):
    # checking if the search bar is empty or not
    if not search_bar.get(1.0,END).strip():
        search_bar.insert(1.0,"Enter Your Message...") # inserting the placeholder text
        
def user_message_send(event=None):
    if search_bar.get(1.0,END).strip()=="Enter Your Message...":
        return None
    else:
        # getting the user message and strip() to remove leading and trailing spaces 
        user_text=search_bar.get(1.0,END).strip() 
    
    # checking if there any text exists or not
    if user_text:
        # storing the place holder
        chat_screen_placehold="\n\n\n\n\n\n\n\n\n\n\n\t              How can I help you today?"
        chat_screen_text=chat_screen.get(1.0,END).strip() # getting chat screen input
        
        # comparing the placeholder with text
        if chat_screen_text==chat_screen_placehold.strip():
            chat_screen.configure(state="normal") # setting the state normal
            chat_screen.delete(1.0,END) # deleting the place holder
            chat_screen.configure(state="disabled") # setting the state disabled
            
        chat_screen.configure(state="normal") # configuring the chatbox to normal
        chat_screen.insert(END,f"You: {user_text}\n\n") # inserting the text
        chat_screen.configure(state="disabled") # disabled the chatbox
        search_bar.delete(1.0,END) # deleting the search box entry
        # ai generated text
        def ai():
            sites_dict={"youtube":"https://www.youtube.com",
                      "google":"https://www.google.com",
                      "facebook": "https://www.facebook.com",
                      "instagram": "https://www.instagram.com",
                      "twitter": "https://www.twitter.com",
                      "whatsapp": "https://www.whatsapp.com",
                      "x":"https://www.x.com",
                      "linkedin": "https://www.linkedin.com",
                      "spotify": "https://www.spotify.com",
                      "github": "https://www.github.com",                     
                      "chatgpt": "https://www.chatgpt.com",
                      "gemini": "https://gemini.google.com",
                      "reddit": "https://www.reddit.com",
                      "pinterest": "https://www.pinterest.com",
                      "tiktok": "https://www.tiktok.com",
                      "slack": "https://slack.com",
                      "dropbox": "https://www.dropbox.com",
                      "zoom": "https://zoom.us",
                      "amazon": "https://www.amazon.com",
                      "flipkart": "https://www.flipkart.com",
                      "netflix": "https://www.netflix.com",
                      "wikipedia": "https://www.wikipedia.org",
                      "apple": "https://www.apple.com",
                      "microsoft": "https://www.microsoft.com",
                     }
            # application dictionary
            apps_dict={"excel" : r"C:\Users\user\Desktop\Excel.lnk",
                       "ms excel" : r"C:\Users\user\Desktop\Excel.lnk",
                       "word" : r"C:\Users\user\Desktop\Word.lnk",
                       "ms word" : r"C:\Users\user\Desktop\Word.lnk",
                       "powerpoint" : r"C:\Users\user\Desktop\PowerPoint.lnk",
                       "ms powerpoint" : r"C:\Users\user\Desktop\PowerPoint.lnk",
                       "power bi" : r"C:\Users\user\Desktop\Power BI Desktop - Shortcut.lnk",
                       "vs code" : r"C:\Users\user\Desktop\Visual Studio Code.lnk",
                       "visual studio code" : r"C:\Users\user\Desktop\Visual Studio Code.lnk",
                       "paint" : r"C:\Users\user\Desktop\Paint.lnk",
                       "ms paint" : r"C:\Users\user\Desktop\Paint.lnk",
                       "notepad" : r"C:\Users\user\Desktop\Notepad.lnk",
                       "drive": r"C:\Users\user\Desktop\Google Drive.lnk",
                       "photoshop":r"C:\Users\user\Desktop\Adobe Photoshop 7.0.lnk",
                       "adobe photoshop":r"C:\Users\user\Desktop\Adobe Photoshop 7.0.lnk",
                       "calculator":r"C:\Users\user\Desktop\Calculator.lnk",
                       "translator":r"C:\Users\user\Desktop\Ultimate Translator Hub.lnk"
                       }       
            
            # checking if any open statement in the user text or not
            if "open" in user_text.lower():
                # searching the website in the dictionary
                for site in sites_dict:
                    # checking if available or not
                    if f"open {site}".lower() in user_text.lower():
                        time.sleep(0.5) # sleep the time
                        chat_screen.configure(state="normal") # configuring the chatbox to normal
                        chat_screen.insert(END,f"  EngageBot: Opening {site} sir...\n\n") # inserting the text
                        chat_screen.configure(state="disabled") # disabled the chatbox
                        search_bar.delete(1.0,END) # deleting the search box entry
                        webbrowser.open(f"{sites_dict[f"{site}"]}") # opening the window 
                # searching the app in the dictionary
                for app in apps_dict: 
                    # checking if available or not
                    if f"open {app}".lower() in user_text.lower():
                        time.sleep(0.5) # sleep the time
                        chat_screen.configure(state="normal") # configuring the chatbox to normal
                        chat_screen.insert(END,f"  EngageBot: Opening {app} sir...\n\n") # inserting the text
                        chat_screen.configure(state="disabled") # disabled the chatbox
                        search_bar.delete(1.0,END) # deleting the search box entry
                        webbrowser.open(f"{apps_dict[f"{app}"]}") # opening the window 
                
            elif "the time" in user_text.lower()\
                or "the time?" in user_text.lower():               
                date=datetime.datetime.now() # getting the time
                time.sleep(0.5) # sleeping the time
                chat_screen.configure(state="normal") # configuring the chatbox to normal
                # inserting the time    
                chat_screen.insert(END,f"  EngageBot: Sir, the time is: {date.strftime("%H:%M:%S")}\n\n")
                chat_screen.configure(state="disabled") # disabled the chatbox
            
            elif "the date" in user_text.lower() or "the date?" in user_text.lower():
                date=datetime.datetime.now() # getting the date
                time.sleep(0.5) # sleeping the time
                chat_screen.configure(state="normal") # configuring the chatbox to normal
                # inserting the date    
                chat_screen.insert(END,f"  EngageBot: Sir, the date is: {date.strftime("%D")}\n\n")
                chat_screen.configure(state="disabled") # disabled the chatbox
            
            elif "who are you".lower() in user_text.lower() or "who are you?".lower() in user_text.lower():
                time.sleep(0.5) # sleep the time
                chat_screen.configure(state="normal") # configuring the chatbox to normal
                # inserting the info   
                chat_screen.insert(END,"  EngageBot: I’m EngageBot, an AI chatbot model created by Soumyajeet Das. I’m here to help withinformation, answer questions, or to open an application or site. How can I assist you today?\n\n")
                chat_screen.configure(state="disabled") # disabled the chatbox
            
            elif "how are you".lower() in user_text.lower()\
                or "how are you?".lower() in user_text.lower():
                time.sleep(0.5) # sleep the time
                chat_screen.configure(state="normal") # configuring the chatbox to normal
                # inserting the info   
                chat_screen.insert(END,"  EngageBot: I’m doing well, thanks for asking! How about you?\n\n")
                chat_screen.configure(state="disabled") # disabled the chatbox
                
            elif "who created you".lower() in user_text.lower()\
                or "who developed you".lower() in user_text.lower()\
                or "who built you".lower() in user_text.lower()\
                or "who made you".lower() in user_text.lower()\
                or "who build you".lower() in user_text.lower()\
                or "who creates you".lower() in user_text.lower()\
                or "who create you".lower() in user_text.lower():
                time.sleep(0.5) # sleep the time
                chat_screen.configure(state="normal") # configuring the chatbox to normal
                # inserting the info   
                chat_screen.insert(END,"  EngageBot: I was created by Soumyajeet Das, on 26/08/2024.\n\n")
                chat_screen.configure(state="disabled") # disabled the chatbox
            
            elif "i'm fine".lower() in user_text.lower()\
                 or "i am fine".lower() in user_text.lower()\
                 or "i'm well".lower() in user_text.lower()\
                 or "i am well".lower() in user_text.lower()\
                 or "i'm good".lower() in user_text.lower()\
                 or "i am good".lower() in user_text.lower():
                time.sleep(0.5) # sleep the time
                chat_screen.configure(state="normal") # configuring the chatbox to normal
                # inserting the info   
                chat_screen.insert(END,"  EngageBot: Glad to hear it! How can I help you?.\n\n")
                chat_screen.configure(state="disabled") # disabled the chatbox
                
            elif "your birthday" in user_text.lower()\
                or "your birthday?" in user_text.lower()\
                or "birthday" in user_text.lower()\
                or "birthday?" in user_text.lower():
                time.sleep(0.5) # sleep the time
                chat_screen.configure(state="normal") # configuring the chatbox to normal
                # inserting the info   
                chat_screen.insert(END,"  EngageBot: I don't have a birthday, I was created on 26/08/2024\n\n")
                chat_screen.configure(state="disabled") # disabled the chatbox
                
            elif "your name".lower() in user_text.lower()\
                or "your name?".lower() in user_text.lower():
                time.sleep(0.5) # sleep the time
                chat_screen.configure(state="normal") # configuring the chatbox to normal
                # inserting the info   
                chat_screen.insert(END,"  EngageBot: I’m EngageBot, an AI chatbot who is created by Soumyajeet Das.\n\n")
                chat_screen.configure(state="disabled") # disabled the chatbox
            
            elif "clear chat".lower() in user_text.lower() or\
                 "clear".lower() in user_text.lower() or\
                 "delete chat".lower() in user_text.lower() or\
                 "delete".lower() in user_text.lower() :
                time.sleep(0.5) # sleep the timme
                chat_screen.configure(state="normal") # configuring the chatbox to normal
                chat_screen.delete(1.0,END) # deleting the chat
                chat_screen.insert(END,"  EngageBot: Chat cleared sir..\n\n") # inserting the message
                chat_screen.configure(state="disabled") # disabled the chatbox
                
            elif "close".lower() in user_text.lower() or\
                 "exit".lower() in user_text.lower() :
                time.sleep(0.5) # sleep the timme
                root.destroy() # closing the window
            
            elif "weather".lower() in user_text.lower():
                # Extract the city name from the user input
                parts = user_text.lower().split(" ")
                if "in" in parts:
                    city_index = parts.index("in") + 1
                    if city_index < len(parts):
                        city_name = parts[city_index]
                    else:
                        city_name = "Haldia"  # Default city if none specified
                else:
                    city_name = "Haldia"  # Default city
                    
                url = "https://weatherapi-com.p.rapidapi.com/forecast.json" # url of weatherapi.com 

                querystring = {"q":city_name,"days":"3"} # sending the city name to api

                headers = {
                    "x-rapidapi-key": "ENTER_YOUR_WEATHER_API_KEY", #   REPLACE IT WITH YOUR API KEY
                    "x-rapidapi-host": "weatherapi-com.p.rapidapi.com" # rapidapi website
                } 

                response = requests.get(url, headers=headers, params=querystring) # getting response

                # Load the response JSON into a Python dictionary
                data = response.json()

                time.sleep(0.5) # sleeping the time
                # changing the state to normal
                chat_screen.configure(state="normal")
                # inserting the content
                chat_screen.insert(END,f'''  EngageBot:\n
                Location:\n  
                Name: {data["location"]['name']},
                Region: {data['location']['region']},
                Country: {data['location']['country']},
                Latitude: {data['location']['lat']},
                Longitude: {data['location']['lon']},
                Local time: {data['location']['localtime']}
                \nCurrent Weather:\n
                Temparature: {data["current"]['temp_c']}°c / {data["current"]['temp_f']}°f,
                Feels like: {data["current"]['feelslike_c']}°c / {data["current"]['feelslike_f']}°f,
                Condition: {data["current"]['condition']["text"]},
                Wind: {data["current"]['wind_kph']} kph / {data["current"]['wind_mph']} mph
                Humidity: {data["current"]['humidity']}
                Cloud: {data["current"]['cloud']}		  
                \nWeather Forecast:\n
                High Temparature: {data["forecast"]["forecastday"][2]["day"]['maxtemp_c']}°c / {data["forecast"]["forecastday"][2]["day"]['maxtemp_f']}°f,
                Low Temparature: {data["forecast"]["forecastday"][2]["day"]['mintemp_c']}°c / {data["forecast"]["forecastday"][2]["day"]['mintemp_f']}°f,
                Average Temparature: {data["forecast"]["forecastday"][2]["day"]['avgtemp_c']}°c / {data["forecast"]["forecastday"][2]["day"]['avgtemp_f']}°f,
                Max Wind: {data["forecast"]["forecastday"][2]["day"]['maxwind_kph']} kph / {data["forecast"]["forecastday"][2]["day"]['maxwind_mph']} mph,
                Rain Probability: {data["forecast"]["forecastday"][2]["day"]['daily_chance_of_rain']}%,
                Snow Probability: {data["forecast"]["forecastday"][2]["day"]['daily_chance_of_snow']}%,
                Future Condition: {data["forecast"]["forecastday"][2]["day"]['condition']["text"]} expected\n\n''')
                
                # changing the state to disablel
                chat_screen.configure(state="disabled")
                
            elif "news".lower() in user_text.lower():
                # Get the current date and the previous day
                current_date = datetime.datetime.now().strftime('%Y-%m-%d')
                previous_date = (datetime.datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

                # Check if there are words before "news" to determine the topic
                news_index = user_text.lower().find("news")
                if news_index != -1:
                    new_str = user_text[:news_index].strip()  # Extracting the words before "news"
                    words = new_str.split(" ")
                    # Checking if words are available before "news"
                    if len(words) > 0:
                        word_before_news = words[-1]
                    else:
                        word_before_news = "All"
                else:
                    word_before_news = "All"

                
                # Construct the URL with a broader date range
                if word_before_news == "All":
                    topic_query = 'All'  # Empty query for all topics
                else:
                    topic_query = f'q={word_before_news}' # setting the query

                # url
                url = f"https://newsapi.org/v2/everything?{topic_query}&from={previous_date}&to={current_date}&sortBy=popularity&apiKey={ENTER_YOUR_API_KEY_HERE}" # REPLACE IT WITH YOUR NEWS API KEY

                # Fetch the data from the NEWS API
                try:
                    getrq = requests.get(url=url)
                    getrq.raise_for_status()  # Raise an HTTPError for bad responses
                    news_api_dic = getrq.json()  # Convert the response to a dictionary

                    # Check if the response contains articles
                    if 'articles' in news_api_dic:
                        articles = news_api_dic['articles']
                        chat_screen.configure(state="normal") # changed the state to normal
                        # inserting total number
                        chat_screen.insert(END,f"  EngageBot: Total number of articles: {len(articles)}\n\n")
                        chat_screen.configure(state="disabled") # disabling the state
                        
                        # checking if articles are there or not
                        if articles:
                            i=1 # count
                            # inserting the articles
                            for article in articles:
                                chat_screen.configure(state="normal") # changed the state to normal
                                # inserting news
                                chat_screen.insert(END,f'''    News {i} from {article['author']}
                                                           \n    Title: {article['title']}
                                                           \n    Description: 
                                                           \n    {article['description']}\n\n
---------------------------------------------------------------------------------------\n\n''')
                                chat_screen.configure(state="disabled") # disabling the state
                                i+=1 # count +=1
                        else:
                            time.sleep(0.5) # sleeping the time
                            chat_screen.configure(state="normal") # changed the state to normal
                            chat_screen.insert(END,"  EngageBot: Sorry! sir, No articles found for this topic.\n\n")
                            chat_screen.configure(state="disabled") # disabling the state
                    else:
                        time.sleep(0.5) # sleeping the time
                        chat_screen.configure(state="normal") # changed the state to normal
                        chat_screen.insert(END,"  EngageBot: Sorry! sir, No articles key found.\n\n")
                        chat_screen.configure(state="disabled") # disabling the state
                except Exception:
                    time.sleep(0.5) # sleeping the time
                    chat_screen.configure(state="normal") # changed the state to normal
                    chat_screen.insert(END,"  EngageBot: Sir, please mention a topic of the news (eg. sports news, etc.)\n\n")
                    chat_screen.configure(state="disabled") # disabling the state
            
            else:            
                # Initialize the InferenceClient
                hf_token = 'ENTER_YOUR_HUGGING_FACE_TOKEN'  # Replace with your Hugging Face token
                repo_id = 'EleutherAI/gpt-neo-2.7B'  # Replace with your model ID

                client = InferenceClient(model=repo_id, token=hf_token, timeout=120)

                def call_llm(inference_client: InferenceClient, prompt: str):
                    try:
                        response = inference_client.post(
                            json={
                                "inputs": prompt,
                                "parameters": {
                                    "max_new_tokens": 400,
                                    "temperature": 0.7,
                                    "top_p": 0.9
                                },
                                "task": "text-generation",
                            },
                        )
                        decoded_response = response.decode()
                        
                        response_json = json.loads(decoded_response)
                        if isinstance(response_json, list) and len(response_json) > 0:
                            return response_json[0].get("generated_text", "").strip()
                        return " EngageBot: Sorry! sir, I can't answer that.\n\n"
                    except Exception :
                        return "  EngageBot: Sorry! sir, I can't answer that.\n\n"

                # Example usage
                prompt = f"{user_text.capitalize()}" # prompt
                response_text = call_llm(client, prompt) # sending the prompt
                chat_screen.configure(state="normal") # select the state to normal
                chat_screen.insert(END,f"  EngageBot: {response_text}\n\n") # inserting the response
                chat_screen.configure(state="disabled") # select the state to disable
                
        ai() # calling ai() function

#About us menu
def ABOUT():  
    # if clicked on about us then this message will be displayed
    tmsg.showinfo("About Us", 
                  "Welcome to EngageBot!\n\n"
                  "EngageBot is an advanced AI chatbot designed and developed by Soumyajeet Das. "
                  "Built using Python's CustomTkinter module, EngageBot serves as an intelligent virtual assistant "
                  "capable of answering questions, providing information, and assisting with various tasks such as "
                  "opening websites or applications. \n\n"
                  "Our goal with EngageBot is to create a seamless and interactive user experience that makes it easier "
                  "for you to find information and complete tasks efficiently.\n\n"
                  "Thank you for using EngageBot! If you have any questions or feedback, feel free to reach out.\n\n"
                  "Date of Creation: 26/08/2024")

about_menu=Menu(root) # about menu
about_menu.add_cascade(label="   Help   ",command=ABOUT)
root.configure(menu=about_menu)#configuring help Menu

# frame 1
frame1=CTkFrame(root, fg_color="grey11",border_color="grey11")
frame1.pack(fill=BOTH)

# show label
show0=CTkLabel(frame1,text="",fg_color="grey11")
show0.pack()

# heading
heading=CTkLabel(frame1, 
                    text="EngageBot",
                    fg_color="grey11",
                    text_color="lightblue",  
                    font=("Montserrat", 60, "bold"),
                    corner_radius=20,
                    padx=20,
                    pady=15
                )
heading.pack()
# show label
show1=CTkLabel(frame1,text="",fg_color="grey11")
show1.pack()

# frame 2
frame2=CTkFrame(root, fg_color="grey11",border_color="grey11")
frame2.pack(fill=BOTH)

# text screen for chat
chat_screen=CTkTextbox(frame2,
                        height=650,
                        width=900,
                        text_color="white",
                        fg_color="grey11",
                        font=("poppins",22),
                        border_color="grey11"
                      )
chat_screen.pack()
# configuring the font size for placeholder in chat_screen
chat_screen.configure(font=("poppins",30,"bold"))
# placeholder text
chat_screen.insert(1.0,"\n\n\n\n\n\n\n\n\n\n\n\t              How can I help you today?")
chat_screen.configure(state="disabled")  
# show label
show2=CTkLabel(frame2,text="",fg_color="grey11")
show2.pack()

# frame 3
frame3=CTkFrame(root, fg_color="grey11")
frame3.pack(fill=BOTH)

# show label
show3=CTkLabel(frame3,text="\t\t               ",fg_color="grey11")
show3.grid(row=1,column=1)

# search bar
search_bar=CTkTextbox(frame3,
                      height=28,
                      width=750,
                      fg_color="white",
                      text_color="black",
                      font=("poppins",22),
                      corner_radius=20,
                      border_spacing=0
                     )
search_bar.grid(row=1,column=2)
# place holder text
search_bar.insert(1.0,"Enter Your Message...")#  # inserting placeholder text
search_bar.bind("<FocusIn>",s_bar_focus_in) # for focus in
search_bar.bind("<FocusOut>",s_bar_focus_out) # for focus out
search_bar.bind("<Return>",user_message_send) # for pressing enter key in keyboard

# show label
show3=CTkLabel(frame3,text="     ",fg_color="grey11")
show3.grid(row=1,column=4)
# submit button
submit=CTkButton(frame3,
                 text="Send",
                 width=10,
                 height=70,
                 fg_color="seagreen1",
                 text_color="black",
                 font=("Roboto",24,"bold"),
                 corner_radius=30,
                 command=user_message_send
                )
submit.grid(row=1,column=5)

root.mainloop() # mainloop() method to execute and show the window