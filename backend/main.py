"""
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

def addPatient(record):
    p_id = record[0]
    first_name = record[1]
    last_name = record[2]
    if p_id in patient_record: 
        return 'patient already exists'
    else:
        patient_record[p_id] = first_name + " " + last_name
        exam_record[p_id] = {}
        return 'new patient added'

def addExam(record):
    patient_id = record[0]
    exam_id = record[1]
    if patient_id in patient_record:
        for p_id in exam_record:
            if exam_id in exam_record[p_id]:
                return 'exam ID already exists'

        exam_record[patient_id][exam_id] = True
        return 'exam ID added'
    else:
        return 'no patient record'

def delPatient(record):
    if record in patient_record:
        patient_record.pop(record)
        exam_record.pop(record)
        return 'patient record deleted'
    else:
        return "patient doesn't exists"

def delExam(record):
    for p_id in exam_record:
        if record in exam_record[p_id]:
            exam_record[p_id].pop(record)
            return 'exam record deleted'
    else:
        return "exam record doesn't exist"

def patientSummary():
    str = ""
    for key in patient_record:
        if key in exam_record:
            str = str + f'Name: {patient_record[key]}, ID: {key}, Exam Count: {len(exam_record[key])}' + '\n'
        else:
            str = str + f'Name: {patient_record[key]}, ID: {key}, Exam Count: 0' + '\n'
    
    return str


#add all to main function
file = open(r'/Users/shaliniagarwal/Documents/IdentifeyeHealth/git-folder/ih-coding-challenge/input/input3.txt','r') #change to generic file read form
data = file.readlines() #records
patient_record = {}
exam_record = {}

for d in data:
    instr = d.split()
    if instr[0] == 'ADD' and instr[1] == 'PATIENT': #if-else
        msg = addPatient(instr[2:])
    
    if instr[0] == 'ADD' and instr[1] == 'EXAM':
        msg = addExam(instr[2:])

    if instr[0] == 'DEL' and instr[1] == 'PATIENT':
        msg = delPatient(instr[2])
    
    if instr[0] == 'DEL' and instr[1] == 'EXAM':
        msg = delExam(instr[2])

print(patientSummary())
