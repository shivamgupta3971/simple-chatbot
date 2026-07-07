import time
import random


# RESPONSE DATA - All chatbot responses


GREETINGS = ["hello", "hi", "hey", "good morning", "good evening", 
             "good afternoon", "howdy", "sup", "what's up", "greetings"]

EXIT_COMMANDS = ["bye", "goodbye", "exit", "quit", "see you", 
                 "farewell", "stop", "end", "close", "leave"]

GREETING_RESPONSES = [
    "Hello! Welcome! How can I help you today? 😊",
    "Hi there! Great to see you! What can I do for you?",
    "Hey! I'm your friendly chatbot. How may I assist you?",
    "Greetings! I'm here to help. What's on your mind?"
]

EXIT_RESPONSES = [
    "Goodbye! Have a wonderful day! 👋",
    "See you later! Take care!",
    "Bye! It was nice chatting with you! 😊",
    "Farewell! Come back anytime you need help!"
]


# CHATBOT BRAIN - Response Logic


def get_response(user_input):
    """
    Main function to process user input and return response.
    Uses if-else logic for decision making.
    """
    
   
    user_input = user_input.lower().strip()
    
    if any(greet in user_input for greet in GREETINGS):
        return random.choice(GREETING_RESPONSES)
 
    elif any(exit_cmd in user_input for exit_cmd in EXIT_COMMANDS):
        return "EXIT"  
    
    
    elif "your name" in user_input or "who are you" in user_input or "what are you" in user_input:
        return "I'm ChatBot 🤖, a simple rule-based AI assistant built for an internship project!"
    
    
    elif "how are you" in user_input or "how r u" in user_input or "you doing" in user_input:
        return "I'm doing great, thanks for asking! 😄 I'm always ready to chat. How about you?"
    
   
    elif "how old" in user_input or "your age" in user_input:
        return "I was just created recently, so I'm pretty young! 🌱 Age doesn't matter for bots though!"
    
    
    elif "help" in user_input or "what can you do" in user_input or "commands" in user_input:
        return show_help()
    
    
    elif "time" in user_input or "what time" in user_input:
        current_time = time.strftime("%I:%M %p")
        return f"⏰ The current time is: {current_time}"
    
    
    elif "date" in user_input or "today" in user_input or "what day" in user_input:
        current_date = time.strftime("%A, %B %d, %Y")
        return f"📅 Today's date is: {current_date}"
    
    
    elif "weather" in user_input or "temperature" in user_input or "forecast" in user_input:
        return "🌤️ I can't check real-time weather yet, but I hope it's sunny wherever you are!"

    elif "joke" in user_input or "funny" in user_input or "make me laugh" in user_input:
        return tell_joke()
    
    
    elif "calculate" in user_input or "math" in user_input or "solve" in user_input:
        return handle_math(user_input)
    
    
    elif "favorite color" in user_input or "favourite color" in user_input:
        return "🎨 My favorite color is blue — just like the sky and the ocean!"
    
    elif "favorite food" in user_input or "favourite food" in user_input:
        return "🍕 If I could eat, I'd definitely choose pizza! What about you?"
    
    elif "favorite movie" in user_input or "favourite movie" in user_input:
        return "🎬 I love 'The Matrix' — a movie about AI! Pretty fitting, right? 😄"
    
    
    elif "python" in user_input or "programming" in user_input or "coding" in user_input:
        return "🐍 Python is amazing! It's the language I was built with. Easy to learn and very powerful!"
    
    
    elif "artificial intelligence" in user_input or " ai " in user_input or "machine learning" in user_input:
        return "🤖 AI is fascinating! I'm a simple rule-based AI. More advanced AIs use machine learning and neural networks!"
    
    
    elif "thank" in user_input or "thanks" in user_input or "thank you" in user_input:
        return "You're welcome! 😊 Happy to help anytime!"
    
    
    elif "sorry" in user_input or "apologize" in user_input or "my bad" in user_input:
        return "No worries at all! 😊 Is there anything I can help you with?"
    
    
    elif user_input in ["yes", "yeah", "yep", "yup", "sure", "absolutely"]:
        return "Great! 👍 Tell me more or ask me anything!"
    
    elif user_input in ["no", "nope", "nah", "not really"]:
        return "Alright! 😊 Let me know if you change your mind or need anything!"
    
    
    elif user_input == "" or user_input == " ":
        return "⚠️ Oops! It seems you didn't type anything. Please enter a message!"
    
    
    else:
        return get_default_response(user_input)



# HELPER FUNCTIONS


def show_help():
    """Show all available commands to the user."""
    help_text = """
╔══════════════════════════════════════════╗
║           📋 CHATBOT COMMANDS            ║
╠══════════════════════════════════════════╣
║  👋 Greetings  → hello, hi, hey         ║
║  ❓ About Bot  → who are you?           ║
║  😊 Status     → how are you?           ║
║  ⏰ Time       → what time is it?       ║
║  📅 Date       → what's today's date?   ║
║  😂 Jokes      → tell me a joke         ║
║  🧮 Math       → calculate 5 + 3        ║
║  🌤️ Weather    → how's the weather?     ║
║  🐍 Python     → tell me about python   ║
║  🤖 AI Info    → what is AI?            ║
║  🙏 Thanks     → thank you              ║
║  🚪 Exit       → bye, quit, exit        ║
╚══════════════════════════════════════════╝
    """
    return help_text


