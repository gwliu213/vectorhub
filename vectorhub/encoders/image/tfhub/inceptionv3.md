---
model_id: "image/inception-v3"
model_name: "Inception" 
vector_length: "2048 (default)"
repo: 'https://tfhub.dev/google/imagenet/inception_v1/feature_vector/4'
installation: "pip install vectorhub[encoders-image-tfhub]"
release_date: "2015-12-11"
---

## Description

We propose a deep convolutional neural network architecture codenamed "Inception", which was responsible for setting the new state of the art for classification and detection in the ImageNet Large-Scale Visual Recognition Challenge 2014 (ILSVRC 2014). The main hallmark of this architecture is the improved utilization of the computing resources inside the network. This was achieved by a carefully crafted design that allows for increasing the depth and width of the network while keeping the computational budget constant. To optimize quality, the architectural decisions were based on the Hebbian principle and the intuition of multi-scale processing. One particular incarnation used in our submission for ILSVRC 2014 is called GoogLeNet, a 22 layers deep network, the quality of which is assessed in the context of classification and detection.

## Example

```python
#pip install vectorhub[encoders-image-tfhub]
from vectorhub.encoders.image.tfhub import InceptionV32Vec
model = InceptionV32Vec()
sample = model.read('https://getvectorai.com/assets/hub-logo-with-text.png')
model.encode(sample)
```
