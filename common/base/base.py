import openpyxl


class Base:
    def __init__(self, file_path, sheet_num):
        self.sheet_num = sheet_num
        self.file_path = file_path

    def get_workspace(self):
        wb = openpyxl.load_workbook(self.file_path)
        sheets = wb.sheetnames
        table = wb[sheets[self.sheet_num - 1]]
        return wb, table

    def save(self, wb):
        wb.save(self.file_path)
        wb.close()
