import sqlite3

tools = [
    ("ChatGPT", "محادثة ذكية من OpenAI", "محادثة", "https://chat.openai.com", ""),
    ("Midjourney", "توليد صور بالذكاء الاصطناعي", "صور", "https://www.midjourney.com", ""),
    ("Canva AI", "تصميم باستخدام الذكاء الاصطناعي", "تصميم", "https://www.canva.com", ""),
    ("Codeium", "مساعد برمجي ذكي", "برمجة", "https://codeium.com", ""),
    ("Runway", "تعديل فيديوهات بالذكاء الاصطناعي", "فيديو", "https://runwayml.com", ""),
    ("Leonardo AI", "إنشاء صور واقعية", "صور", "https://leonardo.ai", ""),
    ("Notion AI", "مساعد كتابة وتوثيق ذكي", "كتابة", "https://www.notion.so/product/ai", ""),
    ("Copy.ai", "إنشاء محتوى تسويقي", "كتابة", "https://www.copy.ai", ""),
    ("Durable", "إنشاء مواقع في ثوانٍ", "مواقع", "https://durable.co", "")
]

conn = sqlite3.connect("database-full.db")
cursor = conn.cursor()

for tool in tools:
    cursor.execute("INSERT INTO tools (name, description, category, url, image) VALUES (?, ?, ?, ?, ?)", tool)

conn.commit()
conn.close()

print("✅ تم إضافة الأدوات بنجاح!")
