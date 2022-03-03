from .utils import *
from rest_framework import serializers
from .models import Quote
import requests
import json



class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = '__all__'

    def get(self, validated_data):
        response_API = requests.get('https://api.kanye.rest').text
        quote = response_API[10:-2]
        quote = Quote.objects.create(
            quote=quote,
            character=calculate_characters(quote),
            consonant=calculate_consonants(quote),
            vowel=calculate_vowels(quote),
            average_lens=average_length(quote),
            longest_word=longest_word(quote),
            repeated_char=repeated_characters(quote)
            )

        return quote