import telebot
from telebot import types

# Bot token
API_TOKEN = '8032404481:AAEiIwEkrfTvYw5QPLL4ToQ8PFsKDFF9YCM'
bot = telebot.TeleBot(API_TOKEN)

# Topics and questions dataset in english
topics_eng = {

    "Basic Concepts": {
        "theory": "Fundamentals of Information Protection*\n\n"
                  "Information protection is a critical discipline focused on safeguarding sensitive data from unauthorized access, misuse, or harm. "
                  "This text explores five essential concepts—*protected information*, *information protection*, *information protection effectiveness*, "
                  "*information protection systems*, and *information protection means*—to provide a solid foundation for understanding information security principles.\n\n"

                  "*1. Protected Information*\n"
                  "Protected information encompasses data that belongs to an entity, such as a government, organization, group of individuals, or a single person, "
                  "and requires safeguarding as mandated by legal regulations or the owner’s specific requirements. This type of information often includes sensitive "
                  "or confidential data, such as personal details, proprietary business records, or classified documents, which must be secured to prevent unauthorized disclosure or use.\n"
                  "_Example_: A corporation’s database containing employee social security numbers is protected information, owned by the company and safeguarded under privacy laws.\n\n"

                  "*2. Information Protection*\n"
                  "Information protection refers to the activities undertaken to prevent the unauthorized disclosure of sensitive data and to shield it from unauthorized "
                  "access or deliberate harmful actions. These activities involve implementing security measures, such as encryption, access restrictions, and monitoring systems, "
                  "to ensure that data remains confidential, unaltered, and accessible only to authorized individuals.\n"
                  "_Example_: A university deploys antivirus software and conducts regular security training for staff to prevent cyberattacks on student records, demonstrating information protection.\n\n"

                  "*3. Information Protection Effectiveness*\n"
                  "Information protection effectiveness evaluates how well security measures achieve their intended objectives. It measures the extent to which protection efforts "
                  "succeed in preventing data breaches, maintaining data integrity, and meeting legal or organizational security goals. This concept helps assess the performance "
                  "and reliability of implemented safeguards.\n"
                  "_Example_: If an organization aims to block all phishing attempts and its email filtering system stops 99% of such emails, the high effectiveness shows alignment with its security objectives.\n\n"

                  "*4. Information Protection System*\n"
                  "An information protection system is a coordinated framework that integrates bodies (e.g., security departments), performers (e.g., IT specialists), protection equipment "
                  "(e.g., software and hardware), and protected objects (e.g., networks or databases). This system operates according to rules and standards outlined in legal, "
                  "organizational, or regulatory documents, ensuring a structured approach to data security.\n"
                  "_Example_: A government agency’s protection system includes its cybersecurity team, intrusion detection software, and compliance policies to secure sensitive public records.\n\n"

                  "*5. Information Protection Means*\n"
                  "Information protection means are the tools, substances, or materials—such as technical, software, or hardware-software solutions—designed or utilized to secure data. "
                  "These include items like encryption programs, firewalls, secure storage devices, or physical security measures, which serve as the practical components for executing protection strategies.\n"
                  "_Example_: A laptop with built-in encryption software used to store confidential research data is an information protection means.\n\n"

                  "*Key Takeaways*\n"
                  "- *Protected Information*: Data owned by an entity that must be secured per legal or owner requirements.\n"
                  "- *Information Protection*: Activities to prevent data leaks and defend against unauthorized or harmful actions.\n"
                  "- *Information Protection Effectiveness*: The degree to which security measures meet their goals.\n"
                  "- *Information Protection System*: A structured combination of people, tools, and processes governed by regulations.\n"
                  "- *Information Protection Means*: Tools or materials used to implement security measures.\n\n"

                  "By mastering these concepts, you’ll gain a clear understanding of the principles underpinning information security, enabling you to apply them in various contexts, "
                  "from personal data protection to organizational cybersecurity.",
        "questions": [
            {
                "question": "1. Define the concept of protected information",
                "options": {
                    "a": "A set of bodies and/or performers, the information protection equipment they use, as well as protected information objects, organized and operating according to rules and norms established by relevant documents in the field of information protection",
                    "b": "The degree of compliance of information protection results with the goal of information protection",
                    "c": "Activities aimed at preventing the leakage of protected information, unauthorized, and intentional impacts on protected information",
                    "d": "Technical, software, or hardware-software means, substances, and/or materials intended or used for information protection",
                    "e": "Information that is subject to ownership and must be protected in accordance with the requirements of legal documents or requirements established by the information owner (state, legal entity, group of individuals, or an individual)"
                },
                "correct": "e"
            },
            {
                "question": "2. Define the concept of information protection",
                "options": {
                    "a": "Activities aimed at preventing the leakage of protected information, unauthorized, and intentional impacts on protected information",
                    "b": "Information that is subject to ownership and must be protected in accordance with the requirements of legal documents or requirements established by the information owner (state, legal entity, group of individuals, or an individual)",
                    "c": "The degree of compliance of information protection results with the set goal",
                    "d": "A set of bodies and/or performers, the information protection equipment they use, as well as protected objects, organized and operating according to rules established by relevant legal, organizational, and regulatory documents in the field of information protection",
                    "e": "Technical, software means, substances, and/or materials intended or used for information protection"
                },
                "correct": "a"
            },
            {
                "question": "3. Define the concept of information protection effectiveness",
                "options": {
                    "a": "Activities aimed at preventing the leakage of protected information, unauthorized, and intentional impacts on protected information",
                    "b": "Information that is subject to ownership and must be protected in accordance with the requirements of legal documents or requirements established by the information owner (state, legal entity, group of individuals, or an individual)",
                    "c": "The degree of compliance of information protection results with the set goal",
                    "d": "A set of bodies and/or performers, the information protection equipment they use, as well as protected objects, organized and operating according to rules established by relevant legal, organizational, and regulatory documents in the field of information protection",
                    "e": "Technical, software means, substances, and/or materials intended or used for information protection"
                },
                "correct": "c"
            },
            {
                "question": "4. Define the concept of an information protection system",
                "options": {
                    "a": "Activities aimed at preventing the leakage of protected information, unauthorized, and intentional impacts on protected information",
                    "b": "Information that is subject to ownership and must be protected in accordance with the requirements of legal documents or requirements established by the information owner (state, legal entity, group of individuals, or an individual)",
                    "c": "The degree of compliance of information protection results with the set goal",
                    "d": "A set of bodies and/or performers, the information protection equipment they use, as well as protected objects, organized and operating according to rules established by relevant legal, organizational, and regulatory documents in the field of information protection",
                    "e": "Technical, software means, substances, and/or materials intended or used for information protection"
                },
                "correct": "d"
            },
            {
                "question": "5. Define the concept of information protection means",
                "options": {
                    "a": "Activities aimed at preventing the leakage of protected information, unauthorized, and intentional impacts on protected information",
                    "b": "Information that is subject to ownership and must be protected in accordance with the requirements of legal documents or requirements established by the information owner (state, legal entity, group of individuals, or an individual)",
                    "c": "The degree of compliance of information protection results with the set goal",
                    "d": "A set of bodies and/or performers, the information protection equipment they use, as well as protected objects, organized and operating according to rules established by relevant legal, organizational, and regulatory documents in the field of information protection",
                    "e": "Technical, software means, substances, and/or materials intended or used for information protection"
                },
                "correct": "e"
            }]
    },
    "Threats and the Intruder Model in Information Security": {
        "theory": "*Understanding Threats and the Intruder Model in Information Security*\n\n"
                  "Information security is centered on protecting data from threats and ensuring its core properties are maintained. This text explores key concepts related to security threats, vulnerabilities, threat sources, attacks, the CIA triad, Parker's Hexad, and the intruder model, providing a foundation for understanding how information systems are safeguarded.\n\n"
                  "*1. Security Threat to an Object*\n"
                  "A security threat to an object is any potential event or action that could directly or indirectly compromise the security of that object, such as a system, network, or data. Threats can arise from various sources and exploit weaknesses, potentially leading to harm like data loss, unauthorized access, or system disruption.\n"
                  "_Example_: A phishing email attempting to steal user credentials poses a security threat to an organization’s information system.\n\n"
                  "*2. Object’s Vulnerability*\n"
                  "A vulnerability is an inherent weakness or flaw within an object—such as a system, application, or process—that can be exploited to breach information security. These weaknesses may stem from design flaws, misconfigurations, or lack of updates, making the object susceptible to threats.\n"
                  "_Example_: An unpatched software bug in a company’s server is a vulnerability that hackers could exploit to gain unauthorized access.\n\n"
                  "*3. Threat Source*\n"
                  "A threat source is any entity or phenomenon capable of carrying out a security threat. These can be human-driven (anthropogenic), technology-related (technogenic), or environmental (natural), encompassing a wide range of potential origins, from malicious actors to equipment failures or natural disasters.\n"
                  "_Example_: A disgruntled employee attempting to leak sensitive data is a human-driven threat source.\n\n"
                  "*4. Attack*\n"
                  "An attack is the realization of a security threat, where a threat source exploits existing vulnerabilities to cause harm to an object. It represents the actual consequences of a threat being carried out, such as data theft, system compromise, or service disruption.\n"
                  "_Example_: A hacker using a vulnerability in a website to steal customer data is executing an attack.\n\n"
                  "*5. Information Confidentiality*\n"
                  "Information confidentiality is the property that ensures data is accessible only to authenticated and authorized system users. It prevents unauthorized individuals from accessing sensitive information, maintaining privacy and trust.\n"
                  "_Example_: Encrypting patient records in a hospital database ensures that only authorized doctors can view them, preserving confidentiality.\n\n"
                  "*6. Information Integrity*\n"
                  "Information integrity refers to the property of data remaining accurate and unchanged in its intended meaning, despite random or intentional distortions or destructive actions. It ensures that information is reliable and trustworthy.\n"
                  "_Example_: Using checksums to verify that a downloaded file has not been altered ensures its integrity.\n\n"
                  "*7. Information Availability*\n"
                  "Information availability is the property that ensures data is accessible to authenticated and authorized users when needed. It prevents disruptions that could block legitimate access, such as denial-of-service attacks.\n"
                  "_Example_: A cloud service provider maintaining redundant servers to keep data accessible during outages supports availability.\n\n"
                  "*8. Threats Against Confidentiality, Integrity, and Availability*\n"
                  "*Threats to Confidentiality*: Actions like information theft, where unauthorized parties gain access to sensitive data, violate confidentiality.\n"
                  "_Example_: Intercepting unencrypted emails to steal trade secrets is a confidentiality threat.\n"
                  "*Threats to Integrity*: Information modification, where data is altered maliciously or accidentally, compromises integrity.\n"
                  "_Example_: Changing financial records to falsify transactions threatens integrity.\n"
                  "*Threats to Availability*: Information destruction, such as deleting critical files or launching a ransomware attack, prevents authorized users from accessing data, undermining availability.\n\n"
                  "*9. Classification of Threat Sources*\n"
                  "Threat sources are generally classified into three categories:\n"
                  "- *Anthropogenic*: Human-related sources, such as malicious insiders or external attackers.\n"
                  "- *Technogenic*: Technology-related sources, like hardware failures or software glitches.\n"
                  "- *Natural*: Environmental sources, including disasters like floods or earthquakes.\n"
                  "_Example_: A hacker (anthropogenic), a server crash (technogenic), or a tsunami (natural) are distinct threat sources.\n\n"
                  "*10. Classification of Vulnerabilities*\n"
                  "Vulnerabilities are typically classified as:\n"
                  "- *Objective*: Inherent flaws independent of human intent, like software bugs.\n"
                  "- *Subjective*: Weaknesses caused by human error, such as weak passwords.\n"
                  "- *Random*: Unpredictable flaws, like unexpected hardware failures.\n"
                  "_Example_: A coding error (objective), a poorly configured firewall (subjective), or a sudden disk failure (random) are different vulnerability types.\n\n"
                  "*11. Types of Threat Sources*\n"
                  "- *Anthropogenic Threats*: Caused by human actions, such as a drunk driver crashing into a data center’s power supply.\n"
                  "- *Technogenic Threats*: Stemming from technological failures, like an aircraft engine failure disrupting communication systems.\n"
                  "- *Natural Threats*: Arising from environmental events, such as a tsunami flooding a server facility.\n"
                  "- *External Anthropogenic Threats*: Originating outside the organization, like technical staff from a telecommunications provider attempting unauthorized access.\n"
                  "- *Internal Anthropogenic Threats*: Arising within the organization, such as a cleaner accessing restricted systems.\n"
                  "- *External Technogenic Threats*: External technology-related issues, like transport-related disruptions affecting data center operations.\n"
                  "- *Internal Technogenic Threats*: Internal technology failures, such as low-quality technical tools used within the facility.\n\n"
                  "*12. Information Security Intruder Model*\n"
                  "The information security intruder model is a framework that outlines assumptions about potential intruders, including their qualifications, motivations, and the technical or material resources they might use to breach security. It helps organizations anticipate and prepare for threats from various actors.\n"
                  "_Example_: A model might assume a highly skilled hacker with advanced tools targeting a bank’s financial systems.\n\n"
                  "*13. Types of Intruders*\n"
                  "- *Internal Intruders*: Individuals within the organization, such as internal security service employees or system operators, who may misuse their access.\n"
                  "- *External Intruders*: Entities outside the organization, like employees of oversight bodies or competitors, attempting to breach security.\n"
                  "- *Non-Internal Intruders*: External actors, such as representatives of competing organizations, who lack legitimate access.\n"
                  "- *Non-External Intruders*: Internal personnel, like users or operators, who are not considered external threats.\n"
                  "_Example_: An internal security employee (internal intruder) versus a rival company’s agent (external intruder).\n\n"
                  "*14. The CIA Triad and Parker’s Hexad*\n"
                  "*CIA Triad*: The foundational framework of information security, consisting of:\n"
                  "- *Confidentiality*: Ensuring data is only accessible to authorized users.\n"
                  "- *Integrity*: Maintaining data accuracy and trustworthiness.\n"
                  "- *Availability*: Ensuring data is accessible to authorized users when needed.\n\n"
                  "*Parker’s Hexad*: Extends the CIA triad by adding three concepts:\n"
                  "- *Authenticity*: Verifying the identity of users or data sources.\n"
                  "- *Possession*: Ensuring control over data to prevent unauthorized use.\n"
                  "- *Utility*: Ensuring data remains useful for its intended purpose.\n"
                  "_Example_: A secure email system ensures confidentiality (only intended recipients read it), integrity (content is unaltered), availability (accessible to recipients), authenticity (sender is verified), possession (data stays under recipient control), and utility (data remains usable)",
        "questions": [
            {
                "question": "6. Define the concept of a security threat to an object",
                "options": {
                    "a": "A possible impact on an object that directly or indirectly may harm its security",
                    "b": "Inherent reasons within an object that lead to a breach of information security",
                    "c": "Potential anthropogenic, technogenic, or natural carriers of security threats",
                    "d": "Possible consequences of threat realization through interaction with a threat source via existing vulnerabilities"
                },
                "correct": "a"
            },
            {
                "question": "7. Define the concept of an object's vulnerability",
                "options": {
                    "a": "A possible impact on an object that directly or indirectly may harm its security",
                    "b": "Inherent reasons within an object that lead to a breach of information security",
                    "c": "Potential anthropogenic, technogenic, or natural carriers of security threats",
                    "d": "Possible consequences of threat realization through interaction with a threat source via existing vulnerabilities"
                },
                "correct": "b"
            },
            {
                "question": "8. Define the concept of a threat source",
                "options": {
                    "a": "A possible impact on an object that directly or indirectly may harm its security",
                    "b": "Inherent reasons within an object that lead to a breach of information security",
                    "c": "Potential anthropogenic, technogenic, or natural carriers of security threats",
                    "d": "Possible consequences of threat realization through interaction with a threat source via existing vulnerabilities"
                },
                "correct": "c"
            },
            {
                "question": "9. Define the concept of an attack",
                "options": {
                    "a": "Possible consequences of threat realization through interaction with a threat source via existing vulnerabilities",
                    "b": "Technical, software means, substances, and/or materials intended or used for information protection",
                    "c": "Potential anthropogenic, technogenic, or natural carriers of security threats",
                    "d": "Inherent reasons within an object that lead to a breach of information security",
                    "e": "A possible impact on an object that directly or indirectly may harm its security"
                },
                "correct": "a"
            },
            {
                "question": "10. What is information confidentiality?",
                "options": {
                    "a": "The property of information to remain unchanged in a semantic sense during system operation under conditions of random or intentional distortions or destructive impacts",
                    "b": "The property of information to be known only to authenticated legitimate system subjects",
                    "c": "The property of information to be accessible to authenticated legitimate system subjects",
                    "d": "The property of information to indicate possible consequences of threat realization through interaction with a threat source via existing vulnerabilities",
                    "e": "The property of information to provide a set of assumptions about one or more potential information security intruders, their qualifications, and their technical and material means"
                },
                "correct": "b"
            },
            {
                "question": "11. What is information integrity?",
                "options": {
                    "a": "The property of information to remain unchanged in a semantic sense during system operation under conditions of random or intentional distortions or destructive impacts",
                    "b": "The property of information to be known only to authenticated legitimate system subjects",
                    "c": "The property of information to be accessible to authenticated legitimate system subjects",
                    "d": "The property of information to indicate possible consequences of threat realization through interaction with a threat source via existing vulnerabilities",
                    "e": "The property of information to provide a set of assumptions about one or more potential information security intruders, their qualifications, and their technical and material means"
                },
                "correct": "a"
            },
            {
                "question": "12. What is information availability?",
                "options": {
                    "a": "The property of information to indicate possible consequences of threat realization through interaction with a threat source via existing vulnerabilities",
                    "b": "The property of information to remain unchanged in a semantic sense during system operation under conditions of random or intentional distortions or destructive impacts",
                    "c": "The property of information to be accessible to authenticated legitimate system subjects",
                    "d": "The property of information to provide a set of assumptions about one or more potential information security intruders, their qualifications, and their technical and material means",
                    "e": "The property of information to be known only to authenticated legitimate system subjects"
                },
                "correct": "c"
            },
            {
                "question": "13. Which of the listed threats pertains to threats against information confidentiality?",
                "options": {
                    "a": "Information theft",
                    "b": "Information destruction",
                    "c": "Information modification"
                },
                "correct": "a"
            },
            {
                "question": "14. Which of the listed threats pertains to threats against information availability?",
                "options": {
                    "a": "Information theft",
                    "b": "Information destruction",
                    "c": "Information modification"
                },
                "correct": "b"
            },
            {
                "question": "15. Which of the listed threats pertains to threats against information integrity?",
                "options": {
                    "a": "Information theft",
                    "b": "Information destruction",
                    "c": "Information modification"
                },
                "correct": "c"
            },
            {
                "question": "16. Which classification of threat sources is generally recognized?",
                "options": {
                    "a": "Anthropogenic, technogenic, natural",
                    "b": "Objective, subjective, random",
                    "c": "Local, global, extraterrestrial"
                },
                "correct": "a"
            },
            {
                "question": "17. Which classification of vulnerabilities of a protected object is generally recognized?",
                "options": {
                    "a": "Objective, subjective, random",
                    "b": "Anthropogenic, technogenic, natural",
                    "c": "External and internal"
                },
                "correct": "a"
            },
            {
                "question": "18. Which of the listed threat sources pertains to anthropogenic threats?",
                "options": {
                    "a": "Impact of electromagnetic fields from power lines",
                    "b": "Relay contact sticking",
                    "c": "Flood",
                    "d": "Tornado",
                    "e": "Drunk driver"
                },
                "correct": "e"
            },
            {
                "question": "19. Which of the listed threat sources pertains to technogenic threats?",
                "options": {
                    "a": "Aircraft engine failure",
                    "b": "Tsunami",
                    "c": "Drunk driver",
                    "d": "Flood",
                    "e": "Tornado"
                },
                "correct": "a"
            },
            {
                "question": "20. Which of the listed threat sources pertains to natural threats?",
                "options": {
                    "a": "Tsunami",
                    "b": "Aircraft engine failure",
                    "c": "Drunk driver",
                    "d": "Impact of electromagnetic fields from power lines",
                    "e": "Relay contact sticking"
                },
                "correct": "a"
            },
            {
                "question": "21. Which of the listed threat sources is an external anthropogenic threat?",
                "options": {
                    "a": "Technical staff of telecommunications service providers",
                    "b": "Communication means",
                    "c": "Cleaner",
                    "d": "Transport",
                    "e": "Tornado"
                },
                "correct": "a"
            },
            {
                "question": "22. Which of the listed threat sources is an internal anthropogenic threat?",
                "options": {
                    "a": "Communication means",
                    "b": "Force majeure circumstances",
                    "c": "Criminal structures",
                    "d": "Cleaner",
                    "e": "Low-quality software tools for information processing used at the facility"
                },
                "correct": "d"
            },
            {
                "question": "23. Which of the listed threat sources is an external technogenic threat?",
                "options": {
                    "a": "Transport",
                    "b": "Cleaner",
                    "c": "Tornado",
                    "d": "Criminal structures",
                    "e": "Flood"
                },
                "correct": "a"
            },
            {
                "question": "24. Which of the listed threat sources is an internal technogenic threat?",
                "options": {
                    "a": "Low-quality technical information processing tools used at the facility",
                    "b": "Cleaner",
                    "c": "Tornado",
                    "d": "Criminal structures",
                    "e": "Flood"
                },
                "correct": "a"
            },
            {
                "question": "25. What is the information security intruder model?",
                "options": {
                    "a": "A set of assumptions about one or more potential information security intruders, their qualifications, and their technical and material means",
                    "b": "A possible impact on an object that directly or indirectly may harm its security",
                    "c": "Inherent reasons within an object that lead to a breach of information security",
                    "d": "Potential anthropogenic, technogenic, or natural carriers of security threats",
                    "e": "Possible consequences of threat realization through interaction with a threat source via existing vulnerabilities"
                },
                "correct": "a"
            },
            {
                "question": "26. Which of the listed types of information security intruders pertains to internal intruders?",
                "options": {
                    "a": "Internal security service employees",
                    "b": "Representatives of competing organizations",
                    "c": "Employees of departmental oversight and management bodies"
                },
                "correct": "a"
            },
            {
                "question": "27. Which of the listed types of information security intruders does not pertain to internal intruders?",
                "options": {
                    "a": "Representatives of competing organizations",
                    "b": "Internal security service employees",
                    "c": "Cleaner"
                },
                "correct": "a"
            },
            {
                "question": "28. Which of the listed types of information security intruders pertains to external intruders?",
                "options": {
                    "a": "Employees of departmental oversight and management bodies",
                    "b": "Internal security service employees",
                    "c": "Cleaner"
                },
                "correct": "a"
            },
            {
                "question": "29. Which of the listed types of information security intruders does not pertain to external intruders?",
                "options": {
                    "a": "Users and operators of the information system",
                    "b": "Representatives of competing organizations",
                    "c": "Invited visitors",
                    "d": "Observers outside the protected area",
                    "e": "Violators of the access control regime"
                },
                "correct": "a"
            },
            {
                "question": "30. Which three concepts form the CIA triad?",
                "options": {
                    "a": "Confidentiality, availability, and integrity",
                    "b": "Peace, labor, May",
                    "c": "Yesterday, today, tomorrow",
                    "d": "Authenticity, possession, and utility"
                },
                "correct": "a"
            },
            {
                "question": "31. Which three concepts complement the CIA triad to form Parker's Hexad?",
                "options": {
                    "a": "Authenticity, possession, and utility",
                    "b": "Confidentiality, availability, and integrity",
                    "c": "Peace, labor, May",
                    "d": "Creation, editing, deletion"
                },
                "correct": "a"
            }]
    },
    "Software Protection Methods": {
        "theory": "*Overview of Software and Information Protection Methods*\n\n"
                  "Information protection methods are critical for securing software and data within computing systems. This text explores various software protection methods, "
                  "including self-protection, methods using system tools, and those involving information requests, as well as key abbreviations and distinctions between hardware, "
                  "software, and organizational protection methods.\n\n"

                  "*1. Self-Protection Methods in Software*\n"
                  "Self-protection methods refer to strategies where the software system itself is designed or configured to maintain its own security without relying heavily on "
                  "external tools or user intervention. These methods often involve internal processes, such as regular system maintenance, updates, or automated security checks, "
                  "to ensure the software remains secure and operational.\n"
                  "_Example_: A software application that automatically checks for and applies security patches during maintenance cycles is using a self-protection method.\n\n"

                  "*2. Protection Methods Using Tools Within a Computing System*\n"
                  "Some software protection methods leverage specialized hardware or tools integrated within the computing system to enhance security. These methods rely on dedicated "
                  "hardware components, such as trusted platform modules (TPMs) or hardware security modules (HSMs), to perform security functions like encryption or secure key storage.\n"
                  "_Example_: A server using a dedicated hardware encryption module to protect sensitive data transactions is employing a protection method within the computing system.\n\n"

                  "*3. Protection Methods Involving Information Requests*\n"
                  "Certain software protection methods require users to provide specific information to gain access, ensuring that only authorized individuals can interact with the system. "
                  "These methods commonly involve authentication mechanisms, such as passwords, biometrics, or security tokens, to verify user identity before granting access.\n"
                  "_Example_: A banking application requiring a user to enter a password and a one-time code sent to their phone is using a protection method involving information requests.\n\n"

                  "*4. Abbreviation: НСД (Unauthorized Access)*\n"
                  "In information protection systems, the abbreviation *НСД* stands for unauthorized access. This term refers to any attempt to gain entry to a system, network, or data "
                  "without proper authorization, posing a significant security threat that protection methods aim to prevent.\n"
                  "_Example_: A hacker attempting to log into a corporate network without credentials is engaging in НСД (unauthorized access).\n\n"

                  "*5. Abbreviation: НСК (Unauthorized Copying)*\n"
                  "The abbreviation *НСК* in information protection systems denotes unauthorized copying. This refers to the act of duplicating protected data or software without permission, "
                  "often leading to intellectual property theft or data breaches.\n"
                  "_Example_: An employee copying proprietary software code to a personal device without approval is committing НСК (unauthorized copying).\n\n"

                  "*6. Hardware-Based Information Protection Methods*\n"
                  "Hardware-based protection methods involve physical devices or components designed to secure information. These methods often focus on shielding systems from external interference, "
                  "such as electromagnetic eavesdropping, or preventing physical tampering with hardware.\n"
                  "_Example_: Installing electromagnetic shielding around a data center to block signal interception is a hardware-based protection method.\n\n"

                  "*7. Software-Based Information Protection Methods*\n"
                  "Software-based protection methods rely on programs or algorithms to secure data and systems. These methods include techniques like file encryption, antivirus software, or "
                  "intrusion detection systems, which operate within the software environment to protect information.\n"
                  "_Example_: Encrypting sensitive documents with a software tool to prevent unauthorized access is a software-based protection method.\n\n"

                  "*8. Organizational Information Protection Methods*\n"
                  "Organizational protection methods involve policies, procedures, and administrative controls to safeguard information. These methods focus on managing human behavior and system access "
                  "through rules, training, and access control regimes to minimize security risks.\n"
                  "_Example_: Implementing a policy that restricts physical and digital access to sensitive areas of an office to authorized personnel only is an organizational protection method.",
        "questions": [
            {
                "question": "32. Which software protection method pertains to self-protection methods?",
                "options": {
                    "a": "Maintenance organization",
                    "b": "Use of passwords",
                    "c": "Use of specialized hardware"
                },
                "correct": "a"
            },
            {
                "question": "33. Which software protection method pertains to methods using protection tools within a computing system?",
                "options": {
                    "a": "Maintenance organization",
                    "b": "Use of passwords",
                    "c": "Use of specialized hardware"
                },
                "correct": "c"
            },
            {
                "question": "34. Which software protection method pertains to methods involving information requests?",
                "options": {
                    "a": "Maintenance organization",
                    "b": "Use of passwords",
                    "c": "Use of specialized hardware"
                },
                "correct": "b"
            },
            {
                "question": "35. What does the abbreviation НСД stand for in information protection systems?",
                "options": {
                    "a": "Unauthorized access",
                    "b": "Shielding",
                    "c": "Unauthorized copying",
                    "d": "File encryption"
                },
                "correct": "a"
            },
            {
                "question": "36. What does the abbreviation НСК stand for in information protection systems?",
                "options": {
                    "a": "Unauthorized access",
                    "b": "Shielding",
                    "c": "Unauthorized copying",
                    "d": "File encryption"
                },
                "correct": "c"
            },
            {
                "question": "37. Which of the following pertains to hardware-based information protection methods?",
                "options": {
                    "a": "Access control regime organization",
                    "b": "Shielding",
                    "d": "File encryption"
                },
                "correct": "b"
            },
            {
                "question": "38. Which of the following pertains to software-based information protection methods?",
                "options": {
                    "a": "Shielding",
                    "b": "File encryption",
                    "c": "Acoustic masking tools using white noise generators",
                    "d": "Access control regime organization",
                    "e": "Protection of a personal computer case from tampering"
                },
                "correct": "b"
            },
            {
                "question": "39. Which of the following pertains to organizational information protection methods?",
                "options": {
                    "a": "Shielding",
                    "b": "File encryption",
                    "c": "Acoustic masking tools using white noise generators",
                    "d": "Access control regime organization",
                    "e": "Protection of a personal computer case from tampering"
                },
                "correct": "d"
            }]
    },
    "Cryptographic Methods for Protecting Software and Databases": {
        "theory": "*Fundamentals of Cryptographic Methods for Information Security*\n\n"
                  "Cryptographic methods are essential for protecting software and databases by transforming information to prevent unauthorized access, ensure authenticity, and maintain integrity. "
                  "This text explores cryptographic transformations, symmetric and asymmetric cryptosystems, specific algorithms, cipher types, and their applications.\n\n"

                  "*1. Cryptographic Information Transformation*\n"
                  "Cryptographic information transformation alters data to secure it from unauthorized access or tampering. A key method is *steganography*, which hides a message within another medium.\n"
                  "_Example_: Hiding a message in the pixels of a photo is steganography.\n\n"

                  "*2. Non-Cryptographic Transformations*\n"
                  "Methods like copying, compression, or translation are not cryptographic since they don’t protect or obscure access.\n"
                  "_Example_: Copying a database file to a backup drive.\n\n"

                  "*3. Symmetric Cryptosystems*\n"
                  "Use the same key for encryption and decryption. Fast and efficient for bulk data.\n"
                  "_Example_: DES encrypts employee records with a shared secret key.\n\n"

                  "*4. Asymmetric Cryptosystems*\n"
                  "Use a public key for encryption and a private key for decryption. Suitable for secure communication.\n"
                  "_Example_: An email encrypted with a public ElGamal key, decrypted by the private key.\n\n"

                  "*5. Digital Signatures*\n"
                  "Verify message authenticity and integrity. RSA is a widely used algorithm.\n"
                  "_Example_: A developer signs an update with an RSA digital signature.\n\n"

                  "*6. Classical Symmetric Cryptosystems*\n"
                  "Use simple substitution/transposition methods. Examples: Caesar cipher, Alberti’s disk, Vigenère table.\n"
                  "_Example_: Caesar cipher shifts letters by 3 positions.\n\n"

                  "*7. Types of Ciphers*\n"
                  "- *Monoalphabetic Cipher*: Fixed substitution (e.g., Caesar, scytale).\n"
                  "- *Polyalphabetic Cipher*: Multiple substitutions (e.g., Alberti’s disk, Vigenère table).\n"
                  "- *Electromechanical Cipher Machine*: Uses moving parts (e.g., Enigma).\n"
                  "- *Software/Hardware Mathematical Cipher*: Uses algorithms and secret keys (e.g., AES).\n"
                  "- *Asymmetric Cryptosystems*: Public/private key pairs (e.g., RSA).\n\n"
                  "_Examples_: Scytale (monoalphabetic), Alberti’s disk (polyalphabetic), Enigma (electromechanical), AES (software/hardware), RSA (asymmetric).\n\n"

                  "*8. Algorithm Classifications*\n"
                  "- *Caesar & Vigenère*: Symmetric cryptosystems with shared keys.\n"
                  "- *DES*: Symmetric with secret key.\n"
                  "- *RSA*: Asymmetric with public/private keys.\n"
                  "_Example_: DES encrypts a database; RSA secures communication.\n\n"

                  "*9. Algorithm Applications*\n"
                  "- *ElGamal*: Used for digital signatures.\n"
                  "- *Diffie-Hellman*: Secure key exchange over insecure channels.\n"
                  "_Example_: ElGamal signs a digital contract; Diffie-Hellman establishes a shared key.\n\n"

                  "*10. DES Specifications*\n"
                  "- *Encryption Cycles*: 16 rounds.\n"
                  "- *Key Length*: 64 bits (56-bit effective).\n"
                  "- *Block Size*: 64-bit data blocks.\n"
                  "_Example_: DES encrypts 64-bit blocks of financial data in 16 cycles with a 64-bit key.",
        "questions": [
            {
                "question": "40. Which of the following is a method of cryptographic information transformation?",
                "options": {
                    "a": "Steganography",
                    "b": "Stenography",
                    "c": "Printing",
                    "d": "Translation to another language"
                },
                "correct": "a"
            },
            {
                "question": "41. Which of the following is not a method of cryptographic information transformation?",
                "options": {
                    "a": "Encryption",
                    "b": "Encoding",
                    "c": "Compression",
                    "d": "Copying",
                    "e": "Steganography"
                },
                "correct": "d"
            },
            {
                "question": "42. Which of the listed algorithms pertains to symmetric cryptosystems?",
                "options": {
                    "a": "DES",
                    "b": "RSA",
                    "c": "ElGamal"
                },
                "correct": "a"
            },
            {
                "question": "43. Which of the listed algorithms pertains to asymmetric cryptosystems?",
                "options": {
                    "a": "Diffie-Hellman",
                    "b": "ElGamal",
                    "c": "DES",
                    "d": "MD5",
                    "e": "GOST 28147-89"
                },
                "correct": "b"
            },
            {
                "question": "44. Which of the listed algorithms is used for creating a digital signature?",
                "options": {
                    "a": "RSA",
                    "b": "DES",
                    "c": "GOST 28147-89"
                },
                "correct": "a"
            },
            {
                "question": "45. Which of the listed algorithms does not pertain to classical symmetric cryptosystems?",
                "options": {
                    "a": "GOST 28147-89",
                    "b": "Caesar cipher",
                    "c": "Encryption using Alberti's disk",
                    "d": "Encryption using the Vigenère table"
                },
                "correct": "a"
            },
            {
                "question": "46. What type of cipher is encryption using a scytale?",
                "options": {
                    "a": "Polyalphabetic cipher",
                    "b": "Monoalphabetic cipher",
                    "c": "Using an electromechanical cipher machine",
                    "d": "Using a software or hardware mathematical cipher with a secret or closed key",
                    "e": "Using a software or hardware mathematical cipher with an open key"
                },
                "correct": "b"
            },
            {
                "question": "47. What type of cipher is encryption using the Caesar cipher?",
                "options": {
                    "a": "Using an electromechanical cipher machine",
                    "b": "Monoalphabetic cipher",
                    "c": "Using a software or hardware mathematical cipher with a secret or closed key",
                    "d": "Polyalphabetic cipher",
                    "e": "Using a software or hardware mathematical cipher with an open key"
                },
                "correct": "b"
            },
            {
                "question": "48. What type of cipher is encryption using Alberti's disk?",
                "options": {
                    "a": "Polyalphabetic cipher",
                    "b": "Using a software or hardware mathematical cipher with a secret or closed key",
                    "c": "Using an electromechanical cipher machine",
                    "d": "Monoalphabetic cipher",
                    "e": "Using a software or hardware mathematical cipher with an open key"
                },
                "correct": "a"
            },
            {
                "question": "49. What type of cipher is encryption using the Vigenère table?",
                "options": {
                    "a": "Monoalphabetic cipher",
                    "b": "Polyalphabetic cipher",
                    "c": "Using an electromechanical cipher machine",
                    "d": "Using a software or hardware mathematical cipher with a secret or closed key",
                    "e": "Using a software or hardware mathematical cipher with an open key"
                },
                "correct": "b"
            },
            {
                "question": "50. What type of cipher is encryption using the Enigma machine?",
                "options": {
                    "a": "Using an electromechanical cipher machine",
                    "b": "Monoalphabetic cipher",
                    "c": "Polyalphabetic cipher",
                    "d": "Using a software or hardware mathematical cipher with a secret or closed key",
                    "e": "Using a software or hardware mathematical cipher with an open key"
                },
                "correct": "a"
            },
            {
                "question": "51. What type of cipher is encryption using Triple DES?",
                "options": {
                    "a": "Using a software or hardware mathematical cipher with a secret or closed key",
                    "b": "Using a software or hardware mathematical cipher with an open key",
                    "c": "Monoalphabetic cipher",
                    "d": "Polyalphabetic cipher",
                    "e": "Using an electromechanical cipher machine"
                },
                "correct": "a"
            },
            {
                "question": "52. What type of cipher is encryption using AES?",
                "options": {
                    "a": "Using a software or hardware mathematical cipher with a secret or closed key",
                    "b": "Using a software or hardware mathematical cipher with an open key",
                    "c": "Monoalphabetic cipher",
                    "d": "Polyalphabetic cipher",
                    "e": "Using an electromechanical cipher machine"
                },
                "correct": "a"
            },
            {
                "question": "53. What type of cipher is encryption using RSA?",
                "options": {
                    "a": "Key distribution algorithms",
                    "b": "Hash functions",
                    "c": "Cryptosystems with a closed key",
                    "d": "Asymmetric cryptosystems",
                    "e": "Symmetric cryptosystems"
                },
                "correct": "d"
            },
            {
                "question": "54. What class of encryption algorithms does the Caesar cipher belong to?",
                "options": {
                    "a": "Symmetric cryptosystems",
                    "b": "Cryptosystems with an open key",
                    "c": "Hash functions",
                    "d": "Asymmetric cryptosystems",
                    "e": "Key distribution algorithms"
                },
                "correct": "a"
            },
            {
                "question": "55. What class of encryption algorithms does encryption with the Vigenère table belong to?",
                "options": {
                    "a": "Symmetric cryptosystems",
                    "b": "Cryptosystems with an open key",
                    "c": "Hash functions",
                    "d": "Asymmetric cryptosystems",
                    "e": "Key distribution algorithms"
                },
                "correct": "a"
            },
            {
                "question": "56. What class of encryption algorithms does the DES algorithm belong to?",
                "options": {
                    "a": "Cryptosystems with an open key",
                    "b": "Hash functions",
                    "c": "Asymmetric cryptosystems",
                    "d": "Cryptosystems with a closed key",
                    "e": "Key distribution algorithms"
                },
                "correct": "d"
            },
            {
                "question": "57. What class of encryption algorithms does the RSA algorithm belong to?",
                "options": {
                    "a": "Asymmetric cryptosystems",
                    "b": "Cryptosystems with a closed key",
                    "c": "Key distribution algorithms",
                    "d": "Symmetric cryptosystems",
                    "e": "Hash functions"
                },
                "correct": "a"
            },
            {
                "question": "58. What is the ElGamal algorithm used for?",
                "options": {
                    "a": "For creating digital signatures",
                    "b": "For secure key transmission",
                    "c": "For symmetric encryption"
                },
                "correct": "a"
            },
            {
                "question": "59. What is the Diffie-Hellman algorithm used for?",
                "options": {
                    "a": "For secure key transmission",
                    "b": "For creating digital signatures",
                    "c": "For symmetric encryption"
                },
                "correct": "a"
            },
            {
                "question": "60. How many encryption cycles does the DES algorithm contain?",
                "options": {
                    "a": "16",
                    "b": "32",
                    "c": "64",
                    "d": "2",
                    "e": "8"
                },
                "correct": "a"
            },
            {
                "question": "61. What is the key length of DES?",
                "options": {
                    "a": "64 bits",
                    "b": "128 bits",
                    "c": "256 bits",
                    "d": "1024 bits",
                    "e": "32 bits"
                },
                "correct": "a"
            },
            {
                "question": "62. What is the length of the information block encrypted by the DES algorithm?",
                "options": {
                    "a": "64 bits",
                    "b": "128 bits",
                    "c": "256 bits",
                    "d": "1024 bits",
                    "e": "32 bits"
                },
                "correct": "a"
            }
        ]
    },
    "Authentication Means for Software and Database Protection": {
        "theory": "*Authentication Methods for Securing Software and Databases*\n\n"
                  "Authentication is a cornerstone of information security, ensuring that only authorized users can access software systems and databases. "
                  "This text explores various authentication methods, including those based on known information, physical tokens, individual physical characteristics, "
                  "and biometric techniques, providing a clear understanding of how these methods protect sensitive data.\n\n"

                  "*1. Authentication Based on Conditional, Pre-Assigned Attributes*\n"
                  "Authentication methods based on conditional, pre-assigned attributes rely on information known only to the authorized user, such as a secret code or phrase. "
                  "These methods verify identity by checking whether the user can provide the correct pre-assigned data, making them simple yet effective for securing access.\n"
                  "_Example_: A user logging into a banking app by entering a password is authenticated using a pre-assigned attribute.\n\n"

                  "*2. Authentication Based on Physical Means*\n"
                  "Some authentication methods use physical devices that function similarly to a traditional key, granting access when presented. "
                  "These devices, often portable and secure, contain cryptographic or identification data that the system verifies to authenticate the user.\n"
                  "_Example_: A smart card inserted into a reader to unlock a secure workstation acts like a physical key for authentication.\n\n"

                  "*3. Authentication Based on Individual Characteristics*\n"
                  "Authentication methods based on individual characteristics leverage unique physical or behavioral traits that distinguish one person from another. "
                  "These traits are inherent to the user and difficult to replicate, providing a high level of security for verifying identity.\n"
                  "_Example_: A fingerprint scanner unlocking a smartphone uses the user’s unique fingerprint pattern to authenticate access.\n\n"

                  "*4. Biometric Authentication Means*\n"
                  "Biometric authentication methods rely on measurable biological or behavioral characteristics, such as physical features or patterns, to verify identity. "
                  "These methods are highly secure due to the uniqueness of biometric data, which is challenging to forge or steal.\n"
                  "_Example_: An iris scanner at a secure facility authenticates employees by analyzing the unique patterns in their eyes.\n\n"

                  "*5. Non-Biometric Authentication Means*\n"
                  "Not all authentication methods are biometric. Non-biometric methods include those based on knowledge (e.g., passwords), possession (e.g., physical tokens), "
                  "or other non-physiological mechanisms. These methods do not rely on the user’s biological or behavioral traits.\n"
                  "_Example_: Using a USB key with embedded cryptographic credentials to access a database is a non-biometric authentication method.",
        "questions": [
            {
                "question": "63. Which of the listed authentication means pertains to those based on conditional, pre-assigned attributes (information) known to the subject?",
                "options": {
                    "a": "Password-based means",
                    "b": "Smart card",
                    "c": "By fingerprint",
                    "d": "By iris",
                    "e": "Using a USB key"
                },
                "correct": "a"
            },
            {
                "question": "64. Which of the listed authentication means pertains to those based on physical means acting similarly to a physical key?",
                "options": {
                    "a": "Smart card",
                    "b": "Password-based means",
                    "c": "By fingerprint",
                    "d": "By iris",
                    "e": "By typing pattern"
                },
                "correct": "a"
            },
            {
                "question": "65. Which of the listed authentication means pertains to those based on individual characteristics of the subject, their physical data, allowing them to be distinguished from others?",
                "options": {
                    "a": "By fingerprint",
                    "b": "Smart card",
                    "c": "Password-based means",
                    "d": "Using a USB key",
                    "e": "PIN code"
                },
                "correct": "a"
            },
            {
                "question": "66. Which of the listed authentication means pertains to biometric means?",
                "options": {
                    "a": "By iris",
                    "b": "Smart card",
                    "c": "Password-based means",
                    "d": "Using a USB key",
                    "e": "PIN code"
                },
                "correct": "a"
            },
            {
                "question": "67. Which of the listed authentication means does not pertain to biometric means?",
                "options": {
                    "a": "Using a USB key",
                    "b": "By voice",
                    "c": "By fingerprint",
                    "d": "By iris",
                    "e": "By typing pattern"
                },
                "correct": "a"
            }
        ]
    },
    "Access Control Rules": {
        "theory": "*Principles of Access Control for Information Security*\n\n"
                  "Access control is a fundamental aspect of information security, ensuring that only authorized users can interact with protected resources, such as software, databases, or data elements. "
                  "This text explores key access control principles, including mandatory access control, discretionary access control, role-based access control, and access control based on access control lists, "
                  "providing a clear understanding of how these methods regulate access.\n\n"

                  "*1. Mandatory Access Control (MAC)*\n"
                  "Mandatory access control is a strict access control principle where each protected resource is assigned a unique label, such as a security classification or identifier. "
                  "Access to the resource is granted only to users who present a matching label in their request, which is typically issued by a system administrator or the resource’s owner. "
                  "This centralized approach enforces rigid security policies, often used in high-security environments.\n"
                  "_Example_: In a military database, a document labeled \"Top Secret\" can only be accessed by users with a \"Top Secret\" clearance label assigned by the security officer.\n\n"

                  "*2. Access Control Based on Access Control Lists (ACLs)*\n"
                  "This method involves creating a list for each protected data element that specifies which users or groups are granted access rights to that element. "
                  "The ACL defines permissions, such as read, write, or execute, for each listed user, allowing fine-grained control over access to resources.\n"
                  "_Example_: A shared folder on a company server has an ACL listing employees who can view or edit its contents, with specific permissions assigned to each.\n\n"

                  "*3. Role-Based Access Control (RBAC)*\n"
                  "RBAC assigns access rights based on roles within an organization, such as job positions or scopes of responsibility. Users are granted permissions according to their role, "
                  "which corresponds to predefined duties, simplifying access management in large organizations.\n"
                  "_Example_: In a hospital, a \"Doctor\" role grants access to patient records, while a \"Receptionist\" role is limited to scheduling data, based on job responsibilities.\n\n"

                  "*4. Discretionary Access Control (DAC)*\n"
                  "DAC allows the owner of a protected resource to determine who can access it and what permissions they have. This principle often uses an access matrix, where rows represent registered users, "
                  "columns represent protected data elements, and cells specify permissions (e.g., read or write). DAC offers flexibility but relies on the owner’s discretion.\n"
                  "_Example_: A project manager creates a document and uses an access matrix to grant read-only access to team members and full edit rights to a co-lead.",
        "questions": [
            {
                "question": "68. Identify the access control principle based on its description: Each protected element is assigned a unique personal label, after which access to this element will be granted only to the user who presents the element’s label in their request, which can be issued by the administrator or the element’s owner.",
                "options": {
                    "a": "Mandatory access control",
                    "b": "Discretionary access control",
                    "c": "Role-based access control",
                    "d": "Access control based on access control lists"
                },
                "correct": "a"
            },
            {
                "question": "69. Identify the access control principle based on its description: For each element of protected data, a list is compiled of all users who are granted access rights to the respective element.",
                "options": {
                    "a": "Mandatory access control",
                    "b": "Discretionary access control",
                    "c": "Role-based access control",
                    "d": "Access control based on access control lists"
                },
                "correct": "d"
            },
            {
                "question": "70. Identify the access control principle based on its description: Concepts such as 'position' and 'scope of job responsibilities' are used, which must correspond to the list of various positions existing in the organization.",
                "options": {
                    "a": "Mandatory access control",
                    "b": "Discretionary access control",
                    "c": "Role-based access control",
                    "d": "Access control based on access control lists"
                },
                "correct": "c"
            },
            {
                "question": "71. Identify the access control principle based on its description: The table rows contain identifiers of registered users, the columns contain identifiers of protected data elements, and the table cells contain permissions.",
                "options": {
                    "a": "Mandatory access control",
                    "b": "Discretionary access control",
                    "c": "Role-based access control",
                    "d": "Access control based on access control lists"
                },
                "correct": "b"
            }]
    },
    "Network Security": {
        "theory": "*Essentials of Network Security*\n\n"
                  "Network security is critical for protecting data and systems in interconnected environments. This text explores key concepts, including traffic filtering, firewalls, "
                  "proxy servers, network traffic monitoring, intrusion detection systems, and various types of malicious software, providing a foundation for understanding how to safeguard computer networks.\n\n"

                  "*1. Traffic Filtering*\n"
                  "Traffic filtering involves the processing of IP packets by network devices, such as routers or firewalls, to selectively discard certain packets or redirect their paths based on predefined rules. "
                  "This process helps control network traffic, block malicious content, and ensure efficient data flow.\n"
                  "_Example_: A router discards packets from an untrusted IP address to prevent unauthorized access to a company’s network.\n\n"

                  "*2. Firewall*\n"
                  "A firewall is a combination of software and hardware tools designed to protect one segment of a computer network from another by analyzing and filtering the traffic that passes between them. "
                  "Firewalls enforce security policies, blocking unauthorized access while allowing legitimate communication.\n"
                  "_Example_: A corporate firewall blocks incoming traffic from suspicious sources while permitting employees to access internal databases securely.\n\n"

                  "*3. Proxy Server*\n"
                  "A proxy server acts as an intermediary between clients on an internal (protected) network and servers on an external (potentially unsafe) network. It handles requests on behalf of clients, "
                  "enhancing security by masking internal network details and filtering harmful content.\n"
                  "_Example_: A proxy server in an office filters web requests, blocking malicious sites while allowing employees to browse approved external resources.\n\n"

                  "*4. Network Traffic Monitoring*\n"
                  "Network traffic monitoring is the continuous, automated process of observing specific traffic parameters to ensure compliance with service level agreements, support network planning, "
                  "and prevent issues like technical failures, threats, or malicious attacks. It provides insights into network performance and security.\n"
                  "_Example_: A network administrator uses monitoring tools to detect unusual traffic spikes, identifying a potential denial-of-service attack early.\n\n"

                  "*5. Intrusion Detection System*\n"
                  "An intrusion detection system (IDS) is a software or hardware tool that continuously monitors network traffic and user activities to prevent, detect, and log potential attacks. "
                  "It alerts administrators to suspicious behavior, aiding in rapid response to security threats.\n"
                  "_Example_: An IDS flags repeated failed login attempts on a server, alerting the security team to a possible brute-force attack.\n\n"

                  "*6. Trojan Program*\n"
                  "A Trojan program is malicious software that disguises itself as a legitimate or useful application but performs harmful actions, such as stealing data or compromising system security, once installed. "
                  "It relies on user interaction to infiltrate systems.\n"
                  "_Example_: A user downloads a seemingly harmless game that secretly logs their keystrokes to steal passwords, revealing it as a Trojan.\n\n"

                  "*7. Network Worm*\n"
                  "A network worm is a malicious program that independently spreads its copies across network nodes, both locally and globally, without requiring user intervention. It exploits vulnerabilities to propagate, "
                  "often causing widespread disruption.\n"
                  "_Example_: A worm infects a corporate network, automatically spreading to connected devices and consuming bandwidth, slowing down operations.\n\n"

                  "*8. Computer Virus*\n"
                  "A computer virus is a malicious software fragment that embeds itself in other files or programs, spreading when those files are executed. It can corrupt data, degrade system performance, "
                  "or perform unauthorized actions.\n"
                  "_Example_: A virus attached to an email attachment infects a user’s computer, corrupting critical files when the attachment is opened.\n\n"

                  "*9. Software Backdoor*\n"
                  "A software backdoor is a hidden feature or code embedded in software that, under specific conditions, activates undocumented functions, allowing unauthorized access or control. "
                  "It is often used by attackers to bypass security measures.\n"
                  "_Example_: A developer inserts a backdoor in an application, enabling remote access to the system when a specific command is entered.\n\n"

                  "*10. Botnet*\n"
                  "A botnet is a collection of network devices infected by malicious software that allows them to be controlled remotely by a central command center. Botnets perform automated tasks, "
                  "such as launching coordinated attacks or sending spam, without user awareness.\n"
                  "_Example_: A hacker uses a botnet of compromised devices to launch a distributed denial-of-service attack against a website, overwhelming its servers.",
        "questions": [
            {
                "question": "72. Define the concept of traffic filtering.",
                "options": {
                    "a": "Processing of IP packets by routers and firewalls, leading to the discarding of some packets or altering their route.",
                    "b": "A set of software and hardware tools that provide information protection for one part of a computer network from another by analyzing and filtering the traffic passing between them.",
                    "c": "A specific type of application that acts as an intermediary between the client and server parts of distributed network applications, assuming that clients belong to an internal (protected) network and servers to an external (potentially dangerous) network.",
                    "d": "A continuous process of instrumental automated monitoring of specific traffic parameters to verify compliance with service level agreements, network planning, and prevention of negative events such as technical failures, threats, and attacks by malicious actors.",
                    "e": "A software or hardware tool that continuously monitors network traffic and system subject activities to prevent, detect, and log attacks."
                },
                "correct": "a"
            },
            {
                "question": "73. Define the concept of a firewall.",
                "options": {
                    "a": "Processing of IP packets by routers and firewalls, leading to the discarding of some packets or altering their route.",
                    "b": "A set of software and hardware tools that provide information protection for one part of a computer network from another by analyzing and filtering the traffic passing between them.",
                    "c": "A specific type of application that acts as an intermediary between the client and server parts of distributed network applications, assuming that clients belong to an internal (protected) network and servers to an external (potentially dangerous) network.",
                    "d": "A continuous process of instrumental automated monitoring of specific traffic parameters to verify compliance with service level agreements, network planning, and prevention of negative events such as technical failures, threats, and attacks by malicious actors.",
                    "e": "A software or hardware tool that continuously monitors network traffic and system subject activities to prevent, detect, and log attacks."
                },
                "correct": "b"
            },
            {
                "question": "74. Define the concept of a proxy server.",
                "options": {
                    "a": "Processing of IP packets by routers and firewalls, leading to the discarding of some packets or altering their route.",
                    "b": "A set of software and hardware tools that provide information protection for one part of a computer network from another by analyzing and filtering the traffic passing between them.",
                    "c": "A specific type of application that acts as an intermediary between the client and server parts of distributed network applications, assuming that clients belong to an internal (protected) network and servers to an external (potentially dangerous) network.",
                    "d": "A continuous process of instrumental automated monitoring of specific traffic parameters to verify compliance with service level agreements, network planning, and prevention of negative events such as technical failures, threats, and attacks by malicious actors.",
                    "e": "A software or hardware tool that continuously monitors network traffic and system subject activities to prevent, detect, and log attacks."
                },
                "correct": "c"
            },
            {
                "question": "75. Define the concept of network traffic monitoring.",
                "options": {
                    "a": "Processing of IP packets by routers and firewalls, leading to the discarding of some packets or altering their route.",
                    "b": "A set of software and hardware tools that provide information protection for one part of a computer network from another by analyzing and filtering the traffic passing between them.",
                    "c": "A specific type of application that acts as an intermediary between the client and server parts of distributed network applications, assuming that clients belong to an internal (protected) network and servers to an external (potentially dangerous) network.",
                    "d": "A continuous process of instrumental automated monitoring of specific traffic parameters to verify compliance with service level agreements, network planning, and prevention of negative events such as technical failures, threats, and attacks by malicious actors.",
                    "e": "A software or hardware tool that continuously monitors network traffic and system subject activities to prevent, detect, and log attacks."
                },
                "correct": "d"
            },
            {
                "question": "76. Define the concept of an intrusion detection system.",
                "options": {
                    "a": "Processing of IP packets by routers and firewalls, leading to the discarding of some packets or altering their route.",
                    "b": "A set of software and hardware tools that provide information protection for one part of a computer network from another by analyzing and filtering the traffic passing between them.",
                    "c": "A specific type of application that acts as an intermediary between the client and server parts of distributed network applications, assuming that clients belong to an internal (protected) network and servers to an external (potentially dangerous) network.",
                    "d": "A continuous process of instrumental automated monitoring of specific traffic parameters to verify compliance with service level agreements, network planning, and prevention of negative events such as technical failures, threats, and attacks by malicious actors.",
                    "e": "A software or hardware tool that continuously monitors network traffic and system subject activities to prevent, detect, and log attacks."
                },
                "correct": "e"
            },
            {
                "question": "77. Define the concept of a Trojan program.",
                "options": {
                    "a": "A malicious software fragment that can be embedded in other files.",
                    "b": "A malicious program that causes harm to a system while masquerading as a useful application.",
                    "c": "A collection of network devices infiltrated by a program that performs automated actions based on commands from a remote control center.",
                    "d": "A program capable of independently spreading its copies among nodes within a local network and via global connections, moving from one computer to another without user involvement.",
                    "e": "An object embedded in software that, under certain conditions, initiates undocumented functions, enabling unauthorized impacts on information."
                },
                "correct": "b"
            },
            {
                "question": "78. Define the concept of a network worm.",
                "options": {
                    "a": "A program capable of independently spreading its copies among nodes within a local network and via global connections, moving from one computer to another without user involvement.",
                    "b": "A malicious software fragment that can be embedded in other files.",
                    "c": "An object embedded in software that, under certain conditions, initiates undocumented functions, enabling unauthorized impacts on information.",
                    "d": "A collection of network devices infiltrated by a program that performs automated actions based on commands from a remote control center."
                },
                "correct": "a"
            },
            {
                "question": "79. Define the concept of a computer virus.",
                "options": {
                    "a": "A program capable of independently spreading its copies among nodes within a local network and via global connections, moving from one computer to another without user involvement.",
                    "b": "A malicious software fragment that can be embedded in other files.",
                    "c": "An object embedded in software that, under certain conditions, initiates undocumented functions, enabling unauthorized impacts on information.",
                    "d": "A collection of network devices infiltrated by a program that performs automated actions based on commands from a remote control center."
                },
                "correct": "b"
            },
            {
                "question": "80. Define the concept of a software backdoor.",
                "options": {
                    "a": "A program capable of independently spreading its copies among nodes within a local network and via global connections, moving from one computer to another without user involvement.",
                    "b": "A malicious software fragment that can be embedded in other files.",
                    "c": "An object embedded in software that, under certain conditions, initiates undocumented functions, enabling unauthorized impacts on information.",
                    "d": "A collection of network devices infiltrated by a program that performs automated actions based on commands from a remote control center."
                },
                "correct": "c"
            },
            {
                "question": "81. Define the concept of a botnet.",
                "options": {
                    "a": "A program capable of independently spreading its copies among nodes within a local network and via global connections, moving from one computer to another without user involvement.",
                    "b": "A malicious software fragment that can be embedded in other files.",
                    "c": "An object embedded in software that, under certain conditions, initiates undocumented functions, enabling unauthorized impacts on information.",
                    "d": "A collection of network devices infiltrated by a program that performs automated actions based on commands from a remote control center."
                },
                "correct": "d"
            }
        ]
    }
}

