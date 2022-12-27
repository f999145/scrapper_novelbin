from yandexfreetranslate import YandexFreeTranslate
from save_and_load import _load_texts
yt = YandexFreeTranslate()
# yt = YandexFreeTranslate(api = "web")
# yt = YandexFreeTranslate(api = "ios")

# yt.set_proxy("socks5", "localhost", 9050, "username", "password")
test = _load_texts()
text = test[list(test.keys())[2]]
print()
print(yt.translate("en", "ru", text))