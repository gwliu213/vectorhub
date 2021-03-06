from datetime import date
from ....import_utils import *
from ....models_dict import MODEL_REQUIREMENTS
if is_all_dependency_installed(MODEL_REQUIREMENTS['encoders-audio-tfhub-yamnet']):
    import tensorflow as tf
    import tensorflow_hub as hub

from ..base import BaseAudio2Vec
from ....base import catch_vector_errors
from ....doc_utils import ModelDefinition

YamnetModelDefinition = ModelDefinition(markdown_filepath='encoders/audio/tfhub/yamnet')
__doc__ = YamnetModelDefinition.create_docs()

class Yamnet2Vec(BaseAudio2Vec):
    definition = YamnetModelDefinition
    def __init__(self, model_url: str = 'https://tfhub.dev/google/yamnet/1'):
        self.model_url = model_url
        self.model = hub.load(self.model_url)
        self.model_name = self.model_url.replace(
            'https://tfhub.dev/google/', '').replace('/', '_')
        self.vector_length = 1024

    @catch_vector_errors
    def encode(self, audio, vector_operation='mean', layer='embeddings'):
        outputs = self.model(audio)
        if layer == 'scores':
            return self._vector_operation(outputs[0], vector_operation)
        elif layer == 'log_mel_spectrogram':
            return self._vector_operation(outputs[2], vector_operation)
        else:
            return self._vector_operation(outputs[1], vector_operation)