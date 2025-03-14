import telebot
from telebot import types
import sqlite3
import random
from datetime import datetime

# Replace 'YOUR_BOT_TOKEN' with your actual bot token from BotFather
bot = telebot.TeleBot("8032404481:AAEiIwEkrfTvYw5QPLL4ToQ8PFsKDFF9YCM")

# List of themes
THEMES = [
    "Introduction to Information Security",
    "Cryptography",
    "Access Control and Authentication",
    "Network Security",
    "Malicious Software",
    "Operating System Security",
    "Database Protection",
    "Security in Cloud",
    "Security Operations",
    "Security Governance"
]


# Database initialization
def init_db():
    conn = sqlite3.connect('first_bot.db')
    c = conn.cursor()

    # Create questions table if it doesn't exist
    c.execute('''CREATE TABLE IF NOT EXISTS questions
(id INTEGER PRIMARY KEY, 
 theme TEXT,
 question TEXT, 
 correct_answer TEXT, 
 options TEXT)''')

    # Check if the 'theme' column exists in the questions table
    c.execute("PRAGMA table_info(questions)")
    columns = [column[1] for column in c.fetchall()]
    if 'theme' not in columns:
        # Add the 'theme' column
        c.execute("ALTER TABLE questions ADD COLUMN theme TEXT")
        # Optionally, set a default theme for existing questions
        c.execute("UPDATE questions SET theme = 'Introduction to Information Security' WHERE theme IS NULL")

    # Create user scores table
    c.execute('''CREATE TABLE IF NOT EXISTS user_scores
                 (user_id INTEGER PRIMARY KEY, 
                  score INTEGER, 
                  total_questions INTEGER)''')

    # Create news table
    c.execute('''CREATE TABLE IF NOT EXISTS news
                 (id INTEGER PRIMARY KEY, 
                  title TEXT, 
                  content TEXT, 
                  date TEXT)''')

    conn.commit()
    conn.close()


