<p align="center">
    <img src="image/goodsell.png" width="50%" >
</p>
<h1 align="center">ShampooSalesAgent</h1>

<div align="center">

<h3 align="center">
A minimal LLM Agent Framework for Sales Agent Fast Deployment and Benchmark 
</h3>

[![license][license-image]][license-url]
![GitHub Release](https://img.shields.io/github/v/release/jackfsuia/ShampooSalesAgent?include_prereleases&display_name=release&logo=github&label=pre-release)

[license-image]: http://img.shields.io/badge/license-MIT-blue.svg
[license-url]: https://github.com/gogogo22/ShampooSalesAgent/blob/master/LICENSE
English | [简体中文](README_zh.md)
</div>

A LLM-powered minimal agent that sells Shampoo (or any product provided a product information) for a living. Fluent conversation with customers on Web and will record their orders in a local .csv [file](customer_orders.csv). 

Support all models, including openai models, huggingface models, claude, gemini, baichuan(百川), qwen(通义千问), moonshot(月之暗面), ernie(文心一言), glm(智谱). Very friendly for beginners, researchers and interested businessman who want to try things out quick.

## Quick Start
Run
```bash
git clone https://github.com/jackfsuia/ShampooSalesAgent.git && cd ShampooSalesAgent
```
After installing the requirements (gradio, openai, etc). Run

```bash
python start.py MODEL YOUR_KEY
```
MODEL can be [gpt3.5/4](https://platform.openai.com/docs/models/overview), [claude](https://www.anthropic.com/api), [gemini](https://ai.google.dev/gemini-api/docs/api-key), [baichuan](https://platform.baichuan-ai.com/console/apikey), [qwen](https://help.aliyun.com/zh/dashscope/developer-reference/activate-dashscope-and-create-an-api-key), [kimi](https://platform.moonshot.cn/console/api-keys), [glm](https://open.bigmodel.cn/usercenter/apikeys).YOUR_KEY is your model API KEY. If you don't have a KEY, click the link on those model names to apply/buy.

But if you're using [ernie](https://cloud.baidu.com/doc/WENXINWORKSHOP/s/clntwmv7t), you should instead run 
```bash
python start.py MODEL API_Key Secret_Key
```
API_Key and Secret_Key are defined by ernie, please refer to their website.

and if you're using [huggingface model](https://huggingface.co/welcome), just run 
```bash
python start.py MODEL
```
That's all!  

If you want to use CLI instead of web as interface, just use `start_CLI.py` instead of `start.py`.

By default, this agent proactively sells Shampoo. Write your own product information to [product_description](product_description) if you want to sell something else. The order infomation (name, address, phone number, purchase quantity, etc. provided by customers)  will be printed to [customer_orders.csv](customer_orders.csv). The mission prompt is in [normal_flow.py](chat_flow/normal_flow.py) in case you want to change it.

## Examples
Let's say you're using gpt-3.5-turbo as model, the KEY you bought is sdjkSOIjkdejs. Then you should be running
```bash
python start.py gpt-3.5-turbo sdjkSOIjkdejs
```
or for short ([a few models have short names](#Table))
```bash
python start.py gpt sdjkSOIjkdejs
```
*For [gradio](https://github.com/gradio-app/gradio) on Windows 10 to successfully work, you might have to download some mystery file that you have to turn off Windows Defender and add some folders to Defender exclusion list to do.*

then the ouput will be something like this
```
path\ShampooSalesAgent>python start.py gpt sdjkSOIjkdejs
please go to one of the following  links to chat, and the second link can be shared public. If the link crash during chat, please keep clicking the Retry button located at the bottom of the chat page. if 
you need it to speak English, you can just say 'speak english' to it.(请点击以下任一网址进入聊天，第二个网址可以分享给其他人。聊天的时候崩溃请点聊天框下面的Retry按钮)
Running on local URL:  http://127.0.0.1:7860
Running on public URL: https://8fefa6c18e039476175.gradio.live

This share link expires in 72 hours. For free permanent hosting and GPU upgrades, run `gradio deploy` from Terminal to deploy to Spaces (https://huggingface.co/spaces)
```

Both links work. Only the second link can be shared to public. Click the link, you'll see the web, and have a chat

<img src="image/e1.PNG">
<img src="image/e2.PNG">

the order infomation will be printed out to the CLI
```
This share link expires in 72 hours. For free permanent hosting and GPU upgrades, run `gradio deploy` from Terminal to deploy to Spaces (https://huggingface.co/spaces)
2024-04-02 13:52:01.748677 <Jack Oliver><490 2nd St, Suite 300, New York><212555-1212><2 bottles><30 USD>
Customer order information has been written to customer_orders.csv
```
and [customer_orders.csv](customer_orders.csv). Open this .csv file, you'll see the order information line
```
2024-04-02 13:52:01.748677,Jack Oliver,"490 2nd St, Suite 300, New York",212555-1212,2 bottles,30 USD
```
has been added.

 *Do you like this project? Give us a :star:*
 
## Model Evaluation—Who is the Sales Champion?

Run 
```bash
python order_counting.py
```
you will find out. You can share your interesting results on this benchmark with us all.

## Future Work
- Finetune the model to be more professional at selling things, and talk more natural just like human. It is important to make people feel connections with each other, even with a robot (like the movie, *her*). 99% of people are not complex reasoning machines, but almost every one of them can make us feel warm and support at some point in life.
- Support multimodal models. This might be simpler and soon.
  
## License

ShampooSalesAgent is licensed under the MIT License found in the [LICENSE](LICENSE) file in the root directory of this repository.

## Citation

If this work is helpful, please kindly cite as:

```bibtex
@article{ShampooSalesAgent,
  title={ShampooSalesAgent: A minimal LLM Sales Agent Framework for Sales Agent Fast Deployment and Benchmark}, 
  author={Yannan Luo},
  year={2024},
  url={https://github.com/gogogo22/ShampooSalesAgent}
}
```
## Acknowledgement

This repo benefits from [gradio](https://github.com/gradio-app/gradio), and the free models I have been using: [baichuan](https://platform.baichuan-ai.com/console/apikey), [qwen](https://help.aliyun.com/zh/dashscope/developer-reference/activate-dashscope-and-create-an-api-key), [kimi](https://platform.moonshot.cn/console/api-keys), [huggingface model](https://huggingface.co/welcome). Thanks for their wonderful works. Thank [gpt3.5/4](https://platform.openai.com/docs/models/overview) for open the imagination. 

## Table
A few models have short names.

Full Name| Short Name
-|-
gpt-3.5-turbo|gpt
gemini-pro|gemini
claude-3-opus-20240229|claude
moonshot-v1-8k|kimi
qwen1.5-72b-chat|qwen
Baichuan2-Turbo|baichuan
ERNIE-4.0-8K|ernie
glm-4|glm
