import pandas as pd

def sort_and_save_links(input_file, output_file):
    # Đọc tệp CSV đã sắp xếp, sử dụng trị số cột 0 và 1
    df = pd.read_csv(input_file, header=None)

    # Tạo một Series chứa số lần xuất hiện của từng phần tử trong cột 0 (Link)
    link_counts = df[0].value_counts()

    # Thêm một cột mới là số lần duplicate (dup)
    df['Dup'] = df[0].map(link_counts) - 1  # Trừ 1 để loại bỏ một lần xuất hiện ban đầu

    # Sắp xếp theo thứ tự giảm dần của số lần duplicate
    df_sorted = df.sort_values(by='Dup', ascending=False)

    # Lấy danh sách các phần tử đã sắp xếp
    sorted_links = df_sorted[0]

    # Ghi danh sách đã sắp xếp và số lần duplicate vào tệp
    df_sorted.to_csv(output_file, index=False)

# Gọi hàm và truyền tên tệp input và output
sort_and_save_links('output_sorted_by_view.csv', 'output_sorted_by_repeat.csv')
