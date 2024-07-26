import os
import google.generativeai as genai
import regex as reg
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
                            "The most common foundation of a patron-client relationship was\nhaving worked together, often many years previously, rather than the\ncommon birthplaces, schooling, clan or religion more usual in other\nsystems. This was because the patron had to have some confidence in\nthe capacity of the client to do the job. Even given the importance of\nnetworks, it was one’s position that determined status and rewards.\nThis was because this was a personalist politics operating within a very\nbureaucratic system. One would indeed try to have loyal clients in a\nrange of important organizational structures (rather than dominate\njust one structure), although support within the top levels of the most\nimportant of them, the party apparatus, was crucial. This view of how\nthings worked was very compatible with Rigby’s goal-rational category\nof legitimacy. While it was very job- and indeed performance-oriented,\nit was not incompatible with personalist relationships. Indeed in Soviet\ncircumstances it required them.\nGiven these views, it is not surprising that Rigby was the Kremlino\u0002logist par excellence – not in the proverbial and superficial sense of\nnoting the lineup on the Mausoleum, but through the deep knowledge\nof and fascination with who knew whom, who came from where, who\nsigned an obituary, and, very importantly, who worked and had worked\nwhere. His office was full of card files of biographies; he had all the\nhandbooks – the Soviet volumes of biographies of Central Committee\nmembers, the CIA handbooks, etc; he had research assistants, including\nthe inestimable Val Ogareff, combing newspapers for personnel details.\nHe loved nothing more than to give a seminar paper and eventually\npublish an article on the intricacies of the background and career links of\nsome cohort of officials.\nThis view of the Soviet world was also reflected in Rigby’s relative\nlack of interest – at least as reflected in his published work – in policy\nissues. Although, as we have seen, he did not reject the institutional\npluralist view, he was always a bit suspicious of it, and he did not do \"get the hard English words for me,,,,   i know intermediate level of English        ,,,, show it like 1.cruel : extremely unkind and unpleasant 2.cobbler : a person who makes or repairs shoes ,3. cider : a beverage made from juice pressed from apples\"",
                        ],
                    },
                    {
                        "role": "model",
                        "parts": [
                            "Here are some of the more challenging words from the text with simplified definitions    \n\n1. **patron-client relationship:** A relationship where a more powerful person (patron) provides support and protection to a less powerful person (client) in exchange for loyalty and service.\n2. **clan:** A large group of families claiming descent from a common ancestor.\n3. **personalist politics:** A political system where power and influence are based on personal relationships and loyalty rather than institutions or ideology.\n4. **bureaucratic:** Relating to a system of government or organization with many departments and complex rules and procedures.\n5. **apparatus:** The organizational structure of a political party or government.\n6. **compatible:** Able to exist or work together successfully.\n7. **goal-rational:** Focused on achieving specific goals through efficient and logical means.\n8. **legitimacy:** The right and acceptance of an authority, usually a governing law or a régime.\n9. **Kremlinologist:** An expert in the politics and policies of the Soviet Union, particularly those related to the Kremlin (the seat of the Soviet government).\n10. **proverbial:** Well-known, commonly spoken of.\n11. **Mausoleum:** A large tomb, especially one built of stone above ground.\n12. **cohort:** A group of people sharing a common characteristic, such as age or occupation.\n13. **institutional pluralist:**  A view that sees political power as being distributed among a variety of groups and institutions, rather than being concentrated in the hands of a single elite. \n",
                        ],
                    },
                    {
                        "role": "user",
                        "parts": [
                            "which is not sufficient They do indeed want to be your soldiers2 while you are not\nmaking war, but when war comes, they either flee or leave.\nIt should be little trouble for me to persuade anyone of this\npoint, because the present ruin ofItaly is caused by nothing\nother than its having relied for a period of many years on\nmercenary arms. These arms once made some progress for\nsome, and may have appeared bold among themselves; but\nwhen the foreigner came, they showed what they were.\nHence Charles, king of France, was allowed to seize Italy\nwith chalk.3 And he who said that our sins were the cause of\nit spoke the truth.4 But the sins were surely not those he\nbelieved, but the ones I have told of, and because these were\nthe sins of princes, they too have suffered the punishment\nfor them.\nI want to demonstrate better the failure of these arms.\nMercenary captains are either excellent men of arms or not:\nif they are, you cannot trust them because they always aspire to their own greatness, either by oppressing you, who\nare their patron, or by oppressing others contrary to your\nintention; but if the captain is not virtuous, he ruins you in\nthe ordinary way. And if one responds that whoever has\narms in hand will do this, mercenary or not, I would reply\nthat arms have to be employed either by a prince or by a\nrepublic. The prince should go in person, and perform himself the office of captain. The republic has to send its citizens, and when it sends one who does not turn out to be a \"get the hard English words for me,,,, i know intermediate level of English,,,, ,,,, i know intermediate level of English,,, show it like 1.cruel : extremely unkind and unpleasant 2.cobbler : a person who makes or repairs shoes ,3. cider : a beverage made from juice pressed from apples\"",
                        ],
                    },
                    {
                        "role": "model",
                        "parts": [
                            "Here are some of the more challenging words from the text with simplified definitions     \n\n1. **sufficient:** enough, adequate\n2. **flee:** run away, escape\n3. **mercenary:** a soldier who fights for any country or group that will pay them\n4. **bold:** brave, courageous\n",
                        ],
                    },
                    {
                        "role": "user",
                        "parts": [
                            "hold them; and one of the greatest and quickest remedies\nwould be for whoever acquires it to go there to live in\nperson. This would make that possession more secure and\nmore lasting, as the Turk has done in Greece. Despite all the\nother orders observed by him so as to hold that state, if he\nhad not gone there to live, it would not have been possible\nfor him to hold it. For if you stay there, disorders may be\nseen as they arise, and you can soon remedy them; if you\nare not there, disorders become understood when they are\ngreat and there is no longer a remedy. Besides this, the\nprovince is not despoiled by your officials; the subjects are\nsatisfied with ready access to the prince, so that they have\nmore cause to love him if they want to be good and, if they\nwant to be otherwise, more cause to fear him. Whatever\noutsider might want to attack that state has more hesitation\nin doing so; hence, when one lives in it, one can lose it with\nthe greatest difficulty.\nThe other, better remedy is to send colonies that are, as\nit were, fetters of that state, to one or two places, because it\nis necessary either to do this or to hold them with many\nmen-at-arms and infantry. One does not spend much on\ncolonies, and without expense of one's own, or with little,\none may send them and hold them; and one offends only\nthose from whom one takes fields and houses in order to\ngive them to new inhabitants-who are a very small part of\nthat state. And those whom he offends, since they remain\ndispersed and poor, can never harm him, while all the others\nremain on the one hand unhurt, and for this they should be\nquiet; on the other, they are afraid to err from fear that\nwhat happened to the despoiled might happen to them. I\nconclude that such colonies are not costly, are more faithful,\nand less offensive; and those who are offended can do no\nharm, since they are poor and dispersed as was said. For this\nhas to be noted: that men should either be caressed or elimi\u0002nated, because they avenge themselves for slight offenses\nbut cannot do so for grave ones; so the offense one does to a \"get the hard English words for me,,,, i know intermediate level of English ,,,,, i know intermediate level of English,,, , show it like 1.cruel : extremely unkind and unpleasant. 2.cobbler : a person who makes or repairs shoes . 3. cider : a beverage made from juice pressed from apples. dont give any examples \"",
                        ],
                    },
                    {
                        "role": "model",
                        "parts": [
                            "Here are some of the more challenging words from the text with simplified definitions  \n\n1. **remedy:** a solution to a problem\n2. **despoiled:** stolen from, plundered\n3. **subjects:** the people ruled by a king or queen\n4. **fetters:** chains or restraints\n5. **infantry:** soldiers who fight on foot\n6. **dispersed:** scattered, spread out\n7. **caressed:** treated with kindness and affection\n8. **eliminated:** completely removed or destroyed\n9. **grave:** very serious \n",
                        ],
                    },
                    {
                        "role": "user",
                        "parts": [
                            "man should be such that one does not fear revenge for it. \nBut when one holds a state with men-at-arms in place of \ncolonies, one spends much more since one has to consume \nall the income of that state in guarding it. So the acquisition \nturns to loss, and one offends much more because one harms \nthe whole state as one's army moves around for lodgings. \nEveryone feels this hardship, and each becomes one's en\u0002emy: and these are enemies that can harm one since they \nremain, though defeated, in their homes. From every side, \ntherefore, keeping guard in this way is as useless as keeping \nguard by means of colonies is useful. \nWhoever is in a province that is disparate, as was said, \nshould also make himself head and defender of the neigh\u0002boring lesser powers, and contrive to weaken the powerful \nin that province and to take care that through some accident \na foreigner as powerful as he does not enter there. And it will \nalways turn out that a foreigner will be brought in by those \nin the province who are malcontent either because of too \nmuch ambition or out of fear, as once the Aetolians were \nseen to bring the Romans into Greece; and in every other \nprovince they entered, they were brought in by its inhabi\u0002tants. And the order of things is such that as soon as a \npowerful foreigner enters a province, all those in it who are \nless powerful adhere to him, moved by the envy they have \nagainst whoever has held power over them. So with respect \nto these lesser powers, he has no trouble in gaining them, \nbecause all together they quickly and willingly make one \nmass with the state that he has acquired there. He has only to \nworry that these lesser powers may get too much force and \ntoo much authority; and with his forces and their support he \ncan easily put down those who are powerful, so as to remain \narbiter of that province in everything. And whoever does \nnot conduct this policy well will soon lose what he has \nacquired, and while he holds it, will have infinite difficulties \nand vexations within it        \"get the hard English words for me,,,, i know intermediate level of English ,,,, show it like 1.cruel : extremely unkind and unpleasant 2.cobbler : a person who makes or repairs shoes ,3. cider : a beverage made from juice pressed from apples\"",
                        ],
                    },
                    {
                        "role": "model",
                        "parts": [
                            "Here are some of the more challenging words from the text with simplified definitions  \n\n1. **disparate:** made up of different and unrelated parts\n2. **contrive:** to plan cleverly or deceitfully\n3. **malcontent:** a person who is dissatisfied and rebellious\n4. **adhere:** to stick firmly to something\n5. **arbiter:** a person who has the power to judge or decide something\n6. **vexations:** annoyances, troubles \n",
                        ],
                    },
                    {
                        "role": "user",
                        "parts": [
                            "to take on greater significance in later times, something to which we\nwill return.\nClearly Rigby was open to the possibility and aware of the limited\nreality of a variety of forms of political activity in the Soviet Union.\nHowever he was also eventually always at pains to keep it all, even the\nbureaucratic politics, in perspective. There might have been a lot of\npursuit of personal and group interests and policy conflict. But in the\nend the political system was what he described, in probably his most\nwidely known and quoted conceptualization of the Soviet system, as\n‘mono-organizational socialism’.33 We have already documented his\nirritation at the conflation of that concept and totalitarianism. He was\nat pains to point out that mono- did not mean monolithic.34\nThe features of mono-organizational socialism included the continu\u0002ing, if subsidiary, role of tradition and exchange (including in personal\nnetworks and the shadow economy). It had a politics, ‘in the sense of\ncompetition to influence decisions and their implementation, [being]\nmostly structured around the formal and the informal organizations \nof the official hierarchies’.35 But the fundamental feature of mono\u0002organizational socialism was the ‘leading role of the party’. Once the\nBolsheviks came to power ‘every field of social activity was soon to\nbecome the monopoly of an officially designated organization run by \na hierarchy of command that culminated in the party leadership, and\nthe whole complex of organizations to be welded into a single organ\u0002izational structure by the command hierarchy of the party apparatus.’36\nThe party determined the goals, structures and leading personnel of all\nsocial organizations; it had a monopoly of public communication and\ninformation; and was able to exercise an extraordinarily high level of\ncoercive control.\nAs far as Rigby was concerned Stalinism was mono-organizational\nsociety with the addition of personal tyranny (assisted by the use of\ncharismatic authority referred to above, as well as made possible by\ntechnological capacity).37 Stalin’s tyranny was not something histor\u0002ically unique – history is not short of murderous personal tyrannies.\nHowever mono-organizational socialism was historically unique.38 That\nwas one reason why mono-organizational socialism was able to survive\nthe death of Stalin and the end of his style of personal tyranny. Indeed\nthe system reverted to the form it had had before Stalin established his\npersonal dominance, a form of oligarchy. Post-Stalin, ‘an oligarchical\nsharing of supreme power painfully established itself and gradually\nacquired a fairly settled institutional shape. Those features of “Stalinism”\nthat had flowed from and supported the personal rule of the tyrant were             \"get the hard English words for me,,,, i know intermediate level of English ,,,, show it like 1.cruel : extremely unkind and unpleasant 2.cobbler : a person who makes or repairs shoes ,3. cider : a beverage made from juice pressed from apples\"",
                        ],
                    },
                    {
                        "role": "model",
                        "parts": [
                            "Here are some of the more challenging words from the text with simplified definitions  \n\n1. **subsidiary:** less important than but related to\n2. **conflation:** the merging of two or more things into one\n3. **totalitarianism:** a system of government that is centralized and dictatorial and requires complete subservience to the state.\n4. **monolithic:** large, powerful, and indivisible\n5. **shadow economy:** illicit economic activity existing alongside a country's official economy, e.g. black market transactions and undeclared work.\n6. **culminated:** reached a climax or point of highest development\n7. **apparatus:**  the organizational structure of a political party or government\n8. **coercive:**  relating to or using force or threats\n9. **tyranny:** cruel and oppressive government or rule\n10. **charismatic:** exercising a compelling charm that inspires devotion in others\n11. **oligarchy:** a small group of people having control of a country, organization, or institution. \n",
                        ],
                    },
                ]
            )

            response = chat_session.send_message(paragraph + """get the hard English words for me,,,,   i know intermediate level of English        ,,,, show it like 1.cruel : extremely unkind and unpleasant 2.cobbler : a person who makes or repairs shoes ,3. cider : a beverage made from juice pressed from apples   avoide this one ""here are some of the more challenging words from the text with simplified definitions:""")

            matches_left, matches_right = reg.extract_words(response.text)

            return matches_left, matches_right
        except Exception as e:
            if attempt < max_retries - 1:
                time.sleep(2)  # Wait for 2 seconds before retrying
            else:
                return None
