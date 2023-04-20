import json
from antlr4 import *
from CSVLexer import CSVLexer
from CSVParser import CSVParser

# Function that will parse a CSV file and return a JSON object
def parse_csv_to_json(filename):
    #create a character stream from the input file.
    input_stream = FileStream(filename)
    #create a lexer that reads from the input stream.
    lexer = CSVLexer(input_stream)
    #create a buffer of tokens that the parser will read from.
    token_stream = CommonTokenStream(lexer)
    #create a parser that reads from the token stream.
    parser = CSVParser(token_stream)
    #get the parse tree for the parser
    parse_tree = parser.file()

    #visitor class that will traverse the parse tree and convert it to a JSON object.
    class CSVToJSONVisitor(ParseTreeVisitor):
        def visitFile(self, ctx):
            #headers will get the headers from the first row of the CSV file.
            headers = ctx.row(0).string()
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
    #serializing the JSON object to a string and return it
    return json.dumps(json_object)