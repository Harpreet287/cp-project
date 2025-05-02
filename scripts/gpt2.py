from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch
import math

model_name = 'gpt2'
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)
model.eval()

def calculate_perplexity(sentence):
    inputs = tokenizer(sentence, return_tensors='pt')
    with torch.no_grad():
        outputs = model(**inputs, labels=inputs["input_ids"])
        loss = outputs.loss
    return math.exp(loss.item())


sentence = "Our plan is therefore to 1) rephrase the execution trace as a polynomial, 2) extend it to a large domain, and 3) transform that, using the polynomial constraints, into yet another polynomial that is guaranteed to be of low degree if and only if the execution trace is valid."
print("Perplexity:", calculate_perplexity(sentence))