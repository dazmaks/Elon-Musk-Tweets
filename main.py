from config import *
from PIL import Image, ImageDraw, ImageFont

try:
	img = Image.open('Static/Templates/Template-2-Line-Black-Theme.png')
	template = ImageDraw.Draw(img)
	bold = ImageFont.truetype('Static/Fonts/Segoe UI Bold.ttf', 15)
	template.text((71, 8), NAME, font=bold, fill =(255, 255, 255))
	text = ImageFont.truetype('Static/Fonts/Segoe UI.ttf', 15)
	template.text((71, 29), TEXT, font=text, fill =(255, 255, 255))
	stats = ImageFont.truetype('Static/Fonts/Segoe UI.ttf', 14)
	template.text((173, 8), USERNAME, font=stats, fill =(107, 125, 140))
	template.text((260, 8), DATE, font=stats, fill =(107, 125, 140))
	template.text((100, 78), COMMENTS, font=stats, fill =(107, 125, 140))
	template.text((230, 78), RETWEETS, font=stats, fill =(107, 125, 140))
	template.text((360, 78), LIKES, font=stats, fill =(107, 125, 140))
	img.save("Result.png")
	img.show()
except Exception as e:
	print("En error occurred: "+e)