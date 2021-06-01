"""
covid_check.py

The program should ask a series of questions interactively.
Based on the users response, advice on the likelyhood of Covid.

Reference :
    https://www.who.int/emergencies/diseases/novel-coronavirus-2019/question-and-answers-hub/q-a-detail/coronavirus-disease-covid-19#:~:text=symptoms

"""
import sys 
import random

def answer2score(yes_or_no, severity):
    #return 1 if the value is yes or 0 otherwise
    score = 0 
    #if user input is yes or y (case insensitive) then consider as yes,
    # otherwise
    if (len(yes_or_no) == 0): #Empty meand user didnt answer
		score = -2
    elif ( yes_or_no.upper() in ["YES", "Y"] ):
        #if yes use the severity as the score
        score = severity
    else: #Anythin other than YES/Y is considered a No and a score of 0
		score = 0
    #return the score
    return score

def check_symptom(n, symptom, severity):
    #show the symptom and collect user input
    symptom_feedback = raw_input("{0}. {1} : ".format(n,symptom))
    #convert the user inpupt into score and return
    return answer2score(symptom_feedback, severity)

def check_symptom_list(symptom_list, randomize, threshold):
    response_list = []
    if(randomize):
        random.shuffle(symptom_list)
    score = 0 
    n = 0   #sequence number
    threshold_crossed = False
    #for each symptom in the list
    for symptom in symptom_list:
        #if score >= threshold, then no need to check for more symptmos.
        if(score >= threshold):
            if(threshold_crossed == False):
                threshold_crossed = True
                print("Current score({0}) crossed the threshold({1}).".
                        format(score, threshold))
    
            #store the user input
            response_list.append(-1)
        else:
            #show the symptom and collect user input transfaormed into a score
            response = check_symptom(n, symptom[0], symptom[1])

            #store the user input
            response_list.append(response)

            #increment the sequence number
            n += 1

            #calculate the total score accumulated
            if(response > 0):
                score += response

    #return the collected responses (in a list)
    return response_list, score

def generate_report(symptoms, response):
    #   
    # Print all the symptoms and user response
    # in a pretty form
    #   

    #Lets conver the score into Yes or No
    #if the score is 0 then No, otherwise Yes
    resp_str = "No"
    #for each symptom
    i = 0 
    max_len = 0 
    #go over each of the symptoms
    for symptom in symptoms:
        #calculate the length of the current symptom
        length = len(symptom[0])
        #update the max length if the current one is greater. else ignore.
        if(length > max_len):
            max_len = length

    for symptom in symptoms:
        #if response is not 0 then Yes.
        if(response[i] == 0): 
            resp_str = "No"
        elif(response[i] > 0): 
            resp_str = "Yes"
        elif (response[i] == -2):
			resp_str = "-"
        elif (response[i] == -1):
            resp_str = "NA"

        print("  {0}({1}) : {2}".format(symptom[0].rjust(max_len), 
            symptom[1], resp_str))
        i += 1

#
#Below is the list of individual symptoms along with
# respective severity
#
MILD_SYMPTOM = 1 
OTHER_SYMPTOM = 2 
SEVERE_SYMPTOM = 3 
RARE_SYMPTOM = 4 

symptoms = [ 
    #Mild Symptoms
    ("Fever", MILD_SYMPTOM),
    ("Dry cough", MILD_SYMPTOM),
    ("Fatigue", MILD_SYMPTOM),
    #Other Symptoms
    ("Loss of taste or smell", OTHER_SYMPTOM),
    ("Nasal congestion", OTHER_SYMPTOM),
    ("Conjunctivitis (red eyes)", OTHER_SYMPTOM),
    ("Sore throat", OTHER_SYMPTOM),
    ("Headache", OTHER_SYMPTOM),
    ("Muscle or joint pain", OTHER_SYMPTOM),
    ("Different types of skin rash", OTHER_SYMPTOM),
    ("Nausea or vomiting", OTHER_SYMPTOM),
    ("Diarrhea", OTHER_SYMPTOM),
    ("Chills or dizziness", OTHER_SYMPTOM),
    #Severe Symptoms
    ("Shortness of breath", SEVERE_SYMPTOM),
    ("Loss of appetite",SEVERE_SYMPTOM),
    ("Confusion",SEVERE_SYMPTOM),
    ("Persistent pain or pressure in the chest", SEVERE_SYMPTOM),
    ("High temperature (above 38 Celsius)", SEVERE_SYMPTOM),
    #Rare Symptoms
    ("Irritability", RARE_SYMPTOM),
    ("Confusion",RARE_SYMPTOM),
    ("Reduced consciousness (sometimes seizures)",RARE_SYMPTOM),
    ("Anxiety",RARE_SYMPTOM),
    ("Depression",RARE_SYMPTOM),
    ("Sleep disorders",RARE_SYMPTOM),
    ("Strokes", RARE_SYMPTOM),
    ("Brain inflammation",RARE_SYMPTOM),
    ("Delirium",RARE_SYMPTOM),
    ("Nerve damage", RARE_SYMPTOM)
    ]   


#control whether to randomize the questions or not
randomize_questions = False

#no need to ask questions if threshold score has reached or exceeded
threshold = 1000

if(len(sys.argv) > 1) and (sys.argv[1] == "1") :
    randomize_questions = True

if(len(sys.argv) > 2) :
    threshold = int(sys.argv[2])

#
# Collect user response
#
print("Please answer Yes/No to the below symptoms")
response, score = check_symptom_list(symptoms, randomize_questions, threshold)

#
#Generate Report
#
print("------------------------------")
print("Report : ")
print("  Randomized Questions : {0}, Threshold : {1}".
        format(randomize_questions, threshold))

generate_report(symptoms, response)

#
#Calculate score
#
print("------------------------------")
print("Score : {0}".format(score))

#
#Final Impression
#
print("------------------------------")
impression = "NONE"
if(score <= 2): 
    impression = "Ignorable Symptoms"
elif(score > 2 and score <= 3): 
    impression = "Onset Symptoms. Stay isolated. Watch for symptmos."
elif(score > 3 and score <= 5): 
    impression = "Progresive Symptoms. Use medication.\n\t Stay home isolated. Watch for symptoms."
elif(score > 5 and score <= 10):
    impression = "Sever Symptoms. Consult Doctor."
else:
    impression = "Call Emergency"


print("Impression : {0}".format(impression))

