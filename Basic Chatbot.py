def response(user_input):      
        if(user in X):
            return "Hello!I am your basic Chatbot,How can I help you?"
        elif(user in Y):
            return "I am doing well,thanks!"
        elif("weather" in words):
            return "India's weather varies by region with temperature ranging from 22-25 degree celsius!!"
        elif("new" in words):
            return "There's nothing new to mention specifically"
        elif("help" in words):
            return "I can assist with answering questions,generating text,and providing information on a wide range of topics"
        elif("trip" in words):
            return "If you're planning to go for a trip there are historic places like Taj Mahal and Red Fort to vibrant cities like Mumbai and Goa, and serene hill stations like Shimla and Manali"
        elif(user in Z):
            return "Bye!Have a great day!"
        else:
            return "Sorry,I couldn't understand that..."        
        
while True:
    user=input("You:").lower()
    X=["hi","hey","hello"]
    Y=["how are you?","how r u?","are you okay?","how are you doing?"]
    words=[]
    words=user.split(" ")
    Z=["bi","bye","goodbye","take care","catch you later"]
    chatbot=response(user)
    print("Chatbot:",chatbot)
    if(user in Z):
        break
