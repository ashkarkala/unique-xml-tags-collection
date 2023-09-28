import xml.etree.ElementTree as ET

# Function to extract unique XML tags from a file
def extract_unique_xml_tags(filename):
    # Creates an empty set to store unique tags
    unique_tags = set()

    try:
        # Parses the XML file
        tree = ET.parse(filename)
        root = tree.getroot()


        # Recursive function to traverse the XML tree and extract tags
        def extract_tags(element):
            # Adds the tag to the set of unique tags
            unique_tags.add(element.tag)


            # Recursively processes child elements
            for child in element:
               extract_tags(child)

        # Starts extracting tags from the root element
        extract_tags(root)

        # Prints unique tags
        for tag in unique_tags:
            print(tag)

    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")
    except FileNotFoundError:
        print(f"File not found: {filename}")

# Specify the XML file to process
xml_file = r"path_to_the_xml_file"

# Calls the function to extract and print unique XML tags
extract_unique_xml_tags(xml_file)
