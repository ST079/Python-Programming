# write.py
def write_inventory(contents, selected_item, update_text):
    with open("furniture.txt", 'w') as f:
        for item in contents:
            if item.strip() == selected_item.strip():
                f.write(update_text)
            else:
                f.write(item)
