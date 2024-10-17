import pandas as pd


data = pd.read_excel('configurator/conf_specific_data/pressel_list.xlsx')
pressel_dict = data.to_dict(orient='index')


def main() -> None:
    get_pressel_types()
    get_pressel_finish()
    get_polycarbonate_colour()
    get_pressel_legend()
    search_in_pressel_dict()
        

def get_pressel_types() -> list:
    unique_values = data['Type'].unique()
    PRESSEL_TYPES = [("", "Select pressel type")] 
    for item in unique_values:
        PRESSEL_TYPES.append((item, item))
    return PRESSEL_TYPES


def get_pressel_finish(pressel_type) -> list:
     # Using a set for efficient duplicate removal
    pressel_finish_set = {
        sub_dict['Pressel / Plate finish'] 
        for sub_dict in pressel_dict.values() 
        if sub_dict.get('Type') == pressel_type
    }
    
    # Converting set back to list before returning
    return [(finish, finish.title()) for finish  in list(pressel_finish_set)]


def get_polycarbonate_colour(pressel_type, pressel_finish) -> list:
    pressel_polycarb_color_set = {
        sub_dict['Polycarbonate Colour'] 
        for sub_dict in pressel_dict.values() 
        if (sub_dict.get('Type') == pressel_type and
            sub_dict.get('Pressel / Plate finish') == pressel_finish)
    }

    return [(color, color.title()) for color in list(pressel_polycarb_color_set)]


def get_pressel_legend(pressel_type, pressel_finish, polycarb_color) -> list:
    pressel_legends = {
        sub_dict['Pressel Legend'] 
        for sub_dict in pressel_dict.values() 
        if (sub_dict.get('Type') == pressel_type and
            sub_dict.get('Pressel / Plate finish') == pressel_finish and
            sub_dict.get('Polycarbonate Colour') == polycarb_color)
    }

    return [(legend, legend) for legend in list(pressel_legends)]


def search_in_pressel_dict(pressel_type, pressel_finish, polycarb_color, pressel_legend)  -> str:

    for key, sub_dict in pressel_dict.items():
        if (sub_dict.get('Type') == pressel_type and
            sub_dict.get('Pressel / Plate finish') == pressel_finish and
            sub_dict.get('Polycarbonate Colour') == polycarb_color and
            str(sub_dict.get('Pressel Legend')) == pressel_legend):
            return sub_dict['Dewhurst Part Number']

    return "Pressel not found."


if __name__ == "__main__":
    main()
