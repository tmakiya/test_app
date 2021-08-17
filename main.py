import streamlit as st
import numpy as np
import pandas as pd

st.title('うつ症状チェックシート')

st.subheader('設問ごとに、あてはまるもの、近いものをひとつ選択してください。')
st.write('')

question1 = st.radio(
     "設問１　寝つき",
     ('問題ない（または、寝付くのに３０分以上かかったことは一度もない）。', 
     '寝つくのに３０分以上かかったこともあるが、一週間の半分以下である。', 
     '寝つくのに３０分以上かかったことが、週の半分以上ある。',
     '寝つくのに６０分以上かかったことが、（１週間の）半分以上ある。'))

if question1 == '問題ない（または、寝付くのに３０分以上かかったことは一度もない）。':
    score1 = 0
elif question1 == '寝つくのに３０分以上かかったこともあるが、一週間の半分以下である。':
    score1 = 1
elif question1 == '寝つくのに３０分以上かかったことが、週の半分以上ある。':
    score1 = 2
elif question1 == '寝つくのに６０分以上かかったことが、（１週間の）半分以上ある。':
    score1 = 3
else:
    score1 = 9999999

st.write('')

question2 = st.radio(
     "設問２　夜間の睡眠",
     ('問題ない（夜間に目が覚めたことはない）。', 
     '落ち着かない、浅い眠りで、何回か短く目が覚めたことがある。', 
     '毎晩少なくとも１回は目が覚めるが、難なくまた眠ることができる。',
     '毎晩１回以上目が覚め、そのまま２０分以上眠れないことが、（１週間の）半分以上ある。'))

if question2 == '問題ない（夜間に目が覚めたことはない）。':
    score2 = 0
elif question2 == '落ち着かない、浅い眠りで、何回か短く目が覚めたことがある。':
    score2 = 1
elif question2 == '毎晩少なくとも１回は目が覚めるが、難なくまた眠ることができる。':
    score2 = 2
elif question2 == '毎晩１回以上目が覚め、そのまま２０分以上眠れないことが、（１週間の）半分以上ある。':
    score2 = 3
else:
    score2 = 9999999

st.write('')

question3 = st.radio(
     "設問３　早く目が覚めすぎる",
     ('問題ない（または、ほとんどの場合、目が覚めるのは、起きなくてはいけない時間の、せいぜい３０分前である）。', 
     '週の半分以上、起きなくてはならない時間より３０分以上早く目が覚める。', 
     'ほとんどいつも、起きなくてはならない時間より１時間早く目が覚めてしまうが、最終的にはまた眠ることができる。',
     '起きなくてはならない時間よりも１時間以上早く起きてしまい、もう一度眠ることができない。'))

if question3 == '問題ない（または、ほとんどの場合、目が覚めるのは、起きなくてはいけない時間の、せいぜい３０分前である）。':
    score3 = 0
elif question3 == '週の半分以上、起きなくてはならない時間より３０分以上早く目が覚める。':
    score3 = 1
elif question3 == 'ほとんどいつも、起きなくてはならない時間より１時間早く目が覚めてしまうが、最終的にはまた眠ることができる。':
    score3 = 2
elif question3 == '起きなくてはならない時間よりも１時間以上早く起きてしまい、もう一度眠ることができない。':
    score3 = 3
else:
    score3 = 9999999

st.write('')

question4 = st.radio(
     "設問４　眠りすぎる",
     ('問題ない（夜間、眠りすぎることはなく、日中に昼寝をすることもない）。', 
     '２４時間のうち、眠っている時間は、昼寝を含めて１０時間ほどである。', 
     '２４時間のうち、眠っている時間は、昼寝を含めて１２時間ほどである。',
     '２４時間のうち、昼寝を含めて１２時間以上眠っている。'))

if question4 == '問題ない（夜間、眠りすぎることはなく、日中に昼寝をすることもない）。':
    score4 = 0
elif question4 == '２４時間のうち、眠っている時間は、昼寝を含めて１０時間ほどである。':
    score4 = 1
