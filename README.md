# Computational Psycholinguistics

## Original Paper
[Using Large Language Models to Simulate Multiple Humans and Replicate Human Subject Studies](https://arxiv.org/abs/2208.10264)
## Datasets

- [LogicBench](https://huggingface.co/datasets/cogint/LogicBench-v1.0https://huggingface.co/datasets/cogint/LogicBench-v1.0)
- [LogicQA](https://github.com/csitfun/LogiQA2.0/tree/main/logiqa)
- [LogicQA2](https://github.com/csitfun/LogiQA2.0/tree/main/logiqa2nli)

## TODO

- [ ] 20 examples from each dataset and 7 datasets, 4 models (ChatGpt-4o, o4 mini, Mistral, Claude 3.7)
- [ ] Automated evaluation of sentence complexity and finding is there any corelation between sentence complexity and llm response(glue or rouge score).
- [ ] Evaluating LLM responses on 4 criteria: answer correctness, explain correctness, explain completeness, explain redudandancy.

## Things to take care of

- Same prompt to all the models.
- Don't reveal the answer before hand to the model.

## Task Division

- Harpreet: LogicBench(2), LogicQA, LogicQA2
- Prkhar Jain: Original paper datasets(4).
