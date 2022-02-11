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

import json
from fpdf import FPDF

data = open("resume personal details.json")
data = json.load(data)
resumepdf = FPDF('P', 'mm', "Legal")
resumepdf.add_page()

def pageintroduction ():
    resumepdf.set_font ('Times', 'B', 25)
    resumepdf.cell (50, 8, str(data["Header Information"]["Name"]), ln = 10)
    resumepdf.set_font ('Times', 'I', 10)
    resumepdf.cell (50, 8, str(data["Header Information"]["Address"]), ln = 10)
    resumepdf.cell (50, 5, "Contact Number:  " +str(data["Header Information"]["Phone Number"]), ln = 10)
    resumepdf.cell (50, 5, "Email Address:     "+str(data["Header Information"]["Email Address"]), ln = 10)
    resumepdf.image ('ID PICTURE.png', 180, 5, 30)
    resumepdf.set_line_width (0.75)
    resumepdf.line (10, 40, 210, 40)
    resumepdf.ln (0)

def resumedata ():
    resumepdf.ln (10)
    resumepdf.set_font ('Times', 'B', 20)
    resumepdf.cell (30, 3, 'Personal Information', ln = 15, align = 'L')
    resumepdf.ln(3)
    resumepdf.set_font ('Times', '', 12)
    resumepdf.cell (50, 8, "Gender                                 " +str(data["Personal Profile"]["Gender"]), ln = 10)
    resumepdf.cell (50, 8, "Age                                      " +str(data["Personal Profile"]["Age"]), ln = 10)
    resumepdf.cell (50, 8, "Birthday                               " +str(data["Personal Profile"]["Birthday"]), ln = 10)
    resumepdf.cell (50, 8, "Nationality                           " +str(data["Personal Profile"]["Nationality"]), ln = 10)
    resumepdf.cell (50, 8, "Height                                  " +str(data["Personal Profile"]["Height"]), ln = 10)
    resumepdf.cell (50, 8, "Weight                                 " +str(data["Personal Profile"]["Weight"]), ln = 10)
    resumepdf.ln(15)
    resumepdf.line (10, 110, 210, 110)
    resumepdf.set_font ('Times', 'B', 20)
    resumepdf.cell (30, 10, 'Educational Background', ln = 15, align = 'L')
    resumepdf.ln(3)
    resumepdf.set_font ('Times', '', 12)
    resumepdf.cell (50, 8, "Elementary                          " +str(data["Educational Background"]["Elementary"]), ln = 5)
    resumepdf.set_font ('Times', 'I', 10)
    resumepdf.cell (50, 8, "                                                    "+str(data["Educational Background"]["Year Started and Graduated (elementary)"]), ln = 3)
    resumepdf.set_font ('Times', '', 12)
    resumepdf.cell (50, 8, "High School                        " +str(data["Educational Background"]["High School"]), ln = 5)
    resumepdf.set_font ('Times', 'I', 10)
    resumepdf.cell (50, 8, "                                                    "+str(data["Educational Background"]["Year Started and Graduated Graduated (high school)"]), ln = 3)
    resumepdf.set_font ('Times', '', 12)
    resumepdf.cell (50, 8, "College                                " +str(data["Educational Background"]["College"]), ln = 5)
    resumepdf.set_font ('Times', 'I', 10)
    resumepdf.cell (50, 8, "                                                     "+str(data["Educational Background"]["Course"]), ln = 3)
    resumepdf.ln (13)
    resumepdf.line (10, 182, 210, 182)
    resumepdf.set_font ('Times', 'B', 20)
    resumepdf.cell (30, 5, 'Work Experience', ln = 15, align = 'L')
    resumepdf.ln(3)
    resumepdf.set_font ('Times', '', 12)
    resumepdf.cell (50, 8, "Fujitsu                                 " +str(data["Work Experience"]["Fujitsu"]), ln = 10)
    resumepdf.cell (50, 8, "Unilab Philippines              " +str(data["Work Experience"]["Unilab Philippines"]), ln = 10)
    resumepdf.ln (15)
    resumepdf.line (10, 223, 210, 223)
    resumepdf.set_font ('Times', 'B', 20)
    resumepdf.cell (30, 10, 'Skills', ln = 15, align = 'L')
    resumepdf.ln(3)
    resumepdf.set_font ('Times', '', 12)
    resumepdf.cell (50, 8, "Programming                      " +str(data["Skills"]["Programming"]), ln = 10)
    resumepdf.cell (50, 8, "Photo Editing                     " +str(data["Skills"]["Photo Editing"]), ln = 10)
    resumepdf.ln (15)
    resumepdf.line (10, 268, 210, 268)
    resumepdf.set_font ('Times', 'B', 20)
    resumepdf.cell (30, 10, 'Awards and Achievements', ln = 15, align = 'L')
    resumepdf.ln(2)
    resumepdf.set_font ('Times', '', 12)
    resumepdf.cell (50, 8, str(data["Awards and Achievements"]["a"]), ln = 10)
    resumepdf.cell (50, 8, str(data["Awards and Achievements"]["b"]), ln = 10)
    resumepdf.cell (50, 8, str(data["Awards and Achievements"]["c"]), ln = 10)
    
def main ():
    pageintroduction()
    resumedata()
    resumepdf.output ('CORPUZ_ANGELA.pdf')

main()
