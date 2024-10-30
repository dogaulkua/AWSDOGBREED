from time import time, sleep
from print_functions_for_lab_checks import *
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results

def main():
    # Measure the start time of the program
    start_time = time()
    
    # Retrieve command line arguments
    input_args = get_input_args()

    # Check the validity of command line arguments
    check_command_line_arguments(input_args)

    # Retrieve pet labels from the directory
    results = get_pet_labels(input_args.dir)

    # Check the correctness of pet labels
    check_creating_pet_image_labels(results)

    # Classify images using the specified model
    classify_images(input_args.dir, results, input_args.arch)

    # Check the correctness of classified images
    check_classifying_images(results)    

    # Adjust results to determine if the labels are dogs or not
    adjust_results4_isadog(results, input_args.dogfile)

    # Check the correctness of dog classification
    check_classifying_labels_as_dogs(results)

    # Calculate statistics of the results
    results_stats = calculates_results_stats(results)

    # Check the correctness of calculated statistics
    check_calculating_results(results, results_stats)

    # Print the results summary
    print_results(results, results_stats, input_args.arch, True, True)
    
    # Measure the end time of the program
    end_time = time()
    
    # Calculate and print the total elapsed time
    total_time = end_time - start_time
    print("\n** Total Elapsed Runtime:",
          str(int((total_time/3600)))+":"+str(int((total_time%3600)/60))+":"
          +str(int((total_time%3600)%60)) )

if __name__ == "__main__":
    main()
