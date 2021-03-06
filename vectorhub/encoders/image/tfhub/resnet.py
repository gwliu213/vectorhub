from ..base import BaseImage2Vec
from ....base import catch_vector_errors
from ....doc_utils import ModelDefinition
from ....import_utils import *
from ....models_dict import MODEL_REQUIREMENTS
from datetime import date
if is_all_dependency_installed(MODEL_REQUIREMENTS['encoders-image-tfhub-resnet']):
    import tensorflow as tf
    import tensorflow_hub as hub

ResNetModelDefinition = ModelDefinition(markdown_filepath='encoders/image/tfhub/resnet')

__doc__ = ResNetModelDefinition.create_docs()

class ResnetV12Vec(BaseImage2Vec):
    definition = ResNetModelDefinition
    def __init__(self, model_url: str = 'https://tfhub.dev/google/imagenet/resnet_v1_50/feature_vector/4'):
        list_of_urls = [
            # 50 layers
            'https://tfhub.dev/google/imagenet/resnet_v1_50/feature_vector/4',

            # 101 layers
            'https://tfhub.dev/google/imagenet/resnet_v1_101/feature_vector/4',

            # 152 layers
            'https://tfhub.dev/google/imagenet/resnet_v1_152/feature_vector/4',
        ]
        self.validate_model_url(model_url, list_of_urls)
        self.init(model_url)
        self.vector_length = 2048

    def init(self, model_url: str):
        self.model_url = model_url
        self.model_name = self.model_url.replace(
            'https://tfhub.dev/google/', '').replace('/', '_')
        self.model = hub.load(self.model_url)

    @catch_vector_errors
    def encode(self, image):
        return self.model([image]).numpy().tolist()[0]

    @catch_vector_errors
    def bulk_encode(self, images, threads=10, chunks=10):
        return [i for c in self.chunk(images, chunks) for i in self.model(c).numpy().tolist()]
