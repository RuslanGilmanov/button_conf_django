
BUTTON_BODY = [
    ("", "Select button body"),
    ("3", "Compact 2"),
	("4", "Compact 2 Micro"),
    ("8", "Compact 3"),
    ("7", "Compact 3P")
]
	

def get_contact_type(button_body):
    if (button_body == "7" or
        button_body == "8" or
        button_body == "3"):
        CONTACT_TYPE = [
            ("1", "2xN/O"),
            ("2", "2xN/C"),
            ("3", "1xN/O 1xN/C")
        ]
    else:
         CONTACT_TYPE = [
            ("4", "1xN/O Screw terminals"),
            ("5", "1xN/O AMP"),
            ("6", "4-WAY MTA100 Vert/Horiz (Thyssen)"),
            ("7", "3-Way Vertical")
        ]
    
    return CONTACT_TYPE


LED_VOLTAGE = [
    ("", "Select LED voltage"),
    ("1", "Non Illuminated"),
    ("2", "12VDC (Phone & Alarm)"),
    ("3", "24VDC"),
    ("4", "110VDC"), #C3W - 110V LED does not exist
    ("5", "Multivolt 12-110V AC/DC"),
    ("6", "6VDC")
]

def get_led_color(led_voltage):
    if led_voltage == "2" or led_voltage == "3":
        LED_COLOR = [
            ("01", "Opal"),
            ("02", "Red"),
            ("04", "Blue"),
            ("03", "Amber"),
            ("05", "Green"),
            ("11", "Dual Opal"),
            ("12", "Dual Red"),
            ("13", "Dual Amber"),
            ("14", "Dual Blue"),
            ("15", "Dual Green"),
            ("22", "Opal/Red"),
            ("23", "Opal/Amber"),
            ("24", "Opal/Blue"),
            ("25", "Opal/Green"),
            ("27", "Amber/Green")
        ]
    elif led_voltage == "4" or led_voltage == "5" or led_voltage == "6":
        LED_COLOR = [
            ("01", "Opal"),
            ("02", "Red"),
            ("04", "Blue"),
            ("03", "Amber"),
            ("05", "Green")
        ]
    
    else:
        LED_COLOR = [
            ("00", "Non illuminated")
        ]
    return LED_COLOR


SURROUND_TYPE = [
    ("", "Select surround type"),
    ("1", "Flush"),
    ("2", "Handicap (Standard)"),
    ("3", "Extended"),
    ("4", "Plus Flush"),
    ("5", "Plus Handicap"),
    ("5", "Plus Extended")
]


SURROUND_COLOR = [
    ("", "Select surround color"),
    ("1", "Chrome (Standard)"),
    ("2", "Black Anodized"),
    ("3", "Brass"),
    ("4", "Unfinished"),
    ("5", "Anti-Bacterial Black Plastic"),
    ("6", "Anti-Bacterial Green Plastic"),
    ("7", "Chrome Exit")
]                    
	

SURROUND_FORM = [
    ("", "Select surround form"),
    ("1", "Square"),
    ("0", "Round"),
]
	