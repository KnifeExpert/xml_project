@echo off
cd C:\Users\larso\xml_project
python download_xml.py
python modify_xml.py
git add modified_supplier.xml modify_xml.py supplier.xml updated_supplier.xml
git commit -m "Added modified feed"
git push origin master
