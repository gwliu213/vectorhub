from datetime import date
from ....import_utils import *
from ....models_dict import *
if is_all_dependency_installed(MODEL_REQUIREMENTS['encoders-audio-tfhub-trill']):
    import tensorflow as tf
    import tensorflow_hub as hub
    import traceback
from ....base import catch_vector_errors
from ....doc_utils import ModelDefinition
from ..base import BaseAudio2Vec

TrillDistilledModelDefinition = ModelDefinition(markdown_filepath="encoders/audio/tfhub/trill_distilled")
__doc__ = TrillDistilledModelDefinition.create_docs()

class TrillDistilled2Vec(BaseAudio2Vec):
    definition = TrillDistilledModelDefinition
    def __init__(self, model_url: str = 'https://tfhub.dev/google/nonsemantic-speech-benchmark/trill-distilled/3', layer: str = 'embedding'):
        self.model_url = model_url
        self.layer = layer
        self.model = hub.load(self.model_url)
        self.model_name = model_url.replace(
            'https://tfhub.dev/google/', '').replace('/', '_')
        self.vector_length = 2048

    @catch_vector_errors
    def encode(self, audio, vector_operation='mean'):
        return self._vector_operation(self.model(samples=audio, sample_rate=16000)[self.layer], vector_operation)