# Topics and questions dataset in russian
topics_ru = {
    "Основные понятия": [
        {
            "question": "1. Дайте понятие защищаемой информации",
            "options": {
                "a": "Совокупность органов и (или) исполнителей, используемой ими техники защиты информации, а также объектов защиты информации, организованная и функционирующая по правилам и нормам, установленным соответствующими документами в области защиты информации",
                "b": "Степень соответствия результатов защиты информации цели защиты информации",
                "c": "Деятельность, направленная на предотвращение утечки защищаемой информации, несанкционированных и преднамеренных воздействий на защищаемую информацию",
                "d": "Техническое, программное, программно-техническое средство, вещество и (или) материал, предназначенные или используемые для защиты информации",
                "e": "Информация, являющаяся предметом собственности и подлежащая защите в соответствии с требованиями правовых документов или требованиями, устанавливаемыми собственником информации (государство, юридическое лицо, группа физических лиц или отдельное физическое лицо)"
            },
            "correct": "e"
        },
        {
            "question": "2. Дайте понятие защите информации",
            "options": {
                "a": "Деятельность, направленная на предотвращение утечки защищаемой информации, несанкционированных и преднамеренных воздействий на защищаемую информацию",
                "b": "Информация, являющаяся предметом собственности и подлежащая защите в соответствии с требованиями правовых документов или требованиями, устанавливаемыми собственником информации (государство, юридическое лицо, группа физических лиц или отдельное физическое лицо)",
                "c": "Степень соответствия результатов защиты информации поставленной цели",
                "d": "Совокупность органов и (или) исполнителей, используемой ими техники защиты информации, а также объектов защиты, организованная и функционирующая по правилам, установленным соответствующими правовыми, организационно-распорядительными и нормативными документами в области защиты информации",
                "e": "Техническое, программное средство, вещество и (или) материал, предназначенные или используемые для защиты информации"
            },
            "correct": "a"
        },
        {
            "question": "3. Дайте понятие эффективности защиты информации",
            "options": {
                "a": "Деятельность, направленная на предотвращение утечки защищаемой информации, несанкционированных и преднамеренных воздействий на защищаемую информацию",
                "b": "Информация, являющаяся предметом собственности и подлежащая защите в соответствии с требованиями правовых документов или требованиями, устанавливаемыми собственником информации (государство, юридическое лицо, группа физических лиц или отдельное физическое лицо)",
                "c": "Степень соответствия результатов защиты информации поставленной цели",
                "d": "Совокупность органов и (или) исполнителей, используемой ими техники защиты информации, а также объектов защиты, организованная и функционирующая по правилам, установленным соответствующими правовыми, организационно-распорядительными и нормативными документами в области защиты информации",
                "e": "Техническое, программное средство, вещество и (или) материал, предназначенные или используемые для защиты информации"
            },
            "correct": "c"
        },
        {
            "question": "4. Дайте понятие системы защиты информации",
            "options": {
                "a": "Деятельность, направленная на предотвращение утечки защищаемой информации, несанкционированных и преднамеренных воздействий на защищаемую информацию",
                "b": "Информация, являющаяся предметом собственности и подлежащая защите в соответствии с требованиями правовых документов или требованиями, устанавливаемыми собственником информации (государство, юридическое лицо, группа физических лиц или отдельное физическое лицо)",
                "c": "Степень соответствия результатов защиты информации поставленной цели",
                "d": "Совокупность органов и (или) исполнителей, используемой ими техники защиты информации, а также объектов защиты, организованная и функционирующая по правилам, установленным соответствующими правовыми, организационно-распорядительными и нормативными документами в области защиты информации",
                "e": "Техническое, программное средство, вещество и (или) материал, предназначенные или используемые для защиты информации"
            },
            "correct": "d"
        },
        {
            "question": "5. Дайте понятие средства защиты информации",
            "options": {
                "a": "Деятельность, направленная на предотвращение утечки защищаемой информации, несанкционированных и преднамеренных воздействий на защищаемую информацию",
                "b": "Информация, являющаяся предметом собственности и подлежащая защите в соответствии с требованиями правовых документов или требованиями, устанавливаемыми собственником информации (государство, юридическое лицо, группа физических лиц или отдельное физическое лицо)",
                "c": "Степень соответствия результатов защиты информации поставленной цели",
                "d": "Совокупность органов и (или) исполнителей, используемой ими техники защиты информации, а также объектов защиты, организованная и функционирующая по правилам, установленным соответствующими правовыми, организационно-распорядительными и нормативными документами в области защиты информации",
                "e": "Техническое, программное средство, вещество и (или) материал, предназначенные или используемые для защиты информации"
            },
            "correct": "e"
        }
    ],
    "Угрозы и модель нарушителя информационной безопасности": [
        {
            "question": "6. Дайте понятие угрозы безопасности объекта",
            "options": {
                "a": "Возможное воздействие на объект, которое прямо или косвенно может нанести ущерб его безопасности",
                "b": "Это присущие объекту причины, приводящие к нарушению безопасности информации на объекте",
                "c": "Это потенциальные антропогенные, техногенные или стихийные носители угрозы безопасности",
                "d": "Это возможные последствия реализации угрозы при взаимодействии источника угрозы через имеющиеся уязвимости"
            },
            "correct": "a"
        },
        {
            "question": "7. Дайте понятие уязвимости объекта",
            "options": {
                "a": "Возможное воздействие на объект, которое прямо или косвенно может нанести ущерб его безопасности",
                "b": "Это присущие объекту причины, приводящие к нарушению безопасности информации на объекте",
                "c": "Это потенциальные антропогенные, техногенные или стихийные носители угрозы безопасности",
                "d": "Это возможные последствия реализации угрозы при взаимодействии источника угрозы через имеющиеся уязвимости"
            },
            "correct": "b"
        },
        {
            "question": "8. Дайте понятие источника угрозы",
            "options": {
                "a": "Возможное воздействие на объект, которое прямо или косвенно может нанести ущерб его безопасности",
                "b": "Это присущие объекту причины, приводящие к нарушению безопасности информации на объекте",
                "c": "Это потенциальные антропогенные, техногенные или стихийные носители угрозы безопасности",
                "d": "Это возможные последствия реализации угрозы при взаимодействии источника угрозы через имеющиеся уязвимости"
            },
            "correct": "c"
        },
        {
            "question": "9. Дайте понятие атаки",
            "options": {
                "a": "Это возможные последствия реализации угрозы при взаимодействии источника угрозы через имеющиеся уязвимости",
                "b": "Техническое, программное средство, вещество и (или) материал, предназначенные или используемые для защиты информации",
                "c": "Это потенциальные антропогенные, техногенные или стихийные носители угрозы безопасности",
                "d": "Это присущие объекту причины, приводящие к нарушению безопасности информации на объекте",
                "e": "Возможное воздействие на объект, которое прямо или косвенно может нанести ущерб его безопасности"
            },
            "correct": "a"
        },
        {
            "question": "10. Что такое конфиденциальность информации?",
            "options": {
                "a": "Это свойство информации быть неизменной в семантическом смысле при функционировании системы в условиях случайных или преднамеренных искажений или разрушающих воздействий",
                "b": "Это свойство информации быть известной только аутентифицированным законным субъектам системы",
                "c": "Это свойство информации быть доступной для аутентифицированных законных субъектов системы",
                "d": "Это свойство информации указывать возможные последствия реализации угрозы при взаимодействии источника угрозы через имеющиеся уязвимости",
                "e": "Это свойство информации предоставлять набор предположений об одном или нескольких возможных нарушителях информационной безопасности, их квалификации, их технических и материальных средствах"
            },
            "correct": "b"
        },
        {
            "question": "11. Что такое целостность информации?",
            "options": {
                "a": "Это свойство информации быть неизменной в семантическом смысле при функционировании системы в условиях случайных или преднамеренных искажений или разрушающих воздействий",
                "b": "Это свойство информации быть известной только аутентифицированным законным субъектам системы",
                "c": "Это свойство информации быть доступной для аутентифицированных законных субъектов системы",
                "d": "Это свойство информации указывать возможные последствия реализации угрозы при взаимодействии источника угрозы через имеющиеся уязвимости",
                "e": "Это свойство информации предоставлять набор предположений об одном или нескольких возможных нарушителях информационной безопасности, их квалификации, их технических и материальных средствах"
            },
            "correct": "a"
        },
        {
            "question": "12. Что такое доступность информации?",
            "options": {
                "a": "Это свойство информации указывать возможные последствия реализации угрозы при взаимодействии источника угрозы через имеющиеся уязвимости",
                "b": "Это свойство информации быть неизменной в семантическом смысле при функционировании системы в условиях случайных или преднамеренных искажений или разрушающих воздействий",
                "c": "Это свойство информации быть доступной для аутентифицированных законных субъектов системы",
                "d": "Это свойство информации предоставлять набор предположений об одном или нескольких возможных нарушителях информационной безопасности, их квалификации, их технических и материальных средствах",
                "e": "Это свойство информации быть известной только аутентифицированным законным субъектам системы"
            },
            "correct": "c"
        },
        {
            "question": "13. Какая из перечисленных угроз относится к угрозам против конфиденциальности информации?",
            "options": {
                "a": "Хищение информации",
                "b": "Уничтожение информации",
                "c": "Модификация информации"
            },
            "correct": "a"
        },
        {
            "question": "14. Какая из перечисленных угроз относится к угрозам против доступности информации?",
            "options": {
                "a": "Хищение информации",
                "b": "Уничтожение информации",
                "c": "Модификация информации"
            },
            "correct": "b"
        },
        {
            "question": "15. Какая из перечисленных угроз относится к угрозам против целостности информации?",
            "options": {
                "a": "Хищение информации",
                "b": "Уничтожение информации",
                "c": "Модификация информации"
            },
            "correct": "c"
        },
        {
            "question": "16. Какая классификация источников угроз является общепризнанной?",
            "options": {
                "a": "Антропогенные, техногенные, стихийные",
                "b": "Объективные, субъективные, случайные",
                "c": "Локальные, глобальные, внеземные"
            },
            "correct": "a"
        },
        {
            "question": "17. Какая классификация уязвимостей объекта защиты является общепризнанной?",
            "options": {
                "a": "Объективные, субъективные, случайные",
                "b": "Антропогенные, техногенные, стихийные",
                "c": "Внешние и внутренние"
            },
            "correct": "a"
        },
        {
            "question": "18. Какой из приведенных источников угроз относится к антропогенным?",
            "options": {
                "a": "Воздействие электромагнитного поля ЛЭП",
                "b": "Залипание контактов реле",
                "c": "Наводнение",
                "d": "Торнадо",
                "e": "Пьяный водитель"
            },
            "correct": "e"
        },
        {
            "question": "19. Какой из приведенных источников угроз относится к техногенным?",
            "options": {
                "a": "Отказ двигателя самолета",
                "b": "Цунами",
                "c": "Пьяный водитель",
                "d": "Наводнение",
                "e": "Торнадо"
            },
            "correct": "a"
        },
        {
            "question": "20. Какой из приведенных источников угроз относится к стихийным?",
            "options": {
                "a": "Цунами",
                "b": "Отказ двигателя самолета",
                "c": "Пьяный водитель",
                "d": "Воздействие электромагнитного поля ЛЭП",
                "e": "Залипание контактов реле"
            },
            "correct": "a"
        },
        {
            "question": "21. Какой из перечисленных источников угроз является антропогенным внешним?",
            "options": {
                "a": "Технический персонал поставщиков телекоммуникационных услуг",
                "b": "Средства связи",
                "c": "Уборщица",
                "d": "Транспорт",
                "e": "Торнадо"
            },
            "correct": "a"
        },
        {
            "question": "22. Какой из перечисленных источников угроз является антропогенным внутренним?",
            "options": {
                "a": "Средства связи",
                "b": "Форс-мажорные обстоятельства",
                "c": "Криминальные структуры",
                "d": "Уборщица",
                "e": "Некачественные программные средства обработки информации, используемые на объекте"
            },
            "correct": "d"
        },
        {
            "question": "23. Какой из перечисленных источников угроз является техногенным внешним?",
            "options": {
                "a": "Транспорт",
                "b": "Уборщица",
                "c": "Торнадо",
                "d": "Криминальные структуры",
                "e": "Наводнение"
            },
            "correct": "a"
        },
        {
            "question": "24. Какой из перечисленных источников угроз является техногенным внутренним?",
            "options": {
                "a": "Некачественные технические средства обработки информации, используемые на объекте",
                "b": "Уборщица",
                "c": "Торнадо",
                "d": "Криминальные структуры",
                "e": "Наводнение"
            },
            "correct": "a"
        },
        {
            "question": "25. Что такое модель нарушителя информационной безопасности?",
            "options": {
                "a": "Это набор предположений об одном или нескольких возможных нарушителях информационной безопасности, их квалификации, их технических и материальных средствах",
                "b": "Возможное воздействие на объект, которое прямо или косвенно может нанести ущерб его безопасности",
                "c": "Это присущие объекту причины, приводящие к нарушению безопасности информации на объекте",
                "d": "Это потенциальные антропогенные, техногенные или стихийные носители угрозы безопасности",
                "e": "Это возможные последствия реализации угрозы при взаимодействии источника угрозы через имеющиеся уязвимости"
            },
            "correct": "a"
        },
        {
            "question": "26. Какой из перечисленный видов нарушителей информационной безопасности относится к внутренним?",
            "options": {
                "a": "Сотрудники внутренней службы безопасности",
                "b": "Представители конкурирующих организаций",
                "c": "Сотрудники органов ведомственного надзора и управления"
            },
            "correct": "a"
        },
        {
            "question": "27. Какой из перечисленный видов нарушителей информационной безопасности не относится к внутренним?",
            "options": {
                "a": "Представители конкурирующих организаций",
                "b": "Сотрудники внутренней службы безопасности",
                "c": "Уборщица"
            },
            "correct": "a"
        },
        {
            "question": "28. Какой из перечисленный видов нарушителей информационной безопасности относится к внешним?",
            "options": {
                "a": "Сотрудники органов ведомственного надзора и управления",
                "b": "Сотрудники внутренней службы безопасности",
                "c": "Уборщица"
            },
            "correct": "a"
        },
        {
            "question": "29. Какой из перечисленный видов нарушителей информационной безопасности не относится к внешним?",
            "options": {
                "a": "Пользователи и операторы информационной системы",
                "b": "Представители конкурирующих организаций",
                "c": "Приглашенные посетители",
                "d": "Наблюдатели за пределами охраняемой территории",
                "e": "Нарушители пропускного режима"
            },
            "correct": "a"
        },
        {
            "question": "30. Какие три понятия составляют триаду КДЦ?",
            "options": {
                "a": "Конфиденциальность, доступность и целостность",
                "b": "Мир, труд, май",
                "c": "Вчера, сегодня, завтра",
                "d": "Аутентичность, владение и полезность"
            },
            "correct": "a"
        },
        {
            "question": "31. Какие три понятия дополняют триаду КДЦ до Гексады Паркера?",
            "options": {
                "a": "Аутентичность, владение и полезность",
                "b": "Конфиденциальность, доступность и целостность",
                "c": "Мир, труд, май",
                "d": "Создание, редактирование, удаление"
            },
            "correct": "a"
        }
    ],
    "Методы защиты программного обеспечения": [
        {
            "question": "32. Какой метод защиты программного обеспечения относится к методам собственной защиты?",
            "options": {
                "a": "Организация сопровождения",
                "b": "Использование паролей",
                "c": "Использование специальной аппаратуры"
            },
            "correct": "a"
        },
        {
            "question": "33. Какой метод защиты программного обеспечения относится к методам использования средств защиты в составе вычислительной системы?",
            "options": {
                "a": "Организация сопровождения",
                "b": "Использование паролей",
                "c": "Использование специальной аппаратуры"
            },
            "correct": "c"
        },
        {
            "question": "34. Какой метод защиты программного обеспечения относится к методам защиты с запросом информации?",
            "options": {
                "a": "Организация сопровождения",
                "b": "Использование паролей",
                "c": "Использование специальной аппаратуры"
            },
            "correct": "b"
        },
        {
            "question": "35. Как раскрывается аббревиатура НСД в системах защиты информации?",
            "options": {
                "a": "Несанкционированный доступ",
                "b": "Экранирование",
                "c": "Несанкционированное копирование",
                "d": "Шифрование файлов"
            },
            "correct": "a"
        },
        {
            "question": "36. Как раскрывается аббревиатура НСК в системах защиты информации?",
            "options": {
                "a": "Несанкционированный доступ",
                "b": "Экранирование",
                "c": "Несанкционированное копирование",
                "d": "Шифрование файлов"
            },
            "correct": "c"
        },
        {
            "question": "37. Что из перечисленного относится к аппаратным методам защиты информации?",
            "options": {
                "a": "Организация пропускного режима",
                "b": "Экранирование",
                "d": "Шифрование файлов"
            },
            "correct": "b"
        },
        {
            "question": "38. Что из перечисленного относится к программным методам защиты информации?",
            "options": {
                "a": "Экранирование",
                "b": "Шифрование файлов",
                "c": "Средства акустического маскирования с использованием генераторов белого шума",
                "d": "Организация пропускного режима",
                "e": "Защита корпуса персонального компьютера от вскрытия"
            },
            "correct": "b"
        },
        {
            "question": "39. Что из перечисленного относится к организационным методам защиты информации?",
            "options": {
                "a": "Экранирование",
                "b": "Шифрование файлов",
                "c": "Средства акустического маскирования с использованием генераторов белого шума",
                "d": "Организация пропускного режима",
                "e": "Защита корпуса персонального компьютера от вскрытия"
            },
            "correct": "d"
        }
    ],
    "Криптографические методы защиты программного обеспечения и баз данных": [
        {
            "question": "40. Что из перечисленного является методом криптографического преобразования информации?",
            "options": {
                "a": "Стеганография",
                "b": "Стенографирование",
                "c": "Распечатывание",
                "d": "Перевод на другой язык"
            },
            "correct": "a"
        },
        {
            "question": "41. Что из перечисленного не является методом криптографического преобразования информации?",
            "options": {
                "a": "Шифрование",
                "b": "Кодирование",
                "c": "Сжатие",
                "d": "Копирование",
                "e": "Стеганография"
            },
            "correct": "d"
        },
        {
            "question": "42. Какой из представленных алгоритмов относится к симметричным криптосистемам?",
            "options": {
                "a": "DES",
                "b": "RSA",
                "c": "Эль Гамаля"
            },
            "correct": "a"
        },
        {
            "question": "43. Какой из представленных алгоритмов относится к асимметричным криптосистемам?",
            "options": {
                "a": "Диффи-Хеллмана",
                "b": "Эль Гамаля",
                "c": "DES",
                "d": "MD5",
                "e": "ГОСТ 28147-89"
            },
            "correct": "b"
        },
        {
            "question": "44. Какой из представленных алгоритмов используется при создании электронной цифровой подписи?",
            "options": {
                "a": "RSA",
                "b": "DES",
                "c": "ГОСТ 28147-89"
            },
            "correct": "a"
        },
        {
            "question": "45. Какой из представленных алгоритмов не относится к классическим симметричным криптосистемам?",
            "options": {
                "a": "ГОСТ 28147-89",
                "b": "шифра Цезаря",
                "c": "шифрование с использованием диска Альберти",
                "d": "шифрование с использованием таблицы Виженера"
            },
            "correct": "a"
        },
        {
            "question": "46. К какому типу шифров относится шифрование с использованием скитала?",
            "options": {
                "a": "Полиалфавитный шифр",
                "b": "Моноалфавитный шифр",
                "c": "С использованием электромеханической шифровальной машинки",
                "d": "С использованием программного или аппаратного математического шифра с секретным или закрытым ключом",
                "e": "С использованием программного или аппаратного математического шифра с открытым ключом"
            },
            "correct": "b"
        },
        {
            "question": "47. К какому типу шифров относится шифрование с использованием шифра Цезаря?",
            "options": {
                "a": "С использованием электромеханической шифровальной машинки",
                "b": "Моноалфавитный шифр",
                "c": "С использованием программного или аппаратного математического шифра с секретным или закрытым ключом",
                "d": "Полиалфавитный шифр",
                "e": "С использованием программного или аппаратного математического шифра с открытым ключом"
            },
            "correct": "b"
        },
        {
            "question": "48. К какому типу шифров относится шифрование с использованием диска Альберти?",
            "options": {
                "a": "Полиалфавитный шифр",
                "b": "С использованием программного или аппаратного математического шифра с секретным или закрытым ключом",
                "c": "С использованием электромеханической шифровальной машинки",
                "d": "Моноалфавитный шифр",
                "e": "С использованием программного или аппаратного математического шифра с открытым ключом"
            },
            "correct": "a"
        },
        {
            "question": "49. К какому типу шифров относится шифрование с использованием таблицы Виженера?",
            "options": {
                "a": "Моноалфавитный шифр",
                "b": "Полиалфавитный шифр",
                "c": "С использованием электромеханической шифровальной машинки",
                "d": "С использованием программного или аппаратного математического шифра с секретным или закрытым ключом",
                "e": "С использованием программного или аппаратного математического шифра с открытым ключом"
            },
            "correct": "b"
        },
        {
            "question": "50. К какому типу шифров относится шифрование с использованием шифровальной машинки Энигма?",
            "options": {
                "a": "С использованием электромеханической шифровальной машинки",
                "b": "Моноалфавитный шифр",
                "c": "Полиалфавитный шифр",
                "d": "С использованием программного или аппаратного математического шифра с секретным или закрытым ключом",
                "e": "С использованием программного или аппаратного математического шифра с открытым ключом"
            },
            "correct": "a"
        },
        {
            "question": "51. К какому типу шифров относится шифрование с использованием шифра Triple DES?",
            "options": {
                "a": "С использованием программного или аппаратного математического шифра с секретным или закрытым ключом",
                "b": "С использованием программного или аппаратного математического шифра с открытым ключом",
                "c": "Моноалфавитный шифр",
                "d": "Полиалфавитный шифр",
                "e": "С использованием электромеханической шифровальной машинки"
            },
            "correct": "a"
        },
        {
            "question": "52. К какому типу шифров относится шифрование с использованием шифра AES?",
            "options": {
                "a": "С использованием программного или аппаратного математического шифра с секретным или закрытым ключом",
                "b": "С использованием программного или аппаратного математического шифра с открытым ключом",
                "c": "Моноалфавитный шифр",
                "d": "Полиалфавитный шифр",
                "e": "С использованием электромеханической шифровальной машинки"
            },
            "correct": "a"
        },
        {
            "question": "53. К какому типу шифров относится шифрование с использованием шифра RSA?",
            "options": {
                "a": "Алгоритмы распределения ключей",
                "b": "Функции хэширования",
                "c": "Криптосистемы с закрытым ключом",
                "d": "Асимметричные криптосистемы",
                "e": "Симметричные криптосистемы"
            },
            "correct": "d"
        },
        {
            "question": "54. К какому классу алгоритмов шифрования относится шифрование Цезаря?",
            "options": {
                "a": "Симметричные криптосистемы",
                "b": "Криптосистемы с открытым ключом",
                "c": "Функции хэширования",
                "d": "Асимметричные криптосистемы",
                "e": "Алгоритмы распределения ключей"
            },
            "correct": "a"
        },
        {
            "question": "55. К какому классу алгоритмов шифрования относится шифрование таблицами Вижинера?",
            "options": {
                "a": "Симметричные криптосистемы",
                "b": "Криптосистемы с открытым ключом",
                "c": "Функции хэширования",
                "d": "Асимметричные криптосистемы",
                "e": "Алгоритмы распределения ключей"
            },
            "correct": "a"
        },
        {
            "question": "56. К какому классу алгоритмов шифрования относится шифрование алгоритмом DES?",
            "options": {
                "a": "Криптосистемы с открытым ключом",
                "b": "Функции хэширования",
                "c": "Асимметричные криптосистемы",
                "d": "Криптосистемы с закрытым ключом",
                "e": "Алгоритмы распределения ключей"
            },
            "correct": "d"
        },
        {
            "question": "57. К какому классу алгоритмов шифрования относится шифрование алгоритмом RSA?",
            "options": {
                "a": "Асимметричные криптосистемы",
                "b": "Криптосистемы с закрытым ключом",
                "c": "Алгоритмы распределения ключей",
                "d": "Симметричные криптосистемы",
                "e": "Функции хэширования"
            },
            "correct": "a"
        },
        {
            "question": "58. Для чего используется алгоритм Эль Гамаля?",
            "options": {
                "a": "Для создания ЭЦП",
                "b": "Для скрытой передачи ключей",
                "c": "Для симметричного шифрования"
            },
            "correct": "a"
        },
        {
            "question": "59. Для чего используется алгоритм Диффи-Хеллмана?",
            "options": {
                "a": "Для скрытой передачи ключей",
                "b": "Для создания ЭЦП",
                "c": "Для симметричного шифрования"
            },
            "correct": "a"
        },
        {
            "question": "60. Сколько циклов шифрования содержит алгоритм DES?",
            "options": {
                "a": "16",
                "b": "32",
                "c": "64",
                "d": "2",
                "e": "8"
            },
            "correct": "a"
        },
        {
            "question": "61. Какова длина ключа DES?",
            "options": {
                "a": "64 бита",
                "b": "128 бит",
                "c": "256 бит",
                "d": "1024 бит",
                "e": "32 бита"
            },
            "correct": "a"
        },
        {
            "question": "62. Какова длина информационного блока, шифрующегося алгоритмом DES?",
            "options": {
                "a": "64 бита",
                "b": "128 бит",
                "c": "256 бит",
                "d": "1024 бит",
                "e": "32 бита"
            },
            "correct": "a"
        }
    ],
    "Средства аутентификации при защите программного обеспечения и баз данных": [
        {
            "question": "63. Какое из перечисленных средств аутентификации относится к средствам, базирующимся на условных, заранее присваиваемых признаках (сведениях), известных субъекту?",
            "options": {
                "a": "Парольное средство",
                "b": "Смарт-карта",
                "c": "По отпечатку пальца",
                "d": "По радужной оболочке глаза",
                "e": "С использованием USB-ключа"
            },
            "correct": "a"
        },
        {
            "question": "64. Какое из перечисленных средств аутентификации относится к средствам, базирующимся на физических средствах, действующих аналогично физическому ключу?",
            "options": {
                "a": "Смарт-карта",
                "b": "Парольное средство",
                "c": "По отпечатку пальца",
                "d": "По радужной оболочке глаза",
                "e": "По клавиатурному почерку"
            },
            "correct": "a"
        },
        {
            "question": "65. Какое из перечисленных средств аутентификации относится к средствам, базирующимся на индивидуальных характеристиках субъекта, его физических данных, позволяющих выделить его среди других лиц?",
            "options": {
                "a": "По отпечатку пальца",
                "b": "Смарт-карта",
                "c": "Парольное средство",
                "d": "С использованием USB-ключа",
                "e": "PIN-код"
            },
            "correct": "a"
        },
        {
            "question": "66. Какое из перечисленных средств аутентификации относится к биометрическим?",
            "options": {
                "a": "По радужной оболочке глаза",
                "b": "Смарт-карта",
                "c": "Парольное средство",
                "d": "С использованием USB-ключа",
                "e": "PIN-код"
            },
            "correct": "a"
        },
        {
            "question": "67. Какое из перечисленных средств аутентификации не относится к биометрическим?",
            "options": {
                "a": "С использованием USB-ключа",
                "b": "По голосу",
                "c": "По отпечатку пальца",
                "d": "По радужной оболочке глаза",
                "e": "По клавиатурному почерку"
            },
            "correct": "a"
        }
    ],
    "Правила разграничения доступа": [
        {
            "question": "68. Определите принцип организации разграничения доступа по его описанию. Каждому защищаемому элементу присваивается персональная уникальная метка, после чего доступ к этому элементу будет разрешен только тому пользователю, который в своем запросе предъявит метку элемента, которую ему может выдать администратор или владелец элемента.",
            "options": {
                "a": "Мандатное управление доступом",
                "b": "Избирательное или дискреционное управление доступом",
                "c": "Ролевое управление доступом",
                "d": "Разграничение доступа по спискам контроля доступа"
            },
            "correct": "a"
        },
        {
            "question": "69. Определите принцип организации разграничения доступа по его описанию. Для каждого элемента защищаемых данных составляется список всех тех пользователей, которым предоставлено право доступа к соответствующему элементу.",
            "options": {
                "a": "Мандатное управление доступом",
                "b": "Избирательное или дискреционное управление доступом",
                "c": "Ролевое управление доступом",
                "d": "Разграничение доступа по спискам контроля доступа"
            },
            "correct": "d"
        },
        {
            "question": "70. Определите принцип организации разграничения доступа по его описанию. Используются такие понятия, как «должность» и «круг должностных обязанностей», наборы которых должны соответствовать перечню различных должностей, существующих на предприятии.",
            "options": {
                "a": "Мандатное управление доступом",
                "b": "Избирательное или дискреционное управление доступом",
                "c": "Ролевое управление доступом",
                "d": "Разграничение доступа по спискам контроля доступа"
            },
            "correct": "c"
        },
        {
            "question": "71. Определите принцип организации разграничения доступа по его описанию. Строки таблицы содержат идентификаторы зарегистрированных пользователей, а столбцы – идентификаторы защищаемых элементов данных, в ячейках таблицы – полномочия.",
            "options": {
                "a": "Мандатное управление доступом",
                "b": "Избирательное или дискреционное управление доступом",
                "c": "Ролевое управление доступом",
                "d": "Разграничение доступа по спискам контроля доступа"
            },
            "correct": "b"
        }
    ],
    "Сетевая безопасность": [
        {
            "question": "72. Дайте понятие фильтрации трафика.",
            "options": {
                "a": "Обработка IP-пакетов маршрутизаторами и файерволами, приводящая к отбрасыванию некоторых пакетов или изменению их маршрута.",
                "b": "Комплекс программно-аппаратных средств, осуществляющий информационную защиту одной части компьютерной сети от другой путем анализа и фильтрации проходящего между ними трафика.",
                "c": "Особый тип приложения, которое выполняет функции посредника между клиентскими и серверными частями распределенных сетевых приложений, причем предполагается, что клиенты принадлежат внутренней (защищаемой) сети, а серверы – внешней (потенциально опасной) сети.",
                "d": "Непрерывный процесс инструментального автоматизированного наблюдения за отдельными параметрами трафика с целью проверки соблюдения соглашения об уровне обслуживания, планирования сети, а также предотвращения негативных событий, таких как технические аварии, угрозы и атаки злоумышленников.",
                "e": "Программное или аппаратное средство, которое выполняет непрерывное наблюдение за сетевым трафиком и деятельностью субъектов системы с целью предупреждения, выявления и протоколирования атак."
            },
            "correct": "a"
        },
        {
            "question": "73. Дайте понятие межсетевого экрана.",
            "options": {
                "a": "Обработка IP-пакетов маршрутизаторами и файерволами, приводящая к отбрасыванию некоторых пакетов или изменению их маршрута.",
                "b": "Комплекс программно-аппаратных средств, осуществляющий информационную защиту одной части компьютерной сети от другой путем анализа и фильтрации проходящего между ними трафика.",
                "c": "Особый тип приложения, которое выполняет функции посредника между клиентскими и серверными частями распределенных сетевых приложений, причем предполагается, что клиенты принадлежат внутренней (защищаемой) сети, а серверы – внешней (потенциально опасной) сети.",
                "d": "Непрерывный процесс инструментального автоматизированного наблюдения за отдельными параметрами трафика с целью проверки соблюдения соглашения об уровне обслуживания, планирования сети, а также предотвращения негативных событий, таких как технические аварии, угрозы и атаки злоумышленников.",
                "e": "Программное или аппаратное средство, которое выполняет непрерывное наблюдение за сетевым трафиком и деятельностью субъектов системы с целью предупреждения, выявления и протоколирования атак."
            },
            "correct": "b"
        },
        {
            "question": "74. Дайте понятие прокси-сервера.",
            "options": {
                "a": "Обработка IP-пакетов маршрутизаторами и файерволами, приводящая к отбрасыванию некоторых пакетов или изменению их маршрута.",
                "b": "Комплекс программно-аппаратных средств, осуществляющий информационную защиту одной части компьютерной сети от другой путем анализа и фильтрации проходящего между ними трафика.",
                "c": "Особый тип приложения, которое выполняет функции посредника между клиентскими и серверными частями распределенных сетевых приложений, причем предполагается, что клиенты принадлежат внутренней (защищаемой) сети, а серверы – внешней (потенциально опасной) сети.",
                "d": "Непрерывный процесс инструментального автоматизированного наблюдения за отдельными параметрами трафика с целью проверки соблюдения соглашения об уровне обслуживания, планирования сети, а также предотвращения негативных событий, таких как технические аварии, угрозы и атаки злоумышленников.",
                "e": "Программное или аппаратное средство, которое выполняет непрерывное наблюдение за сетевым трафиком и деятельностью субъектов системы с целью предупреждения, выявления и протоколирования атак."
            },
            "correct": "c"
        },
        {
            "question": "75. Дайте понятие мониторинга сетевого трафика.",
            "options": {
                "a": "Обработка IP-пакетов маршрутизаторами и файерволами, приводящая к отбрасыванию некоторых пакетов или изменению их маршрута.",
                "b": "Комплекс программно-аппаратных средств, осуществляющий информационную защиту одной части компьютерной сети от другой путем анализа и фильтрации проходящего между ними трафика.",
                "c": "Особый тип приложения, которое выполняет функции посредника между клиентскими и серверными частями распределенных сетевых приложений, причем предполагается, что клиенты принадлежат внутренней (защищаемой) сети, а серверы – внешней (потенциально опасной) сети.",
                "d": "Непрерывный процесс инструментального автоматизированного наблюдения за отдельными параметрами трафика с целью проверки соблюдения соглашения об уровне обслуживания, планирования сети, а также предотвращения негативных событий, таких как технические аварии, угрозы и атаки злоумышленников.",
                "e": "Программное или аппаратное средство, которое выполняет непрерывное наблюдение за сетевым трафиком и деятельностью субъектов системы с целью предупреждения, выявления и протоколирования атак."
            },
            "correct": "d"
        },
        {
            "question": "76. Дайте понятие системы обнаружения вторжений.",
            "options": {
                "a": "Обработка IP-пакетов маршрутизаторами и файерволами, приводящая к отбрасыванию некоторых пакетов или изменению их маршрута.",
                "b": "Комплекс программно-аппаратных средств, осуществляющий информационную защиту одной части компьютерной сети от другой путем анализа и фильтрации проходящего между ними трафика.",
                "c": "Особый тип приложения, которое выполняет функции посредника между клиентскими и серверными частями распределенных сетевых приложений, причем предполагается, что клиенты принадлежат внутренней (защищаемой) сети, а серверы – внешней (потенциально опасной) сети.",
                "d": "Непрерывный процесс инструментального автоматизированного наблюдения за отдельными параметрами трафика с целью проверки соблюдения соглашения об уровне обслуживания, планирования сети, а также предотвращения негативных событий, таких как технические аварии, угрозы и атаки злоумышленников.",
                "e": "Программное или аппаратное средство, которое выполняет непрерывное наблюдение за сетевым трафиком и деятельностью субъектов системы с целью предупреждения, выявления и протоколирования атак."
            },
            "correct": "e"
        },
        {
            "question": "77. Дайте понятие троянской программы.",
            "options": {
                "a": "Вредоносный программный фрагмент, который может внедряться в другие файлы.",
                "b": "Вредоносная программа, которая наносит ущерб системе, маскируясь под какое-либо полезное приложение.",
                "c": "Совокупность сетевых устройств, на которые проникла программа, выполняющая некоторые автоматические действия по командам удаленного центра управления.",
                "d": "Программа, способная к самостоятельному распространению своих копий среди узлов в пределах локальной сети, а также по глобальным связям, перемещаясь от одного компьютера к другому без всякого участия в этом процессе пользователей сети.",
                "e": "Встроенный в программное обеспечение объект, который при определенных условиях инициирует выполнение не описанных в документации функций, позволяющих осуществлять несанкционированные воздействия на информацию."
            },
            "correct": "b"
        },
        {
            "question": "78. Дайте понятие сетевого червя.",
            "options": {
                "a": "Программа, способная к самостоятельному распространению своих копий среди узлов в пределах локальной сети, а также по глобальным связям, перемещаясь от одного компьютера к другому без всякого участия в этом процессе пользователей сети",
                "b": "Вредоносный программный фрагмент, который может внедряться в другие файлы",
                "c": "Встроенный в программное обеспечение объект, который при определенных условиях инициирует выполнение не описанных в документации функций, позволяющих осуществлять несанкционированные воздействия на информацию",
                "d": "Совокупность сетевых устройств, на которые проникла программа, выполняющая некоторые автоматические действия по командам удаленного центра управления"
            },
            "correct": "a"
        },
        {
            "question": "79. Дайте понятие компьютерному вирусу.",
            "options": {
                "a": "Программа, способная к самостоятельному распространению своих копий среди узлов в пределах локальной сети, а также по глобальным связям, перемещаясь от одного компьютера к другому без всякого участия в этом процессе пользователей сети",
                "b": "Вредоносный программный фрагмент, который может внедряться в другие файлы",
                "c": "Встроенный в программное обеспечение объект, который при определенных условиях инициирует выполнение не описанных в документации функций, позволяющих осуществлять несанкционированные воздействия на информацию",
                "d": "Совокупность сетевых устройств, на которые проникла программа, выполняющая некоторые автоматические действия по командам удаленного центра управления"
            },
            "correct": "b"
        },
        {
            "question": "80. Дайте понятие программной закладке.",
            "options": {
                "a": "Программа, способная к самостоятельному распространению своих копий среди узлов в пределах локальной сети, а также по глобальным связям, перемещаясь от одного компьютера к другому без всякого участия в этом процессе пользователей сети",
                "b": "Вредоносный программный фрагмент, который может внедряться в другие файлы",
                "c": "Встроенный в программное обеспечение объект, который при определенных условиях инициирует выполнение не описанных в документации функций, позволяющих осуществлять несанкционированные воздействия на информацию",
                "d": "Совокупность сетевых устройств, на которые проникла программа, выполняющая некоторые автоматические действия по командам удаленного центра управления"
            },
            "correct": "c"
        },
        {
            "question": "81. Дайте понятие ботнету.",
            "options": {
                "a": "Программа, способная к самостоятельному распространению своих копий среди узлов в пределах локальной сети, а также по глобальным связям, перемещаясь от одного компьютера к другому без всякого участия в этом процессе пользователей сети",
                "b": "Вредоносный программный фрагмент, который может внедряться в другие файлы",
                "c": "Встроенный в программное обеспечение объект, который при определенных условиях инициирует выполнение не описанных в документации функций, позволяющих осуществлять несанкционированные воздействия на информацию",
                "d": "Совокупность сетевых устройств, на которые проникла программа, выполняющая некоторые автоматические действия по командам удаленного центра управления"
            },
            "correct": "d"
        }
    ]
}

