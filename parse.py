from otvetmailru import OtvetClient
import gpt, datetime


def parse(client, session, queries):
    for questions in client.iterate_new_questions():
        for question in questions:
            question = client.get_question(question)
            if not question.can_answer:
                continue
            if question.poll_type:
                continue
            url = question.url
            title = question.title
            description = question.text
            print(f'date: {datetime.datetime.now()}')
            print(f'title: {title}')
            print(f'description: {description}')
            print(f'url: {url}')
            gptanswer = gpt.questions_togpt(title, description, session, queries)
            print(f'answer: {gptanswer}')
            answer = f'Привет, на твой вопрос отвечает ChatGPT-4. Ответ может быть неправильным/некорректным/ошибочным.\n\n{gptanswer}\n\nby_chesnok | github.com/chesnokpeter/otvetmailru_answering_machine'

            try:
                client.add_answer(question, answer)
                status = 'answer added'
            except Exception as e:
                status = f'answer dont added | Error: {e}'
                with open('textdata/errors.txt', 'a+') as err:
                    print(f'{datetime.datetime.now()}  |  answer dont added | Error: {e}', file=err)

            print(f'status: {status}')
            print('\n==========\n')
            with open('textdata/answers.txt', 'a+', encoding = 'utf-8') as answrs:
                print(f'date: {datetime.datetime.now()}', file=answrs)
                print(f'title: {title}', file=answrs)
                print(f'description: {description}', file=answrs)
                print(f'url: {url}', file=answrs)
                print(f'answer: {gptanswer}', file=answrs)
                print(f'status: {status}', file=answrs)   
                print('\n==========\n', file=answrs)        


