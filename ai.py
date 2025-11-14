from openai import OpenAI

# --- Cấu hình API Key ---
client = OpenAI(api_key=("")  # <-- Dán API key bạn vào đây

# --- Tạo đoạn hội thoại mẫu ---
response = client.chat.completions.create(
    model="gpt-4o-mini",  # hoặc "gpt-4o" nếu bạn có quyền truy cập
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Xin chào! Hãy giới thiệu bản thân đi."}
    ]
)

# --- In kết quả ra màn hình ---
print(response.choices[0].message.content)
