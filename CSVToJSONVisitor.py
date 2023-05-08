from antlr4 import ParseTreeVisitor
from CSVParser import CSVParser

class CSVToJSONVisitor(ParseTreeVisitor):
    def visitFile(self, ctx: CSVParser.FileContext, delimiter):
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

        headers_ctx = ctx.row(0)
        headers = fix_row_text(headers_ctx, delimiter)
        print('headers', headers)

        rows_as_json = []
        for i in range(1, len(ctx.row())):
            row_ctx = ctx.row(i)
            values = fix_row_text(row_ctx, delimiter)
            row_dict = {}
            for j in range(len(headers)):
                row_dict[headers[j]] = values[j]
            rows_as_json.append(row_dict)

        return rows_as_json