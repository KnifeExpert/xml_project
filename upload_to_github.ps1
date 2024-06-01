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
    & $downloadScript

    # Run the script to modify the XML file
    & $modifyScript

    # Verify the modified file is updated
    if (Test-Path $outputFile) {
        # Check if there are any changes in the modified file
        $changes = git diff $outputFile
        if ($changes) {
            Write-Host "Changes detected in $outputFile. Preparing to commit..."
            # Add the modified XML file to the git repository
            git add $outputFile

            # Commit the changes with a message
            git commit -m "Automatická aktualizácia XML feedu - updated $outputFile"

            # Push the changes to the remote repository
            git push origin master
        } else {
            Write-Host "No changes in $outputFile, nothing to commit."
        }
    } else {
        Write-Host "$outputFile not found or not updated."
    }
}

# Process each supplier
Process-Supplier -downloadScript "C:\Users\larso\xml_project\download_xml.py" -modifyScript "C:\Users\larso\xml_project\modify_xml.py" -outputFile "supplier.xml"
Process-Supplier -downloadScript "C:\Users\larso\xml_project\download_xml_opinel.py" -modifyScript "C:\Users\larso\xml_project\modify_xml_opinel.py" -outputFile "opinel_supplier.xml"
Process-Supplier -downloadScript "C:\Users\larso\xml_project\download_xml_rosler.py" -modifyScript "C:\Users\larso\xml_project\modify_xml_rosler.py" -outputFile "rosler_supplier.xml"

# Add all other changes to the git repository (if needed)
$otherChanges = git status --porcelain
if ($otherChanges) {
    Write-Host "Other changes detected. Adding and committing..."
    git add .
    git commit -m "Automatická aktualizácia - ostatné zmeny"
    git push origin master
} else {
    Write-Host "No other changes detected."
}
