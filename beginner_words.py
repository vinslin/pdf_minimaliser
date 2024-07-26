import time
import google.generativeai as genai
import regex as reg

# Configure the API key
genai.configure(api_key="AIzaSyBSlif-91q43MbqYypAxPnshlKIbFGAT2c")

# Create the model configuration
generation_config = {
  "temperature": 0,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

# Initialize the model
model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

def get_response(paragraph):
    max_retries = 5  # Maximum number of retries
    for attempt in range(max_retries):
        try:
            chat_session = model.start_chat(
                history=[
                    {
                        "role": "model",
                        "parts": [
                            "\n\n**1.  intellectual:**  A very smart person who spends a lot of time thinking about complicated ideas.\n**2.  influences:** Things or people that change how someone thinks.\n**3.  undergraduate:** A student at a college or university who is working towards their first degree.\n**4.  Masters student:** A student who continues studying at a university after their first degree to become even more knowledgeable.\n**5.  stimulated:** Made someone interested and excited to learn more.\n**6.  disciple:** A very dedicated follower who believes strongly in someone's teachings.\n**7.  accommodate:** To make space for something or to fit things together.\n**8.  property:** Things that people own, like land, houses, or possessions.\n**9.  linkages:** Connections or relationships between things.\n**10. typologies:**  Ways of organizing things into different categories or types.\n**11. authority:** The power someone has to make decisions and give orders.\n**12. legitimation:** Making something seem right, acceptable, or official.\n**13. pursued:** Followed a path or tried to achieve something.\n**14. empirical:** Based on real-world observations and evidence, not just ideas.\n**15. thesis:** A long and important research paper written for a high-level university degree.\n**16. personnel:** People who work for an organization.\n**17. pioneering:**  Being the first to do something new and important.\n**18. painstaking:** Done with extreme care and attention to detail.\n**19. subsequent:** Happening later or afterward.\n**20. concepts:**  Important ideas. \n \n",
                        ],
                    },
                    {
                        "role": "user",
                        "parts": [
                            "Doc-Handler: Document Scanner, Manipulator, and Translator based on\nImage and Natural language processing Nilesh P. Sable;Priya Shelke;Ninad\nDeogaonkar;Nachiket Joshi;Rudra Kabadi;Tushar Joshi2023 International\nConference on Emerging Smart Computing and Informatics (ESCI)Year:\n2023 | Conference Paper | Publisher: IEEE\nPhysical documents may easily be converted into digital versions in the modern digital\nera by employing scanning software and the internet. The day when this activity needed printers\nand scanners is long gone. Nowadays, even our smartphones and cameras may be used to\nquickly convert paper documents into digital ones. This is especially useful in the wake of the\nCOVID-19 pandemic, where the ability to share and access documents online is more\nimportant than ever. This study proposes an application for illiterate people to quickly translate\nscanned papers or photos into their native language and save them in a digital format. The\nApplication makes use of image processing methods and has capabilities including PDF\nconversion, image colour adjustment, cropping, and Optical Character Recognition (OCR). \"get the hard english words i know only very basic english show it like 1.cruel== extremely unkind and unpleasant 2.kind==very cruel and violent \"",
                        ],
                    },
                    {
                        "role": "model",
                        "parts": [
                            "\n\n1. **Manipulator:**  Something that changes or controls something else. Think of it like a puppeteer controlling a puppet.\n2. **Natural language processing:** Teaching computers to understand and use human language, like English or Spanish.\n3. **Emerging:**  New and becoming more important.\n4. **Informatics:**  How people use information, especially with computers.\n5. **Convert:** To change something from one form to another, like changing a paper document into a digital one.\n6. **Application:** A program on a phone or computer that does something specific, like a game or a translator.\n7. **Illiterate:**  Someone who cannot read or write.\n8. **Capabilities:** Things the application can do.\n9. **Conversion:**  Changing something from one form to another.\n10. **Adjustment:** Making small changes to improve something.\n11. **Cropping:** Cutting off the edges of an image.\n12. **Optical Character Recognition (OCR):**  Teaching computers to \"read\" text from images. \n",
                        ],
                    },
                    {
                        "role": "user",
                        "parts": [
                            "which is not sufficient They do indeed want to be your soldiers2 while you are not\nmaking war, but when war comes, they either flee or leave.\nIt should be little trouble for me to persuade anyone of this\npoint, because the present ruin ofItaly is caused by nothing\nother than its having relied for a period of many years on\nmercenary arms. These arms once made some progress for\nsome, and may have appeared bold among themselves; but\nwhen the foreigner came, they showed what they were.\nHence Charles, king of France, was allowed to seize Italy\nwith chalk.3 And he who said that our sins were the cause of\nit spoke the truth.4 But the sins were surely not those he\nbelieved, but the ones I have told of, and because these were\nthe sins of princes, they too have suffered the punishment\nfor them.\nI want to demonstrate better the failure of these arms.\nMercenary captains are either excellent men of arms or not:\nif they are, you cannot trust them because they always aspire to their own greatness, either by oppressing you, who\nare their patron, or by oppressing others contrary to your\nintention; but if the captain is not virtuous, he ruins you in\nthe ordinary way. And if one responds that whoever has\narms in hand will do this, mercenary or not, I would reply\nthat arms have to be employed either by a prince or by a\nrepublic. The prince should go in person, and perform himself the office of captain. The republic has to send its citizens, and when it sends one who does not turn out to be a\"get the hard english words he know only very basic english so i want to mark it a show it like 1.cruel== extremely unkind and unpleasant 2.kind==very cruel and violent \"\"get the hard english words he  know only very basic english so i want to mark it and show it like 1.cruel== extremely unkind and unpleasant 2.kind==very cruel and violent \"",
                        ],
                    },
                    {
                        "role": "model",
                        "parts": [
                            "\n\n1. **sufficient:**  Enough, adequate. Think of it like having *sufficient* food for everyone at dinner.\n2. **flee:** To run away from danger, to escape. Imagine a deer *fleeing* from a hunter.\n3. **persuade:** To convince someone to believe or do something.  A salesperson tries to *persuade* you to buy something.\n4. **ruin:** The state of being destroyed or badly damaged.  A powerful storm can leave a town in *ruin*.\n5. **relied:** Depended on, trusted in.  You *rely* on a bridge to hold your weight when you walk across it.\n6. **mercenary:** A soldier who fights for money, not for a specific country or cause. Think of them as hired guns.\n7. **bold:** Brave and confident, daring.  A *bold* knight charges into battle without fear.\n8. **foreigner:** A person from another country. If you travel to a new country, you are a *foreigner* there.\n9. **seize:** To take something quickly and forcefully. A hawk might *seize* a mouse with its talons.\n10. **chalk:** A soft, white rock used for writing or drawing.  The phrase \"seize Italy with chalk\" means to conquer it easily, without much effort.\n11. **sins:** Actions that are considered morally wrong.  Lying and stealing are often considered *sins*.\n12. **princes:**  Rulers of countries or regions, often with inherited power.  Think of kings or queens.\n13. **punishment:**  A penalty for doing something wrong.  Going to jail is a *punishment* for breaking the law.\n14. **demonstrate:** To show or prove something clearly.  A scientist might do an experiment to *demonstrate* a theory.\n15. **failure:**  Lack of success.  A project that doesn't work out is a *failure*.\n16. **captains:** Leaders of soldiers or ships.  A *captain* commands a group of warriors.\n17. **trust:** To believe in the reliability of someone or something. You *trust* your friends to keep your secrets.\n18. **aspire:**  To aim for something great, to have a strong desire to achieve something. A student might *aspire* to become a doctor.\n19. **greatness:**  The quality of being important and outstanding. Famous historical leaders often achieve *greatness*.\n20. **oppressing:**  To control or govern someone harshly or unfairly. A cruel ruler *oppresses* the people.\n21. **patron:**  A supporter or sponsor.  A *patron* of the arts funds artists and musicians.\n22. **virtuous:**  Having good moral qualities.  A *virtuous* person tells the truth and helps others.\n23. **republic:** A country where the power is held by the people or their elected representatives. The United States is a *republic*.\n24. **citizens:**  Members of a country who have rights and responsibilities. *Citizens* vote in elections.\n25. **employed:** Used or hired for a job. A company *employs* workers to do tasks.\n",
                        ],
                    },
                ],
            )

            response = chat_session.send_message(paragraph+"get the hard english words he know only very basic english so i want to mark it and show it like,please give answers in this format  1.cruel: extremely unkind and unpleasant 2.kind:very cruel and violent ")

            matches_left,matches_right=reg.extract_words(response.text)
    
            return matches_left,matches_right

        except Exception as e:
            #print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < max_retries - 1:
                time.sleep(2)  # Wait for 2 seconds before retrying
            else:
              #  print("Max retries reached. Please try again later.")
                return None


