import argparse

from google.cloud import language
import six


def sentiment_text(text):
    """Detects sentiment in the text."""
    language_client = language.Client()

    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')

    # Instantiates a plain text document.
    document = language_client.document_from_text(text)

    # Detects sentiment in the document. You can also analyze HTML with:
    #   document.doc_type == language.Document.HTML
    sentiment = document.analyze_sentiment().sentiment

    print('Score: {}'.format(sentiment.score))
    print('Magnitude: {}'.format(sentiment.magnitude))


x = input('輸入中文：')
sentiment_text(x)
