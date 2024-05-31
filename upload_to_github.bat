@echo off
set LOGFILE=C:\Users\larso\xml_project\upload_to_github.log
echo Task started at %date% %time% > %LOGFILE%

echo Running download_xml.py for original supplier >> %LOGFILE% 2>&1
python C:\Users\larso\xml_project\download_xml.py >> %LOGFILE% 2>&1

echo Running modify_xml.py for original supplier >> %LOGFILE% 2>&1
python C:\Users\larso\xml_project\modify_xml.py >> %LOGFILE% 2>&1

echo Running download_xml_rosler.py for Rosler supplier >> %LOGFILE% 2>&1
python C:\Users\larso\xml_project\download_xml_rosler.py >> %LOGFILE% 2>&1

echo Running modify_xml_rosler.py for Rosler supplier >> %LOGFILE% 2>&1
python C:\Users\larso\xml_project\modify_xml_rosler.py >> %LOGFILE% 2>&1

echo Running download_xml_opinel.py for Opinel supplier >> %LOGFILE% 2>&1
python C:\Users\larso\xml_project\download_xml_opinel.py >> %LOGFILE% 2>&1

echo Running modify_xml_opinel.py for Opinel supplier >> %LOGFILE% 2>&1
python C:\Users\larso\xml_project\modify_xml_opinel.py >> %LOGFILE% 2>&1

echo Running git commands >> %LOGFILE% 2>&1
cd C:\Users\larso\xml_project

echo Explicitly removing files from git >> %LOGFILE% 2>&1
git rm --cached modified_supplier.xml >> %LOGFILE% 2>&1
git rm --cached modified_rosler_supplier.xml >> %LOGFILE% 2>&1
git rm --cached modified_opinel_supplier.xml >> %LOGFILE% 2>&1

echo Adding all files to git >> %LOGFILE% 2>&1
git add --all >> %LOGFILE% 2>&1

echo Checking status >> %LOGFILE% 2>&1
git status >> %LOGFILE% 2>&1

echo Committing changes >> %LOGFILE% 2>&1
git commit --allow-empty -m "Updated modified feeds for all suppliers" >> %LOGFILE% 2>&1

echo Pushing changes to GitHub >> %LOGFILE% 2>&1
git push origin master >> %LOGFILE% 2>&1

echo Task finished at %date% %time% >> %LOGFILE%
















