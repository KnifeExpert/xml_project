from lxml import etree as ET

def convert_feed(input_file, output_file):
    tree = ET.parse(input_file)
    root = tree.getroot()

    shop = ET.Element("SHOP")

    for entry in root.findall("element"):
        shopitem = ET.SubElement(shop, "SHOPITEM")

        id_elem = entry.find("EXTERNI_KOD")
        if id_elem is not None:
            code_new = ET.SubElement(shopitem, "CODE")
            code_new.text = id_elem.text

        title_elem = entry.find("NAZEV_POLOZKY")
        if title_elem is not None:
            name_new = ET.SubElement(shopitem, "NAME")
            name_new.text = title_elem.text

        description_elem = entry.find("POPIS")
        if description_elem is not None:
            description_new = ET.SubElement(shopitem, "DESCRIPTION")
            description_new.text = description_elem.text

        link_elem = entry.find("URL")
        if link_elem is not None:
            orig_url_new = ET.SubElement(shopitem, "ORIG_URL")
            orig_url_new.text = link_elem.text

        condition_new = ET.SubElement(shopitem, "ITEM_CONDITION")
        grade_new = ET.SubElement(condition_new, "GRADE")
        # Use a valid value for GRADE
        grade_new.text = "used"
        description_new = ET.SubElement(condition_new, "DESCRIPTION")
        description_new.text = "New item."

        price_elem = entry.find("MOC")
        if price_elem is not None:
            price_new = ET.SubElement(shopitem, "PRICE_VAT")
            price_new.text = "{:.2f}".format(float(price_elem.text.replace(',', '.')))

        availability_new = ET.SubElement(shopitem, "AVAILABILITY")
        availability_new.text = "3-7 dní"
        negative_amount = ET.SubElement(shopitem, "NEGATIVE_AMOUNT")
        negative_amount.text = "1"

        category_elem = entry.find("KODKATEGORIE")
        categories_new = ET.SubElement(shopitem, "CATEGORIES")
        category_new = ET.SubElement(categories_new, "CATEGORY")
        if category_elem is not None and category_elem.text and category_elem.text.strip():
            category_new.text = category_elem.text
        else:
            category_new.text = "Default Category"  # Nastavíme predvolenú hodnotu

        image_link_elem = entry.find("IMGURL")
        if image_link_elem is not None:
            images_new = ET.SubElement(shopitem, "IMAGES")
            image_new = ET.SubElement(images_new, "IMAGE")
            image_new.text = image_link_elem.text

        brand_elem = entry.find("SKUPINA")
        if brand_elem is not None:
            brand_new = ET.SubElement(shopitem, "MANUFACTURER")
            brand_new.text = brand_elem.text

        gtin_elem = entry.find("EAN")
        if gtin_elem is not None and gtin_elem.text:
            gtin_new = ET.SubElement(shopitem, "EAN")
            gtin_new.text = gtin_elem.text
        else:
            gtin_new = ET.SubElement(shopitem, "EAN")
            gtin_new.text = "N/A"

        required_elements = {
            'ACTION_PRICE': '0', 'ACTION_PRICE_FROM': '2023-01-01', 'ACTION_PRICE_UNTIL': '2023-12-31', 'ADULT': 'false',
            'ALLOWS_IPLATBA': 'false', 'ALLOWS_PAYU': 'false', 'ALLOWS_PAY_ONLINE': 'false', 'APPLY_DISCOUNT_COUPON': 'false',
            'APPLY_LOYALTY_DISCOUNT': 'false', 'APPLY_QUANTITY_DISCOUNT': 'false', 'APPLY_VOLUME_DISCOUNT': 'false',
            'ARUKERESO_HIDDEN': 'false', 'ARUKERESO_MARKETPLACE_HIDDEN': 'false', 'ATYPICAL_BILLING': 'false',
            'ATYPICAL_SHIPPING': 'false', 'CURRENCY': 'EUR', 'DECIMAL_COUNT': '2', 'EXTERNAL_ID': 'N/A', 'FIRMY_CZ': 'false',
            'FREE_BILLING': 'false', 'FREE_SHIPPING': 'false', 'GUID': '00000000-0000-0000-0000-000000000000',
            'HEUREKA_CART_HIDDEN': 'false', 'HEUREKA_HIDDEN': 'false', 'ITEM_TYPE': 'product', 'MIN_PRICE_RATIO': '0.0',
            'PRICE': '0.0', 'PRICE_RATIO': '0.0', 'TOLL_FREE': 'false', 'VAT': '20', 'VISIBILITY': 'visible',
            'VISIBLE': 'true', 'XML_FEED_NAME': 'N/A', 'ZBOZI_HIDDEN': 'false'
        }

        for elem_name, default_value in required_elements.items():
            if shopitem.find(elem_name) is None:
                ET.SubElement(shopitem, elem_name).text = default_value

        sizeid_new = ET.SubElement(shopitem, "SIZEID")
        sizeid_id = ET.SubElement(sizeid_new, "ID")
        sizeid_id.text = "0"
        sizeid_label = ET.SubElement(sizeid_new, "LABEL")
        sizeid_label.text = "N/A"

    if len(shop):
        tree_new = ET.ElementTree(shop)
        tree_new.write(output_file, pretty_print=True, xml_declaration=True, encoding='UTF-8')
        print(f"Feed bol konvertovaný a uložený ako '{output_file}'.")
    else:
        print("No SHOPITEM elements found. Output file not created.")

input_file = 'C:\\Users\\larso\\xml_project\\opinel_supplier.xml'
output_file = 'C:\\Users\\larso\\xml_project\\modified_opinel_supplier.xml'

convert_feed(input_file, output_file)


