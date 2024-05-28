from lxml import etree

def convert_feed(input_file, output_file):
    tree = etree.parse(input_file)
    root = tree.getroot()

    shop = etree.Element("SHOP")

    for entry in root.findall("{http://www.w3.org/2005/Atom}entry"):
        shopitem = etree.SubElement(shop, "SHOPITEM")

        id_elem = entry.find("{http://base.google.com/ns/1.0}id")
        if id_elem is not None:
            code_new = etree.SubElement(shopitem, "CODE")
            code_new.text = id_elem.text

        title_elem = entry.find("{http://base.google.com/ns/1.0}title")
        if title_elem is not None:
            name_new = etree.SubElement(shopitem, "NAME")
            name_new.text = title_elem.text

        description_elem = entry.find("{http://base.google.com/ns/1.0}description")
        if description_elem is not None:
            description_new = etree.SubElement(shopitem, "DESCRIPTION")
            description_new.text = description_elem.text

        link_elem = entry.find("{http://base.google.com/ns/1.0}link")
        if link_elem is not None:
            orig_url_new = etree.SubElement(shopitem, "ORIG_URL")
            orig_url_new.text = link_elem.text

        condition_elem = entry.find("{http://base.google.com/ns/1.0}condition")
        if condition_elem is not None:
            condition_new = etree.SubElement(shopitem, "ITEM_CONDITION")
            grade_new = etree.SubElement(condition_new, "GRADE")
            if condition_elem.text in ["open_box", "refurbished", "used"]:
                grade_new.text = condition_elem.text
            else:
                grade_new.text = "used"  # Default to "used" if invalid value
            description_new = etree.SubElement(condition_new, "DESCRIPTION")
            description_new.text = "No description provided."

        price_elem = entry.find("{http://base.google.com/ns/1.0}price")
        if price_elem is not None:
            price_new = etree.SubElement(shopitem, "PRICE_VAT")
            price_new.text = price_elem.text.replace(' EUR', '')

        availability_elem = entry.find("{http://base.google.com/ns/1.0}availability")
        if availability_elem is not None:
            availability_new = etree.SubElement(shopitem, "AVAILABILITY")
            availability_new.text = availability_elem.text

        product_type_elem = entry.find("{http://base.google.com/ns/1.0}product_type")
        if product_type_elem is not None:
            categories_new = etree.SubElement(shopitem, "CATEGORIES")
            category_new = etree.SubElement(categories_new, "CATEGORY")
            category_new.text = product_type_elem.text

        image_link_elem = entry.find("{http://base.google.com/ns/1.0}image_link")
        if image_link_elem is not None:
            images_new = etree.SubElement(shopitem, "IMAGES")
            image_new = etree.SubElement(images_new, "IMAGE")
            image_new.text = image_link_elem.text

        brand_elem = entry.find("{http://base.google.com/ns/1.0}brand")
        if brand_elem is not None:
            brand_new = etree.SubElement(shopitem, "MANUFACTURER")
            brand_new.text = brand_elem.text

        gtin_elem = entry.find("{http://base.google.com/ns/1.0}gtin")
        if gtin_elem is not None:
            gtin_new = etree.SubElement(shopitem, "EAN")
            gtin_new.text = gtin_elem.text

    tree_new = etree.ElementTree(shop)
    tree_new.write(output_file, pretty_print=True, xml_declaration=True, encoding='UTF-8')

input_file = 'supplier.xml'
output_file = 'modified_supplier.xml'

convert_feed(input_file, output_file)
print(f"Feed bol konvertovaný a uložený ako '{output_file}'.")



