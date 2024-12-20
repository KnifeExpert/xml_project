# Path to your project directory
$projectPath = "C:\Users\larso\xml_project"

# Change to the project directory
Set-Location $projectPath

# Initialize git repository (if not already initialized)
git init

# Add remote repository (ignore error if already exists)
git remote add origin https://github.com/KnifeExpert/xml_project.git 2>$null

# Function to process a supplier
function Process-Supplier {
    param (
        [string]$downloadScript,
        [string]$modifyScript,
        [string]$outputFile
    )

    # Run the script to download the XML file
    Write-Host "Running download script: $downloadScript"
    python $downloadScript

    # Run the script to modify the XML file
    Write-Host "Running modify script: $modifyScript"
    python $modifyScript

    # Verify the modified file is updated
    if (Test-Path $outputFile) {
        Write-Host "Committing $outputFile..."
        # Add the modified XML file to the git repository
        git add $outputFile

        # Commit the changes with a message
        git commit -m "Automatická aktualizácia XML feedu - updated $outputFile" --allow-empty

        # Push the changes to the remote repository
        git push origin master
    } else {
        Write-Host "$outputFile not found or not updated."
    }
}

# Process each supplier
Process-Supplier -downloadScript "C:\Users\larso\xml_project\download_xml.py" -modifyScript "C:\Users\larso\xml_project\modify_xml.py" -outputFile "modified_supplier.xml"
Process-Supplier -downloadScript "C:\Users\larso\xml_project\download_xml_opinel.py" -modifyScript "C:\Users\larso\xml_project\modify_xml_opinel.py" -outputFile "modified_opinel_supplier.xml"
Process-Supplier -downloadScript "C:\Users\larso\xml_project\download_xml_rosler.py" -modifyScript "C:\Users\larso\xml_project\modify_xml_rosler.py" -outputFile "modified_rosler_supplier.xml"

# Add all other changes to the git repository (if needed)
$otherChanges = git status --porcelain
if ($otherChanges) {
    Write-Host "Other changes detected. Adding and committing..."
    git add .
    git commit -m "Automatická aktualizácia - ostatné zmeny" --allow-empty
    git push origin master
} else {
    Write-Host "No other changes detected."
}

