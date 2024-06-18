# Model organization

We filtered the available model resources mentioned in A Survey on Effective Invocation Methods of Massive LLM Services[[link]]() and quoted the corresponding statistics. In addition, it will also care about the accuracy of different models on different data sets, response speed and other multiple parameters, present guidelines for service providers and users, create a good business environment for Lmaas, and update at any time.

## Update log

- Price change! January 24, 2023: Revised official prices for models like M2M100 1.2B
- January 24, 2023 list creation



<p align="center">
    <a href = "https://arxiv.org/pdf/2402.03408.pdf">Arxiv</a> | <a href = "./Paperlist.md">PaperList</a> | <a href = "./README.md">Readme</a>   | <a href = "./Resource.md">Resource</a>
</p>


***


## Model List

| LLM ID | Model Name           | Creator   | Pricing rules | Unit Charge(1M tokens) | Pricing Source                                               | Size | Max Tokens | API Documentation                                            | Tokenizer                                                    | Update     |
| ------ | -------------------- | --------- | ------------- | ---------------------- | ------------------------------------------------------------ | ---- | ---------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ---------- |
| 1      | gpt-4-1106-preview   | OpenAI    | tokens        | I: $10.0 O:$30.0       | [price](https://openai.com/pricing)                          |      | 4096       | [Docu](https://platform.openai.com/docs/api-reference/making-requests) | [Tokenizer](https://github.com/openai/tiktoken)              | 2024.01.24 |
| 2      | gpt-4-0613           | OpenAI    | tokens        | I: $30.0 O:$60.0       | [price](https://openai.com/pricing)                          |      | 4096       | [Docu](https://platform.openai.com/docs/api-reference/making-requests) | [Tokenizer](https://github.com/openai/tiktoken)              | 2024.01.24 |
| 3      | gpt-3.5-turbo-1106   | OpenAI    | tokens        | I: $1.00 O:$2.00       | [price](https://openai.com/pricing)                          |      | 4096       | [Docu](https://platform.openai.com/docs/api-reference/making-requests) | [Tokenizer](https://github.com/openai/tiktoken)              | 2024.01.24 |
| 4      | Jurassic-2 Ultra     | AI21      | tokens        | I/O: $15.0             | [price](https://openai.com/pricing)                          |      |            | [Docu](https://www.ai21.com/studio/pricing)                  | [Tokenizer](https://docs.ai21.com/reference/tokenize-ref)    | 2024.01.24 |
| 5      | Jurassic-2 Mid       | AI21      | tokens        | I/O: $10.0             | [price](https://www.ai21.com/studio/pricing)                 |      |            | [Docu](https://docs.ai21.com/reference/j2-complete-ref/)     | [Tokenizer](https://docs.ai21.com/reference/tokenize-ref)    | 2024.01.24 |
| 6      | Jurassic-2 Light     | AI21      | tokens        | I/O: $3.00             | [price](https://www.ai21.com/studio/pricing)                 |      |            | [Docu](https://docs.ai21.com/reference/j2-complete-ref/)     | [Tokenizer](https://docs.ai21.com/reference/tokenize-ref)    | 2024.01.24 |
| 7      | M2M100 1.2B          | Textsynth | tokens        | I: $0.15 O:$3.00       | [price](https://textsynth.com/pricing.html)                  | 1.2B |            | [Docu](https://textsynth.com/documentation.html)             |                                                              | 2024.01.24 |
| 8      | GPT-J 6B             | Textsynth | tokens        | II: $0.20 O:$5.00      | [price](https://textsynth.com/pricing.html)                  | 6B   |            | [Docu](https://textsynth.com/documentation.html)             |                                                              | 2024.01.24 |
| 9      | Falcon 7B            | Textsynth | tokens        | I: $0.20 O:$5.00       | [price](https://textsynth.com/pricing.html)                  | 7B   |            | [Docu](https://textsynth.com/documentation.html)             |                                                              | 2024.01.24 |
| 10     | Mistral 7B           | Textsynth | tokens        | I: $0.20 O:$2.00       | [price](https://textsynth.com/pricing.html)                  | 7B   |            | [Docu](https://textsynth.com/documentation.html)             |                                                              | 2024.01.24 |
| 11     | Llama2 7B            | Textsynth | tokens        | I: $0.20 O:$2.00 /     | [price](https://textsynth.com/pricing.html)                  | 7B   |            | [Docu](https://textsynth.com/documentation.html)             |                                                              | 2024.01.24 |
| 12     | Flan-T5-XXL          | Textsynth | tokens        | I: $0.20 O:$5.00       | [price](https://textsynth.com/pricing.html)                  | 11B  |            | [Docu](https://textsynth.com/documentation.html)             |                                                              | 2024.01.24 |
| 13     | Falcon 40B           | Textsynth | tokens        | I: $3.30 O:$10.00      | [price](https://textsynth.com/pricing.html)                  | 40B  |            | [Docu](https://textsynth.com/documentation.html)             |                                                              | 2024.01.24 |
| 14     | command              | Cohere    | tokens        | I: $1.00 O:$2.00       | [price](https://cohere.com/pricing)                          |      | 4096       | [Docu](https://docs.cohere.com/reference/generate)           | [Tokenizer](https://docs.cohere.com/reference/tokenize)      | 2024.01.24 |
| 15     | command-light        | Cohere    | tokens        | I: $0.30 O:$0.60       | [price](https://cohere.com/pricing)                          |      | 4096       | [Docu](https://docs.cohere.com/reference/generate)           | [Tokenizer](https://docs.cohere.com/reference/tokenize)      | 2024.01.24 |
| 16     | Claude-2.0           | Anthropic | tokens        | I: $11.02 O:$32.68     | [price](https://www-files.anthropic.com/production/images/model_pricing_july2023.pdf) |      |            | [Docu](https://docs.anthropic.com/claude/reference/complete_post) |                                                              | 2024.01.24 |
| 17     | Claude-2.0           | Anthropic | tokens        | I: $1.63 O:$5.51       | [price](https://www-files.anthropic.com/production/images/model_pricing_july2023.pdf) |      |            | [Docu](https://docs.anthropic.com/claude/reference/complete_post) | [Tokenizer](https://gist.github.com/gamingflexer/3364999976db4f8ba8df7829d7dfe384) | 2024.01.24 |
| 18     | Llama-2-13B-Chat     | Baidu     | tokens        | I/O: 6.00元            | [price](https://cloud.baidu.com/doc/WENXINWORKSHOP/s/Blfmc9dlf#大模型服务相关·产品价格) | 13B  |            | [Docu](https://cloud.baidu.com/doc/WENXINWORKSHOP/s/Nlks5zkzu) |                                                              | 2024.01.24 |
| 19     | Llama-2-70B-Chat     | Baidu     | tokens        | I/O: 35.0元            | [price](https://cloud.baidu.com/doc/WENXINWORKSHOP/s/Blfmc9dlf#大模型服务相关·产品价格) | 70B  |            | [Docu](https://cloud.baidu.com/doc/WENXINWORKSHOP/s/Nlks5zkzu) |                                                              | 2024.01.24 |
| 20     | ERNIE-Bot 4.0        | Baidu     | tokens        | I: 150元 O:300元       | [price](https://cloud.baidu.com/doc/WENXINWORKSHOP/s/Blfmc9dlf#大模型服务相关·产品价格) |      |            | [Docu](https://cloud.baidu.com/doc/WENXINWORKSHOP/s/Nlks5zkzu) |                                                              | 2024.01.24 |
| 21     | ChatGLM2-6B-32K      | Baidu     | tokens        | I/O: 4.00元            | [price](https://cloud.baidu.com/doc/WENXINWORKSHOP/s/Blfmc9dlf#大模型服务相关·产品价格) | 6B   |            | [Docu](https://cloud.baidu.com/doc/WENXINWORKSHOP/s/Nlks5zkzu) |                                                              | 2024.01.24 |
| 22     | Llama-2-7B-Chat      | Baidu     | tokens        | I/O: 4/00元/M          | [price](https://cloud.baidu.com/doc/WENXINWORKSHOP/s/Blfmc9dlf#大模型服务相关·产品价格) | 7B   |            | [Docu](https://cloud.baidu.com/doc/WENXINWORKSHOP/s/Nlks5zkzu) |                                                              | 2024.01.24 |
| 23     | ERNIE-Bot            | Baidu     | tokens        | I/O: 12.0元            | [price](https://cloud.baidu.com/doc/WENXINWORKSHOP/s/Blfmc9dlf#大模型服务相关·产品价格) |      |            | [Docu](https://cloud.baidu.com/doc/WENXINWORKSHOP/s/Nlks5zkzu) |                                                              | 2024.01.24 |
| 24     | BLOOMZ-7B            | Baidu     | tokens        | I/O: 4.00元            | [price](https://cloud.baidu.com/doc/WENXINWORKSHOP/s/Blfmc9dlf#大模型服务相关·产品价格) | 7B   |            | [Docu](https://cloud.baidu.com/doc/WENXINWORKSHOP/s/Nlks5zkzu) |                                                              | 2024.01.24 |
| 25     | ERNIE-Bot-turbo-0922 | Baidu     | tokens        | I: 8.00元 O:12.0元     | [price](https://cloud.baidu.com/doc/WENXINWORKSHOP/s/Blfmc9dlf#大模型服务相关·产品价格) |      |            | [Docu](https://cloud.baidu.com/doc/WENXINWORKSHOP/s/Nlks5zkzu) |                                                              | 2024.01.24 |

注：I and O represent Input and Output,respectively.The price of a request is determined from the number of input tokens  multiplied by the input token price summed with the number of generated tokens multiplied by the generated token price.