# Sample questions with themes (expanded for more comprehensive coverage)
SAMPLE_QUESTIONS = [
    # Introduction to Information Security (5 questions)
    {
        'theme': 'Introduction to Information Security',
        'question': 'What is phishing?',
        'correct_answer': 'A',
        'options': 'A) A cyber attack that uses disguised email as a weapon\n'
                   'B) A type of malware\n'
                   'C) A hardware attack\n'
                   'D) A network protocol'
    },
    {
        'theme': 'Introduction to Information Security',
        'question': 'What does the acronym CIA stand for in information security?',
        'correct_answer': 'B',
        'options': 'A) Central Intelligence Agency\n'
                   'B) Confidentiality, Integrity, Availability\n'
                   'C) Cyber Incident Analysis\n'
                   'D) Critical Infrastructure Assessment'
    },
    {
        'theme': 'Introduction to Information Security',
        'question': 'What is a vulnerability in the context of information security?',
        'correct_answer': 'D',
        'options': 'A) A type of malware\n'
                   'B) A secure protocol\n'
                   'C) A hardware component\n'
                   'D) A weakness that can be exploited by a threat'
    },
    {
        'theme': 'Introduction to Information Security',
        'question': 'What is the purpose of security awareness training?',
        'correct_answer': 'A',
        'options': 'A) To educate employees about security risks and best practices\n'
                   'B) To install antivirus software\n'
                   'C) To configure firewalls\n'
                   'D) To develop new security protocols'
    },
    {
        'theme': 'Introduction to Information Security',
        'question': 'What is the first step in the risk management process?',
        'correct_answer': 'C',
        'options': 'A) Risk mitigation\n'
                   'B) Risk monitoring\n'
                   'C) Risk identification\n'
                   'D) Risk avoidance'
    },

    # Cryptography (5 questions)
    {
        'theme': 'Cryptography',
        'question': 'What does HTTPS stand for?',
        'correct_answer': 'B',
        'options': 'A) Hyper Text Protocol Secure\n'
                   'B) Hyper Text Transfer Protocol Secure\n'
                   'C) Hyper Transfer Text Protocol Secure\n'
                   'D) Hyper Text Transport Protocol Secure'
    },
    {
        'theme': 'Cryptography',
        'question': 'What is the main purpose of encryption?',
        'correct_answer': 'A',
        'options': 'A) To protect data confidentiality\n'
                   'B) To increase data speed\n'
                   'C) To reduce data size\n'
                   'D) To authenticate users'
    },
    {
        'theme': 'Cryptography',
        'question': 'Which of the following is a symmetric encryption algorithm?',
        'correct_answer': 'B',
        'options': 'A) RSA\n'
                   'B) AES\n'
                   'C) ECC\n'
                   'D) Diffie-Hellman'
    },
    {
        'theme': 'Cryptography',
        'question': 'What is a digital signature used for?',
        'correct_answer': 'C',
        'options': 'A) To encrypt data\n'
                   'B) To compress data\n'
                   'C) To verify the authenticity and integrity of a message\n'
                   'D) To store passwords'
    },
    {
        'theme': 'Cryptography',
        'question': 'What is a key feature of public-key cryptography?',
        'correct_answer': 'D',
        'options': 'A) Uses a single key for encryption and decryption\n'
                   'B) Is faster than symmetric cryptography\n'
                   'C) Does not require key exchange\n'
                   'D) Uses two keys: public and private'
    },

    # Access Control and Authentication (5 questions)
    {
        'theme': 'Access Control and Authentication',
        'question': 'What is multi-factor authentication?',
        'correct_answer': 'C',
        'options': 'A) Using multiple passwords\n'
                   'B) Having multiple user accounts\n'
                   'C) Using two or more different factors to verify identity\n'
                   'D) Using biometrics only'
    },
    {
        'theme': 'Access Control and Authentication',
        'question': 'What is the principle of least privilege?',
        'correct_answer': 'A',
        'options': 'A) Users should only have access necessary for their job\n'
                   'B) Users should have full administrative access\n'
                   'C) Users should share accounts\n'
                   'D) Users should not use passwords'
    },
    {
        'theme': 'Access Control and Authentication',
        'question': 'What is a biometric authentication method?',
        'correct_answer': 'B',
        'options': 'A) Using a password\n'
                   'B) Fingerprint scanning\n'
                   'C) Using a smart card\n'
                   'D) Entering a PIN'
    },
    {
        'theme': 'Access Control and Authentication',
        'question': 'What is single sign-on (SSO)?',
        'correct_answer': 'C',
        'options': 'A) Using multiple passwords for one system\n'
                   'B) Logging in separately to each system\n'
                   'C) Using one set of credentials to access multiple systems\n'
                   'D) Disabling authentication'
    },
    {
        'theme': 'Access Control and Authentication',
        'question': 'What is the purpose of a role-based access control (RBAC) system?',
        'correct_answer': 'A',
        'options': 'A) To assign permissions based on user roles\n'
                   'B) To encrypt data\n'
                   'C) To monitor network traffic\n'
                   'D) To store user passwords'
    },

    # Network Security (5 questions)
    {
        'theme': 'Network Security',
        'question': 'What is a firewall?',
        'correct_answer': 'A',
        'options': 'A) A system designed to prevent unauthorized access\n'
                   'B) A type of malware\n'
                   'C) A network monitoring tool\n'
                   'D) A password manager'
    },
    {
        'theme': 'Network Security',
        'question': 'What is a VPN used for?',
        'correct_answer': 'C',
        'options': 'A) To increase network speed\n'
                   'B) To block all network traffic\n'
                   'C) To create a secure connection over a public network\n'
                   'D) To monitor user activity'
    },
    {
        'theme': 'Network Security',
        'question': 'What is a DDoS attack?',
        'correct_answer': 'B',
        'options': 'A) A type of encryption attack\n'
                   'B) An attempt to overwhelm a system with traffic to disrupt service\n'
                   'C) A hardware failure\n'
                   'D) A method to secure data'
    },
    {
        'theme': 'Network Security',
        'question': 'What is the purpose of intrusion detection systems (IDS)?',
        'correct_answer': 'A',
        'options': 'A) To detect unauthorized access or attacks\n'
                   'B) To encrypt network traffic\n'
                   'C) To store user credentials\n'
                   'D) To increase network bandwidth'
    },
    {
        'theme': 'Network Security',
        'question': 'What is packet sniffing?',
        'correct_answer': 'C',
        'options': 'A) A method to compress data\n'
                   'B) A way to secure network traffic\n'
                   'C) Capturing and analyzing network packets\n'
                   'D) Blocking network traffic'
    },

    # Malicious Software (5 questions)
    {
        'theme': 'Malicious Software',
        'question': 'What is ransomware?',
        'correct_answer': 'C',
        'options': 'A) Software that steals data\n'
                   'B) Software that monitors network traffic\n'
                   'C) Malware that encrypts files and demands payment\n'
                   'D) A network scanner'
    },
    {
        'theme': 'Malicious Software',
        'question': 'What is a trojan horse?',
        'correct_answer': 'B',
        'options': 'A) A type of firewall\n'
                   'B) Malware disguised as legitimate software\n'
                   'C) A network protocol\n'
                   'D) A secure encryption method'
    },
    {
        'theme': 'Malicious Software',
        'question': 'What is a worm in the context of malware?',
        'correct_answer': 'A',
        'options': 'A) Malware that spreads without user interaction\n'
                   'B) Malware that requires a host file\n'
                   'C) Malware that encrypts data\n'
                   'D) Malware that monitors user activity'
    },
    {
        'theme': 'Malicious Software',
        'question': 'What is spyware?',
        'correct_answer': 'C',
        'options': 'A) Software that protects against viruses\n'
                   'B) Software that encrypts data\n'
                   'C) Malware that secretly collects user information\n'
                   'D) Software that blocks network traffic'
    },
    {
        'theme': 'Malicious Software',
        'question': 'What is the primary purpose of antivirus software?',
        'correct_answer': 'A',
        'options': 'A) To detect and remove malware\n'
                   'B) To encrypt data\n'
                   'C) To monitor network traffic\n'
                   'D) To manage user passwords'
    },

    # Operating System Security (5 questions)
    {
        'theme': 'Operating System Security',
        'question': 'What is a privilege escalation attack?',
        'correct_answer': 'C',
        'options': 'A) An attack to encrypt data\n'
                   'B) An attack to monitor network traffic\n'
                   'C) An attack to gain unauthorized higher-level access\n'
                   'D) An attack to disable firewalls'
    },
    {
        'theme': 'Operating System Security',
        'question': 'What is the purpose of a security patch?',
        'correct_answer': 'A',
        'options': 'A) To fix vulnerabilities in software\n'
                   'B) To increase system performance\n'
                   'C) To encrypt user data\n'
                   'D) To monitor user activity'
    },
    {
        'theme': 'Operating System Security',
        'question': 'What is a sandbox in OS security?',
        'correct_answer': 'B',
        'options': 'A) A type of malware\n'
                   'B) An isolated environment to run untrusted programs\n'
                   'C) A network monitoring tool\n'
                   'D) A password manager'
    },
    {
        'theme': 'Operating System Security',
        'question': 'What is the purpose of user account control (UAC) in Windows?',
        'correct_answer': 'C',
        'options': 'A) To encrypt data\n'
                   'B) To monitor network traffic\n'
                   'C) To prevent unauthorized changes to the system\n'
                   'D) To disable antivirus software'
    },
    {
        'theme': 'Operating System Security',
        'question': 'What is a rootkit?',
        'correct_answer': 'A',
        'options': 'A) Malware that hides its presence on a system\n'
                   'B) A type of firewall\n'
                   'C) A network protocol\n'
                   'D) A secure encryption method'
    },

    # Database Protection (5 questions)
    {
        'theme': 'Database Protection',
        'question': 'What is SQL injection?',
        'correct_answer': 'C',
        'options': 'A) A type of encryption\n'
                   'B) A network monitoring tool\n'
                   'C) An attack that exploits database vulnerabilities\n'
                   'D) A password manager'
    },
    {
        'theme': 'Database Protection',
        'question': 'What is the purpose of database encryption?',
        'correct_answer': 'A',
        'options': 'A) To protect data confidentiality\n'
                   'B) To increase database performance\n'
                   'C) To monitor database activity\n'
                   'D) To manage user accounts'
    },
    {
        'theme': 'Database Protection',
        'question': 'What is a database audit trail?',
        'correct_answer': 'B',
        'options': 'A) A type of malware\n'
                   'B) A record of database activities for monitoring\n'
                   'C) A network protocol\n'
                   'D) A secure encryption method'
    },
    {
        'theme': 'Database Protection',
        'question': 'What is the purpose of input validation in database security?',
        'correct_answer': 'C',
        'options': 'A) To encrypt data\n'
                   'B) To increase database performance\n'
                   'C) To prevent SQL injection attacks\n'
                   'D) To manage user accounts'
    },
    {
        'theme': 'Database Protection',
        'question': 'What is a database backup used for?',
        'correct_answer': 'A',
        'options': 'A) To recover data after loss or corruption\n'
                   'B) To encrypt data\n'
                   'C) To monitor database activity\n'
                   'D) To increase database performance'
    },

    # Security in Cloud (5 questions)
    {
        'theme': 'Security in Cloud',
        'question': 'What is a key security concern in cloud computing?',
        'correct_answer': 'C',
        'options': 'A) Increasing system performance\n'
                   'B) Reducing hardware costs\n'
                   'C) Data breaches due to shared resources\n'
                   'D) Developing new software'
    },
    {
        'theme': 'Security in Cloud',
        'question': 'What is the purpose of cloud access security brokers (CASB)?',
        'correct_answer': 'A',
        'options': 'A) To enforce security policies between cloud services and users\n'
                   'B) To increase cloud storage capacity\n'
                   'C) To monitor network traffic\n'
                   'D) To develop new cloud applications'
    },
    {
        'theme': 'Security in Cloud',
        'question': 'What is a benefit of using encryption in cloud storage?',
        'correct_answer': 'B',
        'options': 'A) Increasing storage capacity\n'
                   'B) Protecting data confidentiality\n'
                   'C) Reducing cloud costs\n'
                   'D) Improving cloud performance'
    },
    {
        'theme': 'Security in Cloud',
        'question': 'What is a shared responsibility model in cloud security?',
        'correct_answer': 'C',
        'options': 'A) The cloud provider is responsible for all security\n'
                   'B) The user is responsible for all security\n'
                   'C) Security responsibilities are split between provider and user\n'
                   'D) Security is not required in the cloud'
    },
    {
        'theme': 'Security in Cloud',
        'question': 'What is a common cloud security threat?',
        'correct_answer': 'A',
        'options': 'A) Data breaches\n'
                   'B) Increasing storage capacity\n'
                   'C) Reducing cloud costs\n'
                   'D) Improving cloud performance'
    },

    # Security Operations (5 questions)
    {
        'theme': 'Security Operations',
        'question': 'What is the purpose of a security operations center (SOC)?',
        'correct_answer': 'C',
        'options': 'A) To develop new software\n'
                   'B) To increase system performance\n'
                   'C) To monitor and respond to security incidents\n'
                   'D) To manage user accounts'
    },
    {
        'theme': 'Security Operations',
        'question': 'What is incident response?',
        'correct_answer': 'A',
        'options': 'A) The process of handling security breaches\n'
                   'B) The process of encrypting data\n'
                   'C) The process of monitoring network traffic\n'
                   'D) The process of developing new software'
    },
    {
        'theme': 'Security Operations',
        'question': 'What is the purpose of security information and event management (SIEM)?',
        'correct_answer': 'B',
        'options': 'A) To encrypt data\n'
                   'B) To collect and analyze security events\n'
                   'C) To increase system performance\n'
                   'D) To manage user accounts'
    },
    {
        'theme': 'Security Operations',
        'question': 'What is a security audit?',
        'correct_answer': 'C',
        'options': 'A) A type of malware\n'
                   'B) A network protocol\n'
                   'C) A review of security controls and practices\n'
                   'D) A secure encryption method'
    },
    {
        'theme': 'Security Operations',
        'question': 'What is the purpose of penetration testing?',
        'correct_answer': 'A',
        'options': 'A) To identify vulnerabilities by simulating attacks\n'
                   'B) To encrypt data\n'
                   'C) To increase system performance\n'
                   'D) To manage user accounts'
    },

    # Security Governance (5 questions)
    {
        'theme': 'Security Governance',
        'question': 'What is security governance?',
        'correct_answer': 'C',
        'options': 'A) A type of malware\n'
                   'B) A network protocol\n'
                   'C) The framework for managing security risks and policies\n'
                   'D) A secure encryption method'
    },
    {
        'theme': 'Security Governance',
        'question': 'What is the purpose of a security policy?',
        'correct_answer': 'A',
        'options': 'A) To define rules and procedures for security\n'
                   'B) To encrypt data\n'
                   'C) To increase system performance\n'
                   'D) To manage user accounts'
    },
    {
        'theme': 'Security Governance',
        'question': 'What is compliance in security governance?',
        'correct_answer': 'B',
        'options': 'A) A type of malware\n'
                   'B) Adherence to laws, regulations, and standards\n'
                   'C) A network protocol\n'
                   'D) A secure encryption method'
    },
    {
        'theme': 'Security Governance',
        'question': 'What is the role of a chief information security officer (CISO)?',
        'correct_answer': 'C',
        'options': 'A) To develop new software\n'
                   'B) To increase system performance\n'
                   'C) To oversee an organization’s security strategy\n'
                   'D) To manage user accounts'
    },
    {
        'theme': 'Security Governance',
        'question': 'What is risk assessment in security governance?',
        'correct_answer': 'A',
        'options': 'A) Identifying and evaluating security risks\n'
                   'B) Encrypting data\n'
                   'C) Increasing system performance\n'
                   'D) Managing user accounts'
    }
]


