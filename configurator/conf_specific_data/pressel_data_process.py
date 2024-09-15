import pandas as pd


data = pd.read_excel('configurator/conf_specific_data/pressel_list.xlsx')


def main():   
    pressel_dict = read_data_into_dict(data)
    print(get_pressel_types(data))
    # print(pressel_dict)
    # search_result = search_in_pressel_dict(pressel_dict, 'OPAL', 'BRUSHED STAINLESS STEEL', 'GR', 'US91-15')


def read_data_into_dict(data):
    pressel_dict = data.to_dict(orient='index')
    return pressel_dict


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
        if item.upper() in POLYCARBONATE_COLOUR:
            pass 
        else:
            POLYCARBONATE_COLOUR.append((item, item.upper()))
    return POLYCARBONATE_COLOUR


def get_pressel_legend(data):
    unique_values = data['Pressel Legend'].unique()
    PRESSEL_LEGEND = [("None", "Select Pressel Legend")] 
    for item in unique_values:
        PRESSEL_LEGEND.append((item, item))
    return PRESSEL_LEGEND


PRESSEL_TYPES = get_pressel_types(data)
PRESSEL_FINISH = get_pressel_finish(data)
POLYCARBONATE_COLOUR = get_polycarbonate_colour(data)
PRESSEL_LEGEND = get_pressel_legend(data)


if __name__ == "__main__":
    main()