# Topics and questions dataset in uzbek
topics_uz = {
    "Asosiy tushunchalar": [
        {
            "question": "1. Himoyalanadigan ma'lumot tushunchasini aniqlang",
            "options": {
                "a": "Organlar va/yoki ijrochilar, ular foydalanadigan ma'lumotlarni himoya qilish texnikasi, shuningdek, himoyalangan ma'lumot obyektlari to'plami bo'lib, ma'lumotlarni himoya qilish sohasidagi tegishli hujjatlarda belgilangan qoidalar va normalarga muvofiq tashkil etilgan va faoliyat yuritadi",
                "b": "Ma'lumotlarni himoya qilish natijalarining ma'lumotlarni himoya qilish maqsadiga moslik darajasi",
                "c": "Himoyalanadigan ma'lumotlarning oqib chiqishini oldini olish, ruxsatsiz va qasddan ta'sirlarni oldini olishga qaratilgan faoliyat",
                "d": "Ma'lumotlarni himoya qilish uchun mo‘ljallangan yoki ishlatiladigan texnik, dasturiy, apparat-dasturiy vositalar, moddalar va/yoki materiallar",
                "e": "Mulk obyekti bo‘lgan va qonuniy hujjatlar talablariga yoki ma'lumot egasi (davlat, yuridik shaxs, shaxslar guruhi yoki jismoniy shaxs) tomonidan belgilangan talablarga muvofiq himoyalanishi kerak bo‘lgan ma'lumot"
            },
            "correct": "e"
        },
        {
            "question": "2. Ma'lumotlarni himoya qilish tushunchasini aniqlang",
            "options": {
                "a": "Himoyalanadigan ma'lumotlarning oqib chiqishini oldini olish, ruxsatsiz va qasddan ta'sirlarni oldini olishga qaratilgan faoliyat",
                "b": "Mulk obyekti bo‘lgan va qonuniy hujjatlar talablariga yoki ma'lumot egasi (davlat, yuridik shaxs, shaxslar guruhi yoki jismoniy shaxs) tomonidan belgilangan talablarga muvofiq himoyalanishi kerak bo‘lgan ma'lumot",
                "c": "Ma'lumotlarni himoya qilish natijalarining belgilangan maqsadga moslik darajasi",
                "d": "Organlar va/yoki ijrochilar, ular foydalanadigan ma'lumotlarni himoya qilish texnikasi, shuningdek, himoyalangan obyektlar to'plami bo'lib, ma'lumotlarni himoya qilish sohasidagi tegishli qonuniy, tashkiliy va normativ hujjatlarda belgilangan qoidalarga muvofiq tashkil etilgan va faoliyat yuritadi",
                "e": "Ma'lumotlarni himoya qilish uchun mo‘ljallangan yoki ishlatiladigan texnik, dasturiy vositalar, moddalar va/yoki materiallar"
            },
            "correct": "a"
        },
        {
            "question": "3. Ma'lumotlarni himoya qilish samaradorligi tushunchasini aniqlang",
            "options": {
                "a": "Himoyalanadigan ma'lumotlarning oqib chiqishini oldini olish, ruxsatsiz va qasddan ta'sirlarni oldini olishga qaratilgan faoliyat",
                "b": "Mulk obyekti bo‘lgan va qonuniy hujjatlar talablariga yoki ma'lumot egasi (davlat, yuridik shaxs, shaxslar guruhi yoki jismoniy shaxs) tomonidan belgilangan talablarga muvofiq himoyalanishi kerak bo‘lgan ma'lumot",
                "c": "Ma'lumotlarni himoya qilish natijalarining belgilangan maqsadga moslik darajasi",
                "d": "Organlar va/yoki ijrochilar, ular foydalanadigan ma'lumotlarni himoya qilish texnikasi, shuningdek, himoyalangan obyektlar to'plami bo'lib, ma'lumotlarni himoya qilish sohasidagi tegishli qonuniy, tashkiliy va normativ hujjatlarda belgilangan qoidalarga muvofiq tashkil etilgan va faoliyat yuritadi",
                "e": "Ma'lumotlarni himoya qilish uchun mo‘ljallangan yoki ishlatiladigan texnik, dasturiy vositalar, moddalar va/yoki materiallar"
            },
            "correct": "c"
        },
        {
            "question": "4. Ma'lumotlarni himoya qilish tizimi tushunchasini aniqlang",
            "options": {
                "a": "Himoyalanadigan ma'lumotlarning oqib chiqishini oldini olish, ruxsatsiz va qasddan ta'sirlarni oldini olishga qaratilgan faoliyat",
                "b": "Mulk obyekti bo‘lgan va qonuniy hujjatlar talablariga yoki ma'lumot egasi (davlat, yuridik shaxs, shaxslar guruhi yoki jismoniy shaxs) tomonidan belgilangan talablarga muvofiq himoyalanishi kerak bo‘lgan ma'lumot",
                "c": "Ma'lumotlarni himoya qilish natijalarining belgilangan maqsadga moslik darajasi",
                "d": "Organlar va/yoki ijrochilar, ular foydalanadigan ma'lumotlarni himoya qilish texnikasi, shuningdek, himoyalangan obyektlar to'plami bo'lib, ma'lumotlarni himoya qilish sohasidagi tegishli qonuniy, tashkiliy va normativ hujjatlarda belgilangan qoidalarga muvofiq tashkil etilgan va faoliyat yuritadi",
                "e": "Ma'lumotlarni himoya qilish uchun mo‘ljallangan yoki ishlatiladigan texnik, dasturiy vositalar, moddalar va/yoki materiallar"
            },
            "correct": "d"
        },
        {
            "question": "5. Ma'lumotlarni himoya qilish vositalari tushunchasini aniqlang",
            "options": {
                "a": "Himoyalanadigan ma'lumotlarning oqib chiqishini oldini olish, ruxsatsiz va qasddan ta'sirlarni oldini olishga qaratilgan faoliyat",
                "b": "Mulk obyekti bo‘lgan va qonuniy hujjatlar talablariga yoki ma'lumot egasi (davlat, yuridik shaxs, shaxslar guruhi yoki jismoniy shaxs) tomonidan belgilangan talablarga muvofiq himoyalanishi kerak bo‘lgan ma'lumot",
                "c": "Ma'lumotlarni himoya qilish natijalarining belgilangan maqsadga moslik darajasi",
                "d": "Organlar va/yoki ijrochilar, ular foydalanadigan ma'lumotlarni himoya qilish texnikasi, shuningdek, himoyalangan obyektlar to'plami bo'lib, ma'lumotlarni himoya qilish sohasidagi tegishli qonuniy, tashkiliy va normativ hujjatlarda belgilangan qoidalarga muvofiq tashkil etilgan va faoliyat yuritadi",
                "e": "Ma'lumotlarni himoya qilish uchun mo‘ljallangan yoki ishlatiladigan texnik, dasturiy vositalar, moddalar va/yoki materiallar"
            },
            "correct": "e"
        }
    ],
    "Ma'lumot xavfsizligidagi tahdidlar va buzg‘unchi modeli": [
        {
            "question": "6. Obyekt xavfsizligi tahdidi tushunchasini aniqlang",
            "options": {
                "a": "Obyektga bevosita yoki bilvosita zarar yetkazishi mumkin bo‘lgan mumkin bo‘lgan ta'sir",
                "b": "Obyektdagi ma'lumot xavfsizligi buzilishiga olib keladigan ichki sabablar",
                "c": "Xavfsizlik tahdidining potentsial antropogen, texnogen yoki tabiiy tashuvchilari",
                "d": "Mavjud zaifliklar orqali tahdid manbai bilan o‘zaro ta'sir natijasida tahdidning amalga oshirilishi mumkin bo‘lgan oqibatlar"
            },
            "correct": "a"
        },
        {
            "question": "7. Obyektning zaifligi tushunchasini aniqlang",
            "options": {
                "a": "Obyektga bevosita yoki bilvosita zarar yetkazishi mumkin bo‘lgan mumkin bo‘lgan ta'sir",
                "b": "Obyektdagi ma'lumot xavfsizligi buzilishiga olib keladigan ichki sabablar",
                "c": "Xavfsizlik tahdidining potentsial antropogen, texnogen yoki tabiiy tashuvchilari",
                "d": "Mavjud zaifliklar orqali tahdid manbai bilan o‘zaro ta'sir natijasida tahdidning amalga oshirilishi mumkin bo‘lgan oqibatlar"
            },
            "correct": "b"
        },
        {
            "question": "8. Tahdid manbai tushunchasini aniqlang",
            "options": {
                "a": "Obyektga bevosita yoki bilvosita zarar yetkazishi mumkin bo‘lgan mumkin bo‘lgan ta'sir",
                "b": "Obyektdagi ma'lumot xavfsizligi buzilishiga olib keladigan ichki sabablar",
                "c": "Xavfsizlik tahdidining potentsial antropogen, texnogen yoki tabiiy tashuvchilari",
                "d": "Mavjud zaifliklar orqali tahdid manbai bilan o‘zaro ta'sir natijasida tahdidning amalga oshirilishi mumkin bo‘lgan oqibatlar"
            },
            "correct": "c"
        },
        {
            "question": "9. Hujum tushunchasini aniqlang",
            "options": {
                "a": "Mavjud zaifliklar orqali tahdid manbai bilan o‘zaro ta'sir natijasida tahdidning amalga oshirilishi mumkin bo‘lgan oqibatlar",
                "b": "Ma'lumotlarni himoya qilish uchun mo‘ljallangan yoki ishlatiladigan texnik, dasturiy vositalar, moddalar va/yoki materiallar",
                "c": "Xavfsizlik tahdidining potentsial antropogen, texnogen yoki tabiiy tashuvchilari",
                "d": "Obyektdagi ma'lumot xavfsizligi buzilishiga olib keladigan ichki sabablar",
                "e": "Obyektga bevosita yoki bilvosita zarar yetkazishi mumkin bo‘lgan mumkin bo‘lgan ta'sir"
            },
            "correct": "a"
        },
        {
            "question": "10. Ma'lumotlarning maxfiyligi nima?",
            "options": {
                "a": "Tizimning tasodifiy yoki qasddan buzilishlar yoki yo‘q qiluvchi ta'sirlar sharoitida ma'lumotning semantik ma'noda o‘zgarmasligi xususiyati",
                "b": "Ma'lumot faqat autentifikatsiya qilingan qonuniy tizim subyektlariga ma'lum bo‘lishi xususiyati",
                "c": "Ma'lumot autentifikatsiya qilingan qonuniy tizim subyektlari uchun ochiq bo‘lishi xususiyati",
                "d": "Ma'lumot tahdidning amalga oshirilishi mumkin bo‘lgan oqibatlarini ko‘rsatishi xususiyati",
                "e": "Ma'lumot bir yoki bir nechta potentsial ma'lumot xavfsizligi buzg‘unchilari, ularning malakasi va texnik va moddiy vositalari haqida taxminlar to‘plamini taqdim etishi xususiyati"
            },
            "correct": "b"
        },
        {
            "question": "11. Ma'lumotlarning yaxlitligi nima?",
            "options": {
                "a": "Tizimning tasodifiy yoki qasddan buzilishlar yoki yo‘q qiluvchi ta'sirlar sharoitida ma'lumotning semantik ma'noda o‘zgarmasligi xususiyati",
                "b": "Ma'lumot faqat autentifikatsiya qilingan qonuniy tizim subyektlariga ma'lum bo‘lishi xususiyati",
                "c": "Ma'lumot autentifikatsiya qilingan qonuniy tizim subyektlari uchun ochiq bo‘lishi xususiyati",
                "d": "Ma'lumot tahdidning amalga oshirilishi mumkin bo‘lgan oqibatlarini ko‘rsatishi xususiyati",
                "e": "Ma'lumot bir yoki bir nechta potentsial ma'lumot xavfsizligi buzg‘unchilari, ularning malakasi va texnik va moddiy vositalari haqida taxminlar to‘plamini taqdim etishi xususiyati"
            },
            "correct": "a"
        },
        {
            "question": "12. Ma'lumotlarning ochiqligi nima?",
            "options": {
                "a": "Ma'lumot tahdidning amalga oshirilishi mumkin bo‘lgan oqibatlarini ko‘rsatishi xususiyati",
                "b": "Tizimning tasodifiy yoki qasddan buzilishlar yoki yo‘q qiluvchi ta'sirlar sharoitida ma'lumotning semantik ma'noda o‘zgarmasligi xususiyati",
                "c": "Ma'lumot autentifikatsiya qilingan qonuniy tizim subyektlari uchun ochiq bo‘lishi xususiyati",
                "d": "Ma'lumot bir yoki bir nechta potentsial ma'lumot xavfsizligi buzg‘unchilari, ularning malakasi va texnik va moddiy vositalari haqida taxminlar to‘plamini taqdim etishi xususiyati",
                "e": "Ma'lumot faqat autentifikatsiya qilingan qonuniy tizim subyektlariga ma'lum bo‘lishi xususiyati"
            },
            "correct": "c"
        },
        {
            "question": "13. Quyidagi tahdidlardan qaysi biri ma'lumotlar maxfiyligiga qarshi tahdidga tegishli?",
            "options": {
                "a": "Ma'lumotlar o‘g‘irlash",
                "b": "Ma'lumotlar yo‘q qilish",
                "c": "Ma'lumotlar o‘zgartirish"
            },
            "correct": "a"
        },
        {
            "question": "14. Quyidagi tahdidlardan qaysi biri ma'lumotlar ochiqligiga qarshi tahdidga tegishli?",
            "options": {
                "a": "Ma'lumotlar o‘g‘irlash",
                "b": "Ma'lumotlar yo‘q qilish",
                "c": "Ma'lumotlar o‘zgartirish"
            },
            "correct": "b"
        },
        {
            "question": "15. Quyidagi tahdidlardan qaysi biri ma'lumotlar yaxlitligiga qarshi tahdidga tegishli?",
            "options": {
                "a": "Ma'lumotlar o‘g‘irlash",
                "b": "Ma'lumotlar yo‘q qilish",
                "c": "Ma'lumotlar o‘zgartirish"
            },
            "correct": "c"
        },
        {
            "question": "16. Tahdid manbalarining qaysi tasnifi umumiy qabul qilingan?",
            "options": {
                "a": "Antropogen, texnogen, tabiiy",
                "b": "Obyektiv, subyektiv, tasodifiy",
                "c": "Mahalliy, global, kosmik"
            },
            "correct": "a"
        },
        {
            "question": "17. Himoyalangan obyektning zaifliklarining qaysi tasnifi umumiy qabul qilingan?",
            "options": {
                "a": "Obyektiv, subyektiv, tasodifiy",
                "b": "Antropogen, texnogen, tabiiy",
                "c": "Tashqi va ichki"
            },
            "correct": "a"
        },
        {
            "question": "18. Quyidagi tahdid manbalaridan qaysi biri antropogen tahdidlarga tegishli?",
            "options": {
                "a": "Elektr uzatish liniyalarining elektromagnit maydon ta'siri",
                "b": "Rele kontaktlarining yopishib qolishi",
                "c": "Suv toshqini",
                "d": "Tornado",
                "e": "Mast haydovchi"
            },
            "correct": "e"
        },
        {
            "question": "19. Quyidagi tahdid manbalaridan qaysi biri texnogen tahdidlarga tegishli?",
            "options": {
                "a": "Samolyot dvigatelining ishdan chiqishi",
                "b": "Tsunami",
                "c": "Mast haydovchi",
                "d": "Suv toshqini",
                "e": "Tornado"
            },
            "correct": "a"
        },
        {
            "question": "20. Quyidagi tahdid manbalaridan qaysi biri tabiiy tahdidlarga tegishli?",
            "options": {
                "a": "Tsunami",
                "b": "Samolyot dvigatelining ishdan chiqishi",
                "c": "Mast haydovchi",
                "d": "Elektr uzatish liniyalarining elektromagnit maydon ta'siri",
                "e": "Rele kontaktlarining yopishib qolishi"
            },
            "correct": "a"
        },
        {
            "question": "21. Quyidagi tahdid manbalaridan qaysi biri tashqi antropogen tahdid hisoblanadi?",
            "options": {
                "a": "Telekommunikatsiya xizmatlari yetkazib beruvchilarining texnik xodimlari",
                "b": "Aloqa vositalari",
                "c": "Farrosh",
                "d": "Transport",
                "e": "Tornado"
            },
            "correct": "a"
        },
        {
            "question": "22. Quyidagi tahdid manbalaridan qaysi biri ichki antropogen tahdid hisoblanadi?",
            "options": {
                "a": "Aloqa vositalari",
                "b": "Fors-major holatlari",
                "c": "Jinoyatchi tuzilmalar",
                "d": "Farrosh",
                "e": "Obyektda ishlatiladigan sifatsiz ma'lumot ishlov berish dasturiy vositalari"
            },
            "correct": "d"
        },
        {
            "question": "23. Quyidagi tahdid manbalaridan qaysi biri tashqi texnogen tahdid hisoblanadi?",
            "options": {
                "a": "Transport",
                "b": "Farrosh",
                "c": "Tornado",
                "d": "Jinoyatchi tuzilmalar",
                "e": "Suv toshqini"
            },
            "correct": "a"
        },
        {
            "question": "24. Quyidagi tahdid manbalaridan qaysi biri ichki texnogen tahdid hisoblanadi?",
            "options": {
                "a": "Obyektda ishlatiladigan sifatsiz texnik ma'lumot ishlov berish vositalari",
                "b": "Farrosh",
                "c": "Tornado",
                "d": "Jinoyatchi tuzilmalar",
                "e": "Suv toshqini"
            },
            "correct": "a"
        },
        {
            "question": "25. Ma'lumot xavfsizligi buzg‘unchisi modeli nima?",
            "options": {
                "a": "Bir yoki bir nechta potentsial ma'lumot xavfsizligi buzg‘unchilari, ularning malakasi va texnik va moddiy vositalari haqida taxminlar to‘plami",
                "b": "Obyektga bevosita yoki bilvosita zarar yetkazishi mumkin bo‘lgan mumkin bo‘lgan ta'sir",
                "c": "Obyektdagi ma'lumot xavfsizligi buzilishiga olib keladigan ichki sabablar",
                "d": "Xavfsizlik tahdidining potentsial antropogen, texnogen yoki tabiiy tashuvchilari",
                "e": "Mavjud zaifliklar orqali tahdid manbai bilan o‘zaro ta'sir natijasida tahdidning amalga oshirilishi mumkin bo‘lgan oqibatlar"
            },
            "correct": "a"
        },
        {
            "question": "26. Quyidagi ma'lumot xavfsizligi buzg‘unchilari turlaridan qaysi biri ichki buzg‘unchilarga tegishli?",
            "options": {
                "a": "Ichki xavfsizlik xizmati xodimlari",
                "b": "Raqobatchi tashkilotlar vakillari",
                "c": "Idoraviy nazorat va boshqaruv organlari xodimlari"
            },
            "correct": "a"
        },
        {
            "question": "27. Quyidagi ma'lumot xavfsizligi buzg‘unchilari turlaridan qaysi biri ichki buzg‘unchilarga tegishli emas?",
            "options": {
                "a": "Raqobatchi tashkilotlar vakillari",
                "b": "Ichki xavfsizlik xizmati xodimlari",
                "c": "Farrosh"
            },
            "correct": "a"
        },
        {
            "question": "28. Quyidagi ma'lumot xavfsizligi buzg‘unchilari turlaridan qaysi biri tashqi buzg‘unchilarga tegishli?",
            "options": {
                "a": "Idoraviy nazorat va boshqaruv organlari xodimlari",
                "b": "Ichki xavfsizlik xizmati xodimlari",
                "c": "Farrosh"
            },
            "correct": "a"
        },
        {
            "question": "29. Quyidagi ma'lumot xavfsizligi buzg‘unchilari turlaridan qaysi biri tashqi buzg‘unchilarga tegishli emas?",
            "options": {
                "a": "Ma'lumot tizimining foydalanuvchilari va operatorlari",
                "b": "Raqobatchi tashkilotlar vakillari",
                "c": "Taklif qilingan mehmonlar",
                "d": "Himoyalangan hududdan tashqaridagi kuzatuvchilar",
                "e": "Kirish nazorati rejimini buzuvchilar"
            },
            "correct": "a"
        },
        {
            "question": "30. KDX triadasini tashkil etuvchi uchta tushuncha qaysilar?",
            "options": {
                "a": "Maxfiylik, ochiqlik va yaxlitlik",
                "b": "Tinchlik, mehnat, may",
                "c": "Kecha, bugun, ertaga",
                "d": "Autentiklik, egalik va foydalilik"
            },
            "correct": "a"
        },
        {
            "question": "31. KDX triadasini Parker geksadasiga to‘ldiruvchi uchta tushuncha qaysilar?",
            "options": {
                "a": "Autentiklik, egalik va foydalilik",
                "b": "Maxfiylik, ochiqlik va yaxlitlik",
                "c": "Tinchlik, mehnat, may",
                "d": "Yaratish, tahrirlash, o‘chirish"
            },
            "correct": "a"
        }
    ],
    "Dasturiy ta'minotni himoya qilish usullari": [
        {
            "question": "32. Quyidagi dasturiy ta'minotni himoya qilish usullaridan qaysi biri o‘z-o‘zini himoya qilish usullariga tegishli?",
            "options": {
                "a": "Xizmat ko‘rsatishni tashkil etish",
                "b": "Parollardan foydalanish",
                "c": "Maxsus apparaturadan foydalanish"
            },
            "correct": "a"
        },
        {
            "question": "33. Quyidagi dasturiy ta'minotni himoya qilish usullaridan qaysi biri hisoblash tizimi tarkibidagi himoya vositalaridan foydalanish usullariga tegishli?",
            "options": {
                "a": "Xizmat ko‘rsatishni tashkil etish",
                "b": "Parollardan foydalanish",
                "c": "Maxsus apparaturadan foydalanish"
            },
            "correct": "c"
        },
        {
            "question": "34. Quyidagi dasturiy ta'minotni himoya qilish usullaridan qaysi biri ma'lumot so‘rovi bilan himoya usullariga tegishli?",
            "options": {
                "a": "Xizmat ko‘rsatishni tashkil etish",
                "b": "Parollardan foydalanish",
                "c": "Maxsus apparaturadan foydalanish"
            },
            "correct": "b"
        },
        {
            "question": "35. Ma'lumotlarni himoya qilish tizimlarida НСД qisqartmasi nimani anglatadi?",
            "options": {
                "a": "Ruxsatsiz kirish",
                "b": "Ekranlash",
                "c": "Ruxsatsiz nusxa olish",
                "d": "Fayllarni shifrlash"
            },
            "correct": "a"
        },
        {
            "question": "36. Ma'lumotlarni himoya qilish tizimlarida НСК qisqartmasi nimani anglatadi?",
            "options": {
                "a": "Ruxsatsiz kirish",
                "b": "Ekranlash",
                "c": "Ruxsatsiz nusxa olish",
                "d": "Fayllarni shifrlash"
            },
            "correct": "c"
        },
        {
            "question": "37. Quyidagilardan qaysi biri apparatga asoslangan ma'lumotlarni himoya qilish usullariga tegishli?",
            "options": {
                "a": "Kirish nazorati rejimini tashkil etish",
                "b": "Ekranlash",
                "d": "Fayllarni shifrlash"
            },
            "correct": "b"
        },
        {
            "question": "38. Quyidagilardan qaysi biri dasturiy ma'lumotlarni himoya qilish usullariga tegishli?",
            "options": {
                "a": "Ekranlash",
                "b": "Fayllarni shifrlash",
                "c": "Oq shovqin generatorlari yordamida akustik niqoblash vositalari",
                "d": "Kirish nazorati rejimini tashkil etish",
                "e": "Shaxsiy kompyuter korpusini ochilishdan himoya qilish"
            },
            "correct": "b"
        },
        {
            "question": "39. Quyidagilardan qaysi biri tashkiliy ma'lumotlarni himoya qilish usullariga tegishli?",
            "options": {
                "a": "Ekranlash",
                "b": "Fayllarni shifrlash",
                "c": "Oq shovqin generatorlari yordamida akustik niqoblash vositalari",
                "d": "Kirish nazorati rejimini tashkil etish",
                "e": "Shaxsiy kompyuter korpusini ochilishdan himoya qilish"
            },
            "correct": "d"
        }
    ],
    "Dasturiy ta'minot va ma'lumotlar bazasini himoya qilishning kriptografik usullari": [
        {
            "question": "40. Quyidagilardan qaysi biri ma'lumotlarning kriptografik o‘zgartirish usuli hisoblanadi?",
            "options": {
                "a": "Steganografiya",
                "b": "Stenografiya",
                "c": "Chop etish",
                "d": "Boshqa tilga tarjima qilish"
            },
            "correct": "a"
        },
        {
            "question": "41. Quyidagilardan qaysi biri ma'lumotlarning kriptografik o‘zgartirish usuli emas?",
            "options": {
                "a": "Shifrlash",
                "b": "Kodlash",
                "c": "Siqish",
                "d": "Nusxa olish",
                "e": "Steganografiya"
            },
            "correct": "d"
        },
        {
            "question": "42. Quyidagi algoritmlardan qaysi biri simmetrik kriptotizimlarga tegishli?",
            "options": {
                "a": "DES",
                "b": "RSA",
                "c": "ElGamal"
            },
            "correct": "a"
        },
        {
            "question": "43. Quyidagi algoritmlardan qaysi biri assimetrik kriptotizimlarga tegishli?",
            "options": {
                "a": "Diffie-Hellman",
                "b": "ElGamal",
                "c": "DES",
                "d": "MD5",
                "e": "GOST 28147-89"
            },
            "correct": "b"
        },
        {
            "question": "44. Quyidagi algoritmlardan qaysi biri raqamli imzo yaratishda ishlatiladi?",
            "options": {
                "a": "RSA",
                "b": "DES",
                "c": "GOST 28147-89"
            },
            "correct": "a"
        },
        {
            "question": "45. Quyidagi algoritmlardan qaysi biri klassik simmetrik kriptotizimlarga tegishli emas?",
            "options": {
                "a": "GOST 28147-89",
                "b": "Sezar shifri",
                "c": "Alberti diski yordamida shifrlash",
                "d": "Vigenère jadvali yordamida shifrlash"
            },
            "correct": "a"
        },
        {
            "question": "46. Skitala yordamida shifrlash qanday shifr turiga kiradi?",
            "options": {
                "a": "Polialfavitik shifr",
                "b": "Monoalfavitik shifr",
                "c": "Elektromexanik shifrlash mashinasi yordamida",
                "d": "Maxfiy yoki yopiq kalitli dasturiy yoki apparat matematik shifri yordamida",
                "e": "Ochiq kalitli dasturiy yoki apparat matematik shifri yordamida"
            },
            "correct": "b"
        },
        {
            "question": "47. Sezar shifri yordamida shifrlash qanday shifr turiga kiradi?",
            "options": {
                "a": "Elektromexanik shifrlash mashinasi yordamida",
                "b": "Monoalfavitik shifr",
                "c": "Maxfiy yoki yopiq kalitli dasturiy yoki apparat matematik shifri yordamida",
                "d": "Polialfavitik shifr",
                "e": "Ochiq kalitli dasturiy yoki apparat matematik shifri yordamida"
            },
            "correct": "b"
        },
        {
            "question": "48. Alberti diski yordamida shifrlash qanday shifr turiga kiradi?",
            "options": {
                "a": "Polialfavitik shifr",
                "b": "Maxfiy yoki yopiq kalitli dasturiy yoki apparat matematik shifri yordamida",
                "c": "Elektromexanik shifrlash mashinasi yordamida",
                "d": "Monoalfavitik shifr",
                "e": "Ochiq kalitli dasturiy yoki apparat matematik shifri yordamida"
            },
            "correct": "a"
        },
        {
            "question": "49. Vigenère jadvali yordamida shifrlash qanday shifr turiga kiradi?",
            "options": {
                "a": "Monoalfavitik shifr",
                "b": "Polialfavitik shifr",
                "c": "Elektromexanik shifrlash mashinasi yordamida",
                "d": "Maxfiy yoki yopiq kalitli dasturiy yoki apparat matematik shifri yordamida",
                "e": "Ochiq kalitli dasturiy yoki apparat matematik shifri yordamida"
            },
            "correct": "b"
        },
        {
            "question": "50. Enigma mashinasi yordamida shifrlash qanday shifr turiga kiradi?",
            "options": {
                "a": "Elektromexanik shifrlash mashinasi yordamida",
                "b": "Monoalfavitik shifr",
                "c": "Polialfavitik shifr",
                "d": "Maxfiy yoki yopiq kalitli dasturiy yoki apparat matematik shifri yordamida",
                "e": "Ochiq kalitli dasturiy yoki apparat matematik shifri yordamida"
            },
            "correct": "a"
        },
        {
            "question": "51. Triple DES yordamida shifrlash qanday shifr turiga kiradi?",
            "options": {
                "a": "Maxfiy yoki yopiq kalitli dasturiy yoki apparat matematik shifri yordamida",
                "b": "Ochiq kalitli dasturiy yoki apparat matematik shifri yordamida",
                "c": "Monoalfavitik shifr",
                "d": "Polialfavitik shifr",
                "e": "Elektromexanik shifrlash mashinasi yordamida"
            },
            "correct": "a"
        },
        {
            "question": "52. AES yordamida shifrlash qanday shifr turiga kiradi?",
            "options": {
                "a": "Maxfiy yoki yopiq kalitli dasturiy yoki apparat matematik shifri yordamida",
                "b": "Ochiq kalitli dasturiy yoki apparat matematik shifri yordamida",
                "c": "Monoalfavitik shifr",
                "d": "Polialfavitik shifr",
                "e": "Elektromexanik shifrlash mashinasi yordamida"
            },
            "correct": "a"
        },
        {
            "question": "53. RSA yordamida shifrlash qanday shifr turiga kiradi?",
            "options": {
                "a": "Kalitlarni tarqatish algoritmlari",
                "b": "Hash funksiyalari",
                "c": "Yopiq kalitli kriptotizimlar",
                "d": "Asimmetrik kriptotizimlar",
                "e": "Simmetrik kriptotizimlar"
            },
            "correct": "d"
        },
        {
            "question": "54. Sezar shifri qaysi shifrlash algoritmlari sinfiga kiradi?",
            "options": {
                "a": "Simmetrik kriptotizimlar",
                "b": "Ochiq kalitli kriptotizimlar",
                "c": "Hash funksiyalari",
                "d": "Asimmetrik kriptotizimlar",
                "e": "Kalitlarni tarqatish algoritmlari"
            },
            "correct": "a"
        },
        {
            "question": "55. Vigenère jadvali yordamida shifrlash qaysi shifrlash algoritmlari sinfiga kiradi?",
            "options": {
                "a": "Simmetrik kriptotizimlar",
                "b": "Ochiq kalitli kriptotizimlar",
                "c": "Hash funksiyalari",
                "d": "Asimmetrik kriptotizimlar",
                "e": "Kalitlarni tarqatish algoritmlari"
            },
            "correct": "a"
        },
        {
            "question": "56. DES algoritmi yordamida shifrlash qaysi shifrlash algoritmlari sinfiga kiradi?",
            "options": {
                "a": "Ochiq kalitli kriptotizimlar",
                "b": "Hash funksiyalari",
                "c": "Asimmetrik kriptotizimlar",
                "d": "Yopiq kalitli kriptotizimlar",
                "e": "Kalitlarni tarqatish algoritmlari"
            },
            "correct": "d"
        },
        {
            "question": "57. RSA algoritmi yordamida shifrlash qaysi shifrlash algoritmlari sinfiga kiradi?",
            "options": {
                "a": "Asimmetrik kriptotizimlar",
                "b": "Yopiq kalitli kriptotizimlar",
                "c": "Kalitlarni tarqatish algoritmlari",
                "d": "Simmetrik kriptotizimlar",
                "e": "Hash funksiyalari"
            },
            "correct": "a"
        },
        {
            "question": "58. ElGamal algoritmi nima uchun ishlatiladi?",
            "options": {
                "a": "Raqamli imzo yaratish uchun",
                "b": "Xavfsiz kalit uzatish uchun",
                "c": "Simmetrik shifrlash uchun"
            },
            "correct": "a"
        },
        {
            "question": "59. Diffie-Hellman algoritmi nima uchun ishlatiladi?",
            "options": {
                "a": "Xavfsiz kalit uzatish uchun",
                "b": "Raqamli imzo yaratish uchun",
                "c": "Simmetrik shifrlash uchun"
            },
            "correct": "a"
        },
        {
            "question": "60. DES algoritmi necha shifrlash siklini o‘z ichiga oladi?",
            "options": {
                "a": "16",
                "b": "32",
                "c": "64",
                "d": "2",
                "e": "8"
            },
            "correct": "a"
        },
        {
            "question": "61. DES algoritmining kalit uzunligi qancha?",
            "options": {
                "a": "64 bit",
                "b": "128 bit",
                "c": "256 bit",
                "d": "1024 bit",
                "e": "32 bit"
            },
            "correct": "a"
        },
        {
            "question": "62. DES algoritmi tomonidan shifrlanadigan ma'lumot blokining uzunligi qancha?",
            "options": {
                "a": "64 bit",
                "b": "128 bit",
                "c": "256 bit",
                "d": "1024 bit",
                "e": "32 bit"
            },
            "correct": "a"
        }
    ],
    "Dasturiy ta'minot va ma'lumotlar bazasini himoya qilish uchun autentifikatsiya vositalari": [
        {
            "question": "63. Quyidagi autentifikatsiya vositalaridan qaysi biri subyektga oldindan berilgan shartli atributlarga (ma'lumotlarga) asoslangan vositalarga tegishli?",
            "options": {
                "a": "Parolga asoslangan vositalar",
                "b": "Aqlli karta",
                "c": "Barmoq izi orqali",
                "d": "Ko‘z pardasi orqali",
                "e": "USB kaliti yordamida"
            },
            "correct": "a"
        },
        {
            "question": "64. Quyidagi autentifikatsiya vositalaridan qaysi biri jismoniy kalitga o‘xshash tarzda ishlaydigan fizik vositalarga asoslangan vositalarga tegishli?",
            "options": {
                "a": "Aqlli karta",
                "b": "Parolga asoslangan vositalar",
                "c": "Barmoq izi orqali",
                "d": "Ko‘z pardasi orqali",
                "e": "Matn terish uslubi orqali"
            },
            "correct": "a"
        },
        {
            "question": "65. Quyidagi autentifikatsiya vositalaridan qaysi biri subyektning individual xususiyatlariga, ularning fizik ma'lumotlariga asoslangan vositalarga tegishli, bu ularni boshqalardan farqlash imkonini beradi?",
            "options": {
                "a": "Barmoq izi orqali",
                "b": "Aqlli karta",
                "c": "Parolga asoslangan vositalar",
                "d": "USB kaliti yordamida",
                "e": "PIN kod"
            },
            "correct": "a"
        },
        {
            "question": "66. Quyidagi autentifikatsiya vositalaridan qaysi biri biometrik vositalarga tegishli?",
            "options": {
                "a": "Ko‘z pardasi orqali",
                "b": "Aqlli karta",
                "c": "Parolga asoslangan vositalar",
                "d": "USB kaliti yordamida",
                "e": "PIN kod"
            },
            "correct": "a"
        },
        {
            "question": "67. Quyidagi autentifikatsiya vositalaridan qaysi biri biometrik vositalarga tegishli emas?",
            "options": {
                "a": "USB kaliti yordamida",
                "b": "Ovoz orqali",
                "c": "Barmoq izi orqali",
                "d": "Ko‘z pardasi orqali",
                "e": "Matn terish uslubi orqali"
            },
            "correct": "a"
        }
    ],
    "Kirishni boshqarish qoidalari": [
        {
            "question": "68. Quyidagi tavsif asosida kirishni boshqarish printsipini aniqlang: Har bir himoyalangan elementga noyob shaxsiy yorliq beriladi, shundan so‘ng ushbu elementga faqat administrator yoki element egasi tomonidan berilishi mumkin bo‘lgan element yorlig‘ini o‘z so‘rovida taqdim etgan foydalanuvchiga kirish huquqi beriladi.",
            "options": {
                "a": "Majburiy kirishni boshqarish",
                "b": "Ixtiyoriy kirishni boshqarish",
                "c": "Rolga asoslangan kirishni boshqarish",
                "d": "Kirishni boshqarish ro‘yxatlariga asoslangan kirishni boshqarish"
            },
            "correct": "a"
        },
        {
            "question": "69. Quyidagi tavsif asosida kirishni boshqarish printsipini aniqlang: Har bir himoyalangan ma'lumot elementi uchun ushbu elementga kirish huquqiga ega bo‘lgan barcha foydalanuvchilar ro‘yxati tuziladi.",
            "options": {
                "a": "Majburiy kirishni boshqarish",
                "b": "Ixtiyoriy kirishni boshqarish",
                "c": "Rolga asoslangan kirishni boshqarish",
                "d": "Kirishni boshqarish ro‘yxatlariga asoslangan kirishni boshqarish"
            },
            "correct": "d"
        },
        {
            "question": "70. Quyidagi tavsif asosida kirishni boshqarish printsipini aniqlang: Tashkilotda mavjud bo‘lgan turli lavozimlar ro‘yxatiga mos kelishi kerak bo‘lgan 'lavozim' va 'ish vazifalari doirasi' kabi tushunchalar qo‘llaniladi.",
            "options": {
                "a": "Majburiy kirishni boshqarish",
                "b": "Ixtiyoriy kirishni boshqarish",
                "c": "Rolga asoslangan kirishni boshqarish",
                "d": "Kirishni boshqarish ro‘yxatlariga asoslangan kirishni boshqarish"
            },
            "correct": "c"
        },
        {
            "question": "71. Quyidagi tavsif asosida kirishni boshqarish printsipini aniqlang: Jadval qatorlarida ro‘yxatdan o‘tgan foydalanuvchilarning identifikatorlari, ustunlarda himoyalangan ma'lumot elementlarining identifikatorlari, hujayralarda esa ruxsatlar mavjud.",
            "options": {
                "a": "Majburiy kirishni boshqarish",
                "b": "Ixtiyoriy kirishni boshqarish",
                "c": "Rolga asoslangan kirishni boshqarish",
                "d": "Kirishni boshqarish ro‘yxatlariga asoslangan kirishni boshqarish"
            },
            "correct": "b"
        }
    ],
    "Tarmoq xavfsizligi": [
        {
            "question": "72. Trafikni filtrlash tushunchasini aniqlang.",
            "options": {
                "a": "Routerlar va xavfsizlik devorlari tomonidan IP paketlarini qayta ishlash, bu ba'zi paketlarning tashlab yuborilishi yoki marshrutining o‘zgarishiga olib keladi.",
                "b": "Kompyuter tarmog‘ining bir qismini boshqa qismidan ma'lumotlarni himoya qilishni ta'minlaydigan, ular o‘rtasida o‘tadigan trafikni tahlil qilish va filtrlash orqali ishlaydigan dasturiy va apparat vositalar to‘plami.",
                "c": "Mijozlar ichki (himoyalangan) tarmoqqa, serverlar esa tashqi (potentsial xavfli) tarmoqqa tegishli deb hisoblangan holda, tarqatilgan tarmoq ilovalarining mijoz va server qismlari o‘rtasida vositachi sifatida ishlaydigan maxsus ilova turi.",
                "d": "Xizmat ko‘rsatish sifati shartnomalari, tarmoqni rejalashtirish va texnik nosozliklar, tahdidlar va zararli harakatlar kabi salbiy hodisalarni oldini olish uchun maxsus trafik parametrlarni doimiy instrumental avtomatlashtirilgan monitoring jarayoni.",
                "e": "Tarmoq trafigini va tizim subyektlari faoliyatini doimiy ravishda kuzatib, hujumlarni oldini olish, aniqlash va qayd etish uchun mo‘ljallangan dasturiy yoki apparat vositasi."
            },
            "correct": "a"
        },
        {
            "question": "73. Xavfsizlik devori tushunchasini aniqlang.",
            "options": {
                "a": "Routerlar va xavfsizlik devorlari tomonidan IP paketlarini qayta ishlash, bu ba'zi paketlarning tashlab yuborilishi yoki marshrutining o‘zgarishiga olib keladi.",
                "b": "Kompyuter tarmog‘ining bir qismini boshqa qismidan ma'lumotlarni himoya qilishni ta'minlaydigan, ular o‘rtasida o‘tadigan trafikni tahlil qilish va filtrlash orqali ishlaydigan dasturiy va apparat vositalar to‘plami.",
                "c": "Mijozlar ichki (himoyalangan) tarmoqqa, serverlar esa tashqi (potentsial xavfli) tarmoqqa tegishli deb hisoblangan holda, tarqatilgan tarmoq ilovalarining mijoz va server qismlari o‘rtasida vositachi sifatida ishlaydigan maxsus ilova turi.",
                "d": "Xizmat ko‘rsatish sifati shartnomalari, tarmoqni rejalashtirish va texnik nosozliklar, tahdidlar va zararli harakatlar kabi salbiy hodisalarni oldini olish uchun maxsus trafik parametrlarni doimiy instrumental avtomatlashtirilgan monitoring jarayoni.",
                "e": "Tarmoq trafigini va tizim subyektlari faoliyatini doimiy ravishda kuzatib, hujumlarni oldini olish, aniqlash va qayd etish uchun mo‘ljallangan dasturiy yoki apparat vositasi."
            },
            "correct": "b"
        },
        {
            "question": "74. Proksi-server tushunchasini aniqlang.",
            "options": {
                "a": "Routerlar va xavfsizlik devorlari tomonidan IP paketlarini qayta ishlash, bu ba'zi paketlarning tashlab yuborilishi yoki marshrutining o‘zgarishiga olib keladi.",
                "b": "Kompyuter tarmog‘ining bir qismini boshqa qismidan ma'lumotlarni himoya qilishni ta'minlaydigan, ular o‘rtasida o‘tadigan trafikni tahlil qilish va filtrlash orqali ishlaydigan dasturiy va apparat vositalar to‘plami.",
                "c": "Mijozlar ichki (himoyalangan) tarmoqqa, serverlar esa tashqi (potentsial xavfli) tarmoqqa tegishli deb hisoblangan holda, tarqatilgan tarmoq ilovalarining mijoz va server qismlari o‘rtasida vositachi sifatida ishlaydigan maxsus ilova turi.",
                "d": "Xizmat ko‘rsatish sifati shartnomalari, tarmoqni rejalashtirish va texnik nosozliklar, tahdidlar va zararli harakatlar kabi salbiy hodisalarni oldini olish uchun maxsus trafik parametrlarni doimiy instrumental avtomatlashtirilgan monitoring jarayoni.",
                "e": "Tarmoq trafigini va tizim subyektlari faoliyatini doimiy ravishda kuzatib, hujumlarni oldini olish, aniqlash va qayd etish uchun mo‘ljallangan dasturiy yoki apparat vositasi."
            },
            "correct": "c"
        },
        {
            "question": "75. Tarmoq trafigini monitoring qilish tushunchasini aniqlang.",
            "options": {
                "a": "Routerlar va xavfsizlik devorlari tomonidan IP paketlarini qayta ishlash, bu ba'zi paketlarning tashlab yuborilishi yoki marshrutining o‘zgarishiga olib keladi.",
                "b": "Kompyuter tarmog‘ining bir qismini boshqa qismidan ma'lumotlarni himoya qilishni ta'minlaydigan, ular o‘rtasida o‘tadigan trafikni tahlil qilish va filtrlash orqali ishlaydigan dasturiy va apparat vositalar to‘plami.",
                "c": "Mijozlar ichki (himoyalangan) tarmoqqa, serverlar esa tashqi (potentsial xavfli) tarmoqqa tegishli deb hisoblangan holda, tarqatilgan tarmoq ilovalarining mijoz va server qismlari o‘rtasida vositachi sifatida ishlaydigan maxsus ilova turi.",
                "d": "Xizmat ko‘rsatish sifati shartnomalari, tarmoqni rejalashtirish va texnik nosozliklar, tahdidlar va zararli harakatlar kabi salbiy hodisalarni oldini olish uchun maxsus trafik parametrlarni doimiy instrumental avtomatlashtirilgan monitoring jarayoni.",
                "e": "Tarmoq trafigini va tizim subyektlari faoliyatini doimiy ravishda kuzatib, hujumlarni oldini olish, aniqlash va qayd etish uchun mo‘ljallangan dasturiy yoki apparat vositasi."
            },
            "correct": "d"
        },
        {
            "question": "76. Kirishni aniqlash tizimi tushunchasini aniqlang.",
            "options": {
                "a": "Routerlar va xavfsizlik devorlari tomonidan IP paketlarini qayta ishlash, bu ba'zi paketlarning tashlab yuborilishi yoki marshrutining o‘zgarishiga olib keladi.",
                "b": "Kompyuter tarmog‘ining bir qismini boshqa qismidan ma'lumotlarni himoya qilishni ta'minlaydigan, ular o‘rtasida o‘tadigan trafikni tahlil qilish va filtrlash orqali ishlaydigan dasturiy va apparat vositalar to‘plami.",
                "c": "Mijozlar ichki (himoyalangan) tarmoqqa, serverlar esa tashqi (potentsial xavfli) tarmoqqa tegishli deb hisoblangan holda, tarqatilgan tarmoq ilovalarining mijoz va server qismlari o‘rtasida vositachi sifatida ishlaydigan maxsus ilova turi.",
                "d": "Xizmat ko‘rsatish sifati shartnomalari, tarmoqni rejalashtirish va texnik nosozliklar, tahdidlar va zararli harakatlar kabi salbiy hodisalarni oldini olish uchun maxsus trafik parametrlarni doimiy instrumental avtomatlashtirilgan monitoring jarayoni.",
                "e": "Tarmoq trafigini va tizim subyektlari faoliyatini doimiy ravishda kuzatib, hujumlarni oldini olish, aniqlash va qayd etish uchun mo‘ljallangan dasturiy yoki apparat vositasi."
            },
            "correct": "e"
        },
        {
            "question": "77. Troyan dasturi tushunchasini aniqlang.",
            "options": {
                "a": "Boshqa fayllarga kiritilishi mumkin bo‘lgan zararli dasturiy fragment.",
                "b": "Foydali ilova sifatida yashirinib, tizimga zarar keltiradigan zararli dastur.",
                "c": "Masofadan boshqarish markazi buyruqlari asosida avtomatlashtirilgan harakatlarni amalga oshiradigan dastur tomonidan infiltratsiya qilingan tarmoq qurilmalari to‘plami.",
                "d": "Foydalanuvchi ishtirokisiz bir kompyuterdan boshqasiga o‘tib, mahalliy tarmoq va global ulanishlar orqali o‘z nusxalarini mustaqil ravishda tarqatadigan dastur.",
                "e": "Muayyan shartlar ostida hujjatsiz funksiyalarni ishga tushiradigan, ma'lumotga ruxsatsiz ta'sirlarni amalga oshirish imkonini beruvchi dasturiy ta'minotga kiritilgan obyekt."
            },
            "correct": "b"
        },
        {
            "question": "78. Tarmoq qurti tushunchasini aniqlang.",
            "options": {
                "a": "Foydalanuvchi ishtirokisiz bir kompyuterdan boshqasiga o‘tib, mahalliy tarmoq va global ulanishlar orqali o‘z nusxalarini mustaqil ravishda tarqatadigan dastur.",
                "b": "Boshqa fayllarga kiritilishi mumkin bo‘lgan zararli dasturiy fragment.",
                "c": "Muayyan shartlar ostida hujjatsiz funksiyalarni ishga tushiradigan, ma'lumotga ruxsatsiz ta'sirlarni amalga oshirish imkonini beruvchi dasturiy ta'minotga kiritilgan obyekt.",
                "d": "Masofadan boshqarish markazi buyruqlari asosida avtomatlashtirilgan harakatlarni amalga oshiradigan dastur tomonidan infiltratsiya qilingan tarmoq qurilmalari to‘plami."
            },
            "correct": "a"
        },
        {
            "question": "79. Kompyuter virusi tushunchasini aniqlang.",
            "options": {
                "a": "Foydalanuvchi ishtirokisiz bir kompyuterdan boshqasiga o‘tib, mahalliy tarmoq va global ulanishlar orqali o‘z nusxalarini mustaqil ravishda tarqatadigan dastur.",
                "b": "Boshqa fayllarga kiritilishi mumkin bo‘lgan zararli dasturiy fragment.",
                "c": "Muayyan shartlar ostida hujjatsiz funksiyalarni ishga tushiradigan, ma'lumotga ruxsatsiz ta'sirlarni amalga oshirish imkonini beruvchi dasturiy ta'minotga kiritilgan obyekt.",
                "d": "Masofadan boshqarish markazi buyruqlari asosida avtomatlashtirilgan harakatlarni amalga oshiradigan dastur tomonidan infiltratsiya qilingan tarmoq qurilmalari to‘plami."
            },
            "correct": "b"
        },
        {
            "question": "80. Dasturiy ta'minotdagi orqa eshik tushunchasini aniqlang.",
            "options": {
                "a": "Foydalanuvchi ishtirokisiz bir kompyuterdan boshqasiga o‘tib, mahalliy tarmoq va global ulanishlar orqali o‘z nusxalarini mustaqil ravishda tarqatadigan dastur.",
                "b": "Boshqa fayllarga kiritilishi mumkin bo‘lgan zararli dasturiy fragment.",
                "c": "Muayyan shartlar ostida hujjatsiz funksiyalarni ishga tushiradigan, ma'lumotga ruxsatsiz ta'sirlarni amalga oshirish imkonini beruvchi dasturiy ta'minotga kiritilgan obyekt.",
                "d": "Masofadan boshqarish markazi buyruqlari asosida avtomatlashtirilgan harakatlarni amalga oshiradigan dastur tomonidan infiltratsiya qilingan tarmoq qurilmalari to‘plami."
            },
            "correct": "c"
        },
        {
            "question": "81. Botnet tushunchasini aniqlang.",
            "options": {
                "a": "Foydalanuvchi ishtirokisiz bir kompyuterdan boshqasiga o‘tib, mahalliy tarmoq va global ulanishlar orqali o‘z nusxalarini mustaqil ravishda tarqatadigan dastur.",
                "b": "Boshqa fayllarga kiritilishi mumkin bo‘lgan zararli dasturiy fragment.",
                "c": "Muayyan shartlar ostida hujjatsiz funksiyalarni ishga tushiradigan, ma'lumotga ruxsatsiz ta'sirlarni amalga oshirish imkonini beruvchi dasturiy ta'minotga kiritilgan obyekt.",
                "d": "Masofadan boshqarish markazi buyruqlari asosida avtomatlashtirilgan harakatlarni amalga oshiradigan dastur tomonidan infiltratsiya qilingan tarmoq qurilmalari to‘plami."
            },
            "correct": "d"
        }
    ]
}

