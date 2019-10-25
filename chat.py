from chatterbot import ChatBot
bot = ChatBot('My_assistant')  #changing in chatbot name


def main():
	while True:
		msg = input('sir: ') #changing in the msg input 
		if msg.strip() != 'gudbye':
			final = my_assistant.get_response(msg)   #changing the result variable to final and reply variable to response                      
			response = str(final)
			print(response)
		if msg.strip() == 'Bye':
			print('gudbye')  #changing the bye to gudbye
			break

if __name__ == '__main__':
	main()
