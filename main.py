import random
def chatbot():
  print ("Hello, I'm chatbot. what is your name?")
  name = input()
  print(f"Nice to meet you, {name}! What can I help you with today? you can type \"bye\" to leave me :(?")

  while True:
    message = input ()
    answers = ["Can you repeat that again", "You could be right.", "I hear you.", "I can see where you are coming from.", "Ah-ha.", "That could be.", "I don't know; what do you think?"]  # could add more answers. here to be personlized 
    if message == "bye":
      print("Goodbye! Have a great day.")
      break
    elif message == "what are your store hours":
      print("From 9-5")
    elif message == "are you open today?":
      print("Yes")
    elif message == "Is this the right time to buy?":
      print("Yes we have the cheapest price!!")
    else:
      response = random.choice(answers)
      print(response)
      
      
chatbot()
  