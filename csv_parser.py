import csv

undesired_names = ['Maam','maam','Ma.','sir','Sir','SIR','Mrs.','ma.','ma','Dr.','dr','DR','mr.','Mr.']
column_keys = []
indexed_keys = []

with open('evaluation_resp.csv') as csvfile:
    reader = csv.DictReader(csvfile)

    cleaned_names = []
    sections = []
    arrivals = []
    well_organization = []
    manage_climate_orders = []
    cleanliness_checks = []
    time_efficiency = []
    english_elip = []
    varied_learning_activities = []
    clear_instructions = []
    mastery_of_subject = []
    explains_lesson_clearly = []



    for row in reader:
        column_keys = row.keys()
        indexed_keys = list(column_keys)

        rec_timestamp = row[indexed_keys[0]]
        teacher = row[indexed_keys[1]].split()
        section = row[indexed_keys[2]]
        arrival = row[indexed_keys[3]]
        organized = row[indexed_keys[4]]
        climate_order_mngt = row[indexed_keys[5]]
        cleanliness_check = row[indexed_keys[6]]

        #process names

        if len(teacher) > 1:
            if teacher[0] not in undesired_names:
               teacher[0] = teacher[0].capitalize()
               cleaned_names.append(' '.join(teacher[0:]))
        else:
            print("Single name: ",teacher)

        sections.append(section)
        arrivals.append(arrival)
        well_organization.append(organized)
        manage_climate_orders.append(climate_order_mngt)
        cleanliness_checks.append(cleanliness_check)

        print(row['Timestamp'],row['Name of the Teacher'].split())
        print(row)

    print(cleaned_names)

    for i in range(len(cleaned_names)):
        print(cleaned_names[i],sections[i],well_organization[i],manage_climate_orders[i],cleanliness_checks[i],sep="|")

    print(indexed_keys)
    print("Number of columns processed: ",len(indexed_keys))



