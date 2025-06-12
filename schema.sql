
CREATE TABLE tools (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    link TEXT NOT NULL,
    category TEXT NOT NULL
);
INSERT INTO tools (name, description, link, category) VALUES
('ChatGPT', 'مساعد ذكي للإجابة على الأسئلة وكتابة النصوص.', 'https://chat.openai.com/', 'كتابة'),
('Canva AI', 'تصميم صور ومنشورات باستخدام الذكاء الاصطناعي.', 'https://www.canva.com/features/ai-image-generator/', 'تصميم'),
('Copy.ai', 'كتابة محتوى تسويقي باستخدام الذكاء الاصطناعي.', 'https://www.copy.ai/', 'تسويق');