def populate_sample_data():
    conn = sqlite3.connect('first_bot.db')
    c = conn.cursor()

    # Insert sample questions only if they don't already exist
    for q in SAMPLE_QUESTIONS:
        c.execute("SELECT COUNT(*) FROM questions WHERE question = ?", (q['question'],))
        if c.fetchone()[0] == 0:
            c.execute("INSERT INTO questions (theme, question, correct_answer, options) VALUES (?, ?, ?, ?)",
                      (q['theme'], q['question'], q['correct_answer'], q['options']))

    conn.commit()
    conn.close()


# Dictionary to store user states and current questions
user_data = {}


# Create the main menu keyboard
def get_main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_quiz = types.KeyboardButton('Quiz')
    btn_theory = types.KeyboardButton('Theory')
    btn_info = types.KeyboardButton('Info')
    markup.add(btn_quiz, btn_theory, btn_info)
    return markup


# Create the theme selection keyboard
def get_theme_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for i in range(0, len(THEMES), 2):
        if i + 1 < len(THEMES):
            markup.row(types.KeyboardButton(THEMES[i]), types.KeyboardButton(THEMES[i + 1]))
        else:
            markup.add(types.KeyboardButton(THEMES[i]))
    markup.add(types.KeyboardButton('Back to Main Menu'))
    return markup


