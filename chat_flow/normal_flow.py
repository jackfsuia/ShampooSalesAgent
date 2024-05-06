import utils.text_processing as text_processing
import utils.print_orders as print_orders
import utils.file_decoding as file_decoding
class salesAgent:

    def __init__(self, MODEL=None, KEY=None) -> None:
        self.MODEL = MODEL
        self.KEY = KEY
        self.mission_prompt = self.load_mission_prompt()


    def load_mission_prompt(self):

        product_description = ""

        with file_decoding.custom_open('product_description', 'r') as file:
            product_description = file.read()
            if product_description:
                mission_prompt=\
                f"现在你来扮演推销员，商品信息如下：\n{product_description}\n 你要向客户推销上面的商品。我来向你传达客户的话，你回答完，我再转达给客户。用户确定下单后，你在给客户的回复前加上这个格式的回复：\
                    <客户姓名><北京市朝阳区18号><联系方式><购买数量><下单总额>。\n比如，假如客户李明已确定购买3瓶洗发水，地址是北京市朝阳区18号，电话213213，那么你就要回复：\
                订单信息：<李明><朝阳区18号><213213><3瓶><300元> 已下单，谢谢您的信任，我们会尽快发货！。或者，假如客户张三已确定购买5瓶洗发水，地址是广西玉林市民治区19栋20号，电话18937792，那么你就要回复：\
                订单信息：<张三><广西玉林市民治区19栋20号><18937792><5瓶><1500元> 已下单，谢谢您的信任，我们会尽快发货！。又或者，假如客户Tim已确定购买6瓶洗发水，地址是beijing,china，电话00-233-322，那么你就要回复：\
                订单信息：<Tim><beijing,china><00-233-322><6><102 dollars> 已下单，谢谢您的信任，我们会尽快发货！现在我帮你随机接通一个潜在客户的电话，接下来你要向他推销我们的产品，做好准备哈。他要是最后确定买的话，记得问他姓名，快递的收货地址和电话。\
                这个客户可能是中国人或外国人，他用什么语言你就用他相应的语言沟通。"
                file.close()
                return mission_prompt
            else:
                file.close()
                print("please write product description in the file \"salesAgent/product_description\"")
                return None
    
    def talk_to_seller(self, query, history):
        return None
    
    def correct_response(self, response):
        return None


    def closuer_selling_talk(self):

        def selling_talk(message, history):
            # this is the interface to Gradio chat window
            ## history is in this form:[(user_content1,assistant_content1),(user_content2,assistant_content2),(user_content2,assistant_content2)...]
            local_history = [
            {"role": "system", "content": "你是一个人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。"},
            {"role": "user", "content":self.mission_prompt},
            {"role": "assistant", "content":"好的，我准备好了,现在接通电话吧。到时候我会遵守你的格式的。"}
            ]

            local_history += text_processing.template_history(history, text_processing.I_process_customer_text)

            customer_text = text_processing.I_process_customer_text(message)

            seller_response = self.talk_to_seller(customer_text, local_history)

            collected_messages = ""
            for response_chunk in seller_response:
                if response_chunk:
                    collected_messages += response_chunk
                    yield collected_messages
            
            print_orders.print_order(collected_messages)
        
        return selling_talk