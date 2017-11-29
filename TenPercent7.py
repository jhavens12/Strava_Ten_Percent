import ui
import console
import get_time
import get_data
import calc
import matplotlib.pyplot as plt
import pylab
import matplotlib.dates as mdates
import pylab
from io import BytesIO

master_dict = get_data.my_filtered_activities()

def previous_period(dictionary):

    dict_1 = dictionary.copy()
    #if key is newer than last sunday, remove it
    for key in dictionary:
        if key > get_time.LS(0):
            del dict_1[key]
    for key in dictionary:
        if key < get_time.LM(2):
            del dict_1[key]

    past_dict_rev = {k: dict_1[k] for k in list(reversed(sorted(dict_1.keys())))[:4]}
    past_dict = {k: past_dict_rev[k] for k in list(sorted(past_dict_rev.keys()))}
    past_run_count = calc.activity_count(past_dict)
    past_mile_list = []
    for i in past_dict:
        past_mile_list.append(float(past_dict[i]['distance_miles']))
    past_miles = ("{0:.2f}".format(sum(past_mile_list)))
    past_ten_percent = ("{0:.2f}".format(float(past_miles) * .1))

    past_run_title_label = []
    for i in list(sorted(past_dict)):
        past_run_title_label.append(past_dict[i]['weekday_full_date'])
    past_run_mile_label = []
    for i in list(sorted(past_dict)):
        past_run_mile_label.append(past_dict[i]['distance_miles'])
    past_run_pace_label = []
    for i in list(sorted(past_dict)):
        past_run_pace_label.append(past_dict[i]['pace'])
    past_run_elapsed_label = []
    for i in list(sorted(past_dict)):
        past_run_elapsed_label.append(str(past_dict[i]['elapsed']))
    past_run_partner_label = []
    for i in list(sorted(past_dict)):
        past_run_partner_label.append(str(past_dict[i]['athlete_count']))
    #
    # print("past run")
    # print(past_run_count)
    # print(past_miles)
    # print(past_ten_percent)
    # print(past_run_title_label)
    # print(past_run_mile_label)
    # print(past_run_pace_label)
    # print(past_run_elapsed_label)
    # print(past_run_partner_label)

    label1= v['label1']
    label1.text = (get_time.convert_weekday_full(get_time.LM(2)) + " - " + get_time.convert_weekday_full(get_time.LS(0)))

    label2= v['label2']
    label2.text = str(past_run_count)

    label3= v['label3']
    label3.text = str(past_miles)

    label4= v['label4']
    label4.text = str(past_ten_percent)

    label5= v['label5']
    label5.text = ("\n".join(past_run_mile_label))

    label6= v['label6']
    label6.text = ("\n".join(past_run_title_label))

    label19= v['label19']
    label19.text = ("\n".join(past_run_pace_label))

    label20= v['label20']
    label20.text = ("\n".join(past_run_elapsed_label))

    label21= v['label21']
    label21.text = ("\n".join(past_run_partner_label))

    remaining_period(past_ten_percent,past_miles)

def previous_previous_period(dictionary):

    dict_1 = dictionary.copy()
    #if key is newer than last sunday, remove it
    for key in dictionary:
        if key > get_time.LS(0):
            del dict_1[key]
    for key in dictionary:
        if key < get_time.LM(3):
            del dict_1[key]

    past_dict_rev = {k: dict_1[k] for k in list(reversed(sorted(dict_1.keys())))[:8]}
    past_dict = {k: past_dict_rev[k] for k in list(sorted(past_dict_rev.keys()))[:4]}
    past_run_count = calc.activity_count(past_dict)
    past_mile_list = []
    for i in past_dict:
        past_mile_list.append(float(past_dict[i]['distance_miles']))
    past_miles = ("{0:.2f}".format(sum(past_mile_list)))
    past_ten_percent = ("{0:.2f}".format(float(past_miles) * .1))

    past_run_title_label = []
    for i in list(sorted(past_dict)):
        past_run_title_label.append(past_dict[i]['weekday_full_date'])
    past_run_mile_label = []
    for i in list(sorted(past_dict)):
        past_run_mile_label.append(past_dict[i]['distance_miles'])
    past_run_pace_label = []
    for i in list(sorted(past_dict)):
        past_run_pace_label.append(past_dict[i]['pace'])
    past_run_elapsed_label = []
    for i in list(sorted(past_dict)):
        past_run_elapsed_label.append(str(past_dict[i]['elapsed']))
    past_run_partner_label = []
    for i in list(sorted(past_dict)):
        past_run_partner_label.append(str(past_dict[i]['athlete_count']))

    # print("past past run")
    # print(past_run_count)
    # print(past_miles)
    # print(past_ten_percent)
    # print(past_run_title_label)
    # print(past_run_mile_label)
    # print(past_run_pace_label)
    # print(past_run_elapsed_label)
    # print(past_run_partner_label)

    label1= v['label1']
    label1.text = (get_time.convert_weekday_full(get_time.LM(3)) + " - " + get_time.convert_weekday_full(get_time.LS(0)))

    label2= v['label2']
    label2.text = str(past_run_count)

    label3= v['label3']
    label3.text = str(past_miles)

    label4= v['label4']
    label4.text = str(past_ten_percent)

    label5= v['label5']
    label5.text = ("\n".join(past_run_mile_label))

    label6= v['label6']
    label6.text = ("\n".join(past_run_title_label))

    label19= v['label19']
    label19.text = ("\n".join(past_run_pace_label))

    label20= v['label20']
    label20.text = ("\n".join(past_run_elapsed_label))

    label21= v['label21']
    label21.text = ("\n".join(past_run_partner_label))

    remaining_period(past_ten_percent,past_miles)

