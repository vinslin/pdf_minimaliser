"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""

import os
import time
import minimalizer_regex as reg
import google.generativeai as genai

genai.configure(api_key="AIzaSyBSlif-91q43MbqYypAxPnshlKIbFGAT2c")

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": 0,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

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
                        "role": "user",
                        "parts": [
                            "which is not sufficient They do indeed want to be your soldiers2 while you are not\nmaking war, but when war comes, they either flee or leave.\nIt should be little trouble for me to persuade anyone of this\npoint, because the present ruin ofItaly is caused by nothing\nother than its having relied for a period of many years on\nmercenary arms. These arms once made some progress for\nsome, and may have appeared bold among themselves; but\nwhen the foreigner came, they showed what they were.\nHence Charles, king of France, was allowed to seize Italy\nwith chalk.3 And he who said that our sins were the cause of\nit spoke the truth.4 But the sins were surely not those he\nbelieved, but the ones I have told of, and because these were\nthe sins of princes, they too have suffered the punishment\nfor them.\nI want to demonstrate better the failure of these arms.\nMercenary captains are either excellent men of arms or not:\nif they are, you cannot trust them because they always aspire to their own greatness, either by oppressing you, who\nare their patron, or by oppressing others contrary to your\nintention; but if the captain is not virtuous, he ruins you in\nthe ordinary way. And if one responds that whoever has\narms in hand will do this, mercenary or not, I would reply\nthat arms have to be employed either by a prince or by a\nrepublic. The prince should go in person, and perform himself the office of captain. The republic has to send its citizens, and when it sends one who does not turn out to be a...\"get the hard english words i know intermediate level of english so i want to mark it a show it like show the hard words and give replacement words that would not affect the paragraph and listout it like painstaking -> careful\nempirical -> data based\ntypologies - >classifications \"",
                        ],
                    },
                    {
                        "role": "model",
                        "parts": [
                            "Here are some words and phrases from the text that you might find challenging, along with simpler replacements:\n\n\n* **sufficient** -> enough\n* **indeed**  ->  really \n* **flee** -> run away\n* **ruin** -> destruction\n* **mercenary arms** -> hired soldiers\n* **bold** -> brave\n* **foreigner** -> outsider\n* **seize** -> take over\n* **chalk** -> easily (This refers to an idiom about something being incredibly easy.) \n* **demonstrate** -> show\n* **failure** -> shortcomings\n* **aspire to**  -> hope for\n* **greatness** -> power\n* **oppressing** -> hurting\n* **patron** -> supporter\n* **virtuous** -> good, honorable\n* **in the ordinary way** -> in the usual way\n* **employed** -> used\n* **republic** -> a country with elected leaders\n* **perform the office of** -> do the job of\n\n\n\n",
                        ],
                    },
                    {
                        "role": "user",
                        "parts": [
                            "In a brief autobiographical sketch in a 1990 volume of collected writings\nT.H. Rigby described his early intellectual influences.1 As an undergraduate\nand Masters student at the University of Melbourne immediately after\nthe end of World War Two he was intellectually most stimulated by Karl\nMarx and Max Weber – although as he wrote: ‘I could never claim to be\na real disciple of either’. The influence of Marx was limited even at that\nearly stage by Rigby’s inability to accommodate Marx’s views on prop\u0002erty with what he knew of the social distribution of power and privilege\nin the USSR. The influence of Weber was far stronger. From the beginning\nRigby was excited by the linkages that could be made between Weber’s\ntypologies of authority and legitimation and actual social structures,\nincluding those of the Soviet Union.\nBut after completing his studies at the University of Melbourne \nhe put aside his interest in Weber for a decade and a half, while he\npursued empirical investigations of Soviet society and its political sys\u0002tem. His PhD thesis, at the University of London, was on ‘The selection\nof leading personnel in the Soviet state and Communist Party’,2 and\nhad a strong and pioneering orientation towards the painstaking col\u0002lection of data on officials. The accumulation of empirical knowledge\nand expertise continued during subsequent work in the UK Foreign\nOffice Research Department and the British Embassy in Moscow, and\nthen while teaching at the Canberra University College. It was only in\n1963, recently arrived at the Australian National University’s Research\nSchool of Social Sciences, that he found himself part of a working\ngroup on Weber and returned to a serious study of the great German.\nHe continued to be interested in Weber and used his concepts for the\nrest of his career ..\"get the hard english words i know intermediate level intermediate level of english so i want to mark it a show it like show the hard words and give replacement words that would not affect the paragraph and listout it like painstaking -> careful\nempirical -> data based\ntypologies - >classifications \"",
                        ],
                    },
                    {
                        "role": "model",
                        "parts": [
                            "Here are some words and phrases from the text, potential replacements, and a list formatted as requested:\n\n\n* **autobiographical sketch** -> short story about his own life\n* **intellectual influences** -> thinkers who impacted his ideas\n* **stimulated** -> excited, interested\n* **disciple** -> follower\n* **accommodate** -> fit together, agree with\n* **distribution** -> how something is spread out\n* **USSR** -> Soviet Union (a historical country)\n* **linkages** -> connections\n* **typologies** -> classifications\n* **legitimation** -> making something seem right or official\n* **structures** -> systems, organizations\n* **pursued** -> followed\n* **empirical** -> data-based\n* **thesis** -> long research paper\n* **personnel** -> staff, workers\n* **pioneering** -> new and important \n* **orientation** -> focus\n* **painstaking** -> careful\n* **accumulation** -> gathering, collecting \n* **expertise** -> special knowledge\n* **subsequent** -> later\n* **embassy** -> the building where a country's representatives work in another country \n\n",
                        ],
                    },

                ]
            )
            response = chat_session.send_message(paragraph + """.."get the hard english words i know intermediate level of english so i want to mark it a show it like show the hard words and give replacement words that would not affect the paragraph and listout it like painstaking -> careful
                       empirical -> data based
                       typologies - >classifications""")

            matches_left, matches_right = reg.extract_words(response.text)

            return matches_left, matches_right

        except Exception as e:
            if attempt < max_retries - 1:
                time.sleep(2)  # Wait for 2 seconds before retrying
            else:
                return None








