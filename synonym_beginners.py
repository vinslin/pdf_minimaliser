import os
import regex_synonym as reg
import google.generativeai as genai
import time

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
                            "In a brief autobiographical sketch in a 1990 volume of collected writings\nT.H. Rigby described his early intellectual influences.1 As an undergraduate\nand Masters student at the University of Melbourne immediately after\nthe end of World War Two he was intellectually most stimulated by Karl\nMarx and Max Weber – although as he wrote: ‘I could never claim to be\na real disciple of either’. The influence of Marx was limited even at that\nearly stage by Rigby’s inability to accommodate Marx’s views on prop\u0002erty with what he knew of the social distribution of power and privilege\nin the USSR. The influence of Weber was far stronger. From the beginning\nRigby was excited by the linkages that could be made between Weber’s\ntypologies of authority and legitimation and actual social structures,\nincluding those of the Soviet Union.\nBut after completing his studies at the University of Melbourne \nhe put aside his interest in Weber for a decade and a half, while he\npursued empirical investigations of Soviet society and its political sys\u0002tem. His PhD thesis, at the University of London, was on ‘The selection\nof leading personnel in the Soviet state and Communist Party’,2 and\nhad a strong and pioneering orientation towards the painstaking col\u0002lection of data on officials. The accumulation of empirical knowledge\nand expertise continued during subsequent work in the UK Foreign\nOffice Research Department and the British Embassy in Moscow, and\nthen while teaching at the Canberra University College. It was only in\n1963, recently arrived at the Australian National University’s Research\nSchool of Social Sciences, that he found himself part of a working\ngroup on Weber and returned to a serious study of the great German.\nHe continued to be interested in Weber and used his concepts for the\nrest of his career                      ,,,,,\"get the hard english words from the above paragraph  i know only very basic english and get their easy synonyms and put it like this    ( 1.cruel== brutal 2.shed == hut  3.psychiatrist == mind doctor)\"",
                        ],
                    },
                    {
                        "role": "model",
                        "parts": [
                            "Here are the words presented as you requested:\n\n1. **Autobiographical:** About one's own life\n2. **Stimulated:** Excited \n3. **Disciple:** Follower\n4. **Accommodate:** Fit in\n5. **Distribution:** Sharing\n6. **Privilege:** Special advantage\n7. **Typologies:** Categories\n8. **Legitimation:** Making something official\n9. **Structures:** Systems\n10. **Empirical:** Based on experience\n11. **Personnel:** Staff\n12. **Pioneering:** Groundbreaking\n13. **Painstaking:** Careful\n14. **Accumulation:** Gathering \n",
                        ],
                    },
                    {
                        "role": "user",
                        "parts": [
                            "which is not sufficient They do indeed want to be your soldiers2 while you are not\nmaking war, but when war comes, they either flee or leave.\nIt should be little trouble for me to persuade anyone of this\npoint, because the present ruin ofItaly is caused by nothing\nother than its having relied for a period of many years on\nmercenary arms. These arms once made some progress for\nsome, and may have appeared bold among themselves; but\nwhen the foreigner came, they showed what they were.\nHence Charles, king of France, was allowed to seize Italy\nwith chalk.3 And he who said that our sins were the cause of\nit spoke the truth.4 But the sins were surely not those he\nbelieved, but the ones I have told of, and because these were\nthe sins of princes, they too have suffered the punishment\nfor them.\nI want to demonstrate better the failure of these arms.\nMercenary captains are either excellent men of arms or not:\nif they are, you cannot trust them because they always aspire to their own greatness, either by oppressing you, who\nare their patron, or by oppressing others contrary to your\nintention; but if the captain is not virtuous, he ruins you in\nthe ordinary way. And if one responds that whoever has\narms in hand will do this, mercenary or not, I would reply\nthat arms have to be employed either by a prince or by a\nrepublic. The prince should go in person, and perform himself the office of captain. The republic has to send its citizens, and when it sends one who does not turn out to be a  ,,,,,\"get the hard english words from the above paragraph  i know only very basic english and get their easy synonyms and put it like this    ( 1.cruel== brutal 2.shed == hut  3.psychiatrist == mind doctor)\"",
                        ],
                    },
                    {
                        "role": "model",
                        "parts": [
                            "Here are some of the more difficult words from the paragraph, along with simpler synonyms presented as you requested:\n\n1. **Mercenary:**  Hired soldier \n2. **Flee:** Run away\n3. **Ruin:** Destruction\n4. **Bold:** Brave \n5. **Seize:** Take by force\n6. **Virtuous:** Good \n7. **Oppressing:**  Treating cruelly \n8. **Patron:** Supporter \n9. **Contrary:** Opposite \n10. **Republic:** A country with elected leaders\n11. **Citizens:** People of a country\n",
                        ],
                    },
                    {
                        "role": "user",
                        "parts": [
                            "our times we have Ferdinand of Aragon, the present king of \nSpain. This man can be called an almost new prince because \nfrom being a weak king he has become by fame and by glory \nthe first king among the Christians; and, if you consider his \nactions, youl will find them all very great and some of them \nextraordinary. In the beginning of his reign he attacked \nGranada, and that enterprise was the foundation of his state. \nFirst, he made it at leisure and without fear of being inter\u0002fered with; he kept the minds of the barons of Castile \npreoccupied; while thinking of that war, they did not think \nof innovating. And in the meantime he acquired reputation \nand power2 over them which they did not perceive. He was \nable to sustain armies with money from the Church and the \npeople, and with that long war to lay a foundation for his \nown military, which later brought him honor. Besides this, \nin order to undertake greater enterprises, always making use \nof religion, he turned to an act of pious cruelty, expelling the \nMarranos from his kingdom and despoiling it of them;3 nor \ncould there be an example more wretched and rarer than \nthis. He attacked Africa under this same cloak, made his \ncampaign in Italy, and has lately attacked France;4 and so he \nhas always done and ordered great things, which have always \nkept the minds of his subjects in suspense and admiration, \nand occupied with their outcome. And his actions have \nfollowed upon one another in such a mode that he has never \nallowed an interval between them for men to be able to \nwork quietly against him. \nIt also helps very much for a prince to give rare exam\u0002ples of himself in governing internally, similar to those that      ,,,,,\"get the hard english words from the above paragraph  i know only very basic english and get their easy synonyms and put it like this    ( 1.cruel== brutal 2.shed == hut  3.psychiatrist == mind doctor)\"",
                        ],
                    },
                    {
                        "role": "model",
                        "parts": [
                            "Here are some of the more challenging words from the paragraph, presented with simpler synonyms as you requested:\n\n1. **Ferdinand of Aragon:**  A king in the past\n2. **Fame:** Being well-known\n3. **Glory:** Great achievement\n4. **Extraordinary:** Amazing, unusual\n5. **Enterprise:** Project, important task\n6. **Foundation:**  Starting point, base\n7. **Barons:** Important nobles\n8. **Castile:** A kingdom in Spain\n9. **Preoccupied:** Busy with something else\n10. **Innovating:** Making changes\n11. **Reputation:** What people think of you\n12. **Sustain:** Support\n13. **Pious:** Very religious\n14. **Cruelty:**  Brutal behavior\n15. **Expelling:**  Kicking out\n16. **Marranos:** A group of Jewish people\n17. **Despoiling:**  Robbing\n18. **Wretched:**  Awful\n19. **Campaign:**  Military operation\n20. **Suspense:**  Excitement and uncertainty\n21. **Admiration:**  Looking up to someone\n22. **Interval:**  Break, pause \n",
                        ],
                    },

                ]
            )

            response = chat_session.send_message(paragraph + "get the hard english words from the above paragraph i know only very basic english and get their easy synonyms and put it like this ( 1.cruel== brutal 2.shed == hut 3.psychiatrist == mind doctor) ")
            # print(response.text)
            matches_left, matches_right = reg.extract_words(response.text)
            # print(matches_left)
            # print(matches_right)
            return matches_left, matches_right
        except Exception as e:
            if attempt < max_retries - 1:
                time.sleep(2)  # Wait for 2 seconds before retrying
            else:
                return None



