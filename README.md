
# **Secure Horizon - Telegram Member Adder Tool** 🌐

**Secure Horizon Telegram Member Adder Tool** ටූල් එකට ඔබව සාදරයෙන් පිළිගනිමු! මෙම ටූල් එක මගින් ඔබට **source Group** එකක සිට **target group** එකකට Telegram පරිශීලකයන් සාමාජිකයන් ලෙස එක් කිරීමට සහය වන්නේය. මෙය **Automatic Mode** සහ **Manual Mode** මගින් ක්‍රියා කරයි. 

මෙම ටූල් එක **rate limit** සම්බන්ධ ගැටළු, **privacy protection**, සහ තවත් බොහෝ අංග මගින් සපයනු ලබයි.

## **✨ විශේෂාංග**
- **Automatic Mode**: සාමාජිකයන් ස්වයංක්‍රීයව එකතු කිරීම.
- **Manual Mode**: සාමාජිකයන් මනාව තෝරා එකතු කිරීම.
- **Rate Limit Handling**: Telegram මඟින් rate-limited වූ විට ස්වයංක්‍රීයව මාරු කිරීම.
- **Privacy Protection**: ගෝලිකයාගේ පෞද්ගලික සැකසුම් අනුව එකතු කිරීමට නොහැකි සාමාජිකයන් පසුකරයි.
- **ලස්සන Custom Banner**: ද්‍රව්‍ය විස්තර සහ සංවර්ධකගේ තොරතුරු සහිත ලස්සන බැනර් එකක්.

---

## **📸 SCREENSHOT**

![Example Banner](https://github.com/chamidu200/Telegram_Memb_Add/blob/1c3808230b55d4c2dcccafa5c5bd8d0a9f8d2b78/Telegram.PNG)


## **🎥 වීඩියෝ විස්තර**

මෙම ටූල් එක පිළිබඳ අන්තර්ගත වීඩියෝ විස්තර බලන්න:

[![Watch Tutorial](https://img.youtube.com/vi/YOUR_VIDEO_ID_HERE/0.jpg)](https://www.youtube.com/watch?v=YOUR_VIDEO_ID_HERE)


## **📝 අවශ්‍යතා**

මෙම ටූල් එක භාවිතා කිරීම සඳහා පහත දේවල් ඔබගේ පද්ධතියට ස්ථාපනය කර තිබීම අවශ්‍ය වේ:
- Python 3.7 හෝ ඉහළ version

- Telegram API සමඟ අන්තර්ක්‍රියා කිරීම සඳහා `telethon` පුස්තකාලය

## **⚡ ස්ථාපන මාර්ගෝපදේශ**

### පියවර 1: ගිටහි බාගත කිරීම
terminal එකක් විවෘත කර පහත අණවලින් මෙම ගිටහි බාගත කරන්න:

git clone https://github.com/chamidu200/Telegram_Memb_Add.git
cd Telegram_Memb_Add


### පියවර 2: Dependencies ස්ථාපනය කිරීම
අවශ්‍ය Python පුස්තකාල ස්ථාපනය කිරීම:

pip install -r requirements.txt

pip install tqdm

python Telegram_Members_Added.PY

### පියවර 3: Telegram API ක්‍රෙඩෙන්ෂියල් ලබාගන්න
Telegram සමඟ සම්බන්ධ වීම සඳහා API credentials අවශ්‍යයි:
- [Telegram API](https://my.telegram.org/auth) වෙත පිවිස, නව යෙදුමක් සාදන්න සහ ඔබගේ API ID සහ API Hash ලබා ගන්න.

### පියවර 4: ස්ක්‍රිප්ට් එක සැකසීම
`ADVANCERADDER.PY` ගොනුව විවෘත කර පහත සංරචක අයථා කරන්න:
- `API_ID`: ඔබගේ Telegram API ID සමඟ මාරු කරන්න.
- `API_HASH`: ඔබගේ Telegram API Hash සමඟ මාරු කරන්න.
- `SOURCE_GROUP`: ඔබගේ source group username හෝ ID එක සමඟ මාරු කරන්න.
- `TARGET_GROUP`: ඔබගේ target group username හෝ ID එක සමඟ මාරු කරන්න.

---

## **🚀 භාවිතය**

අවශ්‍ය සැකසුම් කිරීමෙන් පසු, ස්ක්‍රිප්ට් එක ක්‍රියාත්මක කරන්න:

python Telegram_Members_Added.PY


ස්ක්‍රිප්ට් එක ක්‍රියාත්මක වන විට, පහත පරිදි මෙනුවක් පෙන්වයි:
1. **Automatic Mode**: මෙම ක්‍රමය මගින් සාමාජිකයන් ස්වයංක්‍රීයව එකතු කෙරේ.
2. **Manual Mode**: ඔබට මනාව සාමාජිකයන් තෝරා එකතු කිරීමට අවස්ථාව ඇත.



## **⚙️ ක්‍රම භාවිතය**

- **Automatic Mode**: source group එකෙන් සාමාජිකයන් ස්වයංක්‍රීයව එකතු කිරීම.
- **Manual Mode**: ඔබට මනාව සාමාජිකයන් තෝරා එකතු කිරීමට අවස්ථාව ඇත.



## **📜 බලපත්‍රය**

මෙම ටූල් එක open-source ය. MIT License මත ලියා ඇති අතර, පෞද්ගලික හෝ අධ්‍යයන භාවිතයට එය වෙනස් කිරීමට සහ බෙදාහැරීමට ඔබට අවස්ථාව ඇත.

---

## **💡 සංවර්ධක තොරතුරු**

මෙම ටූල් එක **[Secure_Horizon](https://securehorizon.kesug.com/)** විසින් සංවර්ධනය කරන ලදි.

- **GitHub**: [https://github.com/chamidu200](https://github.com/chamidu200)
- **YouTube**: [https://www.youtube.com/@chamidunimsara20052](https://www.youtube.com/@chamidunimsara20052)
- **Website**: [https://securehorizon.kesug.com/?i=1](https://securehorizon.kesug.com/?i=1)



## **🔧 සම්බන්ධතා සහ සහාය**

කේෂ්‍ට ප්‍රශ්න හෝ සහාය සඳහා [GitHub Secure_Horizon](https://github.com/chamidu200/Telegram_Memb_Add.git) මත issue එකක් ඉදිරිපත් කරන්න.



> **Secure Horizon Telegram Member Adder Tool භාවිතා කිරීමේදී ස්තුතියි!** 💫
