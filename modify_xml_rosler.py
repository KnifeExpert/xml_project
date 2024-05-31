from lxml import etree as ET

def convert_feed(input_file, output_file):
    tree = ET.parse(input_file)
    root = tree.getroot()

    shop = ET.Element("SHOP")

    for entry in root.findall("shopitem"):
        shopitem = ET.SubElement(shop, "SHOPITEM")

        id_elem = entry.find("item_id")
        if id_elem is not None:
            code_new = ET.SubElement(shopitem, "CODE")
            code_new.text = id_elem.text

        title_elem = entry.find("productname")
        if title_elem is not None:
            name_new = ET.SubElement(shopitem, "NAME")
            name_new.text = title_elem.text

        description_elem = entry.find("description")
        if description_elem is not None:
            description_new = ET.SubElement(shopitem, "DESCRIPTION")
            description_new.text = description_elem.text

        link_elem = entry.find("url")
        if link_elem is not None:
            orig_url_new = ET.SubElement(shopitem, "ORIG_URL")
            orig_url_new.text = link_elem.text

        condition_elem = entry.find("item_type")
        if condition_elem is not None:
            condition_new = ET.SubElement(shopitem, "ITEM_CONDITION")
            grade_new = ET.SubElement(condition_new, "GRADE")
            if condition_elem.text.lower() in ["open_box", "refurbished", "used"]:
                grade_new.text = condition_elem.text.lower()
            else:
                grade_new.text = "used"
            description_new = ET.SubElement(condition_new, "DESCRIPTION")
            description_new.text = "No description provided."

        price_elem = entry.find("price_vat")
        if price_elem is not None:
            price_new = ET.SubElement(shopitem, "PRICE_VAT")
            price_new.text = "{:.2f}".format(float(price_elem.text.replace(',', '.')))

        availability_elem = entry.find("delivery_date")
        if availability_elem is not None:
            availability_new = ET.SubElement(shopitem, "AVAILABILITY")
            negative_amount = ET.SubElement(shopitem, "NEGATIVE_AMOUNT")
            if availability_elem.text == '0':
                availability_new.text = "3-7 dní"
                negative_amount.text = "1"
            else:
                availability_new.text = "Na dotaz"
                negative_amount.text = "0"

        product_type_elem = entry.find("categorytext")
        if product_type_elem is not None:
            categories_new = ET.SubElement(shopitem, "CATEGORIES")
            category_new = ET.SubElement(categories_new, "CATEGORY")
            category_new.text = product_type_elem.text

        image_link_elem = entry.find("imgurl")
        if image_link_elem is not None:
            images_new = ET.SubElement(shopitem, "IMAGES")
            image_new = ET.SubElement(images_new, "IMAGE")
            image_new.text = image_link_elem.text

        brand_elem = entry.find("manufacturer")
        if brand_elem is not None:
            brand_new = ET.SubElement(shopitem, "MANUFACTURER")
            brand_new.text = brand_elem.text

        gtin_elem = entry.find("ean")
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

    tree_new = ET.ElementTree(shop)
    tree_new.write(output_file, pretty_print=True, xml_declaration=True, encoding='UTF-8')

input_file = 'C:\\Users\\larso\\xml_project\\rosler_supplier.xml'
output_file = 'C:\\Users\\larso\\xml_project\\modified_rosler_supplier.xml'

convert_feed(input_file, output_file)
print(f"Feed bol konvertovaný a uložený ako '{output_file}'.")

