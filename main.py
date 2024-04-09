import tkinter
from DB import DB



def main():
    root = tkinter.Tk()
    root.title("T-Cove Impl.")
    #connect to the db
    db = DB()
    #get all rows from db and loop through and collect all unique rooms to create a node in the graph

    #create a graph impl

    root.mainloop()

if __name__ == "__main__":
    main()