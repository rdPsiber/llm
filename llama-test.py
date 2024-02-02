import os
import logging
import sys

logging.basicConfig(stream=sys.stdout, level = logging.DEBUG)
0;276;0clogging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))


os.environ["OPENAI_API_KEY"] = "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"

from llama_index import VectorStoreIndex, SimpleDirectoryReader

from llama_index.node_parser import SentenceSplitter

documents = SimpleDirectoryReader("./data/").load_data()

#print(documents)
index = VectorStoreIndex.from_documents(documents)


query_engine = index.as_query_engine()
query_engine.query("What is the status of my porfolio")

index.storage_context.persist()





