def load_qna(file_path):
    qna = {}
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for i in range(0, len(lines), 2):
            question = lines[i].strip()
            answer = lines[i+1].strip()
            qna[question] = answer
    return qna

def chatbot(qna_file):
    qna = load_qna(qna_file)
    while True:
        user_input = input("User: ")
        if user_input.lower() == 'exit':
            break
        if user_input in qna:
            print("Chatbot: " + qna[user_input])
        else:
            print("Chatbot: Sorry, I don't have an answer for that.")

if __name__ == '__main__':
    qna_file = '/Users/spartan/Downloads/qna.txt'  # Replace with the actual path to your Q&A file
    chatbot(qna_file)

