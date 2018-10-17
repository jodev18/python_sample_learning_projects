import csv

undesired_names = ['Maam','maam','Ma.','sir','Sir','SIR','Mrs.','ma.','ma','Dr.','dr','DR',]

with open('evaluation_resp.csv') as csvfile:
    reader = csv.DictReader(csvfile)

    cleaned_names = []
    sections = []
    for row in reader:
        rec_timestamp = row['Timestamp']
        teacher = row['Name of the Teacher'].split()
        section = row['Grade/Year & Section']

        #process names

        if len(teacher) > 1:
            if teacher[0] not in undesired_names:
               cleaned_names.append(' '.join(teacher[0:]))
        else:
            print("Single name: ",teacher)

        sections.append(section)

        print(row['Timestamp'],row['Name of the Teacher'].split())
        print(row)

    print(cleaned_names)

    for i in range(len(cleaned_names)):
        print(cleaned_names[i],sections[i],sep="|")



