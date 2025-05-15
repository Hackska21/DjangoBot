from openai import OpenAI

from django.conf import settings


class OpenApiClient:
    client = OpenAI(
        api_key=settings.OPEN_API_KEY
    )

    def fetch_messages(self, messages, model="gpt-3.5-turbo", temperature=0):
        response = self.client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
        )
        return response.choices[0].message.content
