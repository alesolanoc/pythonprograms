# Prompt: Let you type an IP address and then says all the information about that IP address. without any imports

# Function to validate the IP address
def validate_ip(ip):
    """
    Validates the given IP address.

    Args:
    - ip (str): The IP address to be validated.

    Returns:
    - bool: True if the IP address is valid, False otherwise.
    """
    # Split the IP address into octets
    octets = ip.split('.')

    # Check if the IP address has 4 octets
    if len(octets) != 4:
        return False

    # Check if each octet is a valid number between 0 and 255
    for octet in octets:
        if not octet.isdigit() or int(octet) < 0 or int(octet) > 255:
            return False

    return True

# Function to get information about the IP address
def get_ip_info(ip):
    """
    Retrieves information about the given IP address.

    Args:
    - ip (str): The IP address to get information about.

    Returns:
    - str: Information about the IP address.
    """
    # Validate the IP address
    if not validate_ip(ip):
        return "Invalid IP address"

    # Split the IP address into octets
    octets = ip.split('.')

    # Get the network class based on the first octet
    first_octet = int(octets[0])
    if first_octet >= 1 and first_octet <= 126:
        network_class = "A"
    elif first_octet >= 128 and first_octet <= 191:
        network_class = "B"
    elif first_octet >= 192 and first_octet <= 223:
        network_class = "C"
    elif first_octet >= 224 and first_octet <= 239:
        network_class = "D"
    elif first_octet >= 240 and first_octet <= 255:
        network_class = "E"

    # Get the default subnet mask based on the network class
    if network_class == "A":
        subnet_mask = "255.0.0.0"
    elif network_class == "B":
        subnet_mask = "255.255.0.0"
    elif network_class == "C":
        subnet_mask = "255.255.255.0"
    else:
        subnet_mask = "N/A"

    # Get the IP address type based on the first octet
    if first_octet == 10 or (first_octet == 172 and int(octets[1]) >= 16 and int(octets[1]) <= 31) or (first_octet == 192 and int(octets[1]) == 168):
        ip_type = "Private"
    else:
        ip_type = "Public"

    # Construct the information string
    info = f"IP Address: {ip}\nNetwork Class: {network_class}\nSubnet Mask: {subnet_mask}\nIP Type: {ip_type}"

    return info

# Get the IP address from the user
ip_address = input("Enter an IP address: ")

# Get the information about the IP address
ip_info = get_ip_info(ip_address)

# Print the information
print(ip_info)
