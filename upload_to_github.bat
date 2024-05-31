@echo off
set LOGFILE=C:\Users\larso\xml_project\upload_to_github.log
echo Task started at %date% %time% > %LOGFILE%

echo Running download_xml.py for original supplier >> %LOGFILE% 2>&1
python C:\Users\larso\xml_project\download_xml.py >> %LOGFILE% 2>&1

echo Running modify_xml.py for original supplier >> %LOGFILE% 2>&1
python C:\Users\larso\xml_project\modify_xml.py >> %LOGFILE% 2>&1

echo Running modify_xml_rosler.py for Rosler supplier >> %LOGFILE% 2>&1
python C:\Users\larso\xml_project\modify_xml_rosler.py >> %LOGFILE% 2>&1

echo Running modify_xml_opinel.py for Opinel supplier >> %LOGFILE% 2>&1
python C:\Users\larso\xml_project\modify_xml_opinel.py >> %LOGFILE% 2>&1

echo Forcing timestamp update on XML files >> %LOGFILE% 2>&1
copy /b modified_supplier.xml +,, >> %LOGFILE% 2>&1
copy /b modified_rosler_supplier.xml +,, >> %LOGFILE% 2>&1
copy /b modified_opinel_supplier.xml +,, >> %LOGFILE% 2>&1

echo Running git commands >> %LOGFILE% 2>&1
cd C:\Users\larso\xml_project

git add -f modified_supplier.xml modified_rosler_supplier.xml modified_opinel_supplier.xml >> %LOGFILE% 2>&1
git commit -m "Force-updated modified feeds" >> %LOGFILE% 2>&1
git push origin master >> %LOGFILE% 2>&1

echo Task finished at %date% %time% >> %LOGFILE%
