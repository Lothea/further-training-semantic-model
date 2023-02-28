# Different ways of further training a pre-trained SentenceTranformer model

## Augmented SBERT
Train an SBERT model by first fine-tuning a BERT model on some question pairs and using the tuned BERT model to then train the SBERT model
[Link](https://www.sbert.net/examples/training/data_augmentation/README.html)


[How to Transfer Domain Knowledge](https://www.youtube.com/watch?v=dhw2-oBbm78)

[DATASET to fine-tune SBERT](https://www.youtube.com/watch?v=Lt62xJAW8nQ)


## Semantic textual similarity
Continue training on STS (semantic textual similarity) data for a pre-trained SentenceTranformer model.
[Example](https://github.com/UKPLab/sentence-transformers/blob/master/examples/training/sts/training_stsbenchmark_continue_training.py)
Example fine-tunes a model using a STS benchmark dataset

## Domain adaptation
Adapt text embedding models (SBERT) to our specific text domain without needing labeled training data. 
[Link](https://www.sbert.net/examples/domain_adaptation/README.html) 


# Adding training to a pre-trained model using augmented SBERT

I created an extended model of 'all-MiniLM-L6-v2' using (augmented SBERT)[https://sbert.net/examples/training/data_augmentation/README.html] using two data sets. Elmore vs CybleAware (annotated), Elmore vs digital_fortress (unannotated & split into 3 files, dev, test, train).

1. run the program 
py train_sts_qqp_crossdomain.py

2. The resulting model will output in output/bi-encoder/modelname. Move the model folder into api and rename to 'model'. 

3. Run the api
```
cd api
py app.py
```

4. Run the front-end
```cd front-end
npm run serve
```

5. Open localhost 8080

6. Fill in the two input fields with questions from the Elmore vs CybeAware found in questions.txt and press submit

## Findings
The domain-trained model showed no improvement or change in output. When comparing the questions from Elmore with CybeAware. 
