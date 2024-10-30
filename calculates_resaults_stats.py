def calculate_statistics(results_dict):
    """
    Computes various statistics based on classification results and stores
    these statistics in a dictionary.
    
    Parameters:
      results_dict - Dictionary with image filename as key and a list as value.
                     The list contains:
                       0: pet image label (string)
                       1: classifier label (string)
                       2: label match (1: Match, 0: No Match)
                       3: whether the pet image label is a dog (1: Dog, 0: Not a Dog)
                       4: whether the classifier label is a dog (1: Dog, 0: Not a Dog)
                       
    Returns:
      stats_dict - Dictionary containing calculated statistics as key-value pairs.
    """
    # Initialize counters for statistics
    total_images = len(results_dict)
    correct_dog_matches = 0
    total_dog_images = 0
    correct_non_dog_matches = 0
    total_non_dog_images = 0
    correct_breed_matches = 0
    total_label_matches = 0

    # Calculate statistics
    for record in results_dict.values():
        is_dog_image = record[3]
        is_dog_classifier = record[4]
        is_label_match = record[2]
        
        # Dog image statistics
        if is_dog_image == 1:
            total_dog_images += 1
            if is_dog_classifier == 1:
                correct_dog_matches += 1
            if is_label_match == 1:
                correct_breed_matches += 1
        else:
            total_non_dog_images += 1
            if is_dog_classifier == 0:
                correct_non_dog_matches += 1
        
        # Overall label match statistics
        if is_label_match == 1:
            total_label_matches += 1

    # Calculate percentages
    dog_accuracy = (correct_dog_matches / total_dog_images * 100) if total_dog_images else 0
    breed_accuracy = (correct_breed_matches / total_dog_images * 100) if total_dog_images else 0
    non_dog_accuracy = (correct_non_dog_matches / total_non_dog_images * 100) if total_non_dog_images else 0
    label_match_rate = (total_label_matches / total_images * 100) if total_images else 0

    # Store results in a dictionary
    stats_dict = {
        'total_images': total_images,
        'total_dog_images': total_dog_images,
        'total_non_dog_images': total_non_dog_images,
        'correct_dog_matches': correct_dog_matches,
        'correct_non_dog_matches': correct_non_dog_matches,
        'correct_breed_matches': correct_breed_matches,
        'dog_accuracy': dog_accuracy,
        'breed_accuracy': breed_accuracy,
        'non_dog_accuracy': non_dog_accuracy,
        'label_match_rate': label_match_rate
    }

    return stats_dict