# News dataset
news_data = [
    {
        "type": "photo",
        "file_path": "news_dataset/photo/img1.png",
        "text": {
            "en": "New HTTPBot Botnet Launches 200+ Precision DDoS Attacks on Gaming and Tech Sectors \n\n Cybersecurity researchers are calling attention to a new botnet malware called HTTPBot that has been used to primarily single out the gaming industry, as well as technology companies and educational institutions in China. Over the past few months, it has expanded aggressively, continuously leveraging infected devices to launch external attacks, NSFOCUS said in a report published this week.By employing highly simulated HTTP Flood attacks and dynamic feature obfuscation techniques, it circumvents traditional rule-based detection mechanisms. HTTPBot, first spotted in the wild in August 2024, gets its name from the use of HTTP protocols to launch distributed denial-of-service attacks. Written in Golang, it's something of an anomaly given its targeting of Windows systems. The Windows-based botnet troja",
            "uz": "📸 Yangi mavzuni ko‘ring!",
            "ru": "📸 Посмотрите нашу новую тему!"
        }
    },
    {
        "type": "photo",
        "file_path": "news_dataset/photo/img2.png",
        "text": {
            "en": "Fake Security Plugin on WordPress Enables Remote Admin Access for Attackers\n\n Cybersecurity researchers have shed light on a new campaign targeting WordPress sites that disguises the malware as a security plugin.The plugin, which goes by the name WP-antymalwary-bot.php, comes with a variety of features to maintain access, hide itself from the admin dashboard, and execute remote code. Pinging functionality that can report back to a command-and-control (C&C) server is also included, as is code that helps spread malware into other directories and inject malicious JavaScript responsible for serving ads, Wordfence's Marco Wotschka said in a report. First discovered during a site cleanup effort in late January 2025, the malware has since been detected in the wild with new variants. Some of the other names used for the plugin are listed below -addons.php -wpconsole.php -wp-performance-booster.php -scr.php",
            "uz": "📸 Yangi mavzuni ko‘ring!",
            "ru": "📸 Посмотрите нашу новую тему!"
        }
    },
    {
        "type": "video",
        "file_path": "news_dataset/video/video1.mp4",
        "text": {
            "en": "🎥 Russia-Linked APT28 Exploited MDaemon Zero-Day to Hack Government Webmail Servers\n\n A Russia-linked threat actor has been attributed to a cyber espionage operation targeting webmail servers such as Roundcube, Horde, MDaemon, and Zimbra via cross-site scripting (XSS) vulnerabilities, including a then-zero-day in MDaemon, according to new findings from ESET. The activity, which commenced in 2023, has been codenamed Operation RoundPress by the Slovak cybersecurity company. It has been attributed with medium confidence to the Russian state-sponsored hacking group tracked as APT28, which is also referred to as BlueDelta, Fancy Bear, Fighting Ursa, Forest Blizzard, FROZENLAKE, Iron Twilight, ITG05, Pawn Storm, Sednit, Sofacy, and TA422. The ultimate goal of this operation is to steal confidential data from specific email accounts, ESET researcher Matthieu Faou said in a report shared with The Hacker News. Most victims are governmental entities and defense companies in Eastern Europe, although we have observed governments in Africa, Europe, and South America being targeted as well.",
            "uz": "🎥 Botimizga tezkor kirish!",
            "ru": "🎥 Быстрое знакомство с нашим ботом."
        }
    }
]

