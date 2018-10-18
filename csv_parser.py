import csv

undesired_names = ['Maam','maam','Ma.','sir','Sir','SIR','Mrs.','ma.','ma','Dr.',
                   'dr','DR','mr.','Mr.','Ms.','Sr.','Sir.','T.','Teacher']
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
    equal_treatment = []
    emphasizes_relevance = []
    using_visual_aids = []
    gives_tests = []
    personality_fair = []
    comments = []

    row_count = sum(1 for row in csvfile)
    print("Total row length",row_count)

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
        time_efficiency_d = row[indexed_keys[7]]
        english_elip_d = row[indexed_keys[8]]
        vld_d = row[indexed_keys[9]]
        clear_instruc = row[indexed_keys[10]]
        subj_mastery = row[indexed_keys[11]]
        clear_explain = row[indexed_keys[12]]
        eq_treat = row[indexed_keys[13]]
        emp_relevance = row[indexed_keys[14]]
        vis_aid = row[indexed_keys[15]]
        test_prov = row[indexed_keys[16]]
        fair_person = row[indexed_keys[17]]
        comment = row[indexed_keys[18]]

        #process names

        if len(teacher) > 1:

            proc_name = []

            for name in teacher:
                proc_name.append(name.capitalize())

            print("processed: ", proc_name)

            if teacher[0] not in undesired_names:
               teacher[0] = teacher[0].capitalize()
               cleaned_names.append(' '.join(proc_name[0:]))
            else:
                teacher[1] = teacher[1].capitalize()
                cleaned_names.append(' '.join(proc_name[1:]))
        else:
            print("Single name: ",teacher)

        sections.append(section)
        arrivals.append(arrival)
        well_organization.append(organized)
        manage_climate_orders.append(climate_order_mngt)
        cleanliness_checks.append(cleanliness_check)

    print(cleaned_names)

    for i in range(len(cleaned_names)):
        print(cleaned_names[i],sections[i],well_organization[i],manage_climate_orders[i],cleanliness_checks[i],sep="|")

    print(indexed_keys)
    print("Number of columns processed: ",len(indexed_keys))

    cleaned_names.sort()
    print(cleaned_names)