def previous_previous_previous_period(dictionary):

    dict_1 = dictionary.copy()
    #if key is newer than last sunday, remove it
    for key in dictionary:
        if key > get_time.LS(0):
            del dict_1[key]
    for key in dictionary:
        if key < get_time.LM(4):
            del dict_1[key]

    past_dict_rev = {k: dict_1[k] for k in list(reversed(sorted(dict_1.keys())))[:12]}
    past_dict = {k: past_dict_rev[k] for k in list(sorted(past_dict_rev.keys()))[:4]}
    past_run_count = calc.activity_count(past_dict)
    past_mile_list = []
    for i in past_dict:
        past_mile_list.append(float(past_dict[i]['distance_miles']))
    past_miles = ("{0:.2f}".format(sum(past_mile_list)))
    past_ten_percent = ("{0:.2f}".format(float(past_miles) * .1))

    past_run_title_label = []
    for i in list(sorted(past_dict)):
        past_run_title_label.append(past_dict[i]['weekday_full_date'])
    past_run_mile_label = []
    for i in list(sorted(past_dict)):
        past_run_mile_label.append(past_dict[i]['distance_miles'])
    past_run_pace_label = []
    for i in list(sorted(past_dict)):
        past_run_pace_label.append(past_dict[i]['pace'])
    past_run_elapsed_label = []
    for i in list(sorted(past_dict)):
        past_run_elapsed_label.append(str(past_dict[i]['elapsed']))
    past_run_partner_label = []
    for i in list(sorted(past_dict)):
        past_run_partner_label.append(str(past_dict[i]['athlete_count']))

    # print("past past run")
    # print(past_run_count)
    # print(past_miles)
    # print(past_ten_percent)
    # print(past_run_title_label)
    # print(past_run_mile_label)
    # print(past_run_pace_label)
    # print(past_run_elapsed_label)
    # print(past_run_partner_label)

    label1= v['label1']
    label1.text = (get_time.convert_weekday_full(get_time.LM(4)) + " - " + get_time.convert_weekday_full(get_time.LS(0)))

    label2= v['label2']
    label2.text = str(past_run_count)

    label3= v['label3']
    label3.text = str(past_miles)

    label4= v['label4']
    label4.text = str(past_ten_percent)

    label5= v['label5']
    label5.text = ("\n".join(past_run_mile_label))

    label6= v['label6']
    label6.text = ("\n".join(past_run_title_label))

    label19= v['label19']
    label19.text = ("\n".join(past_run_pace_label))

    label20= v['label20']
    label20.text = ("\n".join(past_run_elapsed_label))

    label21= v['label21']
    label21.text = ("\n".join(past_run_partner_label))

    remaining_period(past_ten_percent,past_miles)

