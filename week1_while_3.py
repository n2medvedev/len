def ask_user(correct_answer="хорошо"):
	answer=' '
	while answer!=correct_answer: answer=input("Как дела?").lower()
	return answer
def main():
	ask_user()
main()