# Create the post-question keyboard (for continuing in the same theme or changing themes)
def get_post_question_menu(selected_theme):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn_continue = types.KeyboardButton(f'Continue with {selected_theme}')
    btn_change_theme = types.KeyboardButton('Change Theme')
    btn_main_menu = types.KeyboardButton('Back to Main Menu')
    markup.add(btn_continue, btn_change_theme)
    markup.add(btn_main_menu)
    return markup


# Bot commands
@bot.message_handler(commands=['start'])
def start(message):
    user = message.from_user
    welcome_message = f"Welcome, {user.first_name}! 👋\n\n" \
                      "This is an Information Security Quiz Bot. Use the buttons below to:\n" \
                      "- Start a quiz\n" \
                      "- View your statistics\n" \
                      "- Learn about security threats"
    bot.reply_to(message, welcome_message, reply_markup=get_main_menu())


@bot.message_handler(func=lambda message: message.text == 'Quiz')
def quiz(message):
    user_id = message.from_user.id
    user_data[user_id] = {'state': 'SELECTING_THEME'}
    bot.reply_to(message, "Please select a theme for your quiz:", reply_markup=get_theme_menu())


@bot.message_handler(func=lambda message: message.from_user.id in user_data and
                                          user_data[message.from_user.id].get('state') == 'SELECTING_THEME')
