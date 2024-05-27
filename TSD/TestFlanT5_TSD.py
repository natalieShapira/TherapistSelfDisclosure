from FlanT5MyAPI import FlanT5MyAPI
from TSD_Parser import TSD_Parser
from TSD_Evaluation import TSD_Evaluation
from TSD_Test import TSD_Test


gt_answers = []
pred_answers = []
if __name__ == '__main__':
    # MODEL_NAME = "google/flan-t5-xxl" # google/flan-t5-small, google/flan-t5-base, google/flan-t5-large, google/flan-t5-xl, google/flan-t5-xxl
    short_model_name = "flan-t5-xl"
    model_name = "google/"+ short_model_name
    temperature = 0.00001
    number_of_samples = 1
    FlanT5MyAPI.set_seed(0)
    flan_t5 = FlanT5MyAPI(model_name, temperature)

    out_str = ""
    print(flan_t5.model_name)
    out_str += flan_t5.model_name+"\n"
    print(flan_t5.temperature)
    out_str += "Temperature = " + str(flan_t5.temperature)+"\n"
    tsd_parser = TSD_Parser()
    print("The generic prompt:\n")
    print(TSD_Test.MODEL_TEST_PROMPT_PREFIX)
    for i in tsd_parser.tests:
        print("**************************************")
        out_str += "**************************************\n"
        print(i)
        out_str += str(i)+"\n"
        speech_turn, label = tsd_parser.tests[i]
        prompt = TSD_Test.MODEL_TEST_PROMPT_PREFIX + speech_turn + '\n' +'Answer:'
        print(speech_turn)
        out_str += prompt+"\n"
        for s in flan_t5.get_full_predictions(prompt, number_of_samples):
            gt_answers.append(label)
            pred_answers.append(s)
            print("--------------------------------------")
            out_str += "--------------------------------------\n"
            print("ground truth: " + label + " prediction: " +s)
            print(TSD_Evaluation.compare_elements(s, label))
            out_str += "ground truth: " + label + " prediction: " +s +"\n"
            out_str += str(TSD_Evaluation.compare_elements(s, label))+"\n"

    print("**************************************")
    out_str += "**************************************\n"
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

    with open("fp_" + short_model_name+"_s-"+str(number_of_samples)+"_t-"+str(temperature)+"_acc-"+str(acc)+".txt", 'w') as f_out:
        f_out.write(out_str)