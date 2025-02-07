

def create_organizational_units_ldif(filename, ou_names, base_dn):
    """Creates an LDIF file for multiple organizational units."""
    
    ldif_content = """
    # LDIF file for organizational units
    """.strip() + "\n\n"
    
    for ou_name in ou_names:
        ldif_content += f"""# Organizational unit for {ou_name}
dn: ou={ou_name},{base_dn}
changetype: add
objectClass: organizationalUnit
ou: {ou_name}

"""
    
    try:
        with open(filename, "w") as f:
            f.write(ldif_content)
        print(f"LDIF file '{filename}' created successfully.")
    except Exception as e:
        print(f"Error creating LDIF file '{filename}': {e}")


# List of organizational units
ou_names = [
    "directores", "profesores", "alumnos", "personalnodocente", 
    "eso1", "eso2", "eso3", "eso4", 
    "bach1ciencias", "bach1humanidades", "bach2ciencias", "bach2humanidades",
    "profesoreseso", "profesoresbach", "profesoreseso1", "profesoreseso2", "profesoreseso3", "profesoreseso4",
    "profesoresbach1ciencias", "profesoresbach1humanidades", "profesoresbach2ciencias", "profesoresbach2humanidades"
]

# Base DN
domain_base_dn = "dc=example,dc=org"  # Replace with your actual base DN

# Generate the LDIF file
create_organizational_units_ldif("ou.ldif", ou_names, domain_base_dn)