# User set to save first users ,using set to avoid duplicates
saved_users = set()

# User progress dictionary
user_progress = {}

# User selected topic to save selected topic temporarily to provide quizes
user_selected_topic = {}

# Language selection dictionary
user_language = {}

# Language-specific messages
messages = {
    "en": {

        "welcome": "Welcome! Please choose a language:",
        "choose_action": "Choose an action:",
        "choose_topic": "Choose a topic:",
        "start_quiz": "Start the quiz",
        "correct": "✅ Correct!",
        "incorrect": "❌ Incorrect! Correct answer: {correct}",
        "quiz_completed": "Quiz completed. Correct answers: {score} out of {total}",
        "start_quiz_prompt": "Please start the quiz via '📘 Quiz'.",
        "restart_quiz": "Please start the quiz again via '📘 Quiz'.",
        "intro": "🎓 *Welcome to Security QuizBot – your pocket learning companion!*\n\n"
                 "Here, learning becomes fun and engaging. Choose from various topics, explore helpful theory, and test your knowledge with short quizzes.\n\n"
                 "🧠 Learn smart.\n"
                 "🎯 Practice daily.\n"
                 "🏆 Track your improvement.\n\n"
                 "Ready to get started? Let’s grow your knowledge 🚀"
    },
    "ru": {
        "welcome": "Добро пожаловать! Пожалуйста, выберите язык:",
        "choose_action": "Выберите действие:",
        "choose_topic": "Выберите тему:",
        "start_quiz": "Начать викторину",
        "correct": "✅ Правильно!",
        "incorrect": "❌ Неправильно! Правильный ответ: {correct}",
        "quiz_completed": "Викторина завершена. Правильных ответов: {score} из {total}",
        "start_quiz_prompt": "Пожалуйста, начните викторину через '📘 Quiz'.",
        "restart_quiz": "Пожалуйста, начните викторину заново через '📘 Quiz'.",
        "intro": "🎓 *Добро пожаловать в Secure QuizBot – вашего карманного помощника в обучении!*\n\n"
                 "Здесь учиться легко и интересно. Выбирайте тему, изучайте теорию и проходите короткие викторины.\n\n"
                 "🧠 Учитесь с умом.\n"
                 "🎯 Практикуйтесь каждый день.\n"
                 "🏆 Отслеживайте прогресс.\n\n"
                 "Готовы начать? Давайте расти вместе 🚀"
    },
    "uz": {
        "welcome": "Xush kelibsiz! Iltimos, tilni tanlang:",
        "choose_action": "Harakatni tanlang:",
        "choose_topic": "Mavzuni tanlang:",
        "start_quiz": "Viktorinani boshlash",
        "correct": "✅ To‘g‘ri!",
        "incorrect": "❌ Noto‘g‘ri! To‘g‘ri javob: {correct}",
        "quiz_completed": "Viktorina yakunlandi. To‘g‘ri javoblar: {score}/{total}",
        "start_quiz_prompt": "Iltimos, viktorinani '📘 Viktorina' orqali boshlang.",
        "restart_quiz": "Iltimos, viktorinani yana '📘 Viktorina' orqali boshlang.",
        "intro": "🎓 *Secure QuizBot ga xush kelibsiz – sizning shaxsiy o‘quv yordamchingiz!*\n\n"
                 "Bu yerda o‘rganish qiziqarli va samarali bo‘ladi. Mavzuni tanlang, nazariyani o‘rganing va qisqa testlar orqali bilimlaringizni sinab ko‘ring.\n\n"
                 "🧠 Aql bilan o‘rganing.\n"
                 "🎯 Har kuni mashq qiling.\n"
                 "🏆 Rivojlanishingizni kuzating.\n\n"
                 "Boshlashga tayyormisiz? Keling, bilim sari birga odimlaylik! 🚀"
    }
}


