import pandas as pd


def main():
    excell_file = 'configurator/conf_specific_data/pressel_list.xlsx'
    data = load_excell_file(excell_file)
    pressel_dict = read_data_into_dict(data)
    # pprint(pressel_dict)
    search_result = search_in_pressel_dict(pressel_dict, 'OPAL', 'BRUSHED STAINLESS STEEL', 'GR', 'US91-15')


def load_excell_file(excell_file):
    loaded_data = pd.read_excel(excell_file)
    return loaded_data


def read_data_into_dict(data):
    pressel_dict = data.to_dict(orient='index')
    return pressel_dict


def search_in_pressel_dict(pressel_dict,
                           polycarb_colour,
                           pressel_finish,
                           pressel_legend,
                           pressel_type):

    found = False

    for key, sub_dict in pressel_dict.items():
        if (sub_dict.get('Type') == pressel_type and
            sub_dict.get('Pressel / Plate finish') == pressel_finish and
            sub_dict.get('Polycarbonate Colour') == polycarb_colour and
            sub_dict.get('Pressel Legend') == pressel_legend):
            print(f"Dewhurst Part Number: {sub_dict['Dewhurst Part Number']}")
            return sub_dict['Dewhurst Part Number']
            found = True
            break

    if not found:
        print("Pressel not found.")


if __name__ == "__main__":
    main()
