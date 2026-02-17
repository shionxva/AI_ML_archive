# -*- coding: utf-8 -*-
"""
TrainingSample.ipynb
"""

import torch
from torch.optim import AdamW
from transformers import AutoTokenizer, AutoModelForSequenceClassification

#simple training on 2 sentences example
checkpoint = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForSequenceClassification.from_pretrained(checkpoint)
sequences = [
    "I've been waiting for a HuggingFace course my whole life.",
    "This course is amazing!",
]
batch = tokenizer(sequences, padding=True, truncation=True, return_tensors="pt")


batch["labels"] = torch.tensor([1, 1])

optimizer = AdamW(model.parameters())
loss = model(**batch).loss #foward pass , compute cross entropy loss
loss.backward() #back propagation
optimizer.step() #update weight