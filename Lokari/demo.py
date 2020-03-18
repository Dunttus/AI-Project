from Lokari.nlp import load_tokenizer
import pandas as pd

def run(model):
    DEMO_FILE = '../datasets/loglevels/demologs.json'

    # Read the demo data
    data = pd.read_json(DEMO_FILE, lines=True)
    messages = data.MESSAGE
    #
    tokenizer = load_tokenizer()
    tokenized_msgs = tokenizer.texts_to_matrix(messages, mode='tfidf')

    pred = model.predict(tokenized_msgs)
    print(pred)

    return