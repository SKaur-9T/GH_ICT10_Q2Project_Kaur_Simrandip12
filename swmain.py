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
    