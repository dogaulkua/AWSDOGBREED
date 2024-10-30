# TODO 6: Define print_results function below, specifically replace the None
#       below by the function definition of the print_results function. 
#       Notice that this function doesn't to return anything because it  
#       prints a summary of the results using results_dic and results_stats_dic
from prettytable import PrettyTable
import numpy as np


def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs = False, print_incorrect_breed = False):
    
    """
    Prints summary results on the classification and then prints incorrectly 
    classified dogs and incorrectly classified dog breeds if user indicates 
    they want those printouts (use non-default values)
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
      results_stats_dic - Dictionary that contains the results statistics (either
                   a  percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value 
      model - Indicates which CNN model architecture will be used by the 
              classifier function to classify the pet images,
              values must be either: resnet alexnet vgg (string)
      print_incorrect_dogs - True prints incorrectly classified dog images and 
                             False doesn't print anything(default) (bool)  
      print_incorrect_breed - True prints incorrectly classified dog breeds and 
                              False doesn't print anything(default) (bool) 
    Returns:
           None - simply printing results.
    """    


from prettytable import PrettyTable

def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs=False, print_incorrect_breed=False):
    """
    Prints summary results on the classification and then prints incorrectly 
    classified dogs and incorrectly classified dog breeds if the user indicates 
    they want those printouts (use non-default values)
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifier labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
      results_stats_dic - Dictionary that contains the results statistics (either
                   a percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value 
      model - Indicates which CNN model architecture will be used by the 
              classifier function to classify the pet images,
              values must be either: resnet alexnet vgg (string)
      print_incorrect_dogs - True prints incorrectly classified dog images and 
                             False doesn't print anything (default) (bool)  
      print_incorrect_breed - True prints incorrectly classified dog breeds and 
                              False doesn't print anything (default) (bool) 
    Returns:
           None - simply printing results.
    """ 

    table = PrettyTable()
    table.field_names = ["Metric", "ResNet", "AlexNet", "VGG"]
    table.align["Metric"] = "l"
    table.align["ResNet"] = "r"
    table.align["AlexNet"] = "r"
    table.align["VGG"] = "r"

    table.add_row(["Number of Images", results_stats_dic['n_images'], results_stats_dic['n_images'], results_stats_dic['n_images']])
    table.add_row(["Number of Dog Images", results_stats_dic['n_dogs_img'], results_stats_dic['n_dogs_img'], results_stats_dic['n_dogs_img']])
    table.add_row(["Number of Not-a-Dog Images", results_stats_dic['n_notdogs_img'], results_stats_dic['n_notdogs_img'], results_stats_dic['n_notdogs_img']])
    table.add_row(["% Correct Dogs", f"{results_stats_dic['pct_correct_dogs']:.2f}%", f"{results_stats_dic['pct_correct_dogs']:.2f}%", f"{results_stats_dic['pct_correct_dogs']:.2f}%"])
    table.add_row(["% Correct Breed", f"{results_stats_dic['pct_correct_breed']:.2f}%", f"{results_stats_dic['pct_correct_breed']:.2f}%", f"{results_stats_dic['pct_correct_breed']:.2f}%"])
    table.add_row(["% Correct Not-a-Dog", f"{results_stats_dic['pct_correct_notdogs']:.2f}%", f"{results_stats_dic['pct_correct_notdogs']:.2f}%", f"{results_stats_dic['pct_correct_notdogs']:.2f}%"])
    table.add_row(["% Match", f"{results_stats_dic['pct_match']:.2f}%", f"{results_stats_dic['pct_match']:.2f}%", f"{results_stats_dic['pct_match']:.2f}%"])

    if isinstance(results_stats_dic['pct_correct_notdogs'], float):
        pct_correct_notdogs = results_stats_dic['pct_correct_notdogs']
        pct_correct_dogs = results_stats_dic['pct_correct_dogs']
        pct_correct_breed = results_stats_dic['pct_correct_breed']
        pct_match = results_stats_dic['pct_match']
        table.add_row(["% Not-a-Dog Correct", f"{pct_correct_notdogs:.2f}%", f"{pct_correct_notdogs:.2f}%", f"{pct_correct_notdogs:.2f}%"])
        table.add_row(["% Dogs Correct", f"{pct_correct_dogs:.2f}%", f"{pct_correct_dogs:.2f}%", f"{pct_correct_dogs:.2f}%"])
        table.add_row(["% Breeds Correct", f"{pct_correct_breed:.2f}%", f"{pct_correct_breed:.2f}%", f"{pct_correct_breed:.2f}%"])
        table.add_row(["% Match Labels", f"{pct_match:.2f}%", f"{pct_match:.2f}%", f"{pct_match:.2f}%"])
    else:
   
        table.add_row(["% Not-a-Dog Correct", f"{results_stats_dic['pct_correct_notdogs'][model]:.2f}%", f"{results_stats_dic['pct_correct_notdogs'][model]:.2f}%", f"{results_stats_dic['pct_correct_notdogs'][model]:.2f}%"])
        table.add_row(["% Dogs Correct", f"{results_stats_dic['pct_correct_dogs'][model]:.2f}%", f"{results_stats_dic['pct_correct_dogs'][model]:.2f}%", f"{results_stats_dic['pct_correct_dogs'][model]:.2f}%"])
        table.add_row(["% Breeds Correct", f"{results_stats_dic['pct_correct_breed'][model]:.2f}%", f"{results_stats_dic['pct_correct_breed'][model]:.2f}%", f"{results_stats_dic['pct_correct_breed'][model]:.2f}%"])
        table.add_row(["% Match Labels", f"{results_stats_dic['pct_match'][model]:.2f}%", f"{results_stats_dic['pct_match'][model]:.2f}%", f"{results_stats_dic['pct_match'][model]:.2f}%"])

    print("\n\n*** Results Summary for CNN Model Architecture", model.upper(), "***")
    print(table)


    if print_incorrect_dogs or print_incorrect_breed:
        if print_incorrect_dogs:
            print("\nMisclassified Dogs:")
            for key in results_dic:
                if sum(results_dic[key][3:]) == 1:
                    print("Pet Image: {}, Classifier Label: {}".format(key, results_dic[key][1]))

        if print_incorrect_breed:
            print("\nMisclassified Breed's of Dog:")
            for key in results_dic:
                if sum(results_dic[key][3:]) == 2 and results_dic[key][2] == 0:
                    print("Pet Image: {}, Classifier Label: {}".format(key, results_dic[key][1]))