def top_period(dictionary):

    dict_1 = dictionary.copy()

    result = calc.top_running_period(master_dict,4,'distance_miles')
    result_dict = {k: result[k] for k in list(reversed(sorted(result.keys())))[:1]}
    final_dict = dict()
    for i in result_dict.values():
        for w in i:
            final_dict.update({w: i[w]})

    top_run_count = calc.activity_count(final_dict)
    top_mile_list = []
    for i in final_dict:
        top_mile_list.append(float(final_dict[i]['distance_miles']))
    top_miles = ("{0:.2f}".format(sum(top_mile_list)))
    top_ten_percent = ("{0:.2f}".format(float(top_miles) * .1))

    top_run_title_label = []
    for i in list(sorted(final_dict)):
        top_run_title_label.append(final_dict[i]['weekday_full_date'])
    top_run_mile_label = []
    for i in list(sorted(final_dict)):
        top_run_mile_label.append(final_dict[i]['distance_miles'])
    top_run_pace_label = []
    for i in list(sorted(final_dict)):
        top_run_pace_label.append(final_dict[i]['pace'])
    top_run_elapsed_label = []
    for i in list(sorted(final_dict)):
        top_run_elapsed_label.append(str(final_dict[i]['elapsed']))
    top_run_partner_label = []
    for i in list(sorted(final_dict)):
        top_run_partner_label.append(str(final_dict[i]['athlete_count']))

    # print("top period")
    # print(top_run_count)
    # print(top_miles)
    # print(top_ten_percent)
    # print(top_run_title_label)
    # print(top_run_mile_label)
    # print(top_run_pace_label)
    # print(top_run_elapsed_label)
    # print(top_run_partner_label)

    date_list = []
    for key in list(sorted(final_dict)):
        date_list.append(final_dict[key]['start_date_datetime'])
    time1 = date_list[0]
    time2 = date_list[3]

    label1= v['label1']
    label1.text = (get_time.convert_weekday_full(time1) + " - " + get_time.convert_weekday_full(time2))

    label2= v['label2']
    label2.text = str(top_run_count)

    label3= v['label3']
    label3.text = str(top_miles)

    label4= v['label4']
    label4.text = str(top_ten_percent)

    label5= v['label5']
    label5.text = ("\n".join(top_run_mile_label))

    label6= v['label6']
    label6.text = ("\n".join(top_run_title_label))

    label19= v['label19']
    label19.text = ("\n".join(top_run_pace_label))

    label20= v['label20']
    label20.text = ("\n".join(top_run_elapsed_label))

    label21= v['label21']
    label21.text = ("\n".join(top_run_partner_label))

    remaining_period(top_ten_percent,top_miles)

    #current
def current_period(dictionary):
    dict_2 = dictionary.copy()
    global current_miles
    global current_week_count
    for key in dictionary:
        if key < get_time.LM(0):
            del dict_2[key]
    current_week_count = calc.activity_count(dict_2)
    mile_list = []
    for i in dict_2:
        mile_list.append(float(dict_2[i]['distance_miles']))
    current_miles = sum(mile_list)

    current_run_title_label = []
    for i in list(sorted(dict_2)):
        current_run_title_label.append(dict_2[i]['weekday_full_date'])
    current_run_mile_label = []
    for i in list(sorted(dict_2)):
        current_run_mile_label.append(dict_2[i]['distance_miles'])
    current_run_pace_label = []
    for i in list(sorted(dict_2)):
        current_run_pace_label.append(dict_2[i]['pace'])
    current_run_elapsed_label = []
    for i in list(sorted(dict_2)):
        current_run_elapsed_label.append(str(dict_2[i]['elapsed']))
    current_run_partner_label = []
    for i in list(sorted(dict_2)):
        current_run_partner_label.append(str(dict_2[i]['athlete_count']))

    # print("current run")
    # print(current_run_title_label)
    # print(current_run_mile_label)
    # print(current_run_pace_label)
    # print(current_run_elapsed_label)
    # print(current_run_partner_label)

    label7= v['label7']
    label7.text = (get_time.convert_weekday_full(get_time.LM(0)) + " - " + get_time.convert_weekday_full(get_time.now()))

    label8= v['label8']
    label8.text = str(current_week_count)

    label9= v['label9']
    label9.text = str(current_miles)

    label10= v['label10']
    label10.text = ("\n".join(current_run_mile_label))

    label11= v['label11']
    label11.text = ("\n".join(current_run_title_label))

    label23= v['label23']
    label23.text = ("\n".join(current_run_pace_label))

    label24= v['label24']
    label24.text = ("\n".join(current_run_elapsed_label))

    label25= v['label25']
    label25.text = ("\n".join(current_run_partner_label))


    #remaining
def remaining_period(past_ten_percent,past_miles):
    remaining_miles = ("{0:.2f}".format((float(past_ten_percent) + float(past_miles)) - float(current_miles)))
    if int(current_week_count) <= 3:
        remaining_runs = (4 - int(current_week_count))
    if int(current_week_count) == 4:
        remaining_runs = 0
    remaining_miles_per_run = ("{0:.2f}".format(float(remaining_miles)/(4 - int(current_week_count))))

    label12= v['label12']
    label12.text = str(remaining_miles)

    #label13= v['label13']
    #label13.text = str(remaining_runs)

    label14= v['label14']
    label14.text = str(remaining_miles_per_run)

def button_action_1(sender):

    if button1.selected_index == 0:
        previous_period(master_dict)

    if button1.selected_index == 1:
        previous_previous_period(master_dict)

    if button1.selected_index == 2:
        previous_previous_previous_period(master_dict)

    elif button1.selected_index == 3:
        top_period(master_dict)

# starts gui
v = ui.load_view()
v.background_color = "black"

button1 = v['segmentedcontrol1']
button1.action = button_action_1

v.present(style='sheet', hide_title_bar=True)

current_period(master_dict)
previous_period(master_dict)
#previous_previous_period(master_dict)
#top_period(master_dict)
