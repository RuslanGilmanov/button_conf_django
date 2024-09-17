import pandas as pd


data = pd.read_excel('configurator/conf_specific_data/pressel_list.xlsx')
pressel_dict = data.to_dict(orient='index')


def get_pressel_types(data):
    unique_values = data['Type'].unique()
    PRESSEL_TYPES = [("None", "Select pressel type")] 
    for item in unique_values:
        PRESSEL_TYPES.append((item, item))
    return PRESSEL_TYPES


def get_pressel_finish(data):
    unique_values = data['Pressel / Plate finish'].unique()
    PRESSEL_FINISH = [("None", "Select pressel finish")] 
    for item in unique_values:
        PRESSEL_FINISH.append((item, item.upper()))
    return PRESSEL_FINISH


def get_polycarbonate_colour(data):
    unique_values = data['Polycarbonate Colour'].unique()
    POLYCARBONATE_COLOUR = [("None", "Select Polycarbonate colour")] 
    for item in unique_values:
        POLYCARBONATE_COLOUR.append((item, item.upper()))
    return POLYCARBONATE_COLOUR


def get_pressel_legend(data):
    unique_values = data['Pressel Legend'].unique()
    PRESSEL_LEGEND = [("None", "Select Pressel Legend")] 
    for item in unique_values:
        PRESSEL_LEGEND.append((item, item))
    return PRESSEL_LEGEND


def search_in_pressel_dict(pressel_type, pressel_finish, polycarb_colour, pressel_legend):

    for key, sub_dict in pressel_dict.items():
        if (sub_dict.get('Type') == pressel_type and
            sub_dict.get('Pressel / Plate finish') == pressel_finish and
            sub_dict.get('Polycarbonate Colour') == polycarb_colour and
            str(sub_dict.get('Pressel Legend')) == pressel_legend):
            print(pressel_type)
            print(pressel_finish)
            print(polycarb_colour)
            print(type(pressel_legend))
            print(f"Dewhurst Part Number: {sub_dict['Dewhurst Part Number']}")
            return sub_dict['Dewhurst Part Number']

    return "Pressel not found."


PRESSEL_TYPES = get_pressel_types(data)
PRESSEL_FINISH = get_pressel_finish(data)
POLYCARBONATE_COLOUR = get_polycarbonate_colour(data)
PRESSEL_LEGEND = get_pressel_legend(data)
