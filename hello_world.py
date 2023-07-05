import random
import string

def generate_random_url():
    random_string = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(10))
    return f"https://www.example.com/{random_string}"
if __name__== "__main__":
    print("Hello World from the Devops repo!")
    url = generate_random_url()
    with open("random_url.md", "w") as f:
        f.write(f"Random URL: {url}")
