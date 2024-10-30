def adjust_results4_isadog(results_dictionary, dog_file):
    """
    Bu işlev, her bir görüntü etiketi ve sınıflandırıcı etiketi için 
    'köpek' olup olmadığını belirlemek amacıyla sonuçları günceller.

    Parametreler:
      results_dictionary - Anahtarları görüntü dosya adları olan ve değerleri listelerden oluşan bir sözlük.
                           Her listede şunlar bulunur:
                           - resim etiketi (string)
                           - sınıflandırıcı etiketi (string)
                           - etiketlerin eşleşme durumu (1: Aynı, 0: Farklı)
                           Bu işlev, her listeye iki bilgi daha ekleyecektir:
                           - resim etiketinin köpek olup olmadığı (1: Evet, 0: Hayır)
                           - sınıflandırıcı etiketinin köpek olup olmadığı (1: Evet, 0: Hayır)
      dog_file - Köpek isimlerini içeren dosyanın yolu. Her satırda küçük harflerle bir köpek adı bulunur.
      
    Dönen Değerler:
      Yok - Bu işlev, doğrudan results_dictionary üzerinde değişiklik yapar.
    """
    # Dosyadaki köpek isimlerini küme olarak oku
    with open(dog_file, 'r') as file:
        dog_names_set = {line.strip().lower() for line in file}
    
    # Her anahtar için köpek olup olmadığını kontrol et ve sonuç listesine ekle
    for image_name, attributes in results_dictionary.items():
        pet_is_dog = 1 if attributes[0] in dog_names_set else 0
        classifier_is_dog = 1 if attributes[1] in dog_names_set else 0

        # Her görüntü için köpek olup olmama durumlarını sonuç listesine ekle
        attributes += [pet_is_dog, classifier_is_dog]