def select_theme(message):
    user_id = message.from_user.id
    selected_theme = message.text

    if selected_theme == 'Back to Main Menu':
        user_data.pop(user_id, None)
        bot.reply_to(message, "Returning to main menu.", reply_markup=get_main_menu())
        return

    if selected_theme not in THEMES:
        bot.reply_to(message, "Please select a valid theme from the buttons below:", reply_markup=get_theme_menu())
        return

    conn = sqlite3.connect('first_bot.db')
    c = conn.cursor()

    # Get random question from the selected theme
    c.execute("SELECT * FROM questions WHERE theme = ? ORDER BY RANDOM() LIMIT 1", (selected_theme,))
    question = c.fetchone()
    conn.close()

    if question:
        user_data[user_id] = {'current_question': question, 'state': 'QUESTION', 'theme': selected_theme}
        question_text = f"Theme: {selected_theme}\n\nQuestion: {question[1]}\n\n{question[3]}\n\nPlease answer with A, B, C, or D"
        bot.reply_to(message, question_text)
    else:
        bot.reply_to(message, f"No questions available for theme '{selected_theme}'. Please select another theme:", reply_markup=get_theme_menu())


@bot.message_handler(func=lambda message: message.from_user.id in user_data and
                                          user_data[message.from_user.id].get('state') == 'QUESTION')
