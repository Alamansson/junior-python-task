from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import QuoteSerializer
from .utils import *
from .models import Quote
import requests


class QuoteViewSet(viewsets.ModelViewSet):
    serializer_class = QuoteSerializer

    def list(self, request, *args, **kwargs):
        queryset = list(Quote.objects.filter().values('quote'))
        quotes = [i['quote'] for i in queryset]
        response, quotes1 = [], []
        for i in range(10):
            response_api = requests.get('https://api.kanye.rest').text[10:-2]
            if response_api in quotes:
                result = list(Quote.objects.filter(quote=response_api))
                response.extend(result)
                print("RESULT: ", result)

            else:
                print(response_api)
                quote = Quote.objects.create(
                    quote=response_api,
                    character=calculate_characters(response_api),
                    consonant=calculate_consonants(response_api),
                    vowel=calculate_vowels(response_api),
                    average_lens=average_length(response_api),
                    longest_word=longest_word(response_api),
                    repeated_char=repeated_characters(response_api)
                )

        last_ten = Quote.objects.filter().order_by('-id')[:(10 - len(response))][::-1] + response

        serializer = QuoteSerializer(last_ten, many=True)

        return Response(serializer.data, 200)

