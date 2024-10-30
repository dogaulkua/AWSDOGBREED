# Gerekli kütüphaneleri ekliyoruz
from time import time, sleep

# Fonksiyonlar ve program kontrollerini içeren dosyalardan işlevleri çağırıyoruz
from print_functions_for_lab_checks import *
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results

# Ana program işlevi
def main():
    # TODO 0: Program süresini ölçmek için başlangıç zamanını alıyoruz
    baslangic_zamani = time()
    
    # TODO 1: Komut satırından gelen 3 girdiyi alarak in_arg değişkenine atıyoruz
    girdi_degerleri = get_input_args()

    # Komut satırı argümanlarını doğrulamak için kontrol işlevini çalıştırıyoruz  
    check_command_line_arguments(girdi_degerleri)

    
    # TODO 2: get_pet_labels işlevi ile, dosya dizininden hayvan etiketlerini çekiyoruz.
    # Sonuçları sözlük formatında alıp results olarak saklıyoruz.
    etiket_sonuc = get_pet_labels(girdi_degerleri.dir)

    # Etiketlerin doğru oluşup oluşmadığını kontrol ediyoruz  
    check_creating_pet_image_labels(etiket_sonuc)


    # TODO 3: Sınıflandırma işlevini çağırıyoruz. Bu, dosyaları inceleyip
    # belirli bir sınıflandırma modeliyle eşleşmelerini kontrol eder.
    classify_images(girdi_degerleri.dir, etiket_sonuc, girdi_degerleri.arch)

    # Sınıflandırılmış sonuçların doğruluğunu inceliyoruz    
    check_classifying_images(etiket_sonuc)    

    
    # TODO 4: Sonuçları köpek ya da köpek dışı olarak sınıflandırmak için ayar işlevini çağırıyoruz.
    adjust_results4_isadog(etiket_sonuc, girdi_degerleri.dogfile)

    # Köpek sınıflandırmasını kontrol ediyoruz
    check_classifying_labels_as_dogs(etiket_sonuc)


    # TODO 5: İstatistik hesaplama işlevini çağırarak sonuçların istatistiklerini 
    # sonuç istatistikleri sözlüğüne kaydediyoruz.
    istatistik_sonuc = calculates_results_stats(etiket_sonuc)

    # Hesaplanan istatistiklerin doğruluğunu gözden geçiriyoruz
    check_calculating_results(etiket_sonuc, istatistik_sonuc)


    # TODO 6: Sonuçları kullanıcıya özetlemek için ekrana yazdırıyoruz
    print_results(etiket_sonuc, istatistik_sonuc, girdi_degerleri.arch, True, True)
    
    # TODO 0: Programın toplam çalışma süresini hesaplayıp kullanıcıya bildiriyoruz
    bitis_zamani = time()
    
    # Toplam süreyi hh:mm:ss formatında ekrana yazdırıyoruz
    gecen_zaman = bitis_zamani - baslangic_zamani
    print("\n** Toplam Çalışma Süresi:",
          str(int((gecen_zaman/3600)))+":"+str(int((gecen_zaman%3600)/60))+":"
          +str(int((gecen_zaman%3600)%60)) )
    

# Ana programı başlatma çağrısı
if __name__ == "__main__":
    main()
