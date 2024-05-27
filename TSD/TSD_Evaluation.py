

class TSD_Evaluation:

    @staticmethod
    def levenshteinDistance(s1, s2):
        if len(s1) > len(s2):
            s1, s2 = s2, s1

        distances = range(len(s1) + 1)
        for i2, c2 in enumerate(s2):
            distances_ = [i2 + 1]
            for i1, c1 in enumerate(s1):
                if c1 == c2:
                    distances_.append(distances[i1])
                else:
                    distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
            distances = distances_
        return distances[-1]

    @staticmethod
    def compare_elements(e1, e2):
        good = 0
        if e1.strip().lower().startswith('non-immediate') and e2.strip().lower().startswith('nitsd'):
            good += 1
        elif e1.strip().lower().startswith('immediate') and e2.strip().lower().startswith('itsd'):
            good += 1
        elif e1.strip().lower().startswith('not a tsd') and e2.strip().lower().startswith('none'):
            good += 1
        elif e1.strip().lower().startswith('(non-immediate') and e2.strip().lower().startswith('nitsd'):
            good += 1
        elif e1.strip().lower().startswith('(immediate') and e2.strip().lower().startswith('itsd'):
            good += 1
        elif e1.strip().lower().startswith('(not a tsd') and e2.strip().lower().startswith('none'):
            good += 1
        elif e1.strip().lower().startswith('"non-immediate') and e2.strip().lower().startswith('nitsd'):
            good += 1
        elif e1.strip().lower().startswith('"immediate') and e2.strip().lower().startswith('itsd'):
            good += 1
        elif e1.strip().lower().startswith('"not a tsd') and e2.strip().lower().startswith('none'):
            good += 1
        elif e1.strip().lower().startswith('non-immediate') and e2.strip().lower().startswith('(nitsd'):
            good += 1
        elif e1.strip().lower().startswith('immediate') and e2.strip().lower().startswith('(itsd'):
            good += 1
        elif e1.strip().lower().startswith('not a tsd') and e2.strip().lower().startswith('(none'):
            good += 1
        elif e1.strip().lower().startswith('non-immediate') and e2.strip().lower().startswith('"nitsd'):
            good += 1
        elif e1.strip().lower().startswith('immediate') and e2.strip().lower().startswith('"itsd'):
            good += 1
        elif e1.strip().lower().startswith('not a tsd') and e2.strip().lower().startswith('"none'):
            good += 1
        return good

    @staticmethod
    def compare_elements_distance(e1, e2):
        good = 0
        if e1.strip().lower() in e2.strip().lower():
            good += 1
        elif e2.strip().lower() in e1.strip().lower():
            good += 1
        elif e1.strip()[1:-2].lower() in e2.strip().lower():
            good += 1
        elif e2.strip()[1:-2].lower() in e1.strip().lower():
            good += 1
        elif TSD_Evaluation.levenshteinDistance(e1.strip().lower(), e2.strip().lower()) < 3:
            good += 1
        elif TSD_Evaluation.levenshteinDistance(e1.strip()[1:-2].lower(), e2.strip().lower()) < 3:
            good += 1
        elif TSD_Evaluation.levenshteinDistance(e1.strip().lower(), e2.strip()[1:-2].lower()) < 3:
            good += 1
        elif len(e1) > 10 and len(e2) > 10 and TSD_Evaluation.levenshteinDistance(e1.strip().lower(),
                                                                   e2.strip().lower()) < 10:  # He/She instead of a name
            good += 1
        return good

    @staticmethod
    def compare_lists(list1, gt_list, category_name=None):
        good = 0
        category_good = 0
        category_len = 0
        for i in range(len(list1)):
            if category_name != None:
                if gt_list[i] == category_name:
                    category_len+=1
                    if TSD_Evaluation.compare_elements(list1[i], gt_list[i]):
                        category_good += 1

            if TSD_Evaluation.compare_elements(list1[i], gt_list[i]):
                good += 1

        if category_name != None:
            print("compare_lists total category good:" + str(category_good))
            print("compare_lists category_len:" + str(category_len))
            return category_good / category_len

        print("compare_lists_question_level total good:" + str(good))
        print("compare_lists_question_level total len(list1):"+str(len(list1)))
        return good / len(list1)