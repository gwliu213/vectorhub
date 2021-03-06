---
model_id: "image/mobilenet-v2"
model_name: "MobileNet" 
vector_length: "1792 (default)"
paper: "https://arxiv.org/abs/1704.04861"
repo: "https://tfhub.dev/google/imagenet/mobilenet_v1_100_224/feature_vector/4"
installation: pip install vectorhub[encoders-image-tfhub]
release_date: "2018-01-13"
---

## Description

We present a class of efficient models called MobileNets for mobile and embedded vision applications. MobileNets are based on a streamlined architecture that uses depth-wise separable convolutions to build light weight deep neural networks. We introduce two simple global hyper-parameters that efficiently trade off between latency and accuracy. These hyper-parameters allow the model builder to choose the right sized model for their application based on the constraints of the problem. We present extensive experiments on resource and accuracy tradeoffs and show strong performance compared to other popular models on ImageNet classification. We then demonstrate the effectiveness of MobileNets across a wide range of applications and use cases including object detection, finegrain classification, face attributes and large scale geo-localization.

## Example

```python
#pip install vectorhub[encoders-image-tfhub]
from vectorhub.encoders.image.tfhub import MobileNetV22Vec
model = MobileNetV22Vec()
sample = model.read('https://getvectorai.com/assets/hub-logo-with-text.png')
model.encode(sample)
```