# Path to your project directory
$projectPath = "C:\Users\larso\xml_project"

# Change to the project directory
Set-Location $projectPath

# Initialize git repository (if not already initialized)
git init

# Add remote repository (if not already added)
git remote add origin https://github.com/KnifeExpert/xml_project.git 2>$null

# Add all files to the git repository
git add .

# Commit the changes with a message
git commit -m "Automatická aktualizácia XML feedu"

# Push the changes to the remote repository
git push origin master
