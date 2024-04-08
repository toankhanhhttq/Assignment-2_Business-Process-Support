import pandas as pd
# Đọc dữ liệu từ các bảng
sale_history = pd.read_csv("SaleHistory.csv")
customer_table = pd.read_csv("CustomerTable.csv")
product_data = pd.read_csv("ProductData.csv")

print("Sale History:")
print(sale_history.head())
print("\nCustomer Table:")
print(customer_table.head())
print("\nProduct Data:")
print(product_data.head())
customer_table.dropna(inplace=True)
product_data.dropna(inplace=True)
# Loại bỏ dấu phẩy trong cột Price của ProductData và chuyển đổi sang kiểu số
product_data['Price'] = product_data['Price'].replace('[\$,]', '', regex=True).astype(float)

# Đổi tên cột trong ProductData để khớp với bảng SaleHistory
product_data.rename(columns={"ProductName": "ProductName", "Price": "UnitPrice"}, inplace=True)

# Làm sạch dữ liệu trong Customer Table: Xóa các cột không cần thiết
cleaned_customer_table = customer_table.drop(['ContactNumber', 'Email', 'Address'], axis=1)

# Làm sạch dữ liệu trong Sale History: Đổi ngày thành định dạng datetime
sale_history['SaleDate'] = pd.to_datetime(sale_history['SaleDate'])

# Gộp dữ liệu từ SaleHistory, CustomerTable và ProductData dựa trên các cột tương ứng
merged_data = pd.merge(sale_history, cleaned_customer_table, on='CustomerID', how='left')
merged_data = pd.merge(merged_data, product_data, on='ProductID', how='left')

# Lưu dữ liệu đã làm sạch và tiền xử lý
merged_data.to_csv("preprocessed_data.csv", index=False)

# Hiển thị mẫu dữ liệu sau khi đã được làm sạch và tiền xử lý để kiểm tra
print("\nPreprocessed Data:")
print(merged_data.head())