elif question4 == '２４時間のうち、眠っている時間は、昼寝を含めて１２時間ほどである。':
    score4 = 2
elif question4 == '２４時間のうち、昼寝を含めて１２時間以上眠っている。':
    score4 = 3
else:
    score4 = 9999999

score1_4 = max([score1,score2,score3,score4])

st.write('')

question5 = st.radio(
     "設問５　悲しい気持ち",
     ('悲しいとは思わない。', 
     '悲しいと思うことは、半分以下の時間である。', 
     '悲しいと思うことが半分以上の時間ある。',
     'ほとんどすべての時間、悲しいと感じている。'))

if question5 == '悲しいとは思わない。':
    score5 = 0
elif question5 == '悲しいと思うことは、半分以下の時間である。':
    score5 = 1
elif question5 == '悲しいと思うことが半分以上の時間ある。':
    score5 = 2
elif question5 == 'ほとんどすべての時間、悲しいと感じている。':
    score5 = 3
else:
    score5 = 9999999

st.write('')

question6 = st.radio(
     "設問６　食欲低下",
     ('普段の食欲と変わらない、または、食欲が増えた。', 
     '普段よりいくぶん食べる回数が少ないか、量が少ない。', 
     '普段よりかなり食べる量が少なく、食べるよう努めないといけない。',
     'まる１日（２４時間）ほとんどものを食べず、食べるのは極めて強く食べようと努めたり、誰かに食べるよう説得されたときだけである。'))

if question6 == '普段の食欲と変わらない、または、食欲が増えた。':
    score6 = 0
elif question6 == '普段よりいくぶん食べる回数が少ないか、量が少ない。':
    score6 = 1
elif question6 == '普段よりかなり食べる量が少なく、食べるよう努めないといけない。':
    score6 = 2
elif question6 == 'まる１日（２４時間）ほとんどものを食べず、食べるのは極めて強く食べようと努めたり、誰かに食べるよう説得されたときだけである。':
    score6 = 3
else:
    score6 = 9999999

st.write('')

question7 = st.radio(
     "設問７　食欲増進",
     ('普段の食欲と変わらない、または、食欲が減った。', 
     '普段より頻回に食べないといけないように感じる。', 
     '普段とくらべて、常に食べる回数が多かったり、量が多かったりする。',
     '食事の時も、食事と食事の間も、食べ過ぎる衝動にかられている。'))

if question7 == '普段の食欲と変わらない、または、食欲が減った。':
    score7 = 0
elif question7 == '普段より頻回に食べないといけないように感じる。':
    score7 = 1
elif question7 == '普段とくらべて、常に食べる回数が多かったり、量が多かったりする。':
    score7 = 2
elif question7 == '食事の時も、食事と食事の間も、食べ過ぎる衝動にかられている。':
    score7 = 3
else:
    score7 = 9999999

st.write('')

question8 = st.radio(
     "設問８　体重減少（最近２週間で）",
     ('体重は変わっていない、または、体重は増えた。', 
     '少し体重が減った気がする。', 
     '１キロ以上やせた。',
     '２キロ以上やせた。'))

if question8 == '体重は変わっていない、または、体重は増えた。':
    score8 = 0
elif question8 == '少し体重が減った気がする。':
    score8 = 1
elif question8 == '１キロ以上やせた。':
    score8 = 2
elif question8 == '２キロ以上やせた。':
    score8 = 3
else:
    score8 = 9999999

st.write('')

question9 = st.radio(
     "設問９　体重増加（最近２週間で）",
     ('体重は変わっていない、または、体重は減った。', 
     '少し体重が増えた気がする。', 
     '１キロ以上太った。',
     '２キロ以上太った。'))

if question9 == '体重は変わっていない、または、体重は減った。':
    score9 = 0
elif question9 == '少し体重が増えた気がする。':
    score9 = 1
elif question9 == '１キロ以上太った。':
    score9 = 2
elif question9 == '２キロ以上太った。':
    score9 = 3
else:
    score9 = 9999999

score6_9 = max([score6,score7,score8,score9])

st.write('')

