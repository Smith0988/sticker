import os
import shutil
import sys
import openpyxl
from openpyxl.utils import get_column_letter
from openpyxl.styles import Alignment


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

source_path = resource_path("base_form/BumperStickers.xlsm")

destination_path = resource_path("BumperStickers.xlsm")


if not os.path.exists(destination_path):
    shutil.copy(source_path, destination_path)


# Hàm ghi dữ liệu vào tệp Excel
import openpyxl
from openpyxl.styles import Alignment

def write_to_excel(data):
    # Đường dẫn đến tệp Excel
    excel_file = "BumperStickers.xlsm"

    # Mở tệp Excel
    workbook = openpyxl.load_workbook(excel_file, data_only=True)

    # Chọn sheet mà bạn muốn làm việc, hãy chắc chắn rằng sheet có tên chính xác
    sheet = workbook["Template"]

    # Tìm hàng tiếp theo để ghi dữ liệu
    next_row = sheet.max_row + 1

    # Gán giá trị từ list vào các biến
    col_2_data = data[0]
    col_8_data = data[1]
    col_19_data = data[2]

    sheet.cell(row=next_row, column=2, value=col_2_data).alignment = Alignment(horizontal='center')
    sheet.cell(row=next_row, column=11, value=col_2_data).alignment = Alignment(horizontal='center')
    sheet.cell(row=next_row, column=8, value=col_8_data).alignment = Alignment(horizontal='center')
    sheet.cell(row=next_row, column=19, value=col_19_data).alignment = Alignment(horizontal='center')

    # Lưu tệp Excel
    workbook.save(excel_file)

if __name__ == "__main__":
    # Sử dụng hàm để ghi dữ liệu vào tệp Excel
    data_to_write = ["value1", "value2", "value3"]
    write_to_excel(data_to_write)
