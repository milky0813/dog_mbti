print("🐶 犬版MBTI診断を始めましょう！")
import streamlit as st

def dog_mbti_quiz():
    st.title("🐶 犬版MBTI診断テスト")
    
    st.write("AまたはBを選んで、愛犬の性格を診断しよう！")
    
    # 質問リスト
    questions = [
        ("新しいおもちゃをもらったら…", "A. すぐにくわえて遊ぶ！", "B. まずは観察してから触る"),
        ("初対面の犬に会ったとき…", "A. すぐに駆け寄って遊ぼうとする", "B. 少し離れて様子をうかがう"),
        ("知らない人が家に来たとき…", "A. すぐに近づいて歓迎する", "B. 警戒して吠えるか、隠れる"),
        ("飼い主が外出するとき…", "A. どこ行くの？とついて行きたがる", "B. 静かに見送る"),
        ("他の犬と遊ぶとき…", "A. たくさんの犬と遊びたがる", "B. 1匹か2匹の特定の犬とだけ遊ぶ"),
    ]
    
    # カウント変数
    E, I, S, N, T, F, J, P = 0, 0, 0, 0, 0, 0, 0, 0
    
    # 回答選択
    for i, (question, option_a, option_b) in enumerate(questions):
        st.write(f"### {i+1}. {question}")
        choice = st.radio("選んでください:", (option_a, option_b), key=f"q{i}")
        
        # 回答に応じたカウント
        if i < 5: 
            # ここにインデントを入れて、処理を書く
            if choice == option_a:
                E += 1
            else:
                I += 1
