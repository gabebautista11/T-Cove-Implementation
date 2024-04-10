import tkinter
from DB import DB

def create_room_set(all_rows):
    room_set = set()
    for row in all_rows:
        #rooms are index 4 of the row
        room_set.add(row[4])
    return room_set

#report = (mac,start-time,endtime) tuple
def report_query(report):
    pass

#check = (mac,start-time,endtime) tuple
def check_query(check):
    pass

#contact = (start,end) tuple
'''
contact_query: retrieve all users who have come in contact with an affected person
'''
def contact_query(start_time, end_time):
    print("IN CONTACT QUERY")
    print(start_time, end_time)






def main():
    root = tkinter.Tk()
    root.title("T-Cove Impl.")
    contact_frame = tkinter.Frame(root)
    contact_frame.pack()
    start_time_label_contact = tkinter.Label(contact_frame, text="Start Time")
    start_time_label_contact.pack()
    contact_text_start = tkinter.Text(contact_frame, height=1, width=25)
    contact_text_start.pack()
    end_time_label_contact = tkinter.Label(contact_frame, text="End Time")
    end_time_label_contact.pack()
    contact_text_end = tkinter.Text(contact_frame, height=1, width=25)
    contact_text_end.pack()
    contact_button = tkinter.Button(contact_frame, text="Contact Query", command=lambda:
        contact_query(contact_text_start.get("1.0", 'end-1c'), contact_text_end.get("1.0", 'end-1c')))
    contact_button.pack()

    check_frame = tkinter.Frame(root)
    check_frame.pack()
    mac_label_check = tkinter.Label(check_frame, text="MAC Address")
    mac_label_check.pack()
    check_text = tkinter.Text(check_frame, height=1, width=25)
    check_text.pack()
    start_label_check = tkinter.Label(check_frame, text="Start Time")
    start_label_check.pack()
    check_text_start = tkinter.Text(check_frame, height=1, width=25)
    check_text_start.pack()
    end_label_check = tkinter.Label(check_frame, text="End Time")
    end_label_check.pack()
    check_text_end = tkinter.Text(check_frame, height=1, width=25)
    check_text_end.pack()
    check_button = tkinter.Button(check_frame, text="Check Query", command="")
    check_button.pack()

    report_frame = tkinter.Frame(root)
    report_frame.pack()
    mac_label_report = tkinter.Label(report_frame, text="MAC Address")
    mac_label_report.pack()
    report_text_mac = tkinter.Text(report_frame, height=1, width=25)
    report_text_mac.pack()
    start_label_report = tkinter.Label(report_frame, text="Start Time")
    start_label_report.pack()
    report_text_start = tkinter.Text(report_frame, height=1, width=25)
    report_text_start.pack()
    end_label_report = tkinter.Label(report_frame, text="End Time")
    end_label_report.pack()
    report_text_end = tkinter.Text(report_frame, height=1, width=25)
    report_text_end.pack()
    report_button = tkinter.Button(report_frame, text="Report Query", command="")
    report_button.pack()

    root.mainloop()

    # connect to the db
    db = DB()
    # get all rows from db and loop through and collect all unique rooms to create a node in the graph
    all_rows = db.get_all_rows_of_presence_table("presence")
    room_set = create_room_set(all_rows)
    print(room_set)
    # create a graph impl.


if __name__ == "__main__":
    main()