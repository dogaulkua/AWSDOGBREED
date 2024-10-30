def adjust_results4_isadog(results_dict, dog_names_file):
    """
    Updates the results dictionary to indicate whether each image label and classifier label is a dog.

    Parameters:
      results_dict - Dictionary with image filenames as keys and lists as values.
                     Each list contains:
                     - image label (string)
                     - classifier label (string)
                     - label match status (1: Match, 0: No Match)
                     This function will add two more items to each list:
                     - whether the image label is a dog (1: Yes, 0: No)
                     - whether the classifier label is a dog (1: Yes, 0: No)
      dog_names_file - Path to the file containing dog names. Each line in the file contains a dog name in lowercase.
      
    Returns:
      None - This function modifies the results_dict in place.
    """
    # Read dog names from the file into a set
    with open(dog_names_file, 'r') as file:
        dog_names = {line.strip().lower() for line in file}
    
    # Update results dictionary to indicate if labels are dogs
    for filename, attributes in results_dict.items():
        image_label_is_dog = 1 if attributes[0] in dog_names else 0
        classifier_label_is_dog = 1 if attributes[1] in dog_names else 0

        # Append the dog status to the attributes list
        attributes.extend([image_label_is_dog, classifier_label_is_dog])