question10 = st.radio(
     "設問１０　集中力／決断",
     ('集中力や決断力は普段と変わりない。', 
     'ときどき決断しづらくなっているように感じたり、注意が散漫になるように感じる。', 
     'ほとんどの時間、注意を集中したり、決断を下すのに苦労する。',
     'ものを読むこともじゅうぶんにできなかったり、小さなことですら決断できないほど集中力が落ちている。'))

if question10 == '集中力や決断力は普段と変わりない。':
    score10 = 0
elif question10 == 'ときどき決断しづらくなっているように感じたり、注意が散漫になるように感じる。':
    score10 = 1
elif question10 == 'ほとんどの時間、注意を集中したり、決断を下すのに苦労する。':
    score10 = 2
elif question10 == 'ものを読むこともじゅうぶんにできなかったり、小さなことですら決断できないほど集中力が落ちている。':
    score10 = 3
else:
    score10 = 9999999

st.write('')

question11 = st.radio(
     "設問１１　自分についての見方",
     ('自分のことを、他の人と同じくらい価値があって、援助に値する人間だと思う。', 
     '普段よりも自分を責めがちである。', 
     '自分が他の人に迷惑をかけているとかなり信じている。',
     '自分の大小の欠陥について、ほとんど常に考えている。'))

if question11 == '自分のことを、他の人と同じくらい価値があって、援助に値する人間だと思う。':
    score11 = 0
elif question11 == '普段よりも自分を責めがちである。':
    score11 = 1
elif question11 == '自分が他の人に迷惑をかけているとかなり信じている。':
    score11 = 2
elif question11 == '自分の大小の欠陥について、ほとんど常に考えている。':
    score11 = 3
else:
    score11 = 9999999

st.write('')

question12 = st.radio(
     "設問１２　死や自殺についての考え",
     ('死や自殺について考えることはない。', 
     '人生が空っぽに感じ、生きている価値があるかどうか疑問に思う。', 
     '自殺や死について、１週間に数回、数分間にわたって考えることがある。',
     '自殺や死について１日に何回か細部にわたって考える、または、具体的な自殺の計画を立てたり、実際に死のうとしたりしたことがあった。'))

if question12 == '死や自殺について考えることはない。':
    score12 = 0
elif question12 == '人生が空っぽに感じ、生きている価値があるかどうか疑問に思う。':
    score12 = 1
elif question12 == '自殺や死について、１週間に数回、数分間にわたって考えることがある。':
    score12 = 2
elif question12 == '自殺や死について１日に何回か細部にわたって考える、または、具体的な自殺の計画を立てたり、実際に死のうとしたりしたことがあった。':
    score12 = 3
else:
    score12 = 9999999

st.write('')

question13 = st.radio(
     "設問１３　一般的な興味",
     ('他人のことやいろいろな活動についての興味は普段と変わらない。', 
     '人々や活動について、普段より興味が薄れていると感じる。', 
     '以前好んでいた活動のうち、一つか二つのことにしか興味がなくなっていると感じる。',
     '以前好んでいた活動に、ほとんどまったく興味がなくなっている。'))

if question13 == '他人のことやいろいろな活動についての興味は普段と変わらない。':
    score13 = 0
elif question13 == '人々や活動について、普段より興味が薄れていると感じる。':
    score13 = 1
elif question13 == '以前好んでいた活動のうち、一つか二つのことにしか興味がなくなっていると感じる。':
    score13 = 2
elif question13 == '以前好んでいた活動に、ほとんどまったく興味がなくなっている。':
    score13 = 3
else:
    score13 = 9999999

st.write('')

question14 = st.radio(
     "設問１４　エネルギーのレベル",
     ('普段のエネルギーのレベルと変わりない。', 
     '普段よりも疲れやすい。', 
     '普段の日常の活動（例えば、買い物、宿題、料理、出勤など）をやり始めたり、やりとげるのに、大きな努力が必要である。',
     'ただエネルギーがないという理由だけで、日常の活動のほとんどが実行できない。'))

if question14 == '普段のエネルギーのレベルと変わりない。':
    score14 = 0
elif question14 == '普段よりも疲れやすい。':
    score14 = 1