# Function to draw languages buttons
def get_languages_menu(chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        types.KeyboardButton("O‘zbek"),
        types.KeyboardButton("Русский"),
        types.KeyboardButton("English")
    )
    bot.send_message(chat_id, "🇺🇿 Tilni tanlang / 🇷🇺 Выберите язык / 🇬🇧 Choose a language:", reply_markup=markup)


# Function to draw actions buttons
def get_actions_menu(lang):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        types.KeyboardButton(
            "📘 Viktorina" if lang == "uz" else "📘 Викторина" if lang == "ru" else "📘 Quiz"),
        types.KeyboardButton(
            "📘 Teoriya" if lang == "uz" else "📘 Теория" if lang == "ru" else "📘 Theory"),
        types.KeyboardButton(
            "📘 Yangiliklarni olish" if lang == "uz" else "📘 Получить новости" if lang == "ru" else "📘 Get news"),
        types.KeyboardButton(
            "📘 Ortga" if lang == "uz" else "📘 Назад" if lang == "ru" else "📘 Back")
    )
    return markup


# Function to make text available due to 4096 character should be  in one message according toTelegram rule,
def split_message(text, chunk_size=4000):
    lines = text.split('\n')
    chunks = []
    current_chunk = ""

    for line in lines:
        if len(current_chunk) + len(line) + 1 <= chunk_size:
            current_chunk += line + "\n"
        else:
            chunks.append(current_chunk)
            current_chunk = line + "\n"

    if current_chunk:
        chunks.append(current_chunk)
    return chunks


