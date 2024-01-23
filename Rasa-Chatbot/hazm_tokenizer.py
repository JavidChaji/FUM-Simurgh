from typing import Dict, Text, Any, List


from hazm import WordTokenizer
from rasa.engine.graph import GraphComponent, ExecutionContext
from rasa.engine.recipes.default_recipe import DefaultV1Recipe
from rasa.engine.storage.resource import Resource
from rasa.engine.storage.storage import ModelStorage
from rasa.shared.nlu.training_data.message import Message
from rasa.shared.nlu.training_data.training_data import TrainingData
from rasa.nlu.tokenizers.tokenizer import Tokenizer, Token

@DefaultV1Recipe.register(
    component_types=[DefaultV1Recipe.ComponentType.MESSAGE_TOKENIZER],
    is_trainable=True
)
class HazmTokenizer(Tokenizer):

    def tokenize(self, message: Message, attribute: Text) -> List[Token]:
        """Tokenizes the text of the provided attribute of the incoming message."""
        # Create a Hazm WordTokenizer instance
        tokenizer = WordTokenizer()

        # Tokenize the text using Hazm
        tokens = tokenizer.tokenize(text)

        return tokens

    def process(self, messages: List[Message]) -> List[Message]:
        """Tokenize the incoming messages."""
        for message in messages:
            for attribute in MESSAGE_ATTRIBUTES:
                if isinstance(message.get(attribute), str):
                    if attribute in [
                        INTENT,
                        ACTION_NAME,
                        RESPONSE_IDENTIFIER_DELIMITER,
                    ]:
                        tokens = self._split_name(message, attribute)
                    else:
                        tokens = self.tokenize(message, attribute)

                    message.set(TOKENS_NAMES[attribute], tokens)
        return messages
        
    def train(self, training_data: TrainingData) -> Resource:
        """Copies the dictionary to the model storage."""
        self.persist()
        return self._resource