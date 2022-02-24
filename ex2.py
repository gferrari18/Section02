
website = input("Enter a website address: ")

url = website.startswith("http")

if url == True:
    print("Thank you! I will check it out")
else: print("Your link is invalid")