def get_user_language(lang_code: str) -> str:
    """
    Maps a Telegram language code to a supported language key.

    Args:
        lang_code (str): The Telegram language code (e.g., 'uz', 'ru', 'en').

    Returns:
        str: The corresponding language key used in your app ('uz', 'ru', or 'en').
    """
    if lang_code == "uz":
        return "uz"
    elif lang_code == "ru":
        return "ru"
    else:
        return "en"


def get_localized_data(lang: str, uz_data, en_data, ru_data):
    """
    Returns the appropriate dataset based on the selected language.

    Args:
        lang (str): Language key ('uz', 'en', or 'ru').
        uz_data: Data for Uzbek.
        en_data: Data for English.
        ru_data: Data for Russian.

    Returns:
        The dataset corresponding to the language.
    """

    return uz_data if lang == "uz" else en_data if lang == "en" else ru_data


# /start menu
@bot.message_handler(commands=['start'])
def start_handler(message):
    """
      Handles the /start command sent by the user.

      This function:
      - Detects the user's language (Uzbek, Russian, or English)
      - Sends an introductory message
      - Displays the language selection menu
      - Saves the user ID if it's their first interaction

      Args:
          message (telebot.types.Message): The incoming message object from the user.

      Returns:
          NOne
      """

    user_id = message.from_user.id
    chat_id = message.chat.id
    lang_code = message.from_user.language_code
    # lang = "uz" if lang_code == "uz" else "ru" if lang_code == "ru" else "en"
    lang = get_user_language(message.from_user.language_code)

    user_language[user_id] = lang
    # ✅ Save user if not already saved
    if user_id not in saved_users:
        saved_users.add(user_id)
    bot.send_message(chat_id, messages[lang]["intro"], parse_mode="Markdown")
    get_languages_menu(message.chat.id)
    user_language[user_id] = None  # Reset language selection


