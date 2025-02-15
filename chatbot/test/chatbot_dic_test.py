import pickle
from chatbot.utils.Preprocess import Preprocess

# 단어 사전 불러오기
f = open("C:/Users/obybk/OneDrive/바탕 화면/인공지능/deepChat/chatbot/train_tools/dict/chatbot_dict.bin", "rb")
word_index = pickle.load(f)
f.close()

sent = "내일 오전 10시에 탕수육 주문하고 싶어 ㅋㅋ"
p = Preprocess(userdic="C:/Users/obybk/OneDrive/바탕 화면/인공지능/deepChat/Tokenizing/user_dic.txt")

# 형태소 분석기 실행
p = p.pos(sent)

# 품사 태그 없이 키워드 출력
keywords = p.get_keywords(pos, without_tag = True)
for word in keywords:
    try:
        print(word, word_index[word])
    except KeyError:
        # 해당 단어가 없는 경우 OOV처리
        print(word, word_index['OOV'])
