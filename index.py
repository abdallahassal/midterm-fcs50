import json
# function for open a new tab

def open_tab():
     title = input("Enter the title of the new tab: ")
     url = input("Enter the URL of the new tab: ")
# the user will enter the Title and Url 
     tabs[title] = {"title": title, "url": url} 
print("Successfully opened tab ")


# function to close a tab
def close_tab():
    tab_index = int(input("Enter the index of the tab: "))
    #I got this code from Google
    if tab_index in tabs:
        del tabs[tabs.keys()[tab_index]]

        print("closed successfully")
    else:
         print("Tab not found.")
         # The user is prompted to enter an index for a tab,
# then the code attempts to delete it from the tabs dictionary. It prints the success of closure or a message if the tab is not found.
        
        
# function to switch to a tab
def switch_tab():
    tab_index = int(input("Enter the index of the tab : "))
    if tab_index in tabs:
       print("Switched to tab " if tab_index in tabs else "Tab not found.")
       
       
# function to display all tabs
def display_all_tabs():
    if not tabs:
    
        print("No tabs are open.")
        return
    [print("{index}. Title: {title}, URL: {url})") for index, tab in enumerate(tabs.values(), start=1)]
    #The code prints information about open tabs (titles and URLs), or a message if there are none
    
#function to open a nested tab
def open_nested_tab():
    parent_tab_index = int(input("Enter the index of the parent tab"))
    new_tab_title = input("Enter the title of the new tab: ")
    new_tab_url = input("Enter the URL of the new tab: ")
    # Check if the parent tab exists
    if parent_tab_index not in tabs:
        print("Error: Parent tab at index does not exist.")
        return
    
    # Create a nested_tab dictionary
    nested_tab = {"title": new_tab_title, "url": new_tab_url}

    # Create a nested_tabs list if it doesn't exist
    tabs.setdefault(parent_tab_index, {"nested_tabs": []})

    tabs[parent_tab_index]["nested_tabs"].append(nested_tab)
    print(f"Nested tab '{new_tab_title}' opened successfully under tab '{parent_tab_index}'.")
  