import os

paper_folders = ["ML_papers", "Navigation_papers"]
readme_file = "README.md"

def generate_paper_list(folder, start_string):
    # Get a list of Markdown files in the current folder
    markdown_files = [f for f in os.listdir(folder) if f.endswith(".md")]

    # Generate the paper list content for the current folder
    paper_list = start_string
    for i, file_name in enumerate(markdown_files, start=1):
        paper_title = file_name[:-3]
        paper_list += f"{i}. [{paper_title}]({folder}/{file_name})\n"
    
    return paper_list

def update_readme(readme_file, start_marker, end_marker, new_paper_list):
    # Read the existing README.md content
    with open(readme_file, "r") as file:
        readme_content = file.read()
    
    # Replace the paper list in the README.md content
    updated_readme_content = readme_content.replace(
        readme_content[readme_content.index(start_marker): readme_content.index(end_marker)],
        new_paper_list
    )
    # Write the updated content back to README.md
    with open(readme_file, "w") as file:
        file.write(updated_readme_content)

if __name__== "__main__":
    print("Hello World from the Devops repo!")
    
    readme_file = "README.md"

    ml_paper_list = generate_paper_list(folder, "## 📚 ML Paper list\n\n")
    update_readme(readme_file, "## 📚 ML Paper list", "## 📚 Navigation Paper list", ml_paper_list)

    nav_paper_list = generate_paper_list(folder, "## 📚 Navigation Paper list\n\n")
    update_readme(readme_file, "## 📚 Navigation Paper list", "## ✅ Website", nav_paper_list)
    
    # # Get a list of Markdown files in the papers directory
    # markdown_files = [f for f in os.listdir(papers_directory) if f.endswith(".md")]
    
    # # Generate the new paper list content
    # new_paper_list = "## 📚 Paper list\n\n"
    # for i, file_name in enumerate(markdown_files, start=1):
    #     paper_title = file_name[:-3]
    #     new_paper_list += f"{i}. [{paper_title}]({papers_directory}/{file_name})\n"
    
    print("Paper list in README.md has been updated.")
