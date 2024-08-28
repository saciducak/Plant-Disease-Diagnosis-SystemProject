Yapay zeka destekli bitki hastalık tespit sisteminde, derin öğrenme modelleri kullanarak bitki hastalıklarının tespiti ve analizi yapılmıştır. Derin öğrenme modelinin mAP, recall ve f1Score değerleri detaylı analiz edilmiştir. YOLO v8 ve v9 modellerinin sonuç metrikleri ve model ağ yapısı kapsamlı olarak karşılaştırılmıştır.   

In the plant disease detection system supported by artificial intelligence, detection and analysis of plant diseases were performed using deep learning models. The mAP, recall and f1Score values of the deep learning model have been analyzed in detail. The resulting metrics and model network structure of the YOLO v8 and v9 models have been extensively compared.

**PROJE ŞEMASI / PROJECT SCHEME **

![image](https://github.com/user-attachments/assets/6d1cb125-50c0-4783-8205-4abdc7ec04e9)

**DATA LABELİNG**

![image](https://github.com/user-attachments/assets/5b148536-c29c-43e7-8edd-c49028d2d0db)

**DATA AUGMENTATİON**

![image](https://github.com/user-attachments/assets/30bd4a79-2f5c-48ec-abb6-e44c83158671)

**ÖRNEK HASTALIKLI DOMATESLER / SAMPLE DISEASED TOMATOES**

<img width="468" alt="Ekran Resmi 2024-08-28 15 18 43" src="https://github.com/user-attachments/assets/6a14282a-5db5-4ed8-8b1a-c28e1a08eacd">

**ÖRNEK MODEL TESPİT GÖRSELLERİ / SAMPLE MODEL DETECTION VISUALS**

![image](https://github.com/user-attachments/assets/314bc059-8c61-4ae2-bd6f-bcdfba91a9b7)
![image](https://github.com/user-attachments/assets/e073a644-bae8-4968-a5a0-aaf83987ee2c)

**ÖZET**
Proje sürecinde, görüntü verilerinin ön işlenmesi, etiketlenmesi, sınıflandırılması, takip ve analizi gibi adımlar detaylı bir şekilde ele alınmıştır. Öncelikle, literatürdeki mevcut çalışmalar incelenmiş ve güncel YOLO (You Only Look Once) modellerinin sonuçları analiz edilmiştir. YOLOv8 ve YOLOv9 modellerinin performansları karşılaştırılmış, çeşitli metrik değerlerine bakılarak modelin sonuçları yorumlanmıştır. Yolo ağı modellerinin versiyon farklılıklarına göre hiperparametre değişimleri, epoch değerleri ve ağırlık dosyalarının etkileri de araştırılmıştır. YOLOv9 modelinin, YOLOv8'e kıyasla daha büyük model boyutu, veri artırma (augmentation) tekniklerinin daha etkin kullanımı ve yeni aktivasyon fonksiyonlarının (SiLU, Swish vb.) kullanımı gibi yenilikler sayesinde daha yüksek doğruluk ve performans sunduğu gözlemlenmiştir. YOLOv9'un 0.91 gibi yüksek bir mAP (Mean Average Precision) değeri, modelin genel performansının oldukça yüksek olduğunu ve veri setindeki nesne türünü yüksek doğrulukla tespit ettiğini göstermektedir. Recall değeri 0.72 olan modelin, bazı nesneleri gözden kaçırabileceği, ancak 0.96'lık precision değeri ile yanlış alarm verme olasılığının oldukça düşük olduğu görülmüştür. 
Proje daha sonra Yolov8 ile metrik karşılaştırılmasına sokulmuş ve çizelgeler üzerinden analiz edilip sonuçları yorumlanmıştır. 7 çeşit hastalıklı domates görüntüsü modele öğretilerek tespit edilmeye çalışılmış ve model eğitilerek geliştirilmiştir.

**SUMMARY**
During the project process, steps such as pre-processing, labelling, classification, follow-up and analysis of image data are discussed in detail. First, the existing studies in the literature were examined and the results of the current YOLO (You Only Look Once) models were analyzed. The performance of the YOLOV8 and YOLOv9 models was compared and the results of the model were interpreted by looking at various metric values. According to the version differences of yolo network models, hyperparameter changes, epoch values and effects of weight files were also investigated. The YOLOv9 model has a larger model size compared to YOLOv8, more efficient use of data enhancement (augmentation) techniques and new activation functions (SiLU, Swish etc.) thanks to innovations such as use, it has been observed to offer higher accuracy and performance.
YOLOV9's high value of mAP (Mean Average Precision), such as 0.91, shows that the overall performance of the model is quite high, and it detects the object type in the dataset with high accuracy. The model with a Recall value of 0.72 was found to be able to overlook some objects, but was unlikely to sound a false alarm with a precision value of 0.96. 
The project was then introduced to metric comparison with Yolov8 and analyzed through charts and interpreted results.The image of 7 kinds of diseased tomatoes was tried to be detected by teaching the model and the model was developed by training.
