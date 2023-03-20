"""
Approach:- 

Read the complete input file using readlines command and store it in a list with each line represented as a string. 
Take this list and start processing each element.
Break each element into a series of space-delimited segments and identify whether the first element is ADD or DEL. 
    If first element is ADD, identify whether the second element is PATIENT or EXAM. 
        If second element is PATIENT then extract the patient identifier and check whether it already exists- 
            if it exists then we move to the second instruction from our main data list.
            if it doesn't exist, we will add the patient identifier as a new key to a patient record dictionary and add the name of the patient as an element in its value which will be of list data type.
        If second element is EXAM then extract the patient identifier and check whether it exists-
            if it exists then check whether the exam identifier exists-
                if it doesn't exist, add the new exam identifier in the patient record dictionary
                if it exists, ignore the instruction and move to the next instruction in our main data list
            if it doesn't exist, then ignore the instruction and move to the new instruction in our main data list
    If first element is DEL, check whether the second element is PATIENT or EXAM-
        if second element is PATIENT, extract the patient identifier number and whether it exists-
            if it exists, then delete the patient record along with the exam record for that patient from our patient record dictionary
            if it doesn't exist, then ignore the instruction and move to new instruction from our patient record dictionary
        if second element is EXAM, extract the exam identifier number and check whether it exists-
            if it exists, delete the specific exam record
            if it doesn't exist, ignore the instruction and move to new instruction from out patient record dictionary
"""

''' Assumption: The exam record IDs will be unique, i.e. two patients can't have the same exam ID'''

''' Please run the file from backend folder '''

import os

def addPatient(record,patient_record,exam_record):
    p_id = record[0]
    first_name = record[1]
    last_name = record[2]
    if p_id in patient_record: #edge case
        return 'patient already exists'
    else:
        patient_record[p_id] = first_name + " " + last_name #storing new patient data in the dictionary
        exam_record[p_id] = {} #creating an empty exam record for newly added patient #used a dictionary instead of list to reduce complexity
        return 'new patient added'

def addExam(record,patient_record,exam_record):
    patient_id = record[0]
    exam_id = record[1]
    if patient_id in patient_record:
        for p_id in exam_record:
            if exam_id in exam_record[p_id]: #edge case
                return 'exam ID already exists'

        exam_record[patient_id][exam_id] = True #if this exam_id doesn't exist add it to exam record
        return 'exam ID added'
    else:
        return 'no patient record' #edge case

def delPatient(record,patient_record,exam_record):
    if record in patient_record:
        patient_record.pop(record)
        exam_record.pop(record) #remove record from both data structures
        return 'patient record deleted'
    else:
        return "patient doesn't exists" #edge case

def delExam(record,exam_record):
    for p_id in exam_record:
        if record in exam_record[p_id]:
            exam_record[p_id].pop(record) #remove record if found
            return 'exam record deleted'
    else:
        return "exam record doesn't exists" # edge case

def patientSummary(patient_record,exam_record):
    str = ""
    for p_id in patient_record:
        str = str + f'Name: {patient_record[p_id]}, ID: {p_id}, Exam Count: {len(exam_record[p_id]) if p_id in exam_record else 0}\n'    
    return str

def main():
    curr_path = os.getcwd()
    file_name = 'input1.txt' #file name of the test file
    file = open(f'{curr_path}/../input/{file_name}','r') #please run the file from backend folder
    data = file.readlines() #opening the file and storing all lines in memory
    patient_record = {} #using a dictionary to have O(1) time complexity for most functionalities
    exam_record = {} #using a dictionary to have O(1) time complexity for most functionalities

    for record_line in data: #processing each command one-by-one
        instruction = record_line.split() #using python's split() method to process every part of the instruction
        if instruction[0] == 'ADD':
            if instruction[1] == 'PATIENT':
                msg = addPatient(instruction[2:],patient_record,exam_record)

            else: # it is EXAM
                msg = addExam(instruction[2:],patient_record,exam_record)
            
        else: # it is DEL
            if instruction[1] == 'PATIENT':
                msg = delPatient(instruction[2],patient_record,exam_record)
        
            else: # it is EXAM
                msg = delExam(instruction[2],exam_record)

    print(patientSummary(patient_record,exam_record))

main()
