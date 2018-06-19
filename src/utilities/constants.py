# -*- coding: utf-8 -*-
# Basic Directory
from utilities.config_utils import create_base_dir

KG_EMBEDDINGS_PIPELINE_DIR = create_base_dir()

# Related to corpus Walking RDF and OWL
WROC = 'walking_rdf_and_owl_corpus'
WROC_URL = 'http://aber-owl.net/aber-owl/bio2vec/bio-knowledge-graph.n3'

# Related to CSQA filtered Wikidata
CSQA_WIKIDATA = 'csqa_wiki_data'

# Configuration related
CLASS_NAME = 'class_name'
## Reader
READER = 'reader'
WROC_READER = 'WROCReader'
CSQA_WIKIDATA_READER = 'CSQAWikiDataReader'
## KG embedding model
KG_EMBEDDING_MODEL = 'kg_embedding_model'
TRANS_E = 'TransE'
TRANS_H = 'TransH'
# Evaluator
EVALUATOR = 'evaluator'
MEAN_RANK_EVALUATOR = 'MeanRankEvaluator'
# Output paths
ENTITY_TO_EMBEDDINGS = 'entity_to_embeddings'
EVAL_RESULTS ='eval_results'

## Metrics
MEAN_RANK = 'mean_rank'
# ML params
BATCH_SIZE = 'batch_size'
VOCAB_SIZE = 'vocab_size'
EMBEDDING_DIM = 'embedding_dim'
MARGIN_LOSS = 'margin_loss'
NUM_ENTITIES = 'num_entities'
NUM_RELATIONS = 'num_relations'
NUM_EPOCHS = 'num_epochs'
LEARNING_RATE = 'learning_rate'

