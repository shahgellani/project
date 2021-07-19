import pickle


def get_file_data():
    """

    :return: list
    """
    infile = open('accounts.data', 'rb')
    my_list = pickle.load(infile)
    infile.close()

    return my_list


def write_data_infile(my_list):
    """

    :param my_list:
    :return:
    """
    outfile = open('accounts.data', 'wb')
    pickle.dump(my_list, outfile)
    outfile.close()
