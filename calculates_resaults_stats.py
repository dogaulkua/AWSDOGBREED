```python
def calculate_statistics(results_dict):
    """
    Sınıflandırma sonuçlarına dayalı olarak çeşitli istatistikler hesaplar ve
    bu istatistikleri bir sözlük içinde toplar.
    
    Parametreler:
      results_dict - Görüntü dosyası adını anahtar olarak, şu bilgileri içeren bir listeyi değer olarak saklayan sözlük:
                       0: görüntü etiketi (string)
                       1: sınıflandırıcı etiketi (string)
                       2: etiket uyumu (1: Uyumlu, 0: Uyumsuz)
                       3: görüntü etiketinin köpek olup olmadığı (1: Köpek, 0: Değil)
                       4: sınıflandırıcının köpek olarak tanımlayıp tanımlamadığı (1: Köpek, 0: Değil)
                       
    Dönüş:
      stats_dict - Hesaplanan istatistikleri içeren ve her bir istatistik için anahtar-değer çifti içeren sözlük.
    """
    # İstatistik sayacı değişkenlerini tanımlama
    total_images = len(results_dict)
    matching_dog_count = 0
    total_dog_images = 0
    correct_non_dog_count = 0
    non_dog_images = 0
    correct_breed_count = 0
    label_match_count = 0

    # İstatistikleri toplama
    for record in results_dict.values():
        image_is_dog = record[3]
        classifier_says_dog = record[4]
        is_label_match = record[2]
        
        # Köpek görüntüleri ve doğrulama
        if image_is_dog == 1:
            total_dog_images += 1
            if classifier_says_dog == 1:
                matching_dog_count += 1
            if is_label_match == 1:
                correct_breed_count += 1
        else:
            non_dog_images += 1
            if classifier_says_dog == 0:
                correct_non_dog_count += 1
        
        # Genel etiket uyumu
        if is_label_match == 1:
            label_match_count += 1

    # Yüzde hesaplamaları
    dog_accuracy = (matching_dog_count / total_dog_images * 100) if total_dog_images else 0
    breed_accuracy = (correct_breed_count / total_dog_images * 100) if total_dog_images else 0
    non_dog_accuracy = (correct_non_dog_count / non_dog_images * 100) if non_dog_images else 0
    label_match_rate = (label_match_count / total_images * 100) if total_images else 0

    # Sonuçları sözlükte saklama
    stats_dict = {
        'total_images': total_images,
        'dog_images': total_dog_images,
        'non_dog_images': non_dog_images,
        'dog_match_count': matching_dog_count,
        'non_dog_correct_count': correct_non_dog_count,
        'breed_match_count': correct_breed_count,
        'dog_accuracy': dog_accuracy,
        'breed_accuracy': breed_accuracy,
        'non_dog_accuracy': non_dog_accuracy,
        'label_match_rate': label_match_rate
    }

    return stats_dict
