import json
from antlr4 import *
from CSVLexer import CSVLexer
from CSVParser import CSVParser


# Function that will parse a CSV file and return a JSON object
def parse_csv_to_json(input_file, output_file):
    # create a character stream from the input file.
    input_stream = FileStream(input_file, encoding='utf-8')
    # create a lexer that reads from the input stream.
    lexer = CSVLexer(input_stream)
    lexer.delimiter = ','
    # create a buffer of tokens that the parser will read from.
    token_stream = CommonTokenStream(lexer)
    # create a parser that reads from the token stream.
    parser = CSVParser(token_stream)
    # get the parse tree for the parser
    parse_tree = parser.file_()

    # visitor class that will traverse the parse tree and convert it to a JSON object.
    class CSVToJSONVisitor(ParseTreeVisitor):
        def visitFile(self, ctx: CSVParser.FileContext):
            headers_ctx = ctx.row(0)
            headers = [header.getText() for header in headers_ctx.field()]

            rows = []
            for i in range(1, len(ctx.row())):
                row_ctx = ctx.row(i)
                row_text = row_ctx.getText()
                values = [value.strip() for value in row_text.split(',')]

                row_dict = {}
                for j in range(len(headers)):
                    row_dict[headers[j]] = values[j]
                rows.append(row_dict)

            return rows

    # "visitor" instance that will be used to traverse the parse tree.
    visitor = CSVToJSONVisitor()
    json_object = visitor.visitFile(parse_tree)
    json_string = json.dumps(json_object, indent=3)

    # write the JSON string to the output file.
    with open(output_file, 'w+') as f:
        f.write(json_string)

    # Return the JSON object.
    return json_object


# example usage of the function
parse_csv_to_json('./csvFiles/fastfood.csv', './jsonFiles/fastfood.json')
