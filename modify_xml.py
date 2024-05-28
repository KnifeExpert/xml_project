import xml.etree.ElementTree as ET

try:
    tree = ET.parse('supplier.xml')
    root = tree.getroot()

    print("Starting modification of XML")

    for product in root.findall('PRODUCT'):
        in_stock = product.find('in_stock').text.lower() == 'true'
        stock_quantity = int(product.find('stock_quantity').text)

        if in_stock and stock_quantity == 0:
            product.find('availability').text = '3-7 dní'
            print(f"Product {product.find('name').text}: Set availability to 3-7 dní")
        elif not in_stock:
            product.find('availability').text = 'Na dotaz'
            print(f"Product {product.find('name').text}: Set availability to Na dotaz")

    tree.write('modified_supplier.xml')
    print("Finished modification and wrote to modified_supplier.xml")
except Exception as e:
    print(f"An error occurred: {e}")
