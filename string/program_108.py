# Program 108: Product code generator

product_name = "Wireless Keyboard"
product_id = 105

code = (
    product_name[:3].upper()
    + "-"
    + str(product_id).zfill(4)
)

print(f"Product: {product_name}")
print(f"Product Code: {code}")
