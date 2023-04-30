# Portfolio: Chatbot
# Name:         Vincent Nguyen
# NetID:        VTN180000
# Course:       CS 4395.001
# Description:  This program utilizes OpenAI API. This program uses NER to find the name of the user if the user
#               had input it in. Also, this program web scrapes two websites (the origin of basketball and the origin
#               of ice hockey) so that the OpenAI can use it if the user ask about the origin of the two sports

from urllib import request
from bs4 import BeautifulSoup as soup
import re
import openai
import spacy
import gradio
import pickle
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

# API key
openai.api_key = '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'

# Function to read in the file
def file_in(filename):
    # Open file and read in lines
    with open(filename, mode='r') as lines:
        line = lines.read().splitlines()
    # Close file
    lines.close()

    return line


# Read in user model from txt file
def read_user_model():
    # Open txt file and read in contents
    with open('user_model.txt', mode='r') as profile:
        line = profile.read().splitlines()

    # Close file
    profile.close()

    return line


# Function to write in to user_model txt file
def write_user_model(name, user_profile):
    verify = 0

    # Open txt file and read in contents
    with open('user_model.txt', mode='a') as profile:
        # Look if user has a profile in the txt file
        for line in user_profile:
            if line == name:
                verify += 1

        # If the user does not have a profile in txt file, create profile for user
        if verify != 1:
            profile.write('\n\n' + name + "\nLikes:\nDislikes\nPersonal Information:\n")


# Function to change user model information
def change_user_model(name, user_profile, option):
    verify = 0

    # Search for user's name in file
    for line in user_profile:
        print(line)
        if line == name:
            verify += 1

        # Search for the user's likes and append information to the line
        if option == 'like' and line.find("Like: ") and verify == 1:
            verify += 1
            #


# Function to web scrape links
def web_scrape(link, filename):
    # Open file to write to file
    with open(filename, 'w') as file:
        # Decode website
        open_web = request.urlopen(link).read()
        call_soups = soup(open_web, "html.parser")

        for script_style in call_soups(["script", "style"]):
            # Ignore script and style
            script_style.extract()

        # Get contents from website
        website_lines = call_soups.get_text()

        # Get contents and clean it up
        clean = [lines for lines in website_lines.splitlines() if not re.match(r'\s*^$', lines)]
        for counter, texts in enumerate(clean):

            # Tokenize contents
            text_token = sent_tokenize(texts)

            for token_lines in text_token:
                # Write the document contents to file
                file.write(token_lines + " ")
    file.close()


# Function to get term frequency
def term_freq(filename):
    tf_dictionary = {}

    with open(filename, mode='r') as file:
        content = file.read().splitlines()

        # Tokenize the lines from the file
        for line in content:
            tokenizes = word_tokenize(line)

            # Remove stopwords and lower case letters so the term frequency can count right
            tokenizes_content = [tokens_line for tokens_line in tokenizes if tokens_line not in \
                                 stopwords.words('english') and tokens_line.lower()]

            # Get term frequency to dictionary
            for tokens in tokenizes_content:
                if tokens in tf_dictionary:
                    tf_dictionary[tokens] += 1
                elif tokens not in tf_dictionary:
                    tf_dictionary[tokens] = 1

            print(tf_dictionary)


# Chatbot chatting function
def chatting(input_query_user):
    link_one = 'https://springfield.edu/where-basketball-was-invented-the-birthplace-of-basketball'
    link_two = 'https://www.history.com/news/who-invented-hockey-origins-canada'
    name_one = 'file_one.txt'
    name_two = 'file_two.txt'
    system = [{"role": "system", "content": "You are an AI, ready to help the user with anything."}]
    bot_model = "gpt-3.5-turbo"

    # Load in spacy
    nlp_spacy = spacy.load('en_core_web_sm')

    # Call function to web scrape two websites
    web_scrape(link_two, name_two)
    web_scrape(link_one, name_one)

    # Call NER to input
    input_ner = nlp_spacy(input_query_user)

    # Find person name in input after calling NER
    for ner in input_ner.ents:

        # If the user says their name in the input, create new user profile in user model txt file
        if ner.label_ == 'PERSON':
            name = ner.text
            user = read_user_model()
            write_user_model(name, user)

    # Check if the user had query about ice hockey and its origin
    if input_query_user.find('ice hockey') != -1 and input_query_user.find('origin') != -1:

        # Read in file contents in file_two (file_two about origins of ice hockey)
        file_two = file_in('file_two.txt')
        two = ''.join(file_two)
        term_freq('file_two.txt')

        # Append the document to the user input and call OpenAI to read the document and the user's query
        system.append({"role": "user", "content": two + input_query_user})
        bot = openai.ChatCompletion.create(messages=system, model=bot_model)
        bot_reply = bot.choices[0].message.content
        system.append({"role": "assistant", "content": bot_reply})
        return bot_reply

    # Check if the user had query about basketball and its origin
    elif input_query_user.find('basketball') != -1 and input_query_user.find('origin') != -1:
        # Read in file contents in file_one (file_two about origins of basketball)
        file_one = file_in('file_one.txt')
        one = ''.join(file_one)
        term_freq('file_one.txt')

        # Append the document to the user input and call OpenAI to read the document and the user's query
        system.append({"role": "user", "content": one + input_query_user})
        bot = openai.ChatCompletion.create(messages=system, model=bot_model)
        bot_reply = bot.choices[0].message.content
        system.append({"role": "assistant", "content": bot_reply})
        return bot_reply

    # If the user query is not about basktball or ice hockey, don't append any document to user query and call OpenAI
    else:
        # Don't append any document to user query and call OpenAI
        system.append({"role": "user", "content": input_query_user})
        bot = openai.ChatCompletion.create(messages=system, model=bot_model)
        bot_reply = bot.choices[0].message.content
        system.append({"role": "assistant", "content": bot_reply})
        return bot_reply

# Labels are created in mockup
chatbot_inputs = gradio.inputs.Textbox(label="Here is where you will put your inputs to chat with OpenAI")
chatbot_outputs = gradio.outputs.Textbox(label="Here is where the chatbot will reply")

# Launch mockup
test = gradio.Interface(fn=chatting, outputs=chatbot_outputs, inputs=chatbot_inputs, title="Chatbot Assignment")
test.launch()

