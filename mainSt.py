from pyscript import display, document

# clubs dictionary 
club_information = {
    "Science Club": {
        'Name': 'Science Club',
        'Description': 'A club for students who love experiments and scientific exploration.',
        'Meeting Time': 'Monday and Friday, 3:30-4:30 PM',
        'Location': 'Room 420',
        'Club Moderator': 'Mr. Santos',
        'Number of Members': 35
    },

    "Math Club": {
        'Name': 'Math Club',
        'Description': 'A club for students who enjoy problem-solving and competitions.',
        'Meeting Time': 'Tuesday and Wednesday, 4:00-5:30 PM',
        'Location': 'Room 510',
        'Club Moderator': 'Mrs. Dela Cruz',
        'Number of Members': 28
    },

    "Debate Club": {
        'Name': 'Debate Club',
        'Description': 'A club for students who love reasoning, arguments, and public speaking.',
        'Meeting Time': 'Thursday and Friday, 2:30-4:30 PM',
        'Location': 'Room 610',
        'Club Moderator': 'Mr. Ramirez',
        'Number of Members': 22
    }
}

def clubdetails(e):  # function gets data from dropdown, to then display

    values = document.getElementById('cluboptions').value  # getting data

    # Prevent error if user selects "select"
    if values == "select":
        document.getElementById("output").innerHTML = "<b>Please choose a club first.</b>"
        return

    data_display = club_information[values]  # reading dictionary
    document.getElementById("output").innerHTML = ""  # clearing output

    # displaying data
    display(f"{values}", target="output")
    display(f"Description: {data_display['Description']}", target="output")
    display(f"Meeting Time: {data_display['Meeting Time']}", target="output")
    display(f"Location: {data_display['Location']}", target="output")
    display(f"Club Moderator: {data_display['Club Moderator']}", target="output")
    display(f"Members: {data_display['Number of Members']}", target="output")
