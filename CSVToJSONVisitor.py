from antlr4 import ParseTreeVisitor
from CSVParser import CSVParser

class CSVToJSONVisitor(ParseTreeVisitor):
    def visitFile(self, ctx: CSVParser.FileContext, delimiter):
        headers_ctx = ctx.row(0)
        print('headers_ctx', headers_ctx)
        headers = [header.getText() for header in headers_ctx.field()]
        print('headers', headers)

        rows = []
        for i in range(1, len(ctx.row())):
            row_ctx = ctx.row(i)
            row_text = row_ctx.getText()
            values = [value.strip() for value in row_text.split(delimiter)]

            row_dict = {}
            for j in range(len(headers)):
                row_dict[headers[j]] = values[j]
            rows.append(row_dict)

        return rows