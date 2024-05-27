from TSD_Parser import TSD_Parser
from TSD_Evaluation import TSD_Evaluation
from TSD_Test import TSD_Test
from TSD_MI_Dataset import TSD_MI_Dataset
import openai
from Globals.Debug import Debug
#openai.organization = Debug.OPENAI_ORGANIZATION
openai.api_key = (Debug.OPENAI_KEY)
#openai.api_key = (Debug.OPENAI_KEY_XUHUI)
import time

TEMPERATURE = 0
NUMBER_OF_SAMPLES = 1
MODEL_NAME = "gpt-4-0314"
#MODEL_NAME = "text-davinci-002", "text-davinci-003", "gpt-3.5-turbo-0301", "gpt-4-0314"


gt_answers = []
pred_answers = []

if __name__ == '__main__':
    model_name = MODEL_NAME
    temperature = TEMPERATURE
    number_of_samples = NUMBER_OF_SAMPLES
    out_str = ""
    print(model_name)
    out_str += model_name+"\n"
    print(temperature)
    out_str += "Temperature = " + str(temperature)+"\n"
    mi_dataset = TSD_MI_Dataset()
    for id in mi_dataset.tests:
        id, speech_turn, label = mi_dataset.tests[id]
        print("**************************************")
        out_str += "**************************************\n"
        print(id)
        out_str += str(id) + "\n"
        prompt = TSD_Test.MODEL_TEST_PROMPT_PREFIX + speech_turn + '\n' + 'Answer:'
        print(speech_turn)
        out_str += prompt + "\n"
        for j in range(number_of_samples):
            if MODEL_NAME=="gpt-3.5-turbo-0301" or MODEL_NAME=="gpt-4-0314":
                time.sleep(3)
                try:
                    response = openai.ChatCompletion.create(
                        model=model_name,
                        temperature=temperature,
                        messages=[{"role": "user", "content": prompt}]
                    )
                except:
                    time.sleep(10)
                    response = openai.ChatCompletion.create(
                        model=model_name,
                        temperature=temperature,
                        messages=[{"role": "user", "content": prompt}]
                    )
                #print(response)
                s = response["choices"][0]["message"]["content"]

            else:
                response = openai.Completion.create(
                    model=model_name,
                    temperature=temperature,
                    max_tokens=50,
                    prompt=prompt
                )
                s = response["choices"][0]["text"]

            gt_answers.append(label)
            pred_answers.append(s)
            mi_dataset.tests[id] = id, speech_turn, label, s
            print("--------------------------------------")
            out_str += "--------------------------------------\n"
            print("ground truth: " + label + " prediction: " + s)
            #print(TSD_Evaluation.compare_elements(s, label))
            out_str += "ground truth: " + label + " prediction: " + s + "\n"
            #out_str += str(TSD_Evaluation.compare_elements(s, label)) + "\n"
    print("**************************************")
    out_str += "**************************************\n"
    '''
    print("Accuracy (question level):")
    out_str += "Accuracy (question level):\n"
    acc= TSD_Evaluation.compare_lists(pred_answers, gt_answers)
    print(acc)
    out_str += str(acc)

    print("Accuracy ITSD:")
    out_str += "Accuracy ITSD:\n"
    acc1 = TSD_Evaluation.compare_lists(pred_answers, gt_answers, "ITSD")
    print(acc1)
    out_str += str(acc1)

    print("Accuracy NITSD:")
    out_str += "Accuracy NITSD:\n"
    acc1 = TSD_Evaluation.compare_lists(pred_answers, gt_answers, "NITSD")
    print(acc1)
    out_str += str(acc1)

    print("Accuracy None:")
    out_str += "Accuracy None:\n"
    acc1 = TSD_Evaluation.compare_lists(pred_answers, gt_answers, "None")
    print(acc1)
    out_str += str(acc1)
    '''

    acc = 0
    with open("mi_tagged_"+model_name+"_s-"+str(number_of_samples)+"_t-"+str(temperature)+"_acc-"+str(acc)+".txt", 'w', encoding='utf8') as f_out:
        f_out.write(out_str)

    mi_dataset.print_to_file("mi_tagged_" + model_name+".csv")