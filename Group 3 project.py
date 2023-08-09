# GROUP 3 PROJECT
# Build a system saved names and time of entry and
# store them in an empty dictionary,retrive staff that clocked in 8:30 and above
# 1. First create an empty dictionary to store the name and time of entry
# * Initiate an empty dictionary to store names and entry time
entry_dict = {}

# Function to save the name and time of entry
def save_entry(name, time):
    entry_dict[name] = time
save_entry("Ali","07:00")
save_entry("Chris","08:00")
save_entry("Chiamaka","08:15")
save_entry("Chibike","08:30")
save_entry("Debo","08:45")
save_entry("Lateef","09:00")

# Function to retrive staff members who clocked in at 08:30 and above

def retrive_staff():
    staff_list = []
    for name,time in entry_dict.items():
        if time >= "08:30":
            staff_list.append((name,time))
    return staff_list
staff = retrive_staff()
print("staff members that clocked in at 8:30 and later")
for member,time in staff:
    print(f"{member}:{time}")