def tell_joke():
    """Return a random joke."""
    jokes = [
        "😂 Why do programmers prefer dark mode?\n   Because light attracts bugs! 🐛",
        "😄 Why did the computer go to the doctor?\n   Because it had a virus! 🦠",
        "🤣 What do you call a sleeping dinosaur?\n   A dino-snore! 🦕",
        "😆 Why can't a bicycle stand on its own?\n   Because it's two-tired! 🚲",
        "😂 Why did the math book look so sad?\n   Because it had too many problems! 📚",
        "🤖 Why did the robot go on vacation?\n   To recharge its batteries! 🔋"
    ]
    return random.choice(jokes)


def handle_math(user_input):
    """Simple calculator for basic math operations."""
    try:
        # Extract numbers and operator from input
        if "+" in user_input:
            parts = user_input.split("+")
            nums = [float(p.strip().split()[-1]) for p in parts]
            result = nums[0] + nums[1]
            return f"🧮 Result: {nums[0]} + {nums[1]} = {result}"
        
        elif "-" in user_input:
            parts = user_input.split("-")
            nums = [float(p.strip().split()[-1]) for p in parts]
            result = nums[0] - nums[1]
            return f"🧮 Result: {nums[0]} - {nums[1]} = {result}"
        
        elif "*" in user_input or "x" in user_input:
            operator = "*" if "*" in user_input else "x"
            parts = user_input.split(operator)
            nums = [float(p.strip().split()[-1]) for p in parts]
            result = nums[0] * nums[1]
            return f"🧮 Result: {nums[0]} × {nums[1]} = {result}"
        
        elif "/" in user_input:
            parts = user_input.split("/")
            nums = [float(p.strip().split()[-1]) for p in parts]
            if nums[1] == 0:
                return "❌ Error: Cannot divide by zero!"
            result = nums[0] / nums[1]
            return f"🧮 Result: {nums[0]} ÷ {nums[1]} = {result:.2f}"
        
        else:
            return "🧮 For math, type like: 'calculate 5 + 3' or 'solve 10 / 2'"
    
    except:
        return "🧮 I couldn't solve that. Try: 'calculate 5 + 3'"


def get_default_response(user_input):
    """Return a default response when input is not recognized."""
    defaults = [
        f"🤔 Hmm, I'm not sure about '{user_input}'. Type 'help' to see what I can do!",
        f"❓ I don't understand '{user_input}' yet. I'm still learning! Try typing 'help'.",
        f"🤷 That's a tricky one! I couldn't find an answer for '{user_input}'. Type 'help' for options!",
        f"💭 Interesting! But I don't know how to respond to '{user_input}'. Type 'help' to see my commands!"
    ]
    return random.choice(defaults)



# DISPLAY FUNCTIONS - UI Design


def print_welcome():
    """Display a welcome banner when chatbot starts."""
    print("\n" + "="*50)
    print("🤖  WELCOME TO SIMPLE RULE-BASED CHATBOT  🤖")
    print("="*50)
    print("  Built with Python | Internship Project")
    print("  Type 'help' to see available commands")
    print("  Type 'bye' or 'exit' to quit")
    print("="*50 + "\n")


def print_goodbye():
    """Display a goodbye message when chatbot exits."""
    print("\n" + "="*50)
    print("  Thank you for using ChatBot! 🤖")
    print("  See you next time! Goodbye! 👋")
    print("="*50 + "\n")


def typing_effect(text, delay=0.03):
    """Simulate typing effect for bot responses."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # New line after response



# MAIN CHATBOT LOOP


def run_chatbot():
    """
    Main function to run the chatbot.
    Continuous loop that keeps chatbot running
    until user types an exit command.
    """
    
    
    print_welcome()
    
    
    message_count = 0
    
    
    while True:
        try:
            
            user_input = input("You    👤 : ").strip()
            
            
            response = get_response(user_input)
            
            
            if response == "EXIT":
                exit_msg = random.choice(EXIT_RESPONSES)
                print(f"\nBot    🤖 : ", end="")
                typing_effect(exit_msg)
                print_goodbye()
                break  
            
            
            print(f"\nBot    🤖 : ", end="")
            typing_effect(response)
            print()  
            
            
            message_count += 1
            
            
            if message_count % 5 == 0:
                print("💡 Tip: Type 'help' to see all available commands!\n")
        
       
        except KeyboardInterrupt:
            print("\n\nBot    🤖 : Caught a keyboard interrupt! Goodbye! 👋")
            print_goodbye()
            break



# PROGRAM ENTRY POINT


if __name__ == "__main__":
    run_chatbot()
