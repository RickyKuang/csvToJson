from antlr4 import ParseTreeVisitor
from CSVParser import CSVParser

class CSVToJSONVisitor(ParseTreeVisitor):
    def visitFile(self, ctx: CSVParser.FileContext, delimiter):
        headers_ctx = ctx.row(0)
        headers = [header.getText() for header in headers_ctx.field()]
        print('headers', headers)

        def fix_row_text(row_ctx, delimiter):
            row_text = row_ctx.getText()
            values = []

            # handle quoted fields
            in_quoted_field = False
            current_value = ''
            for char in row_text:
                if char == delimiter and not in_quoted_field:
                    values.append(current_value.strip())
                    current_value = ''
                else:
                    if char == '"':
                        in_quoted_field = not in_quoted_field
                    current_value += char
            values.append(current_value.strip())
            return values

        rows = []
        for i in range(1, len(ctx.row())):
            row_ctx = ctx.row(i)
            values = fix_row_text(row_ctx, delimiter)
            row_dict = {}
            for j in range(len(headers)):
                row_dict[headers[j]] = values[j]
            rows.append(row_dict)

        return rows