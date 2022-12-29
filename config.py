from fake_useragent import UserAgent

url = 'https://novelbin.com/b/supreme-magus-novel/chapter-2'

def get_headers() -> dict[str, str]:
    ua = UserAgent()
    headers = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                'User-Agent':ua.random
            }
    return headers

pagin_url = 'https://novelbin.com/ajax/chapter-option?novelId=supreme-magus-novel&currentChapterId=chapter-4'

Cookies = {
	"Host raw": "http://.reg.ru/",
	"Name raw": "advcake_track_id",
	"Path raw": "/",
	"Content raw": "6f8477ef-1c5e-b71b-d460-7df7bbddd998",
	"Expires": "28-01-2023 12:44:36",
	"Expires raw": "1674899076",
	"Send for": "Any type of connection",
	"Send for raw": "false",
	"HTTP only raw": "false",
	"SameSite raw": "no_restriction",
	"This domain only": "Valid for subdomains",
	"This domain only raw": "false",
	"Store raw": "firefox-default",
	"First Party Domain": ""
}