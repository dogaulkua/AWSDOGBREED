from os import listdir

def get_pet_labels(image_dir):
    """
    Generates a dictionary of pet labels based on the filenames of the image files.
    These labels are used to verify the accuracy of the classifier function's output,
    as the filenames contain the true identity of the pet in the image.
    
    Parameters:
     image_dir - The full path to the folder of images to be classified (string)
    
    Returns:
      results_dict - Dictionary with image filename as key and a list as value.
                     The list contains the following item:
                     index 0 = pet image label (string)
    """
    results_dict = {}
    filenames = listdir(image_dir)
    
    for filename in filenames:
        if filename.startswith('.'):
            continue
        
        # Extract pet label from filename
        pet_label = " ".join([word for word in filename.lower().split('_') if word.isalpha()]).strip()
        
        # Add to results dictionary
        results_dict[filename] = [pet_label]
    
    return results_dict
