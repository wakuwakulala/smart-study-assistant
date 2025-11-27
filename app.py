from flask import Flask, request, jsonify, render_template
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# 使用GitHub Models
client = OpenAI(
    base_url=os.getenv("API_BASE"),
    api_key=os.getenv("GITHUB_TOKEN")
)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api/chat', methods=['POST'])
def chat():
    """处理用户提问"""
    try:
        data = request.json
        user_message = data.get('message')

        response = client.chat.completions.create(
            model=os.getenv("MODEL_NAME"),
            messages=[
                {"role": "system",
                 "content": "You are a helpful study assistant. Help students learn by answering their questions clearly and concisely."},
                {"role": "user", "content": user_message}
            ],
            temperature=0.7,
            max_tokens=800
        )

        return jsonify({
            'response': response.choices[0].message.content
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/summarize', methods=['POST'])
def summarize():
    """总结学习材料"""
    try:
        data = request.json
        content = data.get('content')

        response = client.chat.completions.create(
            model=os.getenv("MODEL_NAME"),
            messages=[
                {"role": "system",
                 "content": "You are an expert at summarizing educational content. Create clear, concise summaries that capture key points."},
                {"role": "user", "content": f"Please summarize the following study material:\n\n{content}"}
            ],
            temperature=0.5,
            max_tokens=1000
        )

        return jsonify({
            'summary': response.choices[0].message.content
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/generate-quiz', methods=['POST'])
def generate_quiz():
    """生成测验题"""
    try:
        data = request.json
        content = data.get('content')
        num_questions = data.get('num_questions', 5)

        response = client.chat.completions.create(
            model=os.getenv("MODEL_NAME"),
            messages=[
                {"role": "system",
                 "content": "You are a quiz generator. Create multiple choice questions based on the content provided. Format each question clearly with 4 options (A, B, C, D) and indicate the correct answer."},
                {"role": "user",
                 "content": f"Generate {num_questions} multiple choice questions from this content:\n\n{content}"}
            ],
            temperature=0.7,
            max_tokens=1500
        )

        return jsonify({
            'quiz': response.choices[0].message.content
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)