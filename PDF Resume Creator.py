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
from colorama import Fore, Back, Style
from fpdf import FPDF

def program_intro():
    print ("Hello!")
    time.sleep (2)
    print ("Welcome to PDF Resume Creator.")
    time.sleep (2)
    getfile()

def getfile():
    jsonfile = input("Enter JSON file here:")
    fontname = input("Enter font name to be used:")
    fontsize = int(input("Enter font size to be used:"))
    output = input ("Enter your desired file name here (Note: Please add .pdf after naming it):")
    jsontopdf(jsonfile,fontname, fontsize, output)

def jsontopdf(json_file, fontname_, fontsize_, outputname):
    resume = open (json_file)
    resume = json.load(resume)
    resume = json.dumps(resume)
    lines = resume.split (',')
    pdf = FPDF ()
    pdf.add_page()
    pdf.set_font (fontname_, size = fontsize_)
    for l in lines:
        pdf.cell (200, 10, txt = l, ln = 1, align = 'L')
    pdf.output (outputname)

def main():
    program_intro()

main()