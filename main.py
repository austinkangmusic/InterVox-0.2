#IMPORTANT PARAMETER!!!
active_listening = True
simulated_input = False
reset_memories = False
use_default_model = False
import os
import threading

# Path to the folder containing models
model_directory = "XTTS-v2_models"



def reset_memory():
    with open("statuses/speak_status.txt", "w") as file:
        file.write('false')  

    with open("statuses/playback_active.txt", "w") as file:
        file.write('false')   

    with open("transcription/input.txt", "w") as file:
        file.write('')

    with open("donottouch/user_input.txt", "w") as file:
        file.write('')


    with open("donottouch/halved_user_content.txt", "w") as file:
        file.write('')

    with open("donottouch/chatbot_response.txt", "w") as file:
        file.write('')

    with open("donottouch/chatbot_listening.txt", "w") as file:
        file.write('')      

    with open("conversation_history.txt", "w") as file:
        file.write('')      

    print('Memory has been resetted.')

if reset_memories:
    reset_memory()
















# Function to detect available models in the folder
def get_available_models():
    try:
        # List all directories in the model directory and filter by the pattern 'XTTS-v2_'
        available_models = [d.replace('XTTS-v2_', '') for d in os.listdir(model_directory) 
                            if os.path.isdir(os.path.join(model_directory, d)) and d.startswith('XTTS-v2_')]
        return available_models
    except FileNotFoundError:
        print("Error: Model directory not found.")
        exit(1)

