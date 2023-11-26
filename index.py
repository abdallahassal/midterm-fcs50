import json
# function for open a new tab

def open_tab():
     title = input("Enter the title of the new tab: ")
     url = input("Enter the URL of the new tab: ")
# the user will enter the Title and Url 
     tabs[title] = {"title": title, "url": url} 
print("Successfully opened tab ")


