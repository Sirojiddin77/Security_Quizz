import telebot
from telebot import types
import sqlite3
import random
from datetime import datetime

# Bot tokeni
bot = telebot.TeleBot("8032404481:AAEiIwEkrfTvYw5QPLL4ToQ8PFsKDFF9YCM")

# Mavzular ro‘yxati
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

# Ma’lumotlar bazasini boshlash
def init_db():
    conn = sqlite3.connect('first_bot.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS questions
                 (id INTEGER PRIMARY KEY, 
                  theme TEXT,
                  question TEXT, 
                  correct_answer TEXT, 
                  options TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS user_scores
                 (user_id INTEGER PRIMARY KEY, 
                  score INTEGER, 
                  total_questions INTEGER)''')
    c.execute('''CREATE TABLE IF NOT EXISTS news
                 (id INTEGER PRIMARY KEY, 
                  title TEXT, 
                  content TEXT, 
                  date TEXT)''')
    conn.commit()
    conn.close()

# Namuna savollar (barcha 10 ta mavzu, har birida 5 ta savol)
SAMPLE_QUESTIONS = [
    # Introduction to Information Security
    {'theme': 'Introduction to Information Security', 'question': 'What is phishing?', 'correct_answer': 'A', 'options': 'A) A cyber attack that uses disguised email as a weapon\nB) A type of malware\nC) A hardware attack\nD) A network protocol'},
    {'theme': 'Introduction to Information Security', 'question': 'What does the acronym CIA stand for in information security?', 'correct_answer': 'B', 'options': 'A) Central Intelligence Agency\nB) Confidentiality, Integrity, Availability\nC) Cyber Incident Analysis\nD) Critical Infrastructure Assessment'},
    {'theme': 'Introduction to Information Security', 'question': 'What is a vulnerability in the context of information security?', 'correct_answer': 'D', 'options': 'A) A type of malware\nB) A secure protocol\nC) A hardware component\nD) A weakness that can be exploited by a threat'},
    {'theme': 'Introduction to Information Security', 'question': 'What is the purpose of security awareness training?', 'correct_answer': 'A', 'options': 'A) To educate employees about security risks and best practices\nB) To install antivirus software\nC) To configure firewalls\nD) To develop new security protocols'},
    {'theme': 'Introduction to Information Security', 'question': 'What is the first step in the risk management process?', 'correct_answer': 'C', 'options': 'A) Risk mitigation\nB) Risk monitoring\nC) Risk identification\nD) Risk avoidance'},

    # Cryptography
    {'theme': 'Cryptography', 'question': 'What does HTTPS stand for?', 'correct_answer': 'B', 'options': 'A) Hyper Text Protocol Secure\nB) Hyper Text Transfer Protocol Secure\nC) Hyper Transfer Text Protocol Secure\nD) Hyper Text Transport Protocol Secure'},
    {'theme': 'Cryptography', 'question': 'What is the main purpose of encryption?', 'correct_answer': 'A', 'options': 'A) To protect data confidentiality\nB) To increase data speed\nC) To reduce data size\nD) To authenticate users'},
    {'theme': 'Cryptography', 'question': 'Which of the following is a symmetric encryption algorithm?', 'correct_answer': 'B', 'options': 'A) RSA\nB) AES\nC) ECC\nD) Diffie-Hellman'},
    {'theme': 'Cryptography', 'question': 'What is a digital signature used for?', 'correct_answer': 'C', 'options': 'A) To encrypt data\nB) To compress data\nC) To verify the authenticity and integrity of a message\nD) To store passwords'},
    {'theme': 'Cryptography', 'question': 'What is a key feature of public-key cryptography?', 'correct_answer': 'D', 'options': 'A) Uses a single key for encryption and decryption\nB) Is faster than symmetric cryptography\nC) Does not require key exchange\nD) Uses two keys: public and private'},

    # Access Control and Authentication
    {'theme': 'Access Control and Authentication', 'question': 'What is multi-factor authentication?', 'correct_answer': 'C', 'options': 'A) Using multiple passwords\nB) Having multiple user accounts\nC) Using two or more different factors to verify identity\nD) Using biometrics only'},
    {'theme': 'Access Control and Authentication', 'question': 'What is the principle of least privilege?', 'correct_answer': 'A', 'options': 'A) Users should only have access necessary for their job\nB) Users should have full administrative access\nC) Users should share accounts\nD) Users should not use passwords'},
    {'theme': 'Access Control and Authentication', 'question': 'What is a biometric authentication method?', 'correct_answer': 'B', 'options': 'A) Using a password\nB) Fingerprint scanning\nC) Using a smart card\nD) Entering a PIN'},
    {'theme': 'Access Control and Authentication', 'question': 'What is single sign-on (SSO)?', 'correct_answer': 'C', 'options': 'A) Using multiple passwords for one system\nB) Logging in separately to each system\nC) Using one set of credentials to access multiple systems\nD) Disabling authentication'},
    {'theme': 'Access Control and Authentication', 'question': 'What is the purpose of a role-based access control (RBAC) system?', 'correct_answer': 'A', 'options': 'A) To assign permissions based on user roles\nB) To encrypt data\nC) To monitor network traffic\nD) To store user passwords'},

    # Network Security
    {'theme': 'Network Security', 'question': 'What is a firewall?', 'correct_answer': 'A', 'options': 'A) A system designed to prevent unauthorized access\nB) A type of malware\nC) A network monitoring tool\nD) A password manager'},
    {'theme': 'Network Security', 'question': 'What is a VPN used for?', 'correct_answer': 'C', 'options': 'A) To increase network speed\nB) To block all network traffic\nC) To create a secure connection over a public network\nD) To monitor user activity'},
    {'theme': 'Network Security', 'question': 'What is a DDoS attack?', 'correct_answer': 'B', 'options': 'A) A type of encryption attack\nB) An attempt to overwhelm a system with traffic to disrupt service\nC) A hardware failure\nD) A method to secure data'},
    {'theme': 'Network Security', 'question': 'What is the purpose of intrusion detection systems (IDS)?', 'correct_answer': 'A', 'options': 'A) To detect unauthorized access or attacks\nB) To encrypt network traffic\nC) To store user credentials\nD) To increase network bandwidth'},
    {'theme': 'Network Security', 'question': 'What is packet sniffing?', 'correct_answer': 'C', 'options': 'A) A method to compress data\nB) A way to secure network traffic\nC) Capturing and analyzing network packets\nD) Blocking network traffic'},

    # Malicious Software
    {'theme': 'Malicious Software', 'question': 'What is ransomware?', 'correct_answer': 'C', 'options': 'A) Software that steals data\nB) Software that monitors network traffic\nC) Malware that encrypts files and demands payment\nD) A network scanner'},
    {'theme': 'Malicious Software', 'question': 'What is a trojan horse?', 'correct_answer': 'B', 'options': 'A) A type of firewall\nB) Malware disguised as legitimate software\nC) A network protocol\nD) A secure encryption method'},
    {'theme': 'Malicious Software', 'question': 'What is a worm in the context of malware?', 'correct_answer': 'A', 'options': 'A) Malware that spreads without user interaction\nB) Malware that requires a host file\nC) Malware that encrypts data\nD) Malware that monitors user activity'},
    {'theme': 'Malicious Software', 'question': 'What is spyware?', 'correct_answer': 'C', 'options': 'A) Software that protects against viruses\nB) Software that encrypts data\nC) Malware that secretly collects user information\nD) Software that blocks network traffic'},
    {'theme': 'Malicious Software', 'question': 'What is the primary purpose of antivirus software?', 'correct_answer': 'A', 'options': 'A) To detect and remove malware\nB) To encrypt data\nC) To monitor network traffic\nD) To manage user passwords'},

    # Operating System Security
    {'theme': 'Operating System Security', 'question': 'What is a privilege escalation attack?', 'correct_answer': 'C', 'options': 'A) An attack to encrypt data\nB) An attack to monitor network traffic\nC) An attack to gain unauthorized higher-level access\nD) An attack to disable firewalls'},
    {'theme': 'Operating System Security', 'question': 'What is the purpose of a security patch?', 'correct_answer': 'A', 'options': 'A) To fix vulnerabilities in software\nB) To increase system performance\nC) To encrypt user data\nD) To monitor user activity'},
    {'theme': 'Operating System Security', 'question': 'What is a sandbox in OS security?', 'correct_answer': 'B', 'options': 'A) A type of malware\nB) An isolated environment to run untrusted programs\nC) A network monitoring tool\nD) A password manager'},
    {'theme': 'Operating System Security', 'question': 'What is the purpose of user account control (UAC) in Windows?', 'correct_answer': 'C', 'options': 'A) To encrypt data\nB) To monitor network traffic\nC) To prevent unauthorized changes to the system\nD) To disable antivirus software'},
    {'theme': 'Operating System Security', 'question': 'What is a rootkit?', 'correct_answer': 'A', 'options': 'A) Malware that hides its presence on a system\nB) A type of firewall\nC) A network protocol\nD) A secure encryption method'},

    # Database Protection
    {'theme': 'Database Protection', 'question': 'What is SQL injection?', 'correct_answer': 'C', 'options': 'A) A type of encryption\nB) A network monitoring tool\nC) An attack that exploits database vulnerabilities\nD) A password manager'},
    {'theme': 'Database Protection', 'question': 'What is the purpose of database encryption?', 'correct_answer': 'A', 'options': 'A) To protect data confidentiality\nB) To increase database performance\nC) To monitor database activity\nD) To manage user accounts'},
    {'theme': 'Database Protection', 'question': 'What is a database audit trail?', 'correct_answer': 'B', 'options': 'A) A type of malware\nB) A record of database activities for monitoring\nC) A network protocol\nD) A secure encryption method'},
    {'theme': 'Database Protection', 'question': 'What is the purpose of input validation in database security?', 'correct_answer': 'C', 'options': 'A) To encrypt data\nB) To increase database performance\nC) To prevent SQL injection attacks\nD) To manage user accounts'},
    {'theme': 'Database Protection', 'question': 'What is a database backup used for?', 'correct_answer': 'A', 'options': 'A) To recover data after loss or corruption\nB) To encrypt data\nC) To monitor database activity\nD) To increase database performance'},

    # Security in Cloud
    {'theme': 'Security in Cloud', 'question': 'What is a key security concern in cloud computing?', 'correct_answer': 'C', 'options': 'A) Increasing system performance\nB) Reducing hardware costs\nC) Data breaches due to shared resources\nD) Developing new software'},
    {'theme': 'Security in Cloud', 'question': 'What is the purpose of cloud access security brokers (CASB)?', 'correct_answer': 'A', 'options': 'A) To enforce security policies between cloud services and users\nB) To increase cloud storage capacity\nC) To monitor network traffic\nD) To develop new cloud applications'},
    {'theme': 'Security in Cloud', 'question': 'What is a benefit of using encryption in cloud storage?', 'correct_answer': 'B', 'options': 'A) Increasing storage capacity\nB) Protecting data confidentiality\nC) Reducing cloud costs\nD) Improving cloud performance'},
    {'theme': 'Security in Cloud', 'question': 'What is a shared responsibility model in cloud security?', 'correct_answer': 'C', 'options': 'A) The cloud provider is responsible for all security\nB) The user is responsible for all security\nC) Security responsibilities are split between provider and user\nD) Security is not required in the cloud'},
    {'theme': 'Security in Cloud', 'question': 'What is a common cloud security threat?', 'correct_answer': 'A', 'options': 'A) Data breaches\nB) Increasing storage capacity\nC) Reducing cloud costs\nD) Improving cloud performance'},

    # Security Operations
    {'theme': 'Security Operations', 'question': 'What is the purpose of a security operations center (SOC)?', 'correct_answer': 'C', 'options': 'A) To develop new software\nB) To increase system performance\nC) To monitor and respond to security incidents\nD) To manage user accounts'},
    {'theme': 'Security Operations', 'question': 'What is incident response?', 'correct_answer': 'A', 'options': 'A) The process of handling security breaches\nB) The process of encrypting data\nC) The process of monitoring network traffic\nD) The process of developing new software'},
    {'theme': 'Security Operations', 'question': 'What is the purpose of security information and event management (SIEM)?', 'correct_answer': 'B', 'options': 'A) To encrypt data\nB) To collect and analyze security events\nC) To increase system performance\nD) To manage user accounts'},
    {'theme': 'Security Operations', 'question': 'What is a security audit?', 'correct_answer': 'C', 'options': 'A) A type of malware\nB) A network protocol\nC) A review of security controls and practices\nD) A secure encryption method'},
    {'theme': 'Security Operations', 'question': 'What is the purpose of penetration testing?', 'correct_answer': 'A', 'options': 'A) To identify vulnerabilities by simulating attacks\nB) To encrypt data\nC) To increase system performance\nD) To manage user accounts'},

    # Security Governance
    {'theme': 'Security Governance', 'question': 'What is security governance?', 'correct_answer': 'C', 'options': 'A) A type of malware\nB) A network protocol\nC) The framework for managing security risks and policies\nD) A secure encryption method'},
    {'theme': 'Security Governance', 'question': 'What is the purpose of a security policy?', 'correct_answer': 'A', 'options': 'A) To define rules and procedures for security\nB) To encrypt data\nC) To increase system performance\nD) To manage user accounts'},
    {'theme': 'Security Governance', 'question': 'What is compliance in security governance?', 'correct_answer': 'B', 'options': 'A) A type of malware\nB) Adherence to laws, regulations, and standards\nC) A network protocol\nD) A secure encryption method'},
    {'theme': 'Security Governance', 'question': 'What is the role of a chief information security officer (CISO)?', 'correct_answer': 'C', 'options': 'A) To develop new software\nB) To increase system performance\nC) To oversee an organization’s security strategy\nD) To manage user accounts'},
    {'theme': 'Security Governance', 'question': 'What is risk assessment in security governance?', 'correct_answer': 'A', 'options': 'A) Identifying and evaluating security risks\nB) Encrypting data\nC) Increasing system performance\nD) Managing user accounts'}
]

def populate_sample_data():
    conn = sqlite3.connect('first_bot.db')
    c = conn.cursor()
    for q in SAMPLE_QUESTIONS:
        c.execute("SELECT COUNT(*) FROM questions WHERE question = ?", (q['question'],))
        if c.fetchone()[0] == 0:
            c.execute("INSERT INTO questions (theme, question, correct_answer, options) VALUES (?, ?, ?, ?)",
                      (q['theme'], q['question'], q['correct_answer'], q['options']))
    conn.commit()
    conn.close()

# Foydalanuvchi holatlari
user_data = {}

# Asosiy menyu klaviaturasini yaratish
def get_main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_quiz = types.KeyboardButton('Quiz')
    btn_stats = types.KeyboardButton('Statistika')
    btn_info = types.KeyboardButton('Ma’lumot')
    markup.add(btn_quiz, btn_stats, btn_info)
    return markup

# Mavzu tanlash klaviaturasini yaratish
def get_theme_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for i in range(0, len(THEMES), 2):
        if i + 1 < len(THEMES):
            markup.row(types.KeyboardButton(THEMES[i]), types.KeyboardButton(THEMES[i + 1]))
        else:
            markup.add(types.KeyboardButton(THEMES[i]))
    markup.add(types.KeyboardButton('Asosiy menyuga qaytish'))
    return markup

# Savoldan keyingi klaviatura
def get_post_question_menu(selected_theme):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn_continue = types.KeyboardButton(f'{selected_theme} bilan davom etish')
    btn_change_theme = types.KeyboardButton('Mavzuni o‘zgartirish')
    btn_main_menu = types.KeyboardButton('Asosiy menyuga qaytish')
    markup.add(btn_continue, btn_change_theme)
    markup.add(btn_main_menu)
    return markup

# Javob klaviaturasini yaratish
def get_answer_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(types.KeyboardButton('A'), types.KeyboardButton('B'),
               types.KeyboardButton('C'), types.KeyboardButton('D'))
    return markup

# Bot buyruqlari
@bot.message_handler(commands=['start'])
def start(message):
    user = message.from_user
    welcome_message = f"Salom, {user.first_name}! 👋\n\n" \
                      "Bu axborot xavfsizligi bo‘yicha viktorina botidir. Quyidagi tugmalar yordamida:\n" \
                      "- Viktorinani boshlang\n" \
                      "- Statistikangizni ko‘ring\n" \
                      "- Xavfsizlik haqida ma’lumot oling"
    bot.reply_to(message, welcome_message, reply_markup=get_main_menu())

@bot.message_handler(func=lambda message: message.text == 'Quiz')
def quiz(message):
    user_id = message.from_user.id
    user_data[user_id] = {'state': 'SELECTING_THEME'}
    bot.reply_to(message, "Viktorina uchun mavzu tanlang:", reply_markup=get_theme_menu())

@bot.message_handler(func=lambda message: message.from_user.id in user_data and
                                          user_data[message.from_user.id].get('state') == 'SELECTING_THEME')
def select_theme(message):
    user_id = message.from_user.id
    selected_theme = message.text

    if selected_theme == 'Asosiy menyuga qaytish':
        user_data.pop(user_id, None)
        bot.reply_to(message, "Asosiy menyuga qaytish.", reply_markup=get_main_menu())
        return

    if selected_theme not in THEMES:
        bot.reply_to(message, "Iltimos, quyidagi tugmalar orqali to‘g‘ri mavzu tanlang:", reply_markup=get_theme_menu())
        return

    conn = sqlite3.connect('Security_Quizz/first_bot.db')
    c = conn.cursor()
    c.execute("SELECT * FROM questions WHERE theme = ? ORDER BY RANDOM() LIMIT 1", (selected_theme,))
    question = c.fetchone()
    conn.close()

    if question:
        user_data[user_id] = {'current_question': question, 'state': 'QUESTION', 'theme': selected_theme}
        question_text = f"Mavzu: {selected_theme}\n\nSavol: {question[1]}\n\n{question[3]}"
        bot.reply_to(message, question_text, reply_markup=get_answer_keyboard(), parse_mode='Markdown')
    else:
        bot.reply_to(message, f"'{selected_theme}' mavzusi uchun savollar mavjud emas. Iltimos, boshqa mavzu tanlang:", reply_markup=get_theme_menu())

@bot.message_handler(func=lambda message: message.from_user.id in user_data and
                                          user_data[message.from_user.id].get('state') == 'QUESTION')
def check_answer(message):
    user_id = message.from_user.id
    user_answer = message.text.upper()

    if user_id not in user_data or 'current_question' not in user_data[user_id]:
        bot.reply_to(message, "Iltimos, avval 'Quiz' tugmasini bosib viktorinani boshlang", reply_markup=get_main_menu())
        return

    question = user_data[user_id]['current_question']
    selected_theme = user_data[user_id]['theme']
    correct_answer = question[2]

    conn = sqlite3.connect('Security_Quizz/first_bot.db')
    c = conn.cursor()
    c.execute("SELECT * FROM user_scores WHERE user_id = ?", (user_id,))
    user_score = c.fetchone()

    is_correct = user_answer == correct_answer
    if user_score:
        new_score = user_score[1] + 1 if is_correct else user_score[1]
        new_total = user_score[2] + 1
        c.execute("UPDATE user_scores SET score = ?, total_questions = ? WHERE user_id = ?",
                  (new_score, new_total, user_id))
    else:
        c.execute("INSERT INTO user_scores (user_id, score, total_questions) VALUES (?, ?, ?)",
                  (user_id, 1 if is_correct else 0, 1))

    conn.commit()

    # Keyingi savolni olish
    c.execute("SELECT * FROM questions WHERE theme = ? ORDER BY RANDOM() LIMIT 1", (selected_theme,))
    next_question = c.fetchone()
    conn.close()

    # Javob natijasini ko‘rsatish
    response = f"Sizning javobingiz: {user_answer}\n"
    response += "✅ To‘g‘ri!" if is_correct else f"❌ Noto‘g‘ri! To‘g‘ri javob: {correct_answer}"

    # Keyingi savol bo‘lsa, uni ko‘rsatish
    if next_question:
        user_data[user_id] = {'current_question': next_question, 'state': 'QUESTION', 'theme': selected_theme}
        response += f"\n\nKeyingi savol:\nMavzu: {selected_theme}\n\nSavol: {next_question[1]}\n\n{next_question[3]}"
        bot.reply_to(message, response, reply_markup=get_answer_keyboard(), parse_mode='Markdown')
    else:
        response += f"\n\n'{selected_theme}' mavzusida boshqa savollar yo‘q. Iltimos, boshqa mavzu tanlang yoki menyuga qayting."
        user_data[user_id] = {'state': 'SELECTING_THEME'}
        bot.reply_to(message, response, reply_markup=get_theme_menu())

@bot.message_handler(func=lambda message: message.text.startswith(THEMES) and 'bilan davom etish' in message.text)
def continue_quiz(message):
    user_id = message.from_user.id
    selected_theme = message.text.replace(' bilan davom etish', '')

    if selected_theme not in THEMES:
        bot.reply_to(message, "Noto‘g‘ri mavzu. Iltimos, menyudan mavzu tanlang.", reply_markup=get_theme_menu())
        return

    conn = sqlite3.connect('Security_Quizz/first_bot.db')
    c = conn.cursor()
    c.execute("SELECT * FROM questions WHERE theme = ? ORDER BY RANDOM() LIMIT 1", (selected_theme,))
    question = c.fetchone()
    conn.close()

    if question:
        user_data[user_id] = {'current_question': question, 'state': 'QUESTION', 'theme': selected_theme}
        question_text = f"Mavzu: {selected_theme}\n\nSavol: {question[2]}\n\n{question[4]}"
        bot.reply_to(message, question_text, reply_markup=get_answer_keyboard(), parse_mode='Markdown')
    else:
        bot.reply_to(message, f"'{selected_theme}' mavzusi uchun boshqa savollar yo‘q. Iltimos, boshqa mavzu tanlang:", reply_markup=get_theme_menu())

@bot.message_handler(func=lambda message: message.text == 'Mavzuni o‘zgartirish')
def change_theme(message):
    user_id = message.from_user.id
    user_data[user_id] = {'state': 'SELECTING_THEME'}
    bot.reply_to(message, "Yangi viktorina mavzusini tanlang:", reply_markup=get_theme_menu())

@bot.message_handler(func=lambda message: message.text == 'Asosiy menyuga qaytish')
def back_to_main_menu(message):
    user_id = message.from_user.id
    user_data.pop(user_id, None)
    bot.reply_to(message, "Asosiy menyuga qaytish.", reply_markup=get_main_menu())

@bot.message_handler(func=lambda message: message.text == 'Statistika')
def stats(message):
    user_id = message.from_user.id
    conn = sqlite3.connect('Security_Quizz/first_bot.db')
    c = conn.cursor()
    c.execute("SELECT * FROM user_scores WHERE user_id = ?", (user_id,))
    user_score = c.fetchone()
    conn.close()

    if user_score:
        accuracy = (user_score[1] / user_score[2]) * 100 if user_score[2] > 0 else 0
        stats_text = f"Sizning statistikangiz:\n" \
                     f"To‘g‘ri javoblar: {user_score[1]}\n" \
                     f"Umumiy savollar: {user_score[2]}\n" \
                     f"Aniqlik: {accuracy:.2f}%"
    else:
        stats_text = "Siz hali hech qanday savolga javob bermadingiz. 'Quiz' tugmasini bosib viktorinani boshlang!"

    bot.reply_to(message, stats_text, reply_markup=get_main_menu())

@bot.message_handler(func=lambda message: message.text == 'Ma’lumot')
def info(message):
    info_text = "Axborot xavfsizligi tahdidlariga umumiy nuqtai nazar:\n\n" \
                "1. Zararli dasturlar: Tizimlarga zarar yetkazish uchun mo‘ljallangan dasturlar\n" \
                "2. Fishing: Maxfiy ma’lumotlarni olish uchun soxta urinishlar\n" \
                "3. DDoS hujumlari: Tizimlarni trafik bilan to‘ldirib xizmatni to‘xtatish\n" \
                "4. SQL injeksiyasi: Ma’lumotlar bazasi zaifliklariga qaratilgan hujumlar\n" \
                "5. Ijtimoiy muhandislik: Odamlarning psixologik manipulyatsiyasi\n\n" \
                "Bu tahdidlar haqidagi bilimlaringizni sinash uchun 'Quiz' tugmasini bosing!"
    bot.reply_to(message, info_text, reply_markup=get_main_menu())

def main():
    init_db()
    populate_sample_data()
    print("Bot ishlayapti...")
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")

if __name__ == '__main__':
    main()