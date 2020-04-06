import argparse, json
from src import utils, covid_tracker as ct


def main(args):
    """Gives the information about corona virus

    :param args: input arguments
    :return: None
    """

    # Config parser
    with open(args.config_file_name) as config_file:
        config = json.load(config_file)

    # Fetch covid and world population data
    covid_json = utils.get_url_as_json(config['covid_data_url'])
    world_pop_df = utils.read_csv_as_df(config['world_pop_csv_filename'])

    type_available = {'c': 'confirmed', 'd': 'deaths', 'r': 'recovered'}

    exit_flag = False
    while(not exit_flag):

        input_loop_flag = True
        try_count = 1

        while(input_loop_flag):

            if try_count > 3:
                print("!!!!!! Wrong Input, exiting ......")
                exit(1)

            # Fetch user inputs
            country = str(input('Enter country: '))
            type_input = str(input(
                            'Enter count type{0}: '.format(
                                            type_available)))

            # Print the available countries during wrong user input
            if country in covid_json.keys() and \
                    type_input in type_available.keys():
                input_loop_flag = False
            else:
                print("\n ------ Wrong input, countries available are:\n\n{}\n\n".format(
                    [key for key in covid_json.keys()]))
                try_count = try_count + 1
        # ############################## End of input loop

        # Set count_type
        count_type = type_available[type_input]

        # Execute count percent
        count_percent = ct.get_percent_count(country=country,
                                             count_type=count_type,
                                             covid_json=covid_json,
                                             world_pop_df=world_pop_df)

        print("{0} count percent of {1} is {2}".format(count_type.capitalize(),
                                                       country,
                                                       count_percent))

        # Continue?
        if str(input("Do you want to continue(Y/N): ")).upper() in ['N', 'NO']:
            print(" ~~~~~ Thank You! Goodbye!!!")
            exit_flag = True


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config_file_name',
                        help="name of the config file")
    args = parser.parse_args()
    main(args)
