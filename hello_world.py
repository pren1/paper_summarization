# import random
# import string

# def generate_random_url():
#     random_string = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(10))
#     return f"https://www.example.com/{random_string}"
# if __name__== "__main__":
#     print("Hello World from the Devops repo!")
#     url = generate_random_url()
#     with open("random_url.md", "w") as f:
#         f.write(f"Random URL: {url}")

import os

if __name__== "__main__":
    print("Hello World from the Devops repo!")
    
    papers_directory = "papers"
    readme_file = "README.md"
    
    # Get a list of Markdown files in the papers directory
    markdown_files = [f for f in os.listdir(papers_directory) if f.endswith(".md")]
    
    # Generate the new paper list content
    new_paper_list = "## 📚 Paper list\n\n"
    for i, file_name in enumerate(markdown_files, start=1):
        paper_title = file_name[:-3]
        new_paper_list += f"{i}. [{paper_title}]({papers_directory}/{file_name})\n"
    
    # Read the existing README.md content
    with open(readme_file, "r") as file:
        readme_content = file.read()
    
    # Replace the paper list in the README.md content
    start_marker = "## 📚 Paper list"
    end_marker = "## Credits"
    updated_readme_content = readme_content.replace(
        readme_content[readme_content.index(start_marker): readme_content.index(end_marker)],
        new_paper_list
    )
    
    # Write the updated content back to README.md
    with open(readme_file, "w") as file:
        file.write(updated_readme_content)
    
    print("Paper list in README.md has been updated.")
