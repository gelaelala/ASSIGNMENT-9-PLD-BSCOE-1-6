#PDF Resume Creator
#	- Create a python program that will create your personal resume in PDF format
#	- All personal details are stored in a JSON file
#	- Your program should read the JSON file and write the details in the PDF
#	- The output file should be: LASTNAME_FIRSTNAME.pdf

#Note:
#	- Search for available PDF library that you can use
#	- Search how data is structured using JSON format
#	- Search how to read JSON file
#	- You will create the JSON file manually
#	- Your code should be in github before Feb12

import time
import json
from fpdf import FPDF

data = open("resume personal details.json")
data = json.load(data)
resumepdf = FPDF('P', 'mm', "Legal")
resumepdf.add_page()

def pageintroduction ():
    resumepdf.set_font ('Arial', '', 45)
    resumepdf.cell (0, 23, 'Personal Resume', ln = 10, align = 'C')
    resumepdf.image ('ID PICTURE.png', 180, 10, 25)
    resumepdf.line (10, 40, 210, 40)
    resumepdf.set_line_width (1.5)
    resumepdf.ln (20)

def resumedata ():
    resumepdf.ln (5)
    resumepdf.set_font ('Arial', 'B', 20)
    resumepdf.cell (30, 10, 'Personal Information', ln = 15, align = 'L')
    resumepdf.ln(3)
    resumepdf.set_font ('Arial', '', 12)
    resumepdf.cell (50, 10, "Name                                   " +str(data["Personal Profile"]["Name"]), ln = 10)
    resumepdf.cell (50, 10, "Gender                                 " +str(data["Personal Profile"]["Gender"]), ln = 10)
    resumepdf.cell (50, 10, "Age                                      " +str(data["Personal Profile"]["Age"]), ln = 10)
    resumepdf.cell (50, 10, "Birthday                                " +str(data["Personal Profile"]["Birthday"]), ln = 10)
    resumepdf.cell (50, 10, "Nationality                            " +str(data["Personal Profile"]["Nationality"]), ln = 10)
    resumepdf.cell (50, 10, "Home Address                     " +str(data["Personal Profile"]["Address"]), ln = 10)
    resumepdf.ln(5)
    resumepdf.line (10, 40, 210, 40)
    resumepdf.set_font ('Arial', 'B', 20)
    resumepdf.cell (30, 10, 'Contact Information', ln = 15, align = 'L')
    resumepdf.ln(3)
    resumepdf.set_font ('Arial', '', 12)
    resumepdf.cell (50, 10, "Email Address                     " +str(data["Contact Information"]["Email Address"]), ln = 10)
    resumepdf.cell (50, 10, "Phone Number                    " +str(data["Contact Information"]["Phone Number"]), ln = 10)
    resumepdf.ln (5)
    resumepdf.set_font ('Arial', 'B', 20)
    resumepdf.cell (30, 10, 'Educational Background', ln = 15, align = 'L')
    resumepdf.ln(3)
    resumepdf.set_font ('Arial', '', 12)
    resumepdf.cell (50, 10, "Elementary                          " +str(data["Educational Background"]["Elementary"]), ln = 10)
    resumepdf.cell (50, 10, "High School                         " +str(data["Educational Background"]["High School"]), ln = 10)
    resumepdf.cell (50, 10, "College                                " +str(data["Educational Background"]["College"]), ln = 10)
    resumepdf.ln (5)
    resumepdf.set_font ('Arial', 'B', 20)
    resumepdf.cell (30, 10, 'Work Experience', ln = 15, align = 'L')
    resumepdf.ln(3)
    resumepdf.set_font ('Arial', '', 12)
    resumepdf.cell (50, 10, "Fujitsu                                 " +str(data["Work Experience"]["Fujitsu"]), ln = 10)
    resumepdf.cell (50, 10, "Unilab Philippines               " +str(data["Work Experience"]["Unilab Philippines"]), ln = 10)
    resumepdf.ln (5)
    resumepdf.set_font ('Arial', 'B', 20)
    resumepdf.cell (30, 10, 'Skills', ln = 15, align = 'L')
    resumepdf.ln(3)
    resumepdf.set_font ('Arial', '', 12)
    resumepdf.cell (50, 10, "Programming                      " +str(data["Skills"]["Programming"]), ln = 10)
    resumepdf.cell (50, 10, "Photo Editing                      " +str(data["Skills"]["Photo Editing"]), ln = 10)
    resumepdf.ln (5)
    resumepdf.set_font ('Arial', 'B', 20)
    resumepdf.cell (30, 10, 'Awards and Achivements', ln = 15, align = 'L')
    resumepdf.ln(3)
    resumepdf.set_font ('Arial', '', 12)
    resumepdf.cell (50, 10, str(data["Awards and Achivements"]["a"]), ln = 10)
    resumepdf.cell (50, 10, str(data["Awards and Achivements"]["b"]), ln = 10)
    resumepdf.cell (50, 10, str(data["Awards and Achivements"]["c"]), ln = 10)
    
def main ():
    pageintroduction()
    resumedata()
    resumepdf.output ('CORPUZ_ANGELA.pdf')

main()
