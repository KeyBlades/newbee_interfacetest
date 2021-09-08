import json
from common.contact import Contact
from common.base.base import Base
from common.base.get_config import cf


class Read_Write(Base):
    def __init__(self, file_path, sheet_num):
        super().__init__(file_path, sheet_num)
        self.title = [Contact.case_id,
                      Contact.case_module,
                      Contact.case_description,
                      Contact.request_address,
                      Contact.request_method,
                      Contact.request_param,
                      Contact.request_header,
                      Contact.precondition,
                      Contact.is_exec,
                      Contact.status,
                      Contact.expect_result,
                      Contact.actual_result
                      ]

    def read(self):
        wb, table = self.get_workspace()
        col_values = []
        case_values = []
        for i in range(2, table.max_row + 1):
            for j in range(1, table.max_column + 1):
                col_values.append(table.cell(i, j).value)
            row_values = dict(zip(self.title, col_values))
            col_values = []
            case_values.append(row_values)
        return case_values

    def get_params(self, case_id):
        case_values = self.read()
        for i in range(len(case_values)):
            if case_values[i].get(Contact.case_id) == case_id:
                url = case_values[i].get(Contact.request_address)
                method = case_values[i].get(Contact.request_method)
                data = json.dumps(eval(case_values[i].get(Contact.request_param)))
                header = eval(case_values[i].get(Contact.request_header))
                expect = case_values[i].get(Contact.expect_result)
                return method, url, data, header, expect

    def write(self, case_id, status, is_exec='1', is_exec_col=9, status_col=12):
        wb, table = self.get_workspace()
        for i in range(2, table.max_row + 1):
            if table.cell(i, 1).value == case_id:
                table.cell(i, is_exec_col).value = is_exec
                table.cell(i, status_col).value = status
                break
        self.save(wb)

    def init(self, is_exec_col=9, status_col=12, is_exec="0", status=""):
        wb, table = self.get_workspace()
        for i in range(2, table.max_row + 1):
            table.cell(i, is_exec_col).value = is_exec
            table.cell(i, status_col).value = status
        self.save(wb)


rw = Read_Write(cf.data_dir_path, 1)