def check_answer(message):
    user_id = message.from_user.id
    user_answer = message.text.upper()

    if user_id not in user_data or 'current_question' not in user_data[user_id]:
        bot.reply_to(message, "Please start a quiz first by pressing the 'Quiz' button", reply_markup=get_main_menu())
        return

    question = user_data[user_id]['current_question']
    selected_theme = user_data[user_id]['theme']
    conn = sqlite3.connect('first_bot.db')
    c = conn.cursor()

    # Update user score
    c.execute("SELECT * FROM user_scores WHERE user_id = ?", (user_id,))
    user_score = c.fetchone()

    is_correct = user_answer == question[3]
    if user_score:
        new_score = user_score[1] + 1 if is_correct else user_score[1]
        new_total = user_score[2] + 1
        c.execute("UPDATE user_scores SET score = ?, total_questions = ? WHERE user_id = ?",
                  (new_score, new_total, user_id))
    else:
        c.execute("INSERT INTO user_scores (user_id, score, total_questions) VALUES (?, ?, ?)",
                  (user_id, 1 if is_correct else 0, 1))

    conn.commit()
    conn.close()

    response = f"Your answer: {user_answer}\n"
    response += "✅ Correct!" if is_correct else f"❌ Wrong! The correct answer was {question[3]}"
    response += f"\n\nWhat would you like to do next?"

    bot.reply_to(message, response, reply_markup=get_post_question_menu(selected_theme))


@bot.message_handler(func=lambda message: message.text.startswith('Continue with '))
def continue_quiz(message):
    user_id = message.from_user.id
    selected_theme = message.text.replace('Continue with ', '')

    if selected_theme not in THEMES:
        bot.reply_to(message, "Invalid theme. Please select a theme from the menu.", reply_markup=get_theme_menu())
        return

    conn = sqlite3.connect('first_bot.db')
    c = conn.cursor()

    # Get random question from the selected theme
    c.execute("SELECT * FROM questions WHERE theme = ? ORDER BY RANDOM() LIMIT 1", (selected_theme,))
    question = c.fetchone()
    conn.close()

    if question:
        user_data[user_id] = {'current_question': question, 'state': 'QUESTION', 'theme': selected_theme}
        question_text = f"Theme: {selected_theme}\n\nQuestion: {question[2]}\n\n{question[4]}\n\nPlease answer with A, B, C, or D"
        bot.reply_to(message, question_text)
    else:
        bot.reply_to(message, f"No more questions available for theme '{selected_theme}'. Please select another theme:", reply_markup=get_theme_menu())


@bot.message_handler(func=lambda message: message.text == 'Change Theme')
def change_theme(message):
    user_id = message.from_user.id
    user_data[user_id] = {'state': 'SELECTING_THEME'}
    bot.reply_to(message, "Please select a new theme for your quiz:", reply_markup=get_theme_menu())


@bot.message_handler(func=lambda message: message.text == 'Back to Main Menu')
def back_to_main_menu(message):
    user_id = message.from_user.id
    user_data.pop(user_id, None)
    bot.reply_to(message, "Returning to main menu.", reply_markup=get_main_menu())


@bot.message_handler(func=lambda message: message.text == 'Theory')
def theory(message):
    user_id = message.from_user.id
    conn = sqlite3.connect('first_bot.db')
    c = conn.cursor()

    c.execute("SELECT * FROM user_scores WHERE user_id = ?", (user_id,))
    user_score = c.fetchone()

    conn.close()

    if user_score:
        accuracy = (user_score[1] / user_score[2]) * 100 if user_score[2] > 0 else 0
        stats_text = f"Your Statistics:\n" \
                     f"Correct Answers: {user_score[1]}\n" \
                     f"Total Questions: {user_score[2]}\n" \
                     f"Accuracy: {accuracy:.2f}%"
    else:
        stats_text = "You haven't answered any questions yet. Start a quiz by pressing 'Quiz'!"

    bot.reply_to(message, stats_text, reply_markup=get_main_menu())


@bot.message_handler(func=lambda message: message.text == 'Info')
def info(message):
    info_text = "Information Security Threats Overview:\n\n" \
                "1. Malware: Malicious software designed to harm systems\n" \
                "2. Phishing: Fraudulent attempts to obtain sensitive information\n" \
                "3. DDoS Attacks: Attempts to overwhelm systems with traffic\n" \
                "4. SQL Injection: Attacks targeting database vulnerabilities\n" \
                "5. Social Engineering: Psychological manipulation of people\n\n" \
                "Press 'Quiz' to test your knowledge about these threats!"
    bot.reply_to(message, info_text, reply_markup=get_main_menu())


def main():
    # Initialize database
    init_db()
    populate_sample_data()

    # Start the bot
    print("Bot is running...")
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"Error during polling: {e}")


if __name__ == '__main__':
    main()