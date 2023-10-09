#!/usr/bin/env python
# coding: utf-8

# In[2]:


import csv

# Define the input and output file paths
input_file = 'TUS106_L01.txt'
output_file = 'output1.csv'

# Define the byte positions for each field (start_byte, end_byte)
field_byte_positions = [(1, 3), (4, 8), (9, 11), (12, 15), (16,16), (17,19), (20,21), (22,23), (24,25), (26,26), (27,30), (31,32), (33,34), (35,39), (40,41), (42,42), (43,43), (44,44), (45,56), (57,62), (63,68), (69,71), (72,72), (73,73), (74,74), (75,75), (76,76), (77,126), (127,129), (130,139),  ]  # Adjust these to match your data

# Function to parse a line of text into fields based on byte positions
def parse_line(line):
    fields = []
    for start_byte, end_byte in field_byte_positions:
        field = line[start_byte - 1:end_byte].strip()  # Adjust for 0-based indexing
        fields.append(field)
    return fields

# Open input and output files
with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
    # Create a CSV writer
    csv_writer = csv.writer(outfile)
    
    # Write header
    csv_writer.writerow(["Schedule ID", "FSU Serial No.", "Schedule", "survey year", "Sector", "NSS-Region",
    "District", "Stratum", "Sub-Stratum", "Sub-Round", "FOD Sub-Region", "Sample hhld. No.",
    "Level", "Filler", "Informant Sl.No.", "Response Code", "Survey Code",
    "Substitution Code/ Casualty code", "Filler", "Date of Survey", "Date of Despatch",
    "Time to canvass(minutes)", "No. of investigators(FI/ASO) in the team", "Remarks in block 7",
    "Remarks in block 8", "Remarks elsewhere in Sch.", "Remarks elsewhere in Sch.", "Blank",
    "NSC", "MULT"])
    
    # Read and parse each line from the input file
    for line in infile:
        fields = parse_line(line)
        csv_writer.writerow(fields)

print(f"Data has been successfully converted to CSV and saved to {output_file}.")


# In[3]:


import csv

# Define the input and output file paths
input_file = 'TUS106_L02.txt'
output_file = 'output2.csv'

# Define the byte positions for each field (start_byte, end_byte)
field_byte_positions = [(1, 32), (33, 34), (35, 36), (37, 39), (40,40), (41,41), (42,44), (45,45), (46,47), (48,49), (50,51), (52,126), (127,129), (130,139)  ]  # Adjust these to match your data

# Function to parse a line of text into fields based on byte positions
def parse_line(line):
    fields = []
    for start_byte, end_byte in field_byte_positions:
        field = line[start_byte - 1:end_byte].strip()  # Adjust for 0-based indexing
        fields.append(field)
    return fields

# Open input and output files
with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
    # Create a CSV writer
    csv_writer = csv.writer(outfile)
    
    # Write header
    csv_writer.writerow(["Common-ID", "Level", "Filler", "Person serial no.", "Relation to head", "Gender",
    "Age", "marital status", "highest level of education", "usual principal activity: status (code)",
    "industry of work: 2-digit of NIC 2008", "Blank", "NSC", "MULT"])
    
    # Read and parse each line from the input file
    for line in infile:
        fields = parse_line(line)
        csv_writer.writerow(fields)

print(f"Data has been successfully converted to CSV and saved to {output_file}.")


# In[6]:


import csv

# Define the input and output file paths
input_file = 'TUS106_L03.txt'
output_file = 'output3.csv'

# Define the byte positions for each field (start_byte, end_byte)
field_byte_positions = [(1, 32), (33, 34), (35, 39), (40, 42), (43,43), (44,44), (45,46), (47,56), (57,66), (67,76), (77,86), (87,96), (97,98), (99,99), (100,100), (101,101), (102,102), (103,103), (104,126), (127,129), (130,139),   ]  # Adjust these to match your data

