from pyscript import document

def calculate(e):
    output_summary = document.getElementById("output")
    output_summary.innerHTML = ""
    
    firstName = document.getElementById("fName").value
    lastName = document.getElementById("lName").value
    
    class1 = int(document.getElementById("class1").value)
    class2 = int(document.getElementById("class2").value)
    class3 = int(document.getElementById("class3").value)
    class4 = int(document.getElementById("class4").value)
    class5 = int(document.getElementById("class5").value)
    class6 = int(document.getElementById("class6").value)
    
    units = [5, 5, 5, 2, 1, 1] # Units for each subject
    English, Science, Math, Tle, Ve, Pe = units 
    
    GWA = ((class1 * English) + (class2 * Science) + (class3 * Math) + (class4 * Tle) + (class5 * Ve) + (class6 * Pe))/(English + Science + Math + Tle + Ve + Pe)
    
    final_message = f"""Hello, {firstName} {lastName}\n
    Science: {class1}\n
    English: {class2}\n
    ICT: {class3}\n
    Math: {class4}\n
    Filipino: {class5}\n
    PE: {class6}\n
    Your General Weighted Average (GWA) is: {round(GWA, 2)}"""
    
    output_summary.innerText = final_message


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
