import json
import os
from antlr4 import *
from CSVLexer import CSVLexer
from CSVParser import CSVParser

# Function that will parse a CSV file and return a JSON object
def parse_csv_to_json(input_file, output_file):
    #create a character stream from the input file.
    input_stream = FileStream(input_file, encoding='utf-8')
    #create a lexer that reads from the input stream.
    lexer = CSVLexer(input_stream)
    lexer.delimiter = ','
    #create a buffer of tokens that the parser will read from.
    token_stream = CommonTokenStream(lexer)
    #create a parser that reads from the token stream.
    parser = CSVParser(token_stream)
    #get the parse tree for the parser
    parse_tree = parser.file_()

    #visitor class that will traverse the parse tree and convert it to a JSON object.
    class CSVToJSONVisitor(ParseTreeVisitor):
        def visitFile(self, ctx):
            #headers will get the headers from the first row of the CSV file.
            headers = ctx.row(0).toString(ruleNames=parser.ruleNames, stop=ctx.stop)
            #empty list to hold the rows of data.
            rows = []

            #iterate over the remaining rows of the CSV file.
            for i in range(1, ctx.rowCount()):
                #get the values from the current row of the CSV file.
                values = ctx.row(i).string()
                #dictionary representing the current row of data
                row = {}
                for j in range(len(headers)):
                    row[headers[j]] = values[j]
                #append the row to the list of rows.
                rows.append(row)
            #dictionary representing the final CSV file.
            result = {"data": rows}

            return result

    #"visitor" instance that will be used to traverse the parse tree.
    visitor = CSVToJSONVisitor()
    json_object = visitor.visit(parse_tree)
    json_string = json.dumps(json_object)

    #write the JSON string to the output file.
    with open(output_file, 'w+') as f:
        f.write(json_string)

    # Return the JSON object.
    return json_object

parse_csv_to_json('./csvFiles/fastfood.csv', './jsonFiles/fastfood.json')