# Function to ask the user for the model
def ask_for_model():
    available_models = get_available_models()

    if not available_models:
        print("No models found in the directory.")
        exit(1)

    print("Please select a XTTS model from the following list:")
    for i, model in enumerate(available_models, 1):
        print(f"{i}. {model}")

    while True:
        try:
            choice = int(input("Enter the number of the model you want to use: "))
            if 1 <= choice <= len(available_models):
                selected_model = available_models[choice - 1]
                print(f"You selected: {selected_model}")
                return selected_model
            else:
                print("Invalid choice. Please choose a valid model number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to save the model name to a file
def save_model_to_file(model_name):
    # Create the directory if it doesn't exist
    os.makedirs("statuses", exist_ok=True)

    # Save the selected model to statuses/whisper_model_name.txt
    file_path = "statuses/speaker_name.txt"
    with open(file_path, "w") as file:
        file.write(model_name)
        
# Get the selected model and save it
if not use_default_model:
    speaker_name = ask_for_model()
    save_model_to_file(speaker_name)
    print("--------------------------------------------------------")
else:
    with open("statuses/speaker_name.txt", "r") as file:
        speaker_name = file.read()











import os

import os

# Path to the folder containing models
model_directory = "faster_whisper_models"

# Function to detect available models in the folder
def get_available_models():
    try:
        # List all directories in the model directory
        available_models = [d for d in os.listdir(model_directory) if os.path.isdir(os.path.join(model_directory, d))]
        return available_models
    except FileNotFoundError:
        print("Error: Model directory not found.")
        exit(1)

# Function to ask the user for the model
def ask_for_model():
    available_models = get_available_models()

    if not available_models:
        print("No models found in the directory.")
        exit(1)

    print("Please select a faster-whisper model from the following list:")
    for i, model in enumerate(available_models, 1):
        print(f"{i}. {model}")

    while True:
        try:
            choice = int(input("Enter the number of the model you want to use: "))
            if 1 <= choice <= len(available_models):
                selected_model = available_models[choice - 1]
                print(f"You selected: {selected_model}")
                return selected_model
            else:
                print("Invalid choice. Please choose a valid model number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to save the model name to a file
def save_model_to_file(model_name):
    # Create the directory if it doesn't exist
    os.makedirs("statuses", exist_ok=True)

    # Save the selected model to statuses/whisper_model_name.txt
    file_path = "statuses/whisper_model_name.txt"
    with open(file_path, "w") as file:
        file.write(model_name)

# Get the selected model and save it
if not use_default_model:
    selected_model = ask_for_model()
    save_model_to_file(selected_model)
    print("--------------------------------------------------------")
else:
    with open("statuses/whisper_model_name.txt", "r") as file:
        selected_model = file.read()

    print("--------------------------------------------------------")
    print(f"Using default models.\nTTS: '{speaker_name}'\nSTT: '{selected_model}'")
    print("--------------------------------------------------------")

import os
os.environ['TRANSFORMERS_NO_TF'] = '1'


from thread import execute





from datetime import datetime
import time
import pytz

# Set timezone to Singapore Time (SGT)
sgt_tz = pytz.timezone('Asia/Singapore')

# Function to get formatted current time in Singapore Time (SGT)
def get_sgt_time():
    # Set timezone to Singapore Time (SGT)
    sgt_tz = pytz.timezone('Asia/Singapore')
    # Get current time in SGT
    current_time = datetime.now(sgt_tz)
    # Format time in HH:MM:SS and extended microseconds
    formatted_time = current_time.strftime('%H:%M:%S.') + f'{current_time.microsecond}'
    return formatted_time

#user_start_time = get_sgt_time()
#user_end_time = get_sgt_time()
#ai_start_time = get_sgt_time()
#ai_end_time = get_sgt_time()

def input_simulation():
    global playback_active
    while True:
        time.sleep(1)
        # Given sentence
        sentence = input("\nUser:\n")

        if sentence != '':
            with open("statuses/chatbot_replied.txt", "w") as file:
                file.write('false')

        # Get start and end times
        user_start_time = get_sgt_time()

        # Split the sentence into words
        words = sentence.split()

        # Initialize an empty string to build the output
        current_content = ""

        for word in words:
            user_latest_word_time = get_sgt_time()

            # Add the next word to the current content
            current_content += word + " "

            # Open the file in write mode and overwrite it with the current content
            with open("transcription/input.txt", "w") as file:
                file.write(f'(start time: {user_start_time}) ' + current_content.strip() + f"... [Speaking] (latest word time: {user_latest_word_time})\n")  # Add [Speaking] after each incremental addition
            
            time.sleep(0.25)  # Wait 2 seconds before adding the next word

        user_latest_word_time = get_sgt_time()

        # Open the file in write mode and overwrite it with the current content
        with open("transcription/input.txt", "w") as file:
            file.write(f'(start time: {user_start_time}) ' + current_content.strip() + f" [Not Speaking] (latest word time: {user_latest_word_time})\n")  # Add [Not Speaking]

        def input_threading_lol():
            while True:
                with open('transcription/input.txt', 'r') as file:
                    user_input = file.read()
                with open('statuses/speak_status.txt', 'r') as file:
                    speak_status = file.read()
                with open('statuses/chatbot_replied.txt', 'r') as file:
                    chatbot_replied = file.read()
                if speak_status == 'false' and chatbot_replied == 'true' and '[Not Speaking]' in user_input:

                    with open("transcription/input.txt", "w") as file:
                        file.write('')  
        input_lol = threading.Thread(target=input_threading_lol)
        input_lol.start()

# input_simulation()

# from thinking_model import thoughts_loop
import chat_utils
import files
import json

from initialize_tts import initialize_tts_model

import generate_voice

# Initialize LLM models
chat_utils.initialize()

chat_llm = chat_utils.use_chat_llm()


from initialize_whisper import initialize_whisper_model
import time
import threading
import pyaudio
import wave
import numpy as np
import os
from robotic_voice import if_robotic, apply_vocoder
from C3PO_effect import apply_c3po_effect

# Load VAD model
sampling_rate = 16000
chunk_size = 512
speech_threshold = 0.9

# Global variables

buffer = b''  # Buffer to store audio data
wf_global = None  # To keep a reference to the wave file object
speak_status = True
playback_active = False

# Initialize Whisper model
print("Initializing Whisper model...")
whisper_model = initialize_whisper_model()
print("Whisper model initialized.")





visualizer_on = False

if visualizer_on:
    from visualizer import run_visualizer, play_visualizer, stop_visualizer




from system_status.battery_status import get_battery_status
from system_status.wifi_status import check_wifi_status
from system_status.system_status import get_system_status











def play(file_path):
    global buffer, wf_global, speak_status, playback_active
    speak_status = True
    playback_active = True
    with open("statuses/playback_active.txt", "w") as file:
        file.write('true')   
    if not os.path.exists(file_path):
        print(f"Audio file not found: {file_path}")
        return

    wf = wave.open(file_path, 'rb')
    wf_global = wf
    p = pyaudio.PyAudio()
    
    try:
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)
        
        data = wf.readframes(512)
        while data and speak_status:
            buffer += data
            stream.write(data)
            data = wf.readframes(512)
        
        playback_active = False
        with open("statuses/playback_active.txt", "w") as file:
            file.write('false')   
        # print("AI has stopped talking.")

        buffer = b''  # Clear buffer after saving if needed
        
        stream.stop_stream()
    except Exception as e:
        print(f"Error playing audio: {e}")
    finally:
        stream.close()
        wf.close()
        p.terminate()


def run():
    if if_robotic:
        play("audios/vocoder_output.wav")
    else:
        play("audios/output_c3po_effect.wav")


# Function to transcribe audio with word timestamps using Whisper model
# Function to transcribe audio with word timestamps using Whisper model
def transcribe_ai_voice_with_whisper(audio_file, whisper_model):
    try:
        segments, info = whisper_model.transcribe(audio_file, beam_size=5, word_timestamps=True)
        
        transcription = ""
        word_timestamps = []
        
        # Collect transcription and timestamps
        for segment in segments:
            transcription += segment.text + " "
            
            # For each word in the segment, get its timestamp
            for word in segment.words:
                word_timestamps.append({
                    'word': word.word,
                    'start': word.start,
                    'end': word.end
                })
        
        return transcription.strip(), word_timestamps, info.language, info.language_probability
    except Exception as e:
        return "", [], "", 0.0


def file_to_transcribe(if_robotic):
    if if_robotic:
        apply_c3po_effect("audios/output.wav", "audios/output_c3po_effect.wav")
        apply_vocoder("audios/output_c3po_effect.wav", "audios/vocoder_output.wav", "audios/carrier.wav", speech_volume=1, vocoder_volume=1)
        audio_file = 'audios/output.wav'
    else:
        apply_c3po_effect("audios/output.wav", "audios/output_c3po_effect.wav")
        audio_file = 'audios/output.wav'
    return audio_file


def write_file_in_real_time(word_timestamps, output_file_path):
    global speak_status
    start_time = time.time()  # Start timer 
    last_word_index = 0  # To keep track of the last word printed
    ai_start_time = get_sgt_time()

    current_transcription = f"(start time: {ai_start_time})"  # To build the current transcription

    # Print word-level timestamps in real time
    while last_word_index < len(word_timestamps):
        current_time = time.time() - start_time
        
        # Check if any word's start time has been reached
        while (last_word_index < len(word_timestamps) and 
                word_timestamps[last_word_index]['start'] <= current_time):
            # Get the current word
            word_info = word_timestamps[last_word_index]
            current_transcription += word_info['word'] + " "  # Add the word to current transcription
            
            # Clean up extra spaces
            current_transcription = ' '.join(current_transcription.split())
            ai_latest_word_time = get_sgt_time()
            
            # Write the current transcription to the file, overwriting it each time
            with open(output_file_path, "w") as file:  # Open in write mode to overwrite
                file.write(current_transcription.strip() + f' (latest word time: {ai_latest_word_time})')  # Write current transcription without trailing space
            
            last_word_index += 1
            if not speak_status:
                break
        if not speak_status:
            break






















def stream_response_speak(model, prompt):
    
    chunks = []
    response_generator = model.stream(prompt)
    for chunk in response_generator:
        delta_content = chunk.content
        if delta_content is not None:
            chunks.append(delta_content)

    return ''.join(chunks)






def stream_response(model, system_prompt, conversation_history):
    # Combine system prompt, conversation history, and user input
    full_conversation = [{"role": "system", "content": system_prompt}] + conversation_history
    
    chunks = []
    response_generator = model.stream(full_conversation)
    for chunk in response_generator:
        delta_content = chunk.content
        if delta_content is not None:
            chunks.append(delta_content)
            print(delta_content, end="", flush=True)
    print('\n')
    return ''.join(chunks)


import time
import random

def simulated_stream_response(system_prompt, conversation_history, action_index):
    # Read the contents of the transcription/input.txt file
    with open("transcription/input.txt", "r") as file:
        transcription = file.read().strip()

    time.sleep(1)

    full_conversation = [{"role": "system", "content": system_prompt}] + conversation_history

    # List of possible actions
    actions = input('what action?:')
    # If the transcription is empty, always pick 'listen'
    if transcription == '':
        current_action = 'listen'
    else:
        # Pick 'listen' first, then randomly choose one from the remaining actions
        if action_index == 0:
            current_action = 'listen'
        else:
            current_action = random.choice(actions[1:])  # Exclude 'listen' from random selection

    # Update the action index to the next one in sequence (cycle back if needed)
    action_index = (action_index + 1) % len(actions)

    # Determine the 'tool_args' based on the selected action
    if current_action in ['response', 'backchannel', 'interrupt']:
        tool_args = {"text": "Shut up Austin"}
    else:
        tool_args = {}

    # Create the sentence with the sequential action, ensuring proper JSON format with double quotes
    sentence = f'''{{
        "thoughts": [
            "I have no thoughts"
        ],
        "tool_name": "{current_action}",
        "tool_args": {json.dumps(tool_args)}
    }}'''

    print(sentence)

    return sentence, action_index




def save_response(text):
    with open('ai_response.txt', 'w', encoding='utf-8') as file:
        # Convert list to string if text is a list
        if isinstance(text, list):
            text = '\n'.join(text)  # Join list elements into a single string with newline
        file.write(text)

listening = False        
conversation_history = []    
pretty_conversation_history = []
with open("statuses/locked.txt", "w") as file:
    file.write('Not delete')



def chat_bot(conversation_history, user_input, halved_user_content, chatbot_listening, chatbot_response):
    global speak_status, playback_active, listening, speaker_name, active_listening

    # Initialize an empty conversation history
    conversation_history = []
    listening = False        


    # action_index = 0  # Start with the first action in the sequence

    # Read from conversation_history.txt and store the content into conversation_history
    with open('conversation_history.txt', 'r') as file:
        lines = file.readlines()

    # Parse each line to convert from JSON strings to Python objects
    for line in lines:
        try:
            # First, strip newlines, then load the JSON string into Python dict
            conversation_history.append(json.loads(line.strip()))
        except json.JSONDecodeError as e:
            print(f"Error parsing line: {line}, error: {e}")

    while True:
        battery = get_battery_status()
        wifi = check_wifi_status()
        system = get_system_status()

        system_md = files.read_file("prompts/system.md")
        personality = files.read_file(f"XTTS-v2_models/XTTS-v2_{speaker_name}/personality/{speaker_name}.md")
        system_prompt = f"{personality}\n\n---\n\n**# Wi-Fi Status:**\n{wifi}\n**# Battery Status:**\n{battery}\n**# System Status:**\n{system}\n\n{system_md}"
        try:
            with open("transcription/input.txt", "r") as file:
                user_input = file.read()
                 
        except:
            user_input = ''
        with open("donottouch/user_input.txt", "w") as file:
            file.write(user_input)
        with open("statuses/spoken_user.txt", "w") as file:
            file.write('')    

        # user_input = input('\nUser:\n')
        conversation_history.append({"role": "user", "content": user_input})


        words = user_input.split()  # Split the input into words

        # If there's only one word, just return it
        if len(words) <= 1:
            halved_user_content = user_input
        else:
            half_index = len(words) // 2  # Calculate the index for half
            halved_user = ' '.join(words[:half_index])  # Join the first half of words
            halved_user_content = f'{halved_user}... [Speaking]'
        with open("donottouch/halved_user_content.txt", "w") as file:
            file.write(halved_user_content)





        
        # # Stream the response with the system prompt, user input, and conversation history
        chatbot_response = stream_response(chat_llm, system_prompt, conversation_history)




        # Call the function
        # chatbot_response, action_index = simulated_stream_response(system_prompt, conversation_history, action_index)

        # Print the generated response and the updated action index
        # print(f"Updated action index: {action_index}")




        with open("donottouch/chatbot_response.txt", "w") as file:
            file.write(chatbot_response)

        conversation_history.append({"role": "ai", "content": chatbot_response})
        if '[Not Speaking]' in user_input:
            with open("statuses/chatbot_replied.txt", "w") as file:
                file.write('true')

        tool_name, tool_args = chat_utils.extract_tool_info(chatbot_response)

        # Ensure tool_name is not None before writing
        if tool_name is None:
            tool_name = "unknown_tool"  # Default or fallback value

        with open("statuses/status.txt", "w") as file:
            file.write(tool_name)


        if tool_name in ('listen', 'ignore'):
            listening = True
            chatbot_listening = chatbot_response
            with open("donottouch/chatbot_listening.txt", "w") as file:
                file.write(chatbot_listening)            
            conversation_history = conversation_history[:-2] # REMOVES LAST TWO IF LISTEN
        else:
            if listening:
                conversation_history = conversation_history[:-2]
                conversation_history.append({"role": "user", "content": halved_user_content})
                conversation_history.append({"role": "ai", "content": chatbot_listening})       
                conversation_history.append({"role": "user", "content": user_input})                 
                conversation_history.append({"role": "ai", "content": chatbot_response})
                listening = False

        if '[Not Speaking]' in user_input and tool_name in ('listen', 'ignore'):
            conversation_history.append({"role": "user", "content": user_input})
            conversation_history.append({"role": "ai", "content": chatbot_response})




        if tool_args is not None:
            text_to_save = tool_args.get('text', '')
        else:
            text_to_save = ''   

        save_response(text_to_save)
        # print(chatbot_response)

        if len(conversation_history) > 20:
            conversation_history = conversation_history[-20:]


        # Open a file in write mode
        with open('conversation_history.txt', 'w') as file:
            for item in conversation_history:
                file.write(json.dumps(item) + '\n')
        # print("\n\n\nCONVERSATION HISTORY\n\n\n", conversation_history)

        if tool_name in ('response', 'backchannel', 'interrupt'):
            spoken_ai_response = tool_args.get('text', '')
            print('\nAI:', spoken_ai_response)
            try:
                with open("transcription/output.txt", "w") as file:
                    file.write(spoken_ai_response)
            except Exception as e:
                print("Error writing to file: ", e)

            generate_voice.run()

            audio_file = file_to_transcribe(if_robotic)

        #     # Get transcription, timestamps, language info
            ai_transcription, word_timestamps, detected_language, language_probability = transcribe_ai_voice_with_whisper(audio_file, whisper_model)

        #     # Print results
        #     # print(f"Transcription: {ai_transcription}")
        #     # print(f"Detected language: {detected_language} (Probability: {language_probability})")

        #     # Write output to file in real time
            output_file_path = "transcription/output.txt"

            play_audio_thread = threading.Thread(target=run)
            play_audio_thread.start()

            save_stream_words = threading.Thread(target=write_file_in_real_time, args=(word_timestamps, output_file_path))
            save_stream_words.start()



        #     # print(f"Transcription written to {output_file_path}")
            if playback_active:
                print('playback_active is active')
                with open("statuses/speak_status.txt", "w") as file:
                    file.write('true')     
                if visualizer_on:

                    play_visualizer()

                with open("transcription/output.txt", "w") as file:
                    file.write('')   


                while True:
                    time.sleep(0.1)
                    speak_system_md = files.read_file("prompts/speak_system.md")
                    speak_status_md = files.read_file("prompts/speak_status.md")

                    with open("transcription/output.txt", "r") as file:
                        spoken_ai_response = file.read()
                        
                    with open("transcription/input.txt", "r") as file:
                        spoken_user_input = file.read()
                    if spoken_user_input == '':
                        spoken_user_input = 'none'

                    speak_system_prompt = f"{personality}\n{speak_system_md}\n{speak_status_md}\n{conversation_history}\nCurrent spoken words by you: '{spoken_ai_response}'\nCurrent spoken words by the user: '{spoken_user_input}'"
                    with open("speak_system_prompt.txt", "w") as file:
                        file.write(speak_system_prompt)   

                    prompt = [{"role": "system", "content": speak_system_prompt}]
                    speak_status_response = stream_response_speak(chat_llm, prompt)
                    print("speak_status_response:\n", speak_status_response)

                    # Parse the JSON string into a Python dictionary
                    response_dict = json.loads(speak_status_response)

                    # Extract the value of the 'speak' key
                    speak_status_str = response_dict.get('continue')
                    thoughts_str = response_dict.get('reason')
                    print("speak_status: ", speak_status_str)
                    print("thought_str: ", thoughts_str)
                    print("")
                     
                    if speak_status_str.lower() == 'true':
                        speak_status = True
                        with open("statuses/speak_status.txt", "w") as file:
                            file.write('true')       
                        if not playback_active:
                            with open("statuses/speak_status.txt", "w") as file:
                               file.write('false')         
                            if spoken_user_input != 'none':  
                                finished_speaking_system = f"You have finished speaking; however, the user has overlapped your words with their own.\nYour thoughts: {thoughts_str}\nYour spoken words: {spoken_ai_response}\nThe user's spoken words: {spoken_user_input}"
                                conversation_history.append({"role": "system", "content": finished_speaking_system})   
                                if '[Speaking]' in spoken_user_input:
                                    break        
                            if '[Not Speaking]' in spoken_user_input:
                                with open("transcription/input.txt", "w") as file:
                                    file.write('')
                                print('break loop 1...')
                                break
                            if spoken_user_input == 'none':
                                finished_speaking_system = f'You have finished speaking without any interruptions.\nYour thoughts: {thoughts_str}\nYour spoken words: {spoken_ai_response}'
                                conversation_history.append({"role": "system", "content": finished_speaking_system})   
                                print('break loop 2...')
                                break
                    else:
                        speak_status = False
                        with open("statuses/speak_status.txt", "w") as file:
                            file.write('false')     
                        interrupted_ai_system = f"You have decided to stop speaking.\nYour thoughts: {thoughts_str}\nYour spoken words: {spoken_ai_response}\n The user's spoken words: {spoken_user_input}"
                        conversation_history.append({"role": "system", "content": interrupted_ai_system})
                        if '[Not Speaking]' in spoken_user_input:
                            with open("transcription/input.txt", "w") as file:
                                file.write('')
                        print('break loop 3...')
                        break
        if not active_listening:                   
            if user_input == '':
                print("Breaking the loop 3...")
                break

import threading

def run_thread():
    global simulated_input
    if visualizer_on:
        visualizer_thread = threading.Thread(target=run_visualizer)
        visualizer_thread.start()

    with open("donottouch/user_input.txt", "r") as file:
        user_input = file.read()
    with open("donottouch/halved_user_content.txt", "r") as file:
        halved_user_content = file.read()
    with open("donottouch/chatbot_response.txt", "r") as file:
        chatbot_response = file.read()
    with open("donottouch/chatbot_listening.txt", "r") as file:
        chatbot_listening = file.read()

    if simulated_input:
        simulation = threading.Thread(target=input_simulation)
        simulation.start()
    else:
        real_time_transcription = threading.Thread(target=execute)
        real_time_transcription.start()

    chat_bot(conversation_history, user_input, halved_user_content, chatbot_listening, chatbot_response)



def run_thread_stop():
    global simulated_input
    if visualizer_on:
        visualizer_thread = threading.Thread(target=run_visualizer)
        visualizer_thread.start()

    with open("donottouch/user_input.txt", "r") as file:
        user_input = file.read()
    with open("donottouch/halved_user_content.txt", "r") as file:
        halved_user_content = file.read()
    with open("donottouch/chatbot_response.txt", "r") as file:
        chatbot_response = file.read()
    with open("donottouch/chatbot_listening.txt", "r") as file:
        chatbot_listening = file.read()


    if simulated_input:
        simulation = threading.Thread(target=input_simulation)
        simulation.start()
    else:
        real_time_transcription = threading.Thread(target=execute)
        real_time_transcription.start()

    while True:
        time.sleep(1)
        try:
            with open("transcription/input.txt", "r") as file:
                user_input = file.read()
                    
        except:
            user_input = ''





        if user_input == '':
            pass
        else:
            chat_bot(conversation_history, user_input, halved_user_content, chatbot_listening, chatbot_response)




if active_listening:
    run_thread()   
    print('Active Listening: On')
else:
    run_thread_stop()
    print('Active Listening: Off')
