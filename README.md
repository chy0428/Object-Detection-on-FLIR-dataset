# Object-Detection-on-FLIR-dataset


### FLIR_to_YOLO_format.py

> FLIR data format to YOLO format

FLIR dataset (열화상 이미지)에 대한 정보가 thermal_annotation.json에 주석으로 나와있다.

이를 YOLO 모델을 이용하여 학습하기 위해 YOLO data format으로 적절하게 재구성 하여야 한다.

해당 코드를 이용하여 YOLO format으로 변환하면 다음과 같은 레이블들이 형성된다.

```
2 0.418750 0.490234 0.206250 0.238281
2 0.701562 0.452148 0.137500 0.150391
2 0.162500 0.457031 0.075000 0.054688
2 0.223438 0.460938 0.043750 0.066406
```
