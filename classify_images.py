from classifier import classifier

def classify_images(image_dir, results_dict, model_name):
    """
    Generates classifier labels using the classifier function, compares these labels with pet labels,
    and updates the results dictionary with the classifier label and the comparison result.
    
    Parameters:
      image_dir - The full path to the folder of images to be classified (string)
      results_dict - Dictionary with image filename as key and a list as value. The list contains:
                     index 0 = pet image label (string)
                     index 1 = classifier label (string) [added by this function]
                     index 2 = 1/0 (int) where 1 = match between pet image and classifier labels, 0 = no match [added by this function]
      model_name - The CNN model architecture to be used by the classifier function (string), must be one of: resnet, alexnet, vgg
     
    Returns:
      None - results_dict is a mutable data type, so no return is needed.
    """
    for image_filename in results_dict:
        image_path = f"{image_dir}/{image_filename}"
        classifier_output = classifier(image_path, model_name)
        classifier_label = classifier_output.lower().strip()
        pet_label = results_dict[image_filename][0]
        is_match = int(pet_label in classifier_label)
        results_dict[image_filename].extend([classifier_label, is_match])
