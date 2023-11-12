filename = "ST20231109_204419_Love Actually is All Around copy.jpg"

# Tách phần cần thiết bằng cách sử dụng slicing
prefix = filename.split('_')[:2]
result = '_'.join(prefix)

print(result)