elif question14 == '普段の日常の活動（例えば、買い物、宿題、料理、出勤など）をやり始めたり、やりとげるのに、大きな努力が必要である。':
    score14 = 2
elif question14 == 'ただエネルギーがないという理由だけで、日常の活動のほとんどが実行できない。':
    score14 = 3
else:
    score14 = 9999999

st.write('')

question15 = st.radio(
     "設問１５　動きが遅くなった気がする",
     ('普段どおりの速さで考えたり、話したり、動いたりしている。', 
     '頭の働きが遅くなっていたり、声が単調で平坦に感じる。', 
     'ほとんどの質問に答えるのに何秒かかかり、考えが遅くなっているのがわかる。',
     '最大の努力をしないと、質問に答えられないことがしばしばである。'))

if question15 == '普段どおりの速さで考えたり、話したり、動いたりしている。':
    score15 = 0
elif question15 == '頭の働きが遅くなっていたり、声が単調で平坦に感じる。':
    score15 = 1
elif question15 == 'ほとんどの質問に答えるのに何秒かかかり、考えが遅くなっているのがわかる。':
    score15 = 2
elif question15 == '最大の努力をしないと、質問に答えられないことがしばしばである。':
    score15 = 3
else:
    score15 = 9999999

st.write('')

question16 = st.radio(
     "設問１６　落ち着かない",
     ('落ち着かない気持ちはない。', 
     'しばしばそわそわしていて、手をもんだり、座り直したりせずにはいられない。', 
     '動き回りたい衝動があって、かなり落ち着かない。',
     'ときどき、座っていられなくて歩き回らずにはいられないことがある。'))

if question16 == '落ち着かない気持ちはない。':
    score16 = 0
elif question16 == 'しばしばそわそわしていて、手をもんだり、座り直したりせずにはいられない。':
    score16 = 1
elif question16 == '動き回りたい衝動があって、かなり落ち着かない。':
    score16 = 2
elif question16 == 'ときどき、座っていられなくて歩き回らずにはいられないことがある。':
    score16 = 3
else:
    score16 = 9999999

score15_16 = max([score15,score16])

total_score = score1_4+score5+score6_9+score10+score11+score12+score13+score14+score15_16

st.write('合計点数(0-27点):',total_score)

st.subheader("チェック結果")
message = '6点以上の場合にはうつ病の傾向が疑われます。チェックシートの結果のみで正確な診断をすることはできません。
結果の如何にかかわらず不安がある場合には、カウンセラーもしくは専門の医師にに相談してください。'
counseling_link = '[カウンセリング予約サイトのリンク先](https://outlook.office365.com/owa/calendar/Bookings@kyowayakuhin.co.jp/bookings/)'
medical_link = '[医療機関検索のリンク先](https://www.qlifeweb.jp/utsunoitami/)'

セルフチェックの結果のみで正確に診断することはできません。
結果の如何にかかわらず不安がある場合には、専門の医師に相談してください。

if total_score>=0 and total_score<=5:
    st.write('あなたのうつ症状は正常です。')
elif total_score>=6 and total_score<=10:
    st.write('あなたのうつ症状は軽度です。',message)
    st.markdown(counseling_link)
    st.markdown(medical_link)
elif total_score>=11 and total_score<=15:
    st.write('あなたのうつ症状は中等度です。',message)
    st.markdown(counseling_link)
    st.markdown(medical_link)
elif total_score>=16 and total_score<=20:
    st.write('あなたのうつ症状は重度です。',message)
    st.markdown(counseling_link)
    st.markdown(medical_link)
elif total_score>=21 and total_score<=27:
    st.write('あなたのうつ症状はきわけて重度です。',message)
    st.markdown(counseling_link)
    st.markdown(medical_link)
else:
    st.write('ロジックエラー')

st.write('厚生労働省ホームページ「QIDS-J解説」を参考にチャックシートを作成しております')
st.markdown('[厚生労働省ホームページ「QIDS-J解説」](https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/hukushi_kaigo/shougaishahukushi/kokoro/index.html)')
