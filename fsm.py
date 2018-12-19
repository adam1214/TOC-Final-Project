from transitions.extensions import GraphMachine

from utils import send_text_message
from utils import send_image_url


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )

    def is_going_to_state1(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '飯'
        return False

    def is_going_to_state2(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '麵'
        return False
    def is_going_to_state3(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '牛肉湯'
        return False
    def is_going_to_state4(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '小妞炒飯'
        return False
    
    def is_going_to_state5(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '介紹'
        return False
    def is_going_to_state6(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '日食堂'
        return False    
    def is_going_to_state7(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '介紹'
        return False    
    def is_going_to_state8(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '佑師絕鼎炒飯'
        return False    
    def is_going_to_state9(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '介紹'
        return False    
    def is_going_to_state10(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '上海味香小吃店'
        return False    
    def is_going_to_state11(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '介紹'
        return False
    def is_going_to_state12(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '神武拉麵'
        return False  
    def is_going_to_state13(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '介紹'
        return False 
    def is_going_to_state14(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '覺丸拉麵'
        return False 
    def is_going_to_state15(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '介紹'
        return False  
    def is_going_to_state16(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '恭仔意麵'
        return False 
    def is_going_to_state17(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '介紹'
        return False
    def is_going_to_state18(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '文章'
        return False
    def is_going_to_state19(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '介紹'
        return False
    def is_going_to_state20(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '旗哥'
        return False
    def is_going_to_state21(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '介紹'
        return False
    def is_going_to_state22(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '劉哥'
        return False    
    def is_going_to_state23(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '介紹'
        return False  
    def on_enter_state1(self, event):
        print("小妞炒飯\n日食堂\n佑師絕鼎炒飯\n上海味香小吃店")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "小妞炒飯\n日食堂\n佑師絕鼎炒飯\n上海味香小吃店")

    def on_exit_state1(self,update):
        print('Leaving state1')

    def on_enter_state2(self, event):
        print("神武拉麵\n覺丸拉麵\n恭仔意麵")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "神武拉麵\n覺丸拉麵\n恭仔意麵")

    def on_exit_state2(self,update):
        print('Leaving state2')
    def on_enter_state3(self, event):
        print("文章\n旗哥\n劉哥")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "文章\n旗哥\n劉哥")

    def on_exit_state3(self,update):
        print('Leaving state3')

    def on_enter_state4(self, event):
        print("想吃小妞炒飯嗎？\n附上位置與營業時間：\nhttps://www.google.com.tw/maps/place/%E5%B0%8F%E5%A6%9E%E7%82%92%E9%A3%AF%26%E8%98%87%E8%83%96%E9%8E%96%E5%BA%97/@23.546162,120.6402133,8z/data=!4m5!3m4!1s0x346e769289978b4f:0x96b161750347ea90!8m2!3d22.995893!4d120.2178727?hl=zh-TW")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "想吃小妞炒飯嗎？\n附上位置與營業時間：\nhttps://www.google.com.tw/maps/place/%E5%B0%8F%E5%A6%9E%E7%82%92%E9%A3%AF%26%E8%98%87%E8%83%96%E9%8E%96%E5%BA%97/@23.546162,120.6402133,8z/data=!4m5!3m4!1s0x346e769289978b4f:0x96b161750347ea90!8m2!3d22.995893!4d120.2178727?hl=zh-TW")

    def on_exit_state4(self,update):
        print('Leaving state4')

    def on_enter_state5(self, event):
        print("最推宮保雞丁炒飯,但是切記,你去點餐的時候不能說很冗,例如：我要吃宮保雞丁炒飯,這樣會被老闆娘碎碎念,你只能說我要吃宮保")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "最推宮保雞丁炒飯,但是切記,你去點餐的時候不能說很冗,例如：我要吃宮保雞丁炒飯,這樣會被老闆娘碎碎念,你只能說我要吃宮保")
        send_image_url(sender_id,"https://cfcdn2.azsg.opensnap.com/azsg/snapphoto/photo/LA/GTPU/3BNBSCBBBECCC2C04C3569lv.jpg")
        self.go_back()

    def on_exit_state5(self):
        print('Leaving state5')

    def on_enter_state6(self, event):
        print("想吃日食堂嗎？\n附上位置與營業時間：\nhttps://www.google.com/maps/place/%E6%97%A5%E9%A3%9F%E5%A0%82/@22.9984143,120.2252319,17z/data=!3m1!4b1!4m5!3m4!1s0x346e76ea8528c353:0x1f3d2c22af58ad83!8m2!3d22.9984143!4d120.2274206")
        sender_id = event['sender']['id']
        send_text_message(sender_id, "想吃日食堂嗎？\n附上位置與營業時間：\nhttps://www.google.com/maps/place/%E6%97%A5%E9%A3%9F%E5%A0%82/@22.9984143,120.2252319,17z/data=!3m1!4b1!4m5!3m4!1s0x346e76ea8528c353:0x1f3d2c22af58ad83!8m2!3d22.9984143!4d120.2274206")

    def on_exit_state6(self,update):
        print('Leaving state6')

    def on_enter_state7(self, event):
        print("是我吃過CP值最高的丼飯～價位在100附近,便宜又大碗,最推炸豬排丼飯")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "是我吃過CP值最高的丼飯～價位在100附近,便宜又大碗,最推炸豬排丼飯")
        send_image_url(sender_id,"https://pic.pimg.tw/fanimko1/1483517475-869695584_n.jpg")
        self.go_back()

    def on_exit_state7(self):
        print('Leaving state7')
    def on_enter_state8(self, event):
        print("想吃佑師絕鼎炒飯嗎？\n附上位置與營業時間：\nhttps://www.google.com/maps/place/%E4%BD%91%E5%B8%AB%E7%B5%95%E9%BC%8E%E7%82%92%E9%A3%AF%E5%B0%88%E9%96%80%E5%BA%97/@23.0055545,120.2558223,17z/data=!3m1!4b1!4m5!3m4!1s0x346e712eb1246a31:0xbfda8f3a6255695!8m2!3d23.0055545!4d120.258011")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "想吃佑師絕鼎炒飯嗎？\n附上位置與營業時間：\nhttps://www.google.com/maps/place/%E4%BD%91%E5%B8%AB%E7%B5%95%E9%BC%8E%E7%82%92%E9%A3%AF%E5%B0%88%E9%96%80%E5%BA%97/@23.0055545,120.2558223,17z/data=!3m1!4b1!4m5!3m4!1s0x346e712eb1246a31:0xbfda8f3a6255695!8m2!3d23.0055545!4d120.258011")

    def on_exit_state8(self,update):
        print('Leaving state8')
    def on_enter_state9(self, event):
        print("最推小卷炒飯,100元有5條小卷94爽,建議電話預約,不然有時候要等很久")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "最推小卷炒飯,100元有5條小卷94爽,建議電話預約,不然有時候要等很久")
        send_image_url(sender_id,"https://img.gwan.tw/20171008230104_80.jpg")
        self.go_back()

    def on_exit_state9(self):
        print('Leaving state9')    
    def on_enter_state10(self, event):
        print("想吃上海味香小吃店嗎？\n附上位置與營業時間：\nhttps://www.google.com/maps/place/%E4%B8%8A%E6%B5%B7%E5%91%B3%E9%A6%99%E5%B0%8F%E5%90%83%E5%BA%97/@22.9931959,120.2046487,17z/data=!3m1!4b1!4m5!3m4!1s0x346e7689ba172f0d:0x82be4745c8b490!8m2!3d22.9931959!4d120.2068427")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "想吃上海味香小吃店嗎？\n附上位置與營業時間：\nhttps://www.google.com/maps/place/%E4%B8%8A%E6%B5%B7%E5%91%B3%E9%A6%99%E5%B0%8F%E5%90%83%E5%BA%97/@22.9931959,120.2046487,17z/data=!3m1!4b1!4m5!3m4!1s0x346e7689ba172f0d:0x82be4745c8b490!8m2!3d22.9931959!4d120.2068427")

    def on_exit_state10(self,update):
        print('Leaving state10')
    def on_enter_state11(self, event):
        print("最推排骨蛋炒飯+小籠包,排骨蛋炒飯的肉是炸的喔,然後比較油,吃清淡的朋友自行斟酌")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "最推排骨蛋炒飯+小籠包,排骨蛋炒飯的肉是炸的喔,然後比較油,吃清淡的朋友自行斟酌")
        send_image_url(sender_id,"https://img.bopomo.tw/20180825150654_31.jpg")
        self.go_back()

    def on_exit_state11(self):
        print('Leaving state11')  

    def on_enter_state12(self, event):
        print("想吃神武拉麵嗎？\n附上位置與營業時間：\nhttps://www.google.com/maps/place/%E7%A5%9E%E6%AD%A6%E6%97%A5%E6%9C%AC%E6%8B%89%E9%BA%B5/@23.0120426,120.1930567,13z/data=!4m8!1m2!2m1!1z56We5q2m5ouJ6bq1!3m4!1s0x346e767b1867cbe5:0x4c47bd68bd198a52!8m2!3d22.9905971!4d120.197034")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "想吃神武拉麵嗎？\n附上位置與營業時間：\nhttps://www.google.com/maps/place/%E7%A5%9E%E6%AD%A6%E6%97%A5%E6%9C%AC%E6%8B%89%E9%BA%B5/@23.0120426,120.1930567,13z/data=!4m8!1m2!2m1!1z56We5q2m5ouJ6bq1!3m4!1s0x346e767b1867cbe5:0x4c47bd68bd198a52!8m2!3d22.9905971!4d120.197034")

    def on_exit_state12(self,update):
        print('Leaving state12')

    def on_enter_state13(self, event):
        print("全品項拉麵都是無限加到爽,吃過CP值最高的拉麵")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "全品項拉麵都是無限加到爽,吃過CP值最高的拉麵")
        send_image_url(sender_id,"https://pic.pimg.tw/kel8257/1515676810-3435954578_n.jpg")
        self.go_back()

    def on_exit_state13(self):
        print('Leaving state13')

    def on_enter_state14(self, event):
        print("想吃覺丸拉麵嗎？\n附上位置與營業時間：\nhttps://www.google.com/maps/place/%E8%A6%BA%E4%B8%B8%E6%8B%89%E9%BA%B5/@22.9959558,120.2276864,17z/data=!3m1!4b1!4m5!3m4!1s0x346e76c075aa3a33:0x6399402cf32a429c!8m2!3d22.9959558!4d120.2298804")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "想吃覺丸拉麵嗎？\n附上位置與營業時間：\nhttps://www.google.com/maps/place/%E8%A6%BA%E4%B8%B8%E6%8B%89%E9%BA%B5/@22.9959558,120.2276864,17z/data=!3m1!4b1!4m5!3m4!1s0x346e76c075aa3a33:0x6399402cf32a429c!8m2!3d22.9959558!4d120.2298804")

    def on_exit_state14(self,update):
        print('Leaving state14')

    def on_enter_state15(self, event):
        print("是我吃過台南最頂級的拉麵,價位偏高,大概200元一碗,建議開店前20分鐘到,否則都要等一小時甚至更久")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "是我吃過台南最頂級的拉麵,價位偏高,大概200元一碗,建議開店前20分鐘到,否則都要等一小時甚至更久")
        send_image_url(sender_id,"https://pic.pimg.tw/pinkmayday0928/1498578575-2851167905.jpg")
        self.go_back()

    def on_exit_state15(self):
        print('Leaving state15')
    def on_enter_state16(self, event):
        print("想吃恭仔意麵嗎？\n附上位置與營業時間：\nhttps://www.google.com/maps/place/%E6%81%AD%E4%BB%94%E8%82%89%E7%87%A5%E6%84%8F%E9%BA%B5/@22.9947159,120.1980375,17z/data=!3m1!4b1!4m5!3m4!1s0x346e76639060776f:0xeb16e257a3e4145e!8m2!3d22.9947159!4d120.2002315")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "想吃恭仔意麵嗎？\n附上位置與營業時間：\nhttps://www.google.com/maps/place/%E6%81%AD%E4%BB%94%E8%82%89%E7%87%A5%E6%84%8F%E9%BA%B5/@22.9947159,120.1980375,17z/data=!3m1!4b1!4m5!3m4!1s0x346e76639060776f:0xeb16e257a3e4145e!8m2!3d22.9947159!4d120.2002315")

    def on_exit_state16(self,update):
        print('Leaving state16')
    def on_enter_state17(self, event):
        print("台南傳統小吃代表,每次必點大碗意麵+10顆水餃")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "台南傳統小吃代表,每次必點大碗意麵+10顆水餃")
        send_image_url(sender_id,"https://farm8.staticflickr.com/7062/6937935363_2d6fdd001c_b.jpg")
        self.go_back()

    def on_exit_state17(self):
        print('Leaving state17')
    def on_enter_state18(self, event):
        print("想吃文章牛肉湯嗎？\n附上位置與營業時間：\nhttps://www.google.com/maps/place/%E6%96%87%E7%AB%A0%E7%89%9B%E8%82%89%E6%B9%AF/@22.998482,120.1759331,17z/data=!3m1!4b1!4m5!3m4!1s0x346e761abb62710d:0xc31bcd84dd49574a!8m2!3d22.998482!4d120.1781271")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "想吃文章牛肉湯嗎？\n附上位置與營業時間：\nhttps://www.google.com/maps/place/%E6%96%87%E7%AB%A0%E7%89%9B%E8%82%89%E6%B9%AF/@22.998482,120.1759331,17z/data=!3m1!4b1!4m5!3m4!1s0x346e761abb62710d:0xc31bcd84dd49574a!8m2!3d22.998482!4d120.1781271")

    def on_exit_state18(self,update):
        print('Leaving state18')
    def on_enter_state19(self, event):
        print("網路最夯牛肉湯,多觀光客與藝人光臨")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "網路最夯牛肉湯,多觀光客與藝人光臨")
        send_image_url(sender_id,"https://img.foodieteller.com/20160813204740_12.jpg")
        self.go_back()

    def on_exit_state19(self):
        print('Leaving state19')
    def on_enter_state20(self, event):
        print("想吃旗哥牛肉湯嗎？\n附上位置與營業時間：\nhttps://www.google.com/maps/place/%E6%97%97%E5%93%A5%E7%89%9B%E8%82%89%E6%B9%AF/@23.0099623,120.1833534,17z/data=!3m1!4b1!4m5!3m4!1s0x346e76f7aaaaaaab:0xcdb2bf6a690a5c12!8m2!3d23.0099623!4d120.1855474")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "想吃旗哥牛肉湯嗎？\n附上位置與營業時間：\nhttps://www.google.com/maps/place/%E6%97%97%E5%93%A5%E7%89%9B%E8%82%89%E6%B9%AF/@23.0099623,120.1833534,17z/data=!3m1!4b1!4m5!3m4!1s0x346e76f7aaaaaaab:0xcdb2bf6a690a5c12!8m2!3d23.0099623!4d120.1855474")

    def on_exit_state20(self,update):
        print('Leaving state20')
    def on_enter_state21(self, event):
        print("在地台南人公認最好喝牛肉湯,沒有之一,在網路上比較不有名,多台南在地老饕光顧")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "在地台南人公認最好喝牛肉湯,沒有之一,在網路上比較不有名,多台南在地老饕光顧")
        send_image_url(sender_id,"https://pic.pimg.tw/songster/1428286360-2889139926.jpg")
        self.go_back()

    def on_exit_state21(self):
        print('Leaving state21')
    def on_enter_state22(self, event):
        print("想吃劉哥牛肉湯嗎？\n附上位置與營業時間：\nhttps://www.google.com/maps/place/%E5%8A%89%E5%93%A5%E7%89%9B%E8%82%89%E6%B9%AF/@22.9894814,120.2278251,17z/data=!3m1!4b1!4m5!3m4!1s0x346e76bdc6ae9c67:0x8dea65d88b4ea98f!8m2!3d22.9894814!4d120.2300191")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "想吃劉哥牛肉湯嗎？\n附上位置與營業時間：\nhttps://www.google.com/maps/place/%E5%8A%89%E5%93%A5%E7%89%9B%E8%82%89%E6%B9%AF/@22.9894814,120.2278251,17z/data=!3m1!4b1!4m5!3m4!1s0x346e76bdc6ae9c67:0x8dea65d88b4ea98f!8m2!3d22.9894814!4d120.2300191")

    def on_exit_state22(self,update):
        print('Leaving state22')
    def on_enter_state23(self, event):
        print("個人認為是離成大最近且最好喝的牛肉湯,大推他們的牛肉炒飯,但是有點辣,不吃辣的朋友自行斟酌")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "個人認為是離成大最近且最好喝的牛肉湯,大推他們的牛肉炒飯,但是有點辣,不吃辣的朋友自行斟酌")
        send_image_url(sender_id,"https://cdn3.tw.orstatic.com/userphoto/photo/9/7Q6/01IY8MD7E08BFDBBDA2051px.jpg")
        self.go_back()

    def on_exit_state23(self):
        print('Leaving state23')

        
