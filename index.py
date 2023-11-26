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
    # Takes user input for parent tab index, new tab title, and URL. Appends a nested tab to the parent tab. Prints success message
    
# function to sort all tabs
def sort_all_tabs(tabs):
    sorted_tabs = sorted(tabs, key=lambda x: x[0])
    print("Sorted tabs:")
    for index, (title, url) in enumerate(sorted_tabs, start=1):
        print(f"{index}. Title: {title}, URL: {url}")
#the code sorts a list of tabs by title and prints the sorted tabs with their index, title, and URL.

#function to save tabs

def save_tabs(tabs):
    with open("tabs.json", "w") as f:
        json.dump(tabs, f, indent=2)
    print("Tabs saved to 'tabs.json'.")
 #The code saves a list of tabs as a formatted JSON file named "tabs.json.
 
 #function to import tabs
 

def import_tabs(tabs):
    file_path = "tabs.json"

    if not os.path.exists(file_path):
        print("No file found. Please open and save tabs before importing.")
        return

    with open(file_path, "r") as f:
        tabs.clear()
        tabs.update(json.load(f))

    print("Tabs imported ")
 #Here I used Google to solve it.
 #Loads tabs from "tabs.json" into tabs, handles non-existent files, and provides status messages.


# Main loop
def main():
     while True:
        print("\nMenu:")
        print("1. Open Tab")
        print("2. Close Tab")
        print("3. Switch Tab")
        print("4. Display All Tabs")
        print("5. Open Nested Tab")
        print("6. Sort All Tabs")
        print("7. Save Tabs")
        print("8. Import Tabs")
        print("9. Exit")
 #Infinite loop presenting a menu for various tab operations: open, close, switch, display, open nested, sort, save, import, and exit
        choice = input("Enter your choice: ")
        match choice:
         case 1:
            open_tab()
         case 2:
            close_tab()
         case 3:
            switch_tab()
         case 4:
            display_all_tabs()
         case 5:
            open_nested_tab()
         case 6:
            sort_all_tabs()
         case 7:
            save_tabs()
         case 8:
            import_tabs()
         case 9:
            break
            print("\n")

#User chooses tab operations: open, close, switch, display, open nested, sort, save, import, or exit, with corresponding function calls.
    