     # Path to your project directory
     $projectPath = "C:\Users\larso\xml_project"

     # Change to the project directory
     Set-Location $projectPath

     # Add the modified file to the git repository
     git add modified_supplier.xml

     # Commit the changes with a message
     git commit -m "Automatická aktualizácia XML feedu"

     # Push the changes to the remote repository
     git push origin main
