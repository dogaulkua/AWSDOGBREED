# TODO 5: Define calculates_results_stats function below, please be certain to replace None
#       in the return statement with the results_stats_dic dictionary that you create 
#       with this function
# 
def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run using classifier's model 
    architecture to classifying pet images. Then puts the results statistics in a 
    dictionary (results_stats_dic) so that it's returned for printing as to help
    the user to determine the 'best' model for classifying images. Note that 
    the statistics calculated as the results are either percentages or counts.
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
    Returns:
     results_stats_dic - Dictionary that contains the results statistics (either
                    a percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value. See comments above
                     and the previous topic Calculating Results in the class for details
                     on how to calculate the counts and statistics.
    """        
    # Replace None with the results_stats_dic dictionary that you created with 
    # this function 
    num_images = len(results_dic)
    num_correct_dogs = 0
    num_dog_images = 0
    num_correct_notdogs = 0
    num_notdog_images = 0
    num_correct_breed = 0
    num_label_matches = 0
    for key in results_dic:
        if results_dic[key][3] == 1 and results_dic[key][4] == 1:
            num_correct_dogs += 1
        if results_dic[key][3] == 1:
            num_dog_images += 1
        if results_dic[key][3] == 0 and results_dic[key][4] == 0:
            num_correct_notdogs += 1
        if results_dic[key][3] == 0:
            num_notdog_images += 1
        if results_dic[key][3] == 1 and results_dic[key][2] == 1:
            num_correct_breed += 1
        if results_dic[key][2] == 1:
            num_label_matches += 1
    pct_correct_dogs = (num_correct_dogs / num_dog_images) * 100 if num_dog_images > 0 else 0
    pct_correct_notdogs = (num_correct_notdogs / num_notdog_images) * 100 if num_notdog_images > 0 else 0
    pct_correct_breed = (num_correct_breed / num_dog_images) * 100 if num_dog_images > 0 else 0
    pct_match = (num_label_matches / num_images) * 100 if num_images > 0 else 0
    results_stats_dic = {
        'n_images': num_images,
        'n_dogs_img': num_dog_images,
        'n_notdogs_img': num_notdog_images,
        'n_correct_dogs': num_correct_dogs,
        'n_correct_notdogs': num_correct_notdogs,
        'n_correct_breed': num_correct_breed,
        'pct_correct_dogs': pct_correct_dogs,
        'pct_correct_notdogs': pct_correct_notdogs,
        'pct_correct_breed': pct_correct_breed,
        'pct_match': pct_match
    }
    return results_stats_dic