# Language selection
@bot.message_handler(func=lambda message: message.text in ["English", "Русский", "O‘zbek"])
def language_handler(message):
    """
    Handles the language selection message from the user.

    This function:
    - Sets the selected language ('en', 'ru', or 'uz') for the user
    - Updates the `user_language` dictionary
    - Sends the user an action menu in the selected language

    Args:
        message (telebot.types.Message): The incoming message containing the selected language.

    Returns:
        None
    """

    user_id = message.from_user.id
    lang = get_user_language(message.from_user.language_code)
    user_language[user_id] = lang
    markup = get_actions_menu(lang)
    # Add the "Back to Language Selection" button
    bot.reply_to(message, messages[lang]["choose_action"], reply_markup=markup)


# Quiz selection
@bot.message_handler(func=lambda message: message.text in ["📘 Quiz", "📘 Викторина", "📘 Viktorina"])
def quiz_handler(message):
    user_id = message.from_user.id
    if user_id not in user_language or user_language[user_id] is None:
        bot.reply_to(message, messages["en"]["welcome"])
        return
    lang = user_language[user_id]
    # topics = topics_uz if lang == "uz" else topics_eng if lang == "en" else topics_ru
    topics = get_localized_data(lang, topics_uz, topics_eng, topics_ru)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for topic in topics.keys():
        markup.add(types.KeyboardButton(topic))

    bot.set_state(user_id, "from_quiz_side", message.chat.id)

    back_text = "Orqaga qaytish" if lang == "uz" else "Назад работа" if lang == "ru" else "Back to actions"
    markup.add(types.KeyboardButton(back_text))
    bot.reply_to(message, messages[lang]["choose_topic"], reply_markup=markup)


# new code for thero selection
@bot.message_handler(func=lambda message: message.text in ["📘 Theory", "📘 Теория", "📘 Teoriya"])
def theory_handler(message):
    user_id = message.from_user.id
    if user_id not in user_language or user_language[user_id] is None:
        bot.reply_to(message, messages["en"]["welcome"])
        return
    lang = user_language[user_id]
    # topics = topics_uz if lang == "uz" else topics_eng if lang == "en" else topics_ru
    topics = get_localized_data(lang, topics_uz, topics_eng, topics_ru)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for topic in topics.keys():
        markup.add(types.KeyboardButton(topic))

    back_text = "Orqaga qaytish" if lang == "uz" else "Назад работа" if lang == "ru" else "Back to actions"
    markup.add(types.KeyboardButton(back_text))

    bot.set_state(user_id, "awaiting_theory_topic", message.chat.id)
    bot.reply_to(message, messages[lang]["choose_topic"], reply_markup=markup)


# news
@bot.message_handler(func=lambda message: message.text in ["📘 Get news", "📘 Получить новости", "📘 Get news"])
def news_handler(message):
    user_id = message.from_user.id
    if user_id not in user_language or user_language[user_id] is None:
        bot.reply_to(message, messages["en"]["welcome"])
        return
    lang = user_language[user_id]

    last_news_text = "🆕 So‘nggi yangilik" if lang == "uz" else "🆕 Последняя новость" if lang == "ru" else "🆕 Get Last News"
    all_news_text = "📚 Barcha yangiliklar" if lang == "uz" else "📚 Все новости" if lang == "ru" else "📚 Get All News"
    # back_to_news_main = "Yangilikarga qaytish" if lang == "uz" else "Вернуться к новостям" if lang == "ru" else "📚 Bact to news"
    back_to_action = "Orqaga qaytish" if lang == "uz" else "Назад работа" if lang == "ru" else "Back to actions"
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        types.KeyboardButton(last_news_text),
        types.KeyboardButton(all_news_text),
        types.KeyboardButton(back_to_action)
    )

    bot.send_message(message.chat.id, "📰 News options:", reply_markup=markup)
    bot.set_state(user_id, "awaiting_news_choice", message.chat.id)


# def send_news_item(chat_id, news, lang):
#     text = news["text"].get(lang, news["text"]["en"])
#     file_path = news["file_path"]
#
#     if news["type"] == "photo":
#         with open(file_path, 'rb') as photo:
#             bot.send_photo(chat_id, photo=photo, caption=text)
#     elif news["type"] == "video":
#         with open(file_path, 'rb') as video:
#             bot.send_video(chat_id, video=video, caption=text)

def send_news_item(chat_id, news, lang):
    text = news["text"].get(lang, news["text"]["en"])
    file_path = news["file_path"]

    # Truncate caption if it's too long
    max_caption_length = 1024
    if len(text) > max_caption_length:
        text = text[:1021] + "..."

    if news["type"] == "photo":
        with open(file_path, 'rb') as photo:
            bot.send_photo(chat_id, photo=photo, caption=text)
    elif news["type"] == "video":
        with open(file_path, 'rb') as video:
            bot.send_video(chat_id, video=video, caption=text)


@bot.message_handler(
    func=lambda message: bot.get_state(message.from_user.id, message.chat.id) == "awaiting_news_choice")
def news_choice_handler(message):
    user_id = message.from_user.id
    lang = user_language.get(user_id, "en")
    text = message.text

    if text in ["🆕 So‘nggi yangilik", "🆕 Последняя новость", "🆕 Get Last News"]:
        news = news_data[-1]
        send_news_item(message.chat.id, news, lang)

    elif text in ["📚 Barcha yangiliklar", "📚 Все новости", "📚 Get All News"]:
        for news in news_data:
            send_news_item(message.chat.id, news, lang)

    elif text in ["Orqaga qaytish", "Назад работа", "Back to actions"]:
        bot.delete_state(message.chat.id)
        markup = get_actions_menu(lang)
        bot.send_message(message.chat.id, messages[lang]["choose_action"], reply_markup=markup)

    else:
        bot.reply_to(message, "⚠️ Unknown option.")


# back button
@bot.message_handler(func=lambda message: message.text in ["📘 Ortga", "📘 Назад", "📘 Back"])
def back_to_language_selection(message):
    get_languages_menu(message.chat.id)


@bot.message_handler(func=lambda message: message.text in ["Orqaga qaytish", "Назад работа", "Back to actions"])
def back_to_actions_selection(message):
    # Detect language based on message text
    if message.text == "Orqaga qaytish":
        lang = "uz"
    elif message.text == "Назад работа":
        lang = "ru"
    elif message.text == "Back to actions":
        lang = "en"
    else:
        lang = "en"  # default fallback
    markup = get_actions_menu(lang)
    # bot.reply_to(message, messages[lang]["choose_action"], reply_markup=markup)
    bot.send_message(message.chat.id, messages[lang]["choose_action"], reply_markup=markup)


@bot.message_handler(
    func=lambda message: bot.get_state(message.from_user.id, message.chat.id) == "awaiting_theory_topic")
def send_theory(message):
    user_id = message.from_user.id
    lang = user_language.get(user_id, "en")  # Fallback to English
    topics = topics_uz if lang == "uz" else topics_eng if lang == "en" else topics_ru
    chosen_topic = message.text

    if chosen_topic in topics:
        theory_text = topics[chosen_topic]["theory"]

        chunks = split_message(theory_text)
        for chunk in chunks:
            bot.send_message(message.chat.id, chunk)
        bot.set_state(user_id, "theory_viewed", message.chat.id)

        user_selected_topic[user_id] = chosen_topic
        back_text = "Orqaga qaytish" if lang == "uz" else "Назад работа" if lang == "ru" else "Back to actions"

        reply_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        reply_keyboard.add(back_text)

        # Send question with inline options AND reply keyboard (back button)
        bot.send_message(message.chat.id, "👇", reply_markup=reply_keyboard)

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton(text="Start quiz", callback_data="action:start_quiz"))
        markup.add(types.InlineKeyboardButton(text="⬅️ Back to topics", callback_data="action:back_to_topics"))
        bot.send_message(message.chat.id, "Choose:", reply_markup=markup)


    else:
        bot.reply_to(message, messages[lang]["invalid_topic"])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        for topic in topics.keys():
            markup.add(types.KeyboardButton(topic))
        bot.send_message(message.chat.id, messages[lang]["choose_topic"], reply_markup=markup)


@bot.message_handler(func=lambda message: bot.get_state(message.from_user.id, message.chat.id) == "theory_viewed")
def handle_quiz_start_or_back(message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    lang = user_language.get(user_id, "en")
    user_input = message.text.lower()

    start_quiz_text = "Boshlash" if lang == "uz" else "Начать" if lang == "ru" else "Start quiz"
    back_text = "Ortga" if lang == "uz" else "Назад" if lang == "ru" else "Back to topics"

    if user_input == start_quiz_text:
        topic = user_selected_topic.get(user_id)

        if not topic:
            bot.send_message(chat_id, "⚠️ No topic selected. Please go back and choose a topic again.")
            return

        # Get quiz data
        quiz = topics_uz[topic]["quiz"] if lang == "uz" else topics_eng[topic]["quiz"] if lang == "en" else \
            topics_ru[topic]["quiz"]

        if not quiz:
            bot.send_message(chat_id, "❌ Quiz not available for this topic.")
            return

        # Save quiz data and start from question 0
        # user_quiz_progress[user_id] = {
        #     "topic": topic,
        #     "questions": quiz,
        #     "current_index": 0,
        #     "score": 0
        # }

        bot.set_state(user_id, "in_quiz", chat_id)
        # send_quiz_question(user_id, chat_id)

    elif user_input in ["⬅️ Ortga", "⬅️ Назад", "⬅️ Back to topics"]:
        # Go back to topic selection
        bot.set_state(user_id, "awaiting_theory_topic", chat_id)
        topics = topics_uz if lang == "uz" else topics_eng if lang == "en" else topics_ru

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        for topic in topics.keys():
            markup.add(types.KeyboardButton(topic))

        bot.send_message(chat_id, messages[lang]["choose_topic"], reply_markup=markup)

    else:
        bot.send_message(chat_id, "❓ Invalid option. Please choose again.")
        bot.set_state(user_id, "awaiting_theory_topic", chat_id)
        # topics = topics_uz if lang == "uz" else topics_eng if lang == "en" else topics_ru
        topics = get_localized_data(lang, topics_uz, topics_eng, topics_ru)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        for topic in topics.keys():
            markup.add(types.KeyboardButton(topic))

        bot.send_message(chat_id, messages[lang]["choose_topic"], reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data.startswith("action:"))
def handle_quiz_callback(call):
    user_id = call.from_user.id
    chat_id = call.message.chat.id
    lang = user_language.get(user_id, "en")
    # data = call.data
    data = call.data.split(":")[1]

    if data == "start_quiz":
        topic = user_selected_topic.get(user_id)
        if not topic:
            bot.send_message(chat_id, "⚠️ No topic selected. Please go back and choose a topic again.")
            return
        quiz = topics_uz[topic]["questions"] if lang == "uz" else \
            topics_eng[topic]["questions"] if lang == "en" else \
                topics_ru[topic]["questions"]

        # quiz = topics_uz[topic]["quiz"] if lang == "uz" else topics_eng[topic]["quiz"] if lang == "en" else topics_ru[topic]["quiz"]

        if not quiz:
            bot.send_message(chat_id, "❌ Quiz not available for this topic.")
            return

            # ✅ Initialize quiz progress here
        user_progress[user_id] = {
            "language": lang,
            "topic": topic,
            "index": 0,
            "score": 0
        }
        bot.set_state(user_id, "in_quiz", chat_id)
        send_question(chat_id, user_id)

    elif data == "back_to_topics":
        bot.set_state(user_id, "awaiting_theory_topic", chat_id)
        # topics = topics_uz if lang == "uz" else topics_eng if lang == "en" else topics_ru
        topics = get_localized_data(lang, topics_uz, topics_eng, topics_ru)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        for topic in topics.keys():
            markup.add(types.KeyboardButton(topic))

        back_text = "Orqaga qaytish" if lang == "uz" else "Назад работа" if lang == "ru" else "Back to actions"
        markup.add(types.KeyboardButton(back_text))

        bot.send_message(chat_id, messages[lang]["choose_topic"], reply_markup=markup)

    bot.answer_callback_query(call.id)


# Start quiz for selected topic
@bot.message_handler(
    func=lambda message: message.text in topics_ru or message.text in topics_uz or message.text in topics_eng)
def start_quiz(message):
    user_id = message.from_user.id
    if user_id not in user_language or user_language[user_id] is None:
        bot.reply_to(message, messages["en"]["welcome"])
        return
    lang = user_language[user_id]
    # topics = topics_uz if lang == "uz" else topics_eng if lang == "en" else topics_ru
    topics = get_localized_data(lang, topics_uz, topics_eng, topics_ru)
    topic = message.text
    if topic not in topics:
        bot.reply_to(message, messages[lang]["choose_topic"])
        return
    user_progress[user_id] = {
        "topic": topic,
        "index": 0,
        "score": 0,
        "language": lang
    }
    send_question(message.chat.id, user_id)


# Start quiz for selected topic
@bot.message_handler(func=lambda message: bot.get_state(message.from_user.id, message.chat.id) == "from_quiz_side")
def start_quiz(message):
    user_id = message.from_user.id
    if user_id not in user_language or user_language[user_id] is None:
        bot.reply_to(message, messages["en"]["welcome"])
        return
    lang = user_language[user_id]
    # topics = topics_uz if lang == "uz" else topics_eng if lang == "en" else topics_ru
    topics = get_localized_data(lang, topics_uz, topics_eng, topics_ru)
    topic = message.text
    if topic not in topics:
        bot.reply_to(message, messages[lang]["choose_topic"])
        return
    user_progress[user_id] = {
        "topic": topic,
        "index": 0,
        "score": 0,
        "language": lang
    }
    send_question(message.chat.id, user_id)


# new code for printing theory by topic
@bot.message_handler(
    func=lambda message: message.text in topics_ru or message.text in topics_uz or message.text in topics_eng)
def start_quiz(message):
    user_id = message.from_user.id
    if user_id not in user_language or user_language[user_id] is None:
        bot.reply_to(message, messages["en"]["welcome"])
        return
    lang = user_language[user_id]
    topics = topics_uz if lang == "uz" else topics_eng if lang == "en" else topics_ru
    topic = message.text
    if topic not in topics:
        bot.reply_to(message, messages[lang]["choose_topic"])
        return
    user_progress[user_id] = {
        "topic": topic,
        "index": 0,
        "score": 0,
        "language": lang
    }
    theory_text = topics[topic]["theory"]
    # Send the theory text
    bot.reply_to(message, theory_text, parse_mode="Markdown")
    # send_question(message.chat.id, user_id)


# Send question to user
def send_question(chat_id, user_id):
    if user_id not in user_progress:
        lang = user_language.get(user_id, "en")
        bot.send_message(chat_id, messages[lang]["start_quiz_prompt"])
        return

    lang = user_progress[user_id]["language"]
    # topics = topics_uz if lang == "uz" else topics_eng if lang == "en" else topics_ru
    topics = get_localized_data(lang, topics_uz, topics_eng, topics_ru)

    topic = user_progress[user_id]["topic"]
    index = user_progress[user_id]["index"]
    # questions = topics[topic]
    questions = topics[topic]["questions"]

    # back_text = "Orqaga qaytish" if lang == "uz" else "Назад работа" if lang == "ru" else "Back to actions"
    #
    # reply_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # reply_keyboard.add(back_text)
    #
    # # Send question with inline options AND reply keyboard (back button)
    # bot.send_message(chat_id, message_text, reply_markup=reply_keyboard)

    if index >= len(questions):
        bot.send_message(
            chat_id,
            messages[lang]["quiz_completed"].format(
                score=user_progress[user_id]["score"],
                total=len(questions)
            )
        )
        del user_progress[user_id]  # Clear user progress after quiz completion
        return

    question = questions[index]
    # Formiramiz xabarni savol va to‘liq javob variantlari bilan
    options_text = "\n".join([f"{key}) {val}" for key, val in question["options"].items()])
    message_text = f"{question['question']}\n\n{options_text}"

    back_text = "Orqaga qaytish" if lang == "uz" else "Назад работа" if lang == "ru" else "Back to actions"

    reply_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    reply_keyboard.add(back_text)

    # Send question with inline options AND reply keyboard (back button)
    bot.send_message(chat_id, message_text, reply_markup=reply_keyboard)

    # Faqat harfli tugmalar (a, b, c va h.k.) yaratamiz
    markup = types.InlineKeyboardMarkup()
    for key in question["options"].keys():
        markup.add(types.InlineKeyboardButton(f"{key}", callback_data=key))

    bot.send_message(chat_id, message_text, reply_markup=markup)


# Handle user answers
@bot.callback_query_handler(func=lambda call: call.data in ['a', 'b', 'c', 'd', 'e'])
def answer_handler(call):
    user_id = call.from_user.id
    data = call.data

    if user_id not in user_progress:
        lang = user_language.get(user_id, "en")
        bot.send_message(call.message.chat.id, messages[lang]["restart_quiz"])
        return

    lang = user_progress[user_id]["language"]
    # topics = topics_uz if lang == "uz" else topics_eng if lang == "en" else topics_ru
    topics = get_localized_data(lang, topics_uz, topics_eng, topics_ru)
    topic = user_progress[user_id]["topic"]
    index = user_progress[user_id]["index"]
    # question = topics[topic][index]
    question = topics[topic]["questions"][index]
    correct = question["correct"]

    if data == correct:
        user_progress[user_id]["score"] += 1
        bot.send_message(call.message.chat.id, messages[lang]["correct"])
    else:
        bot.send_message(
            call.message.chat.id,
            messages[lang]["incorrect"].format(correct=correct)
        )

    user_progress[user_id]["index"] += 1
    send_question(call.message.chat.id, user_id)


# Start the bot
if __name__ == '__main__':
    print("Bot is running...")
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"Error occurred: {e}")
