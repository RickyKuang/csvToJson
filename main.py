import json
from antlr4 import *
from CSVLexer import CSVLexer
from CSVParser import CSVParser
from CSVToJSONVisitor import CSVToJSONVisitor
import chardet
import csv
import os

def csv_to_json(input_file, output_file, encoding, delimiter):
    input_stream = FileStream(input_file, encoding=encoding)
    lexer = CSVLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = CSVParser(token_stream)
    parse_tree = parser.file_()

    visitor = CSVToJSONVisitor()
    json_object = visitor.visitFile(parse_tree, delimiter)
    json_string = json.dumps(json_object, indent=3)

    with open(output_file, 'w+') as json_file:
        json_file.write(json_string)

# ask user for filename input
file_csv = ""
file_json = ""
request_file = True
while request_file:
    file_name = input('Please enter the CSV file name you would like to parse (don\'t include .csv): ')
    file_csv = "./csvFiles/" + file_name + ".csv"
    if not os.path.exists(file_csv):
        print("The file you are looking for does not exist.")
    else:
        try:
            with open(file_csv, 'r') as csv_file:
                csv_reader = csv.reader(csv_file)
                next(csv_reader)

                file_json = "./jsonFiles/" + file_name + ".json"
                request_file = False
        except (csv.Error, UnicodeDecodeError):
            print("The file is not a valid CSV file. Please select a different file.")

# get the file's encoding
with open(file_csv, 'rb') as csv_file:
    csv_detect = chardet.detect(csv_file.read(10000))
encoding = csv_detect['encoding']
print("Encoding:", encoding)

# get the file's delimiter
with open(file_csv, 'r', encoding=encoding) as csv_file:
    csv_file_line = csv_file.readline()
csv_sniffer = csv.Sniffer().sniff(csv_file_line)
delimiter = csv_sniffer.delimiter
print("Delimiter:", delimiter)

# parse the csv to json
csv_to_json(file_csv, file_json, encoding, delimiter)
print("Access", file_name+".json", "in the jsonFiles folder.")