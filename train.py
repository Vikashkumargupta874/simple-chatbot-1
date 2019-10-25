from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

def train(my_assistant):
	path = 'data\\english\\'
	for file in os.listdir(path):
		data = open(path + file, 'r').readlines()
		my_assistant.train(data)

def main():
	my_assistant = ChatBot('My_assistant')
	my_assistant.set_trainer(ListTrainer)
	train(my_assistant)


if __name__ == '__main__':
	main()