# Function to parse a line of text into fields based on byte positions
def parse_line(line):
    fields = []
    for start_byte, end_byte in field_byte_positions:
        field = line[start_byte - 1:end_byte].strip()  # Adjust for 0-based indexing
        fields.append(field)
    return fields

# Open input and output files
with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
    # Create a CSV writer
    csv_writer = csv.writer(outfile)
    
    # Write header
    csv_writer.writerow(["Common-ID", "Level", "Filler", "Household size", "religion", "Social group",
    "Land possessed as on date of survey(code)",
    "usual consumer expenditure in a month for household purposes out of purchase (A)",
    "imputed value of usual consumption in a month from home grown stock (B)",
    "imputed value of usual consumption in a month from wages in kind, free collection, gifts, etc (C)",
    "expenditure on purchase of household durable during last 365 days (D)",
    "usual monthly consumer expenditure E: [A+B+C+(D/12)]",
    "Primary source of energy for cooking",
    "Primary source of energy for lighting",
    "Type of washing of clothes",
    "Type of sweeping of floor",
    "Type of structure of the dwelling unit",
    "member of age 5 years and above needing special care but no caregiver is available",
    "Blank",
    "NSC",
    "MULT"]) 
    
    # Read and parse each line from the input file
    for line in infile:
        fields = parse_line(line)
        csv_writer.writerow(fields)

print(f"Data has been successfully converted to CSV and saved to {output_file}.")


# In[7]:


import csv

# Define the input and output file paths
input_file = 'TUS106_L04.txt'
output_file = 'output4.csv'

# Define the byte positions for each field (start_byte, end_byte)
field_byte_positions = [(1, 32), (33, 34), (35, 36), (37, 39), (40,42), (43,44), (45,45), (46,46), (47,47), (48,126), (127,129), (130,139)   ]  # Adjust these to match your data

# Function to parse a line of text into fields based on byte positions
def parse_line(line):
    fields = []
    for start_byte, end_byte in field_byte_positions:
        field = line[start_byte - 1:end_byte].strip()  # Adjust for 0-based indexing
        fields.append(field)
    return fields

# Open input and output files
with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
    # Create a CSV writer
    csv_writer = csv.writer(outfile)
    
    # Write header
    csv_writer.writerow(["Common-ID", "Level", "Filler", "srl. No of member", "age",
    "relationship of the informant with the household member", "day of week",
    "type of the day", "response code", "Blank", "NSC", "MULT"])
    
    # Read and parse each line from the input file
    for line in infile:
        fields = parse_line(line)
        csv_writer.writerow(fields)

print(f"Data has been successfully converted to CSV and saved to {output_file}.")


# In[8]:


import csv

# Define the input and output file paths
input_file = 'TUS106_L05.txt'
output_file = 'output5.csv'

# Define the byte positions for each field (start_byte, end_byte)
field_byte_positions = [(1, 32), (33, 34), (35, 36), (37, 39), (40,42), (43,45), (46,50), (51,55), (56,56), (57,57), (58,58), (59,61), (62,62), (63,64), (65,65), (66,126), (127,129), (130,139),   ]  # Adjust these to match your data

# Function to parse a line of text into fields based on byte positions
def parse_line(line):
    fields = []
    for start_byte, end_byte in field_byte_positions:
        field = line[start_byte - 1:end_byte].strip()  # Adjust for 0-based indexing
        fields.append(field)
    return fields

# Open input and output files
with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
    # Create a CSV writer
    csv_writer = csv.writer(outfile)
    
    # Write header
    csv_writer.writerow(["Common-ID", "Level", "Filler", "Serial no.of member", "age",
    "srl. No of activity", "time from", "time to",
    "whether performed multiple activity in the time slot",
    "whether simultaneous activity", "whether a major activity",
    "3-digit activity code", "where the activity was performed",
    "unpaid/paid status of activity", "enterprise type", "Blank", "NSC", "MULT"])
    
    # Read and parse each line from the input file
    for line in infile:
        fields = parse_line(line)
        csv_writer.writerow(fields)

print(f"Data has been successfully converted to CSV and saved to {output_